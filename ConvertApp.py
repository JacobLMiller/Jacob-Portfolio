import pandas as pd
import os
import glob
import shutil
import sys
from tkinter import filedialog
from tkinter import *

##################################################################
# Filename: ConvertApp.py
#
# Author: Jacob Miller
#
# Date: 07/29/2020
#
# Written in: Python 3.6.9
#
# Libraries: pandas, tkinter, shutil, os, glob, sys
#
# Purpose: To convert all xlsx (excel) files in a
#          directory into csv files. Removes empty spaces
#          and automates an otherwise tedious task.
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

outfile = ""


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.dirPath = ""

    def init_window(self):
        """
        This method initializes the window. Buttons, menus, and text are defined here.
        """

        self.master.title("xlsx to csv converter")

        self.pack(fill=BOTH, expand=1)

        self.textDisplay = StringVar()
        Label(self, textvariable=self.textDisplay).pack()

        myMenu = Menu(self.master)
        self.master.config(menu=myMenu)
        file = Menu(myMenu)

        file.add_command(label="Exit", command=self.KillProgram)
        myMenu.add_cascade(label="File", menu=file)
        edit = Menu(myMenu)

        # button instance
        quitButton = Button(self, text="Quit", command=self.KillProgram)
        askDirectoryButton = Button(
            self, text="Select Directory", command=self.SelectDirectory)
        self.executeButton = Button(
            self, text="Convert .xlsx Files", command=self.ConvertCSV, state=DISABLED)

        # place buttons
        quitButton.place(relx=.5, rely=.75, anchor=CENTER)
        askDirectoryButton.place(relx=.5, rely=.25, anchor=CENTER)
        self.executeButton.place(relx=.5, rely=.5, anchor=CENTER)

    def KillProgram(self):
        """
        Exits the program.
        """

        sys.exit()

    def DisplayText(self, newText):
        """
        Input: str newText
        Output: Updates the message along the top of the window to the string newText.
        """

        self.textDisplay.set(newText)
        self.update_idletasks()

    def SelectDirectory(self):
        """
        Called when the Select Directory button is pressed. Asks the operating system for a window
        that the user can use to select the desired directory. Saves the path to a class string, dirPath.
        Will also display the number of excel files in the directory.
        """

        self.dirPath = filedialog.askdirectory(title="Select Directory")
        if self.dirPath != "":
            self.executeButton["state"] = NORMAL
            self.DisplayText(str(len(self.GetExcel())) + " xlsx files found.")

    def ConvertCSV(self):
        """
               Iterates through a list of excel files from GetExcel(), loads them into a pandas dataframe,
           passes it to FixRows(), FixColumns(), and saves each new dataframe to a .csv with the same name.
               """

        excelFiles = self.GetExcel()
        self.DisplayText("0 of " + str(len(excelFiles)) + " completed.")
        for x in excelFiles:
            outfile = x.split(".")[0] + ".csv"
            myClass = pd.read_excel(x)
            myClass = self.FixRows(myClass)
            myClass = self.FixColumns(myClass)
            myClass.to_csv(outfile, index=False, encoding="utf-8")
            self.DisplayText(str(excelFiles.index(x) + 1) +
                             " of " + str(len(excelFiles)) + " completed.")
        self.CleanUp()

    def FixRows(self, myFile):
        """
        This method looks for any rows that are duplicates of the header row (a recurring problem in the original
        dataset this was written for) and returns the dataframe with those rows dropped. Will only noticeably affect
        performance on very large spreadsheets.
        """

        myList = []
        defString = str(myFile.columns.values[0])
        for x in myFile.iterrows():
            if x[1][0] == defString:
                myList.append(x[0])
        return myFile.drop(myFile.index[myList])

    def FixColumns(self, myFile):
        """
        This method removes empty columns from the spreadsheet by adding the indices
        of any empty columns (by checking if "Unnamed" is in the header row) and returns
        the dataframe with those columns dropped.
        """

        myList = []
        myColumns = list(myFile)
        for x in range(len(myColumns)):
            if "Unnamed" in myColumns[x]:
                myList.append(x)

        return myFile.drop(columns=myFile.columns[myList])

    def GetExcel(self):
        """
        This function first checks the selected directory exists,
        then returns a list of all .xlsx files in the directory.
        """

        try:
            os.chdir(self.dirPath)
        except FileNotFoundError:
            print("No such file or directory.")
            self.DisplayText(
                "Error. File directory not found, please try again.")

        return glob.glob("*xlsx")

    def CleanUp(self):
        """
        This function will move all .xlsx files into a folder called "Raw_Files",
        move all .csv files into a folder called "CSV_Files", and all other file extensions (if
        there are any left) into a folder titled, "Other."
        """

        if not os.path.exists("Raw_Files"):
            os.mkdir("Raw_Files")
        if not os.path.exists("CSV_Files"):
            os.mkdir("CSV_Files")
        for x in glob.glob("*xlsx"):
            shutil.move(x, "Raw_Files/" + x)
        for x in glob.glob("*csv"):
            shutil.move(x, "CSV_Files/" + x)
        if len(glob.glob("*.*")) > 0:
            if not os.path.exists("Other"):
                os.mkdir("Other")
            for x in glob.glob("*.*"):
                shutil.move(x, "Other/" + x)

print("Running ConvertApp.py")

root = Tk()

# Window size
root.geometry("600x200")

app = Window(root)

root.mainloop()
