# Golland_TimesheetBot
This tool sends automated email reminders to staff for them to fill out their timesheets. It was inspired by messages received from a colleague who  used to copy and paste clock images in emails prompting staff who were late with completing time sheets to turn them in.  The notifications helped expedite payroll processing of the HR team who were often frustrated by our forgetfulness.   

This improves the manual reminders for timesheet completion and replaces the weird copy pasted clock pics with NewYorker caption contest image to give employees something funny, unique and memorable every two weeks that this task is required.

## Sample Program Output
![program output email](https://github.com/brl1906/timesheets_gollandbot/blob/master/images/example_output.png)



## Getting Started
1. Make sure your machine has Python installed.
2. Ensure you have [pip](https://pypi.org/project/pip/), a package manager for Python modules.  
2. Install virtualenv -- it is a tool for creating isolated Python environments and is really handy when you have multiple projects in various stages on your machine.  You can install it from the terminal with ```pip install virtualenv```

3. Create a folder for the project with file finder or the terminal:```mkdir GOLLANDPROJECT```

4. Move into that new directory:```cd GOLLANDPROJECT```

5. Clone the project by copying and using the url string produced when you hit the green button
<img src="https://github.com/brl1906/timesheets_gollandbot/blob/master/images/clone_button.png" width=80, height=40> and pasting it after the command ```git clone THEURLSTRINGFORTHEREPOSITORY```

5. From within this directory create a virtual environment for your project using virtualenv. For example: ```virtualenv GOLLAND_VIRTUAL_ENVIRONMENT```

6. Activate the virtual environment with the following command so that you can install the required packages this program needs and contain them to this environment. Run: ```source GOLLAND_VIRTUAL_ENVIRONMENT/bin/activate```

7. To create your environment to match that of the project you just cloned, install the required packages into the virtual environment via the terminal using the command: ```pip install -r requirements.txt```

8. Create a file in the configuration folder named 'config.ini' following the format provided in the [example file ](https://github.com/brl1906/timesheets_gollandbot/blob/master/configuration/example_config_file.txt) in which you add your gmail credentials to the file.

9. You can run the program from the virtual environment with the command ```python app.py```

### Note:
This program was designed to be deployed via PythonAnywhere to enable remote hosting and running through the scheduling of timed jobs on a remote server.  You have the option of running the program manually on your machine through the terminal or deploying on [PythonAnywhere](https://help.pythonanywhere.com/pages/).  

If you use PythonAnywhere you can test by setting an hourly task to run your program--there is a repo clone and bash script creation step in between.  You know it works if output of an hourly task for 1 minute after the hour give you something like this:


<img src='https://github.com/brl1906/timesheets_gollandbot/blob/master/images/hourly_emails_test.png' height=500> <img src='https://github.com/brl1906/timesheets_gollandbot/blob/master/images/gmail_hourly.png' height=500, width=465>

## TODO:
* [ ] add biweekly timesheet submission day test function for running biweekly with PythonAnywhere
* [ ] add log drop some print statements
* [ ] add function for cleaning images directory
* [ ] update .gitignore for logs
* [ ] add to docs
