Stata_SMS
=========

* Version 1.0
* Date: July 18, 2014


Sends text message (SMS) after Stata has ended (completed the do file, stopped due to error in code, or crashed, etc.). This is useful if you're running a do file that will take a few hours to run and you want to know immediately when it finishes, runs into an error, or crashes. 

## System Requirements
* Windows XP and later
* [Python 2.7.3](http://www.python.org/download/releases/2.7.3/)

### Background
Many of my colleagues have expressed frustation when they start a `.do` file, expecting it to run uninterupted for hours, only to have it stop due to a coding error a little while after they move onto another task. Now we have a solution. This set of scripts will alert you as soon as Stata stops. While there are `.ado` files and other programs that allow you to utilize Python within Stata, what happens if Stata never reaches the line that calls on Python? Nothing! No notification at all. Now, with this set up you'll be alerted once Stata stops, no matter the outcome.

### Description
This set of files will allow a text message (SMS) to be sent when the `.do` ends (either successfully or after running into an error, either way, a `.log` file will be produced and named after the `.do` file in the same folder as the `.do` file). There is an option to convert the `.log` file to `.txt` and have it emailed to you.. but this feature isn't relevant for sending a text message and more useful if you wish to receive an email with an attachement (which could be a `.log` file, graphics, or even a `.dta` file).

## Set up
The default directory is `C:\SMS\`
1. Download [Stata_SMS-master](https://github.com/tonijung/Stata_SMS/archive/master.zip) and extract the `Stata_SMS-master` folder's `run_me.bat` and `test.py` files to the same folder as the `.do` file that you're planning on using. 
2. In `run_me.bat`..
3. Update the path to your Stata installation in line 3. The default is set to `"C:\Program Files (x86)\Stata12\StataSE-64.exe"`
4. On line 3, update the path to the `.do` file you'd like to run. The default is set to `C:\SMS\test.do`.
5. On line 4, update the path to your installation of Python. The default is set to `C:\Python27\python.exe`
6. On line 4, update the path to where you've extracted the `test.py` file to. The default is set to `C:\SMS\test.py`
7. In `test.py`..
8. On line 8, insert your email information into the relevant fields. The default is for gmail.
9. On line 9, update the relevant fields. The `'<author>'` and `'<message here>'`field is optional, but you'll want to update the second field with either your phone number that will receive the SMS or the email you wish to send the alert to. the default is set to AT&T. Notes for different carriers and email providers are listed in the URL in the python script. 
