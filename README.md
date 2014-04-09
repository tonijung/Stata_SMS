Stata_SMS
=========

Sends text message (SMS) after Stata has ended (completed the do file, stopped due to error in code, or crashed)

<h4>Motivation</h4>
Many of my colleagues have expressed frustation when they start a do-file, expecting it to run uninterupted for hours, only to have it stop due to a coding error a little while after they walked away. Now we have a solution. This set of scripts will alert you as soon as Stata stops. While there are ado files and other programs that allow you to utilize Python within Stata, what happens if Stata never reaches that line? Nothing! No notification at all. Now, with this set up you'll be alerted once Stata stops, no matter the outcome.


<h4>Description</h4>
This set of files will allow a text message (SMS) to be sent when the do-file ends (either successfully or after running into an error, either way, a .log file will be produced and named after the do-file in the same folder as the do-file). There is an option to convert the .log file to .txt and have it emailed to you.. but this feature isn't relevant for sending a text message and more useful if you wish to receive an email with an attachement (which could be a .log file, graphics, or even a .dta file).

This is useful if you're running a do file that will take a few hours to run and you want to know when it finishes, runs into an error, or crashes.


<h4>Instructions..</h4>
This is for Windows OS (XP and beyond) using Python 2.7.3

The batch and python files need to be in the same folder as the do-file that you're trying to run.

Download the 2 files (run_me.bat and test.py) into a folder (I use C:/SMS/ for simplicity). 

In run_me.bat, update the directories and change the third line to the do-file that you're planning to run. (I have the default as test.do for testing). 

In test.py, insert your information into lines 8 and 9. Update line 6 if necessary. The default is for gmail and at&t. 
