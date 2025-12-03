from tkinter import *
import csv

class GUI:
    def __init__(self, window):
        self.window = window;

        self.frameN = Frame(self.window)
        self.labelN = Label(self.frameN, text = "Name");
        self.inputN = Entry(self.frameN);
        self.labelN.pack(side = 'left')
        self.inputN.pack(padx = 5, side = 'left')
        self.frameN.pack(anchor = 'w', padx = 10, pady = 10);

        
        self.frameA = Frame(self.window)
        self.labelA = Label(self.frameA, text = "Age");
        self.inputA = Entry(self.frameA);
        self.labelA.pack(side = 'left')
        self.inputA.pack(padx = 15, side = 'left')
        self.frameA.pack(anchor = 'w', padx = 10, pady = 10);

        self.frameR = Frame(self.window)
        self.selection = IntVar()
        self.labelR = Label(self.frameR, text = "Status")
        self.radio1 = Radiobutton(self.frameR, text = "Student", variable=self.selection, value=1)
        self.radio2 = Radiobutton(self.frameR, text = "Staff", variable=self.selection, value=2)
        self.radio3 = Radiobutton(self.frameR, text = "Both", variable=self.selection, value=3)
        self.labelR.pack(side='left')
        self.radio1.pack(side='left')
        self.radio2.pack(side='left')
        self.radio3.pack(side='left')
        self.frameR.pack(anchor='w',padx = 10, pady=10)

        self.frameB = Frame(self.window)
        self.buttonB = Button(self.frameB, text="SAVE", command=self.submit)
        self.buttonB.pack(anchor='center')
        self.frameB.pack(anchor='center',padx=10,pady=10)

        self.statusL = StringVar()
        self.statusL.set("Please fill out all values")
        self.frameL = Frame(self.window)
        self.labelL = Label(self.frameL, textvariable=self.statusL)
        self.labelL.pack(anchor='center')
        self.frameL.pack(anchor='center',padx=10)


    def submit(self):
        nametext = self.inputN.get().strip()
        agetext = self.inputA.get().strip()
        statusint = self.selection.get();
        
        ageval = -1;

        if (len(agetext) == 0):
            self.statusL.set("Enter correct age value");
            return -1
        else:
            try:
                ageval = int(agetext);
            except ValueError:
                self.statusL.set("Enter correct age value");
                return -1;
            if (ageval < 0):
                self.statusL.set("Enter correct age value");
                return -1;


        if (len(nametext) == 0):
            nametext = "Anonymous";

        ageval = ageval * 10

        statustext = "NA"
        if (statusint == 1):
            statustext = "Student";
        elif (statusint == 2):
            statustext = "Staff";
        elif (statusint == 3):
            statustext = "Both";
        else:
            statustext = "NA";


        # write
        file_name = "./data.csv"
        new_row_data = [nametext,ageval,statustext];
        try:
            with open(file_name, "a", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(new_row_data)
        except:
            return -1
        # Clear entry stuffs and focus
        self.inputA.delete(0,END)
        self.inputN.delete(0,END)
        self.selection.set(0)
        self.inputN.focus_set()
        self.statusL.set("")
