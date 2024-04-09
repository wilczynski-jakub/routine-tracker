# Routine Tracker
Track the daily progress of your routine goals with an automatized spreadsheet, and never be late for work again!

## [routine-tracker.xlsx](routine-tracker.xlsx)
| Cell | Functionality |
|-------|------|
| ![Screenshot 1](screenshots/1.png) | Baseline time: preferably 0:00 but it can also be a specific hour. |
| ![Screenshot 2](screenshots/2.png) | The time at which you're planning to wake up on that day. |
| ![Screenshot 3](screenshots/3.png) | How much timm does each activity have to take at most. |
| ![Screenshot 4](screenshots/4.png) | The time at which you've completed it: if you managed within the limit, the below cell becomes "Yes". |
| ![Screenshot 5](screenshots/5.png) | If you've completed the activity but didn't manage to do it on time, the below cell becomes "Meh". |
| ![Screenshot 6](screenshots/6.png) | If you're not doing it at all: once "x" is put, the below cell becomes "No". |
| ![Screenshot 7](screenshots/7.png) | You can see the percentage of your activities' completion (where each "Yes" counts as 1 and each "Meh" counts as ½). |

## [auto_type_time.sh](auto_type_time.sh)
The script can be used for automatizing this step:
<br>
![Screenshot 4](screenshots/4.png)
<br>
Once runned, it will type the current time automatically.
