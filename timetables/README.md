# TIMETABLE MATCHING

* I have these two timetable, and i want to find out the lapse of time in between they're both free at the same time.
* There's a minimum timespan.
* There's also a total availability for both the timetable.

### EXAMPLE:
Timetable of A: **[[9:00, 11:30], [12:30, 15:00], [16:00, 18:00]]**.  
Total availability of A: [[8:20, 18:00]].  
Timetable of B: **[[9:30, 11:00], [15:30, 16:30], [17:00, 18:30]]**.  
Total availability of B: [[8:30, 18:30].  
Minimum timespan: 30 minutes.  

The **output** should be: **[[11:30, 12:30], [15:00, 15:30]]**.
