import pandas as pd
import os
import sys
from tkinter import filedialog
from tkinter import *
from datetime import datetime
import time

#########################################################
# File: SimLogApp.py
#
# Author: Jacob Miller
#
# Libraries: pandas, os, sys, tkinter, datetime, time
#
# Last Updated: 07/29/2020
#
# Written in: Python 3.6.9
#
# Purpose: Allows users to log time on the flight simulator
#          without being logged into the IOS. Exports the
#          logged info into a .csv file upon exit.
#
# Compile: Load it into IDLE/your favorite python
#          environment, or run it from the command line.
#          If you want an exe for easy execution or need
#          it on a machine without python, use pyinstaller.
#          You can install it using pip install pyinstaller
#          Then complie it with the command:
#          pyinstaller /path/to/file.py --onefile
#          Note, you must compile on the same OS as your target.
#          If you're aiming for a Windows machine, don't compile
#          on a Linux environment.


#Quick changes
outputDir = "/home/jacob/Desktop/workDir/LoggingApp/"
defaultTimeoutTime = 7200           #Default 2 hours
#outfile assignment in PrintToCsv() in class LoggingData

class LoggingData:
    """
    Class to store data related to time logging.
    """
    def __init__(self):
        self.startTime = None
        self.endTime = None
        self.name = None
        self.purpose = None

        self.headerList = ["Name", "Date", "Time in", "Time out", "Duration", "Task"]

        self.dirPath = outputDir
        self.outfile = ""

    def SetStartTime(self, starttime):
        self.startTime = starttime

    def SetName(self, newName):
        self.name = newName

    def SetPurpose(self, newPurpose):
        self.purpose = newPurpose

    def SetOutfile(self, outFile):
        self.outfile = outFile

    def SetEndTime(self, endtime):
        self.endTime = endtime

    def ChangePath(self, newPath):
        self.dirPath = newPath

    def CompleteLog(self):
        """
        Called when log time is up or ended manually. Takes all the Information
        to be logged, puts it into a list, and sends it to be exported.
        """
        self.endTime = datetime.now()
        print(self.endTime)

        myList=[str(self.name),
        self.startTime.strftime("%m/%d"),
        self.startTime.strftime("%H:%M:%S"),
        self.endTime.strftime("%H:%M:%S"),
        str(self.endTime - self.startTime).split(".")[0],
        str(self.purpose)]

        self.PrintToCsv(myList)

    def PrintToCsv(self, myList):
        """
        Exports data into a CSV. Tries to ensure the directory exists, and looks
        checks whether a log file already exists or not. If it doesn't, it creates
        one with a header of self.headerList. If a file does exist, it appends
        the new information to the end and writes it. Will create a new file every
        calendar month.
        """

        self.outfile = "B73_"+self.startTime.strftime("%Y_%m") + "_log.csv"

        myFile = None
        print(self.dirPath+self.outfile)
        try:
            os.chdir(self.dirPath)
        except:
            print("Error: Could not change to output directory. Check read/write "+
            "permissions, and that the directory exists. Output directory can be "+
            "changed under the edit dropdown menu.")
        if os.path.exists(self.dirPath+self.outfile):
            myFile = pd.read_csv(self.dirPath + self.outfile)
        else:
            myFile = pd.DataFrame(columns = self.headerList)

        myFile.loc[len(myFile)] = myList
        myFile.to_csv(self.dirPath + self.outfile, index = False)
        print(myFile)


