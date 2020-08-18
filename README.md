# Jacob-Portfolio
This repository contains various small projects I've worked on.

**ConvertApp.py**

One of the applications I wrote while interning for the FAA. I needed to convert
several 10000+ long excel files into csv files, and clean them up while I was
at it. I was later asked to turn the script into a simple application that could
be used again if needed, and on a machine without a python environment.

The script stores the path of all the .xlsx files in a user-selected directory,
then iterates through each file: reading them in (using the library pandas),
cleaning up the pandas dataframes (removing duplicate rows, and removing
empty columns), then saving the cleaned dataframe as a csv. Once it's finished,
it creates a directory to store the csv files, the xlsx files, and anything else
that might have been in the directory.

**SimLogApp**

Another application I wrote while interning for the FAA. I was asked to write an
application that could log a users time on their simulator without needing to be
logged into the simulator's system.

*SimLogApp.py*

This is the application itself. On start, the user can begin to log their time
after inputting some basic information like name and task. The start
time is stored in a class variable. It was requested that the program would time
out after two hours or so, and that timer starts once the start time is recorded.
Once the timeout time reaches 1/4 of it's total, it'll prompt for the user to
extend the time. Additionally, the user can adjust various values through the
edit tab, such as the timeout time, and the output directory.

Once the user clicks to end their time (or the program times out), the end time
is stored and all of the information is appended to a csv file, or one is created
if there is not one for the current month.

*SimLogAppNames.txt*

This text file stores the names of all members of the team. Names are changed
to placeholders here.

**Programming-Challenges**

This folder contains some of the free challenges I completed on Coderbyte to
practice my programming skills. In each of the python files, the challenge is
pasted into a comment, and one or two print statements are included with example
inputs.

**MultiplicationsFlashCards.py**

This is mostly a place to store this so I remember how to use the genanki package
when I get back to it. My sister needed multiplication flash cards and I've used
Anki with success in the past, so I made her a quick deck. I hope to come back to
this to create a deck for a second language vocabulary.
