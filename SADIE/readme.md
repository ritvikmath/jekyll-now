# SADIE, A Fast and Efficient Job Shift Scheduling Algorithm

**Getting Worker Preferences**

1. From my GitHub download a file called **example_preferences.csv**
2. This file shows how the scheduler wants the preferences to look. The time period in this example document is the same we have used through this post for convenience
3. You need to replace the names with your own worker's names and change the date range to what you prefer. You should add / remove weeks if needed
4. Workers should put **one of four things** in each cell corresponding to their name. They can put:
	- 'ON PREF': Please try and schedule me ON that day
	- 'IN PREF': Please try and schedule me IN that day but do NOT schedule me ON
	- 'OFF': Do NOT schedule me that day
	- blank: No preference, anything is fine
5. Please keep the preferences in csv format and rename the file to whatever name you prefer

**Making the Optimal Schedule**

1. From my GitHub download a file called **SADIE.exe**
2. Put SADIE.exe in the same folder as your preferences csv document
3. Run SADIE.exe 
4. SADIE will ask you some questions including:
	- What day you want to start scheduling
	- How many days you want to schedule
	- How many ON / IN shifts there should be per day
5. SADIE will then run for a while depending on how strict the preferences are and how many weeks you are trying to schedule
6. Once SADIE is done, you will have a file called **duty_sched.csv** in the same folder that SADIE.exe is in
7. duty_sched.csv contains the optimized shift schedule 
8. There is a chance that, if your staff's preferences make for an impossible schedule, SADIE will inform you that there is no possible schedule, in which case you will need to change the preferences csv file and try again

**For Second, Third, etc. Scheduling Periods**

It is totally up to you how much of SADIE's suggestions about optimal schedule you use. But, when you want to run SADIE again after a few weeks, it needs to know what the previous shift assignments were so that it can use that past to optimize the future. Follow these steps for a second, third, etc. scheduling run.

1. In your preferences csv document include **ALL** dates from the beginning of the quarter / year / term until the last date you are trying to schedule. Eg. If you scheduled May 15 - Jun 10 and now you want to schedule Jun 11 - Jun 30, include all days from May 15 - Jun 30. 
2. For the dates that have already been scheduled (eg. May 15 - Jun 10), put 'ON 1', 'ON 2', etc. for the workers who have been assigned to those shifts on each day. Same goes for putting in 'IN 1', 'IN 2', etc. 
3. It is OK to leave 'ON PREF', 'IN PREF', 'OFF' in the past dates
4. For the dates you are trying to schedule (eg. Jun 11 - Jun 30), you just need to make sure all workers have put 'ON PREF', 'IN PREF', 'OFF'
5. Run SADIE as usual, making sure to input the start schedule date and number of days to schedule properly