class Window(Frame):
    """
    Tkinter class for all the graphical interfaces. Also responsible for the
    timeout function.
    """

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

        self.loggingClass = LoggingData()

        self.timeoutTime = defaultTimeoutTime #2 hours default
        self.warningFlag = True
        self.timeoutFlag = True


    def init_window(self):
        """
        This method initializes the window. Buttons, menus, and text are defined here.
        """

        self.master.title("Sim Time Logging")

        self.pack(fill=BOTH, expand=1)

        self.textDisplay = StringVar()
        Label(self, textvariable=self.textDisplay).pack()

        myMenu = Menu(self.master)
        self.master.config(menu=myMenu)
        file = Menu(myMenu)

        file.add_command(label="Exit", command=self.KillProgram)
        myMenu.add_cascade(label="File", menu=file)

        edit = Menu(myMenu)
        edit.add_command(label="Change Path", command=self.ChangePath)
        edit.add_command(label="Adjust Timeout",command=self.AdjustTimeout)
        edit.add_command(label="Add Name", command=self.AddName)
        myMenu.add_cascade(label="Edit", menu=edit)

        # button instance
        #quitButton = Button(self, text="Quit", command=self.KillProgram)
        self.startButton = Button(
            self, text="Start time", command=self.StartLogging)
        self.endButton = Button(
            self, text="End time", state = DISABLED, command =self.EndLogging)

        # place buttons
        #quitButton.place(relx=.5, rely=.75, anchor=CENTER)
        self.startButton.place(relx=.5, rely=.25, anchor=CENTER)
        self.endButton.place(relx=.5, rely=.6, anchor=CENTER)

    def AddName(self):
        def StoreNewName():
            myFile = open("SimLogNames.txt", "a")
            myFile.write(str(nameEntry.get()) + "\n")
            myFile.close()
            form.destroy()

        form = Toplevel()
        form.wm_title("New Timeout")
        form.geometry("200x150")

        nameEntry = Entry(form)
        nameEntry.place(relx=.5, rely=.25, anchor=CENTER)
        nameLabel = Label(form, text="New name")
        nameLabel.place(relx=.5, rely=.1, anchor=CENTER)

        submitButton = Button(form, text="Submit", command=StoreNewName)
        submitButton.place(relx=.5, rely=.75, anchor=CENTER)

    def StartLogging(self):
        """
        Called when the Start button is pressed. Creates a new window with
        entry forms for name and purpose, then stores that info in a LoggingData
        class: self.loggingClass.
        """
        def StoreNameandPurpose():
            """
            This nested method defies convention, but the Tkinter button function
            got messy when I tried to call a function and pass arguments.
            """
            #self.loggingClass.SetName(nameEntry.get())
            nameString = ""
            for x in range(len(myList)):
                if myList[x][1].get() == 1:
                    nameString = nameString + myList[x][0] + " / "
            nameString = nameString[0:-2]
            self.loggingClass.SetName(nameString)
            self.loggingClass.SetPurpose(purposeEntry.get())
            self.loggingClass.SetStartTime(datetime.now())

            form.destroy()
            self.endButton["state"] = NORMAL
            self.startButton["state"] = DISABLED
            print(self.loggingClass.startTime)

            self.Countdown(self.timeoutTime)

        form = Toplevel()
        form.wm_title("Information")
        form.geometry("300x400")

        myList = []

        myFile = open("SimLogNames.txt")
        for x in myFile:
            myList.append((x.split("\n")[0],IntVar()))
        myFile.close()

        for y in range(len(myList)):
            Checkbutton(form, text = myList[y][0], \
                        onvalue = 1, offvalue = 0, \
                        height = 2, width = 20, \
                        variable = myList[y][1]).pack()

        purposeEntry = Entry(form)
        purposeLabel = Label(form, text="Task", height = 2)
        purposeLabel.pack()
        purposeEntry.pack()

        emptyLabel = Label(form, text = "", height = 1)
        emptyLabel.pack()

        submitButton = Button(form, text="Submit", command=StoreNameandPurpose)
        submitButton.pack()

    def Countdown(self, count):
        """
        Method responsible for keeping track of timeout. Definitely not the best
        way, but it's how I got it to work. The if/else block functions something
        like a switch statement, with a boolean to keep track of the state when
        time's up (and another bool for prompting a time extension).
        """
        self.DisplayText(str(ConvertSeconds(count)))

        if count <= .25*self.timeoutTime and self.warningFlag:
            self.warningFlag = False
            self.TimeoutPrompt(count)
        elif count == 0 and self.timeoutFlag:
            self.EndLogging()
        elif not self.timeoutFlag:
            self.timeoutFlag = True
            self.warningFlag = True
            count = self.timeoutTime
            root.after(1000, self.Countdown, count)         #Not recursion. Calls the function after int milliseconds
        elif count> 0:
            count = count -1
            root.after(1000, self.Countdown, count)

    def TimeoutPrompt(self, count):
        """
        Window that is created when timeoutTime gets to 25% of it's total.
        Includes the button to reset the time back to it's stored value.
        """
        def ExtendTimeout():
            """
            This nested method defies convention, but the Tkinter button function
            got messy when I tried to call a function and pass arguments.
            """
            self.timeoutFlag = False
            timeoutprompt.destroy()

        timeoutprompt = Toplevel()
        timeoutprompt.wm_title("Timeout Warning")
        timeoutprompt.geometry("600x200")

        nameLabel = Label(timeoutprompt, text="Still Working?")
        nameLabel.place(relx=.5, rely=.1, anchor=CENTER)

        submitButton = Button(timeoutprompt, text="I'm still working", command=ExtendTimeout)
        submitButton.place(relx=.5, rely=.5, anchor=CENTER)

        self.Countdown(count)

    def EndLogging(self):
        """
        Called when timeout is up or when the end button is pressed.
        Tells the loggingClass to store the data in a csv, waits just a bit
        to be absolutely sure everything finishes writing, then ends the program.
        """
        self.loggingClass.CompleteLog()
        time.sleep(1.5)
        self.KillProgram()

    def KillProgram(self):
        """
        Exits the program.
        """
        sys.exit()

    def DisplayText(self, newText):
        """
        Input: str newText
        Output: Updates the message along the top of the window to the string, newText.
        """

        self.textDisplay.set(newText)
        self.update_idletasks()

    def ChangePath(self):
        """
        Changes the path to the directory selected.
        """
        #self.dirPath = filedialog.askdirectory(title="Select Directory")
        self.loggingClass.ChangePath(filedialog.askdirectory(title="Select Directory"))
        try:
            os.exists(self.loggingClass.dirPath)
        except:
            self.loggingClass.ChangePath(outputDir)


    def AdjustTimeout(self):
        """
        Adjusts the amount of time to newTime, in seconds.
        """
        def StoreNewTime():
            self.timeoutTime = int(timeEntry.get())
            form.destroy()
        form = Toplevel()
        form.wm_title("New Timeout")
        form.geometry("200x150")

        timeEntry = Entry(form)
        timeEntry.place(relx=.5, rely=.25, anchor=CENTER)
        timeLabel = Label(form, text="New timeout (in seconds)")
        timeLabel.place(relx=.5, rely=.1, anchor=CENTER)

        submitButton = Button(form, text="Submit", command=StoreNewTime)
        submitButton.place(relx=.5, rely=.75, anchor=CENTER)

def ConvertSeconds(seconds):
    """
    Converts int seconds into str hours:minutes:seconds
    """
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

print("Executing SimLogApp.py")

root = Tk()

root.geometry("600x200")

app = Window(root)

root.mainloop()
