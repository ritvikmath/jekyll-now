###########################################
##	RITVIK KHARKAR						  
##  UCLA CLASS OF 2017					  
##  COMPUTATIONAL MATHEMATICS & ECONOMICS 
##  www.ritvikmath.com					  
##  SEPT 2016							  
###########################################


from pulp import *
import numpy as np
import pandas as pd
from random import shuffle
import datetime

start_date = raw_input("Start Date for Scheduling (eg. Sun 15 / Fri 10): ")
num_days = int(raw_input("Number of Days to Schedule: "))
staff_size = int(raw_input("Staff Size: "))
on_shifts_per_day = int(raw_input("ON Shifts per day: "))
in_shifts_per_day = int(raw_input("IN Shifts per day: "))

start = datetime.datetime.now()


pref_doc = raw_input("Name of Shift Preference file (eg. example_preferences.csv): ")

try:

	duty_prefs = pd.read_csv(pref_doc, header = None)


	

	for index, row in duty_prefs.iterrows():
		for item in row:
			if type(item) == str and 'Sun' in item:
				x = index+1
				y = row.tolist().index(item)
				df = duty_prefs.iloc[x:x+staff_size,y-1:y]
				names = df.iloc[:,0].tolist()
				if type(names[0]) == str:
					break


	# In[1361]:

	key_names = dict(zip(range(len(names)), names))


	# In[1362]:

	all_days = []
	allow = False
	
	for index, row in duty_prefs.iterrows():
		#print row
		#raw_input()
		for item in row:
			if type(item) == str and 'Sun' in item:
				x = index
				y = row.tolist().index(item) - 1
				
				df = duty_prefs.iloc[x:x+staff_size+1,y:y + 8]
				df.columns = pd.Series(['Name']).append(df.iloc[0].iloc[1:])
				
				df.index = range(len(df))
				df = df.ix[1:]
				
				df['Name'] = names
				df.index = names
				df = df.drop('Name',1)
				
				all_days.append(df)
				

					
	full_df = all_days[0]
	if len(all_days) > 1:
		for df in all_days[1:]:
			full_df = full_df.merge(df, left_index = True, right_index = True)
			
	for i, col in enumerate(full_df.columns):
		if type(col) == float:
			full_df.drop(col, 1, inplace = True)
		if col == start_date:
			split_loc = i  

	total_df = full_df.iloc[:, split_loc:]
	past_df = full_df.iloc[:, :split_loc]


	days_prev = len(past_df.columns)

	
	prev_shifts_on = {}
	prev_shifts_in = {}
	for name in names:
		prev_shifts_on[name] = {}
		prev_shifts_in[name] = {}
		for i in range(on_shifts_per_day):
			prev_shifts_on[name]['ON '+str(i+1)] = 0
		for i in range(in_shifts_per_day):
			prev_shifts_in[name]['IN '+str(i+1)] = 0
	for i,row in past_df.iterrows():
		for item in row:
			if item == 'ON 1' or item == 'ON 2' or item == 'ON 3':
				prev_shifts_on[i][item] += 1
			elif item == 'IN 1' or item == 'IN 2' or item == 'IN 3':
				prev_shifts_in[i][item] += 1

	
	hist_dict = {}
	for name in names:
		hist_dict[name] = (0, 'NIL')

	for i,row in past_df.iterrows():
		searchlist = row.tolist()[::-1]
		for item in searchlist:
			if item == 'ON 1' or item == 'ON 2' or item == 'ON 3' or \
				item == 'IN 1' or item == 'IN 2' or item == 'IN 3':
				hist_dict[i] = (searchlist.index(item)+1, item.strip('123 '))
				break


	# In[1365]:

	total_df = total_df.ix[:,0:num_days]


	# In[1366]:

	total_df = total_df.dropna(axis=1,how='all')
	total_df = total_df.ix[0:]


	# In[1367]:

	total_df = total_df.replace(np.nan, 'NONE')
	days = total_df.columns


	

	# In[1485]:

	
	n = staff_size
	m = num_days

	fair_amt_on = (m + days_prev)*on_shifts_per_day/float(n)
	fair_amt_in = (m + days_prev)*in_shifts_per_day/float(n)


	def run_LP(days_off_on = 1, days_off_in = 1, days_off_ei = 1, max_days_week = 3, on_tol = (0,1), in_tol = (0,1), tot_tol = (0,1), on_reward = 2, in_reward = 1):

		on_vars = []
		in_vars = []
		
		
		prob = LpProblem("DUTY", LpMaximize)


		# In[1487]:

		
		for i in range(n):
			l = []
			p = []
			for j in range(m):
				on_var = LpVariable('O'+str(i)+'_'+str(j), 0,1,LpInteger)
				in_var = LpVariable('I'+str(i)+'_'+str(j), 0,1,LpInteger)
				l.append(on_var)
				p.append(in_var)
			on_vars.append(l)
			in_vars.append(p)


		# In[1488]:

		
		all_on_pref = 0.0
		all_in_pref = 0.0
		run_sum = 0
		for i in range(n):
			for j in range(m):
				pref = total_df.ix[:,j][key_names[i]]
				if pref == 'ON PREF':
					all_on_pref += 1
					run_sum += on_reward * on_vars[i][j]
				elif pref == 'IN PREF':
					all_in_pref += 1
					run_sum += in_reward * in_vars[i][j]
		prob += run_sum


		# In[1489]:

		
		free_days_on = {}
		free_days_in = {}
		for worker, tup in hist_dict.iteritems():
			if tup[1] == 'ON':
				free_days_on[worker] = max(days_off_on - tup[0], 0)
				free_days_in[worker] = max(days_off_ei - tup[0], 0)
			elif tup[1] == 'IN':
				free_days_in[worker] = max(days_off_in - tup[0], 0)
				free_days_on[worker] = max(days_off_ei - tup[0], 0)
			else:
				free_days_on[worker] = 0
				free_days_in[worker] = 0

		for i in range(n):
			prob += sum(on_vars[i][:free_days_on[key_names[i]]]) + sum(in_vars[i][:free_days_in[key_names[i]]]) == 0


		# In[1490]:

		
		for j in range(n):
			t_sum = sum(on_vars[j]) + prev_shifts_on[key_names[j]]
			prob += t_sum <= int(fair_amt_on) + on_tol[1]
			prob += t_sum >= int(fair_amt_on) - on_tol[0]
			t_sum = sum(in_vars[j]) + prev_shifts_in[key_names[j]]
			prob += t_sum <= int(fair_amt_in) + in_tol[1]
			prob += t_sum >= int(fair_amt_in) - in_tol[0]
			t_sum = sum(on_vars[j]) + prev_shifts_on[key_names[j]] + sum(in_vars[j]) + prev_shifts_in[key_names[j]]
			prob += t_sum <= int(fair_amt_on + fair_amt_in) + tot_tol[1]
			prob += t_sum >= int(fair_amt_on + fair_amt_in) - tot_tol[0]


		# In[1491]:

		
		for j in range(m):
			prob += sum([i[j] for i in on_vars]) == on_shifts_per_day
			prob += sum([i[j] for i in in_vars]) == in_shifts_per_day


		# In[1492]:

		
		for i in range(n):
			l = on_vars[i]
			p = in_vars[i]
			for j in range(m-6):
				prob += sum(l[j:j+7]) + sum(p[j:j+7]) <= max_days_week
			for j in range(m-days_off_ei+1):
				prob += sum(l[j:j+days_off_ei]) + sum(p[j:j+days_off_ei]) <= 1
			for j in range(m-days_off_on+1):
				prob += sum(l[j:j+days_off_on]) <= 1
			for j in range(m-days_off_in+1):
				prob += sum(p[j:j+days_off_in]) <= 1
			


		# In[1493]:

		
		for i in range(n):
			for j in range(m):
				prob += on_vars[i][j] + in_vars[i][j] <= 1


		# In[1494]:

		
		run_sum = 0
		for i in range(n):
			for j in range(m):
				pref = total_df.ix[:,j][key_names[i]]
				if pref == 'OFF':
					prob += on_vars[i][j] == 0
					prob += in_vars[i][j] == 0
				elif pref == 'IN PREF':
					prob += on_vars[i][j] == 0
				elif pref == 'ON':
					prob += on_vars[i][j] == 1
				elif pref == 'IN':
					prob += in_vars[i][j] == 1


		# In[1495]:

		

		# In[1496]:

		
		prob.solve()


		# In[1497]:

		

		return prob


		

	days_off_on = 7
	days_off_in = 7
	days_off_ei = 7
	on_reward = 2
	in_reward = 1
	on_tol_tup = (0,1)
	in_tol_tup = (0,1)
	tot_tol_tup = (0,1)

	print '------------------------------'
	print 'Finding Lower Thresholds ...'
	while (run_LP(days_off_on, days_off_in, days_off_ei, on_tol = on_tol_tup, in_tol = in_tol_tup, tot_tol = tot_tol_tup).status == -1):
		days_off_on -= 1
		days_off_in -= 1
		days_off_ei -= 1
		if days_off_ei == 1:
			days_off_on = 7
			days_off_in = 7
			days_off_ei = 7
			on_tol_tup = (on_tol_tup[0] + 1, on_tol_tup[1])
			in_tol_tup = (in_tol_tup[0] + 1, in_tol_tup[1])
			tot_tol_tup = (tot_tol_tup[0] + 1, tot_tol_tup[1])
		if sum(on_tol_tup) > 2:
			print "Preferences too Strict to Build Valid Schedule"
			raise SystemExit
		
			

	print '------------------------------'
	print 'Boosting time between ON shifts ...'	
	while (run_LP(days_off_on, days_off_in, days_off_ei, on_tol = on_tol_tup, in_tol = in_tol_tup, tot_tol = tot_tol_tup).status == 1 and days_off_on <= 7):
		days_off_on += 1
	days_off_on -= 1

	print '------------------------------'
	print 'Boosting time between IN shifts ...'
	while (run_LP(days_off_on, days_off_in, days_off_ei, on_tol = on_tol_tup, in_tol = in_tol_tup, tot_tol = tot_tol_tup).status == 1 and days_off_in <= 7):
		days_off_in += 1
	days_off_in -= 1
		
	prob = run_LP(days_off_on, days_off_in, days_off_ei, on_tol = on_tol_tup, in_tol = in_tol_tup, tot_tol = tot_tol_tup)
		
	duty_mtx = np.zeros((n,m))

	print '------------------------------'
	print "Status:", LpStatus[prob.status]
	print "Objective Function Score =", value(prob.objective)
	print "Minimum days off between ON Shifts =", days_off_on
	print "Minimum days off between IN Shifts =", days_off_in
	print "Minimum days off between ON Shift and IN Shift =", days_off_ei
	print "Range for number of ON/IN/Total shifts =", on_tol_tup[1] + on_tol_tup[0]
	for v in prob.variables():
		try:
			coords = [int(i) for i in v.name.strip('IO').split('_')]
			if v.varValue > 0:
				if v.name[0] == 'O':
					duty_mtx[coords[0]][coords[1]] = (v.varValue * 2)
				else:
					duty_mtx[coords[0]][coords[1]] = v.varValue 
		except ValueError:
			pass

	# In[1499]:

	duty_df = pd.DataFrame(duty_mtx)


	# In[1500]:

	duty_df = duty_df.replace([0,1,2], ['X','IN','ON'])


	# In[1501]:

	duty_df.columns = days
	duty_df.index = names

	
	fair_amt_on_each = fair_amt_on / on_shifts_per_day
	fair_amt_in_each = fair_amt_in / in_shifts_per_day




	# In[1502]:

	master_df = pd.DataFrame(columns = ['ON 1', 'ON 2', 'ON 3', 'IN 1', 'IN 2', 'IN 3'], index = days)

	def update_shifts(prev_shifts_on, prev_shifts_in):
		need_on = {}
		need_in = {}
		for name in names:
			on_distr = prev_shifts_on[name].values()
			in_distr = prev_shifts_in[name].values()
			need_on[name] = (min(prev_shifts_on[name], key =prev_shifts_on[name].get) , (min(on_distr)- np.mean(on_distr)))
			need_in[name] = (min(prev_shifts_in[name], key =prev_shifts_in[name].get) , (min(in_distr)- np.mean(in_distr)))
		return (need_on, need_in)
		
	for col in duty_df.columns:
		dts = duty_df[col]
		on_names = (dts[dts == 'ON']).index.tolist()
		in_names = (dts[dts == 'IN']).index.tolist()
		shuffle(on_names)
		shuffle(in_names)
		need = update_shifts(prev_shifts_on, prev_shifts_in)
		need_on = need[0]
		need_in = need[1]
		
		names_on_values = []
		names_in_values = []
		for name in on_names:
			names_on_values.append((name, need_on[name][0], need_on[name][1]))
		for name in in_names:
			names_in_values.append((name, need_in[name][0], need_in[name][1]))
		
		sorted_on_values = sorted(names_on_values, key = lambda x: x[2])
		sorted_in_values = sorted(names_in_values, key = lambda x: x[2])
		
		on_names = [i[0] for i in sorted_on_values]
		in_names = [i[0] for i in sorted_in_values]
		
		assigned = {}
		
		for name in on_names:
			assigned[name] = 'ONX'
		for name in in_names:
			assigned[name] = 'INX'
		 
		fill_dict = {}
		for i in range(on_shifts_per_day):
			fill_dict['ON '+str(i+1)] = ''
		for i in range(in_shifts_per_day):
			fill_dict['IN '+str(i+1)] = ''
		fill_dict[sorted_on_values[0][1]] = sorted_on_values[0][0]
		fill_dict[sorted_in_values[0][1]] = sorted_in_values[0][0]
		
		assigned[on_names[0]] = 'ONC'
		assigned[in_names[0]] = 'INC'
		prev_shifts_on[on_names[0]][sorted_on_values[0][1]] += 1
		prev_shifts_in[in_names[0]][sorted_in_values[0][1]] += 1
		
		for name in on_names[1:]:
			preference = need_on[name][0]
			if fill_dict[preference] == '':
				fill_dict[preference] = name
				prev_shifts_on[name][preference] += 1
				assigned[name] = 'ONC'
			else:
				continue
				
		for name in in_names[1:]:
			preference = need_in[name][0]
			if fill_dict[preference] == '':
				fill_dict[preference] = name
				prev_shifts_in[name][preference] += 1
				assigned[name] = 'INC'
			else:
				continue
				
		unassigned_on = []
		unassigned_in = []
		
		for key in assigned.keys():
			if assigned[key] == 'ONX':
				unassigned_on.append(key)
			if assigned[key] == 'INX':
				unassigned_in.append(key)
				
		need_workers_on = []
		need_workers_in = []
		
		for shift,status in fill_dict.iteritems():
			if 'ON' in shift and status == '':
				need_workers_on.append(shift)
			if 'IN' in shift and status == '':
				need_workers_in.append(shift)
		
		for tup in zip(unassigned_on, need_workers_on):
			fill_dict[tup[1]] = tup[0]
			prev_shifts_on[tup[0]][tup[1]] += 1
		for tup in zip(unassigned_in, need_workers_in):
			fill_dict[tup[1]] = tup[0]
			prev_shifts_in[tup[0]][tup[1]] += 1
			
		for shift,status in fill_dict.iteritems():
			master_df.ix[col][shift] = status
	 
	stop = datetime.datetime.now() 
		
	store_name = 'duty_sched.csv'           
		
	master_df.to_csv(store_name)
	print '----------'
	print "Optimal Scheduled stored in " + store_name
	print '----------'
	print "Total Time:", (stop - start).total_seconds()

	raw_input()


except:
	print '----------'
	print "Error! Possible Causes:"
	print "- Errors in your inputs"
	print "- duty_sched.csv is still open"
	print "- Past history of duties not listed"
	raw_input()

