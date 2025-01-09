from tkinter import *
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import numpy as np
import csv
 
# diagram generator
class App:
    # define user interface
    def __init__(self, master):
        frame = Frame(master)
        # use grid layout
        frame.grid()
        # diagram label
        self.diagrammLabel = Label(frame, text="Diagram").grid(row=0)
        # open file chooser button
        self.open = Button(frame, text="Open CSV File", command=self.open_file_chooser).grid(row=0, column=2)
        # diagram title input
        self.titleLabel = Label(frame, text="Title:").grid(row=1)
        self.titleInput = Entry(frame)
        self.titleInput.grid(row=1, column=1)
        # x/y axis input
        self.xAxisLabel = Label(frame, text="X-Axis:").grid(row=2)
        self.xAxisInput = Entry(frame)
        self.xAxisInput.grid(row=2, column=1)
        self.yAxisLabel = Label(frame, text="Y-Axis:").grid(row=3)
        self.yAxisInput = Entry(frame)
        self.yAxisInput.grid(row=3, column=1)
        # create diagram button
        self.create = Button(frame, text="Create Diagram", command=self.create_diagram).grid(row=4, column=2)
 
    # define and show diagram
    def create_diagram(self):
        try:
            plt.plot(self.xValues, self.yValues)
            plt.title(self.titleInput.get())
            plt.xlabel(self.xAxisInput.get())
            plt.ylabel(self.yAxisInput.get())
        except AttributeError:
            print("ERROR: Please chose a CSV-File")
 
        plt.show()
 
    # open file chooser for csv files
    def open_file_chooser(self):
        filename = askopenfilename(filetypes=(("csv Files", "*.csv"),("CSV Files", "*.CSV")), title="Choose a file")
        if not filename:
            print("ERROR: You have to choose a CSV-File")
            return
        csvFile = open(filename, "rt")
        reader = csv.reader(csvFile, delimiter=';')
        # cast string array to float array for diagram
        xStrings = np.array(next(reader))
        yStrings = np.array(next(reader))
        # check array lengths
        if len(xStrings) != len(yStrings):
            print("ERROR: Value arrays in file " + filename + " do not have the same length")
        # store arrays to variables
        try:
            self.xValues = xStrings.astype(np.float)
            self.yValues = yStrings.astype(np.float)
        except ValueError:
            print("ERROR: Values in CSV-File have to be numeric")
             
 
# start application
root = Tk()
root.title("Diagram-Creator")
app = App(root)
root.mainloop()
