from tkinter import *
from tkinter import simpledialog
import csv
import pandas as pd
from pathlib import Path 




# Initializing the Main Window(Container)
calculator = Tk()

# Assigning our Main Window A title
calculator.title("Co2 Calculator")

# This is the screen that will serve as our display
inputScreen = Entry(calculator, borderwidth=5, width=35)

# Positioning the input screen on the Tkinter's Window grid
inputScreen.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#creating a menubar so the user can change what type of waste they are sorting
menu_bar = Menu(calculator)
calculator.config(menu=menu_bar)
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Waste types", menu=file_menu)
file_menu.add_command(label="Metal", command=lambda: [metal(), button_clear()])
file_menu.add_command(label="Plastic", command=lambda: [plastic(), button_clear()])
file_menu.add_command(label="Paper", command=lambda: [paper(), button_clear()])
file_menu.add_command(label="Glass", command=lambda: [glass(), button_clear()])
file_menu.add_command(label="Cardboard", command=lambda: [paper(), button_clear()])
file_menu.add_command(label="Scoreboard", command=lambda: [scoreboard()])

def scoreboard():
    #Display scoreboard
    for filename in ['/Users/sebastianlarsen/Desktop/Eksamen/Python/Scoreboard.csv']:
        file = pd.read_csv(filename)
        file = file.sort_values('Score', ascending=False).head(10)
        file['Rank'] = file['Score'].rank(ascending=False)
        print(file)
        

def button_clear():
        #Clears the input Screen
        inputScreen.delete(0, END)

def button_click(number):
        #Displays the numbers pressed
        inputScreen.insert(END, number)

    

#Defining functions to make the CO2 calculater work
def metal():

    def button_equals():
    #Triggers display of results
        fnum = inputScreen.get()
        firstNumber = int(fnum)
        inputScreen.insert(0, int(firstNumber) * 5.3)
        a = inputScreen.get()

        user = simpledialog.askstring(title="Competition", prompt="Enter your first & last name to enter the competition?:")
        
        columns = ['Users','Score']
        PATH = '/Users/sebastianlarsen/Desktop/Eksamen/Python/Scoreboard.csv'
        filepath = Path(PATH)
        if not filepath.exists():
            with open(filepath, 'w'):
                filepath.touch()
      
        with open('/Users/sebastianlarsen/Desktop/Eksamen/Python/Scoreboard.csv', 'r') as f:
            reader = [row for row in csv.DictReader(f)]

        with open('/Users/sebastianlarsen/Desktop/Eksamen/Python/Scoreboard.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            is_edited = False
            for row in reader:
                if row['Users'] == user:
                    prev_score = row['Score'].strip() or 0
                    score = float(a) + float(prev_score)
                    row['Score'] = round(score, 2)
                    is_edited = True
                writer.writerow(row)
            if not is_edited:
                score1 = float(a)
                writer.writerow({'Users': user, 'Score': round(score1, 2)})
            

    #declaring the buttons and assign them their respective functions

    buttonOne = Button(calculator, text="1", padx=40, pady=20, command=lambda: button_click(1))
    buttonTwo = Button(calculator, text="2", padx=40, pady=20, command=lambda: button_click(2))
    buttonThree = Button(calculator, text="3", padx=40, pady=20, command=lambda: button_click(3))

    buttonFour = Button(calculator, text="4", padx=40, pady=20, command=lambda: button_click(4))
    buttonFive = Button(calculator, text="5", padx=40, pady=20, command=lambda: button_click(5))
    buttonSix = Button(calculator, text="6", padx=40, pady=20, command=lambda: button_click(6))

    buttonSeven = Button(calculator, text="7", padx=40, pady=20, command=lambda: button_click(7))
    buttonEight = Button(calculator, text="8", padx=40, pady=20, command=lambda: button_click(8))
    buttonNine = Button(calculator, text="9", padx=40, pady=20, command=lambda: button_click(9))

    buttonZero = Button(calculator, text="0", padx=40, pady=20, command=lambda: button_click(0))
    buttondot = Button(calculator, text=".", padx=43, pady=20, command=lambda: button_click('.'))

    buttonEquals = Button(calculator, text="Calculate Co2", padx=119, pady=20, command=button_equals)
    buttonClear = Button(calculator, text="Clear", padx=29, pady=20, command=button_clear)

    buttonOne.grid(row=3, column=0)
    buttonTwo.grid(row=3, column=1)
    buttonThree.grid(row=3, column=2)

    buttonFour.grid(row=2, column=0)
    buttonFive.grid(row=2, column=1)
    buttonSix.grid(row=2, column=2)

    buttonSeven.grid(row=1, column=0)
    buttonEight.grid(row=1, column=1)
    buttonNine.grid(row=1, column=2)

    buttonZero.grid(row=4, column=0)
    buttondot.grid(row=4, column=1)

    buttonEquals.grid(row=5, column=0, columnspan=3) 
    buttonClear.grid(row=4, column=2)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def plastic():

    def button_equals():

        fnum = inputScreen.get()
        firstNumber = int(fnum)
        inputScreen.insert(0, int(firstNumber) * 1.8)
        a = inputScreen.get()
        
        user = simpledialog.askstring(title="Competition", prompt="Enter your first & last name to enter the competition?:")
        
        columns = ['Users','Score']
        PATH = '/Users/sebastianlarsen/Desktop/Eksamen/Python/Scoreboard.csv'
        filepath = Path(PATH)
        if not filepath.exists():
            with open(filepath, 'w'):
                filepath.touch()
      
        with open('/Users/sebastianlarsen/Desktop/Eksamen/Python/Scoreboard.csv', 'r') as f:
            reader = [row for row in csv.DictReader(f)]

        with open('/Users/sebastianlarsen/Desktop/Eksamen/Python/Scoreboard.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            is_edited = False
            for row in reader:
                if row['Users'] == user:
                    prev_score = row['Score'].strip() or 0
                    score = float(a) + float(prev_score)
                    row['Score'] = round(score, 2)
                    is_edited = True
                writer.writerow(row)
            if not is_edited:
                score1 = float(a)
                writer.writerow({'Users': user, 'Score': round(score1, 2)})


    buttonOne = Button(calculator, text="1", padx=40, pady=20, command=lambda: button_click(1))
    buttonTwo = Button(calculator, text="2", padx=40, pady=20, command=lambda: button_click(2))
    buttonThree = Button(calculator, text="3", padx=40, pady=20, command=lambda: button_click(3))

    buttonFour = Button(calculator, text="4", padx=40, pady=20, command=lambda: button_click(4))
    buttonFive = Button(calculator, text="5", padx=40, pady=20, command=lambda: button_click(5))
    buttonSix = Button(calculator, text="6", padx=40, pady=20, command=lambda: button_click(6))

    buttonSeven = Button(calculator, text="7", padx=40, pady=20, command=lambda: button_click(7))
    buttonEight = Button(calculator, text="8", padx=40, pady=20, command=lambda: button_click(8))
    buttonNine = Button(calculator, text="9", padx=40, pady=20, command=lambda: button_click(9))

    buttonZero = Button(calculator, text="0", padx=40, pady=20, command=lambda: button_click(0))
    buttondot = Button(calculator, text=".", padx=43, pady=20, command=lambda: button_click('.'))

    buttonEquals = Button(calculator, text="Calculate Co2", padx=119, pady=20, command=button_equals)
    buttonClear = Button(calculator, text="Clear", padx=29, pady=20, command=button_clear)

    buttonOne.grid(row=3, column=0)
    buttonTwo.grid(row=3, column=1)
    buttonThree.grid(row=3, column=2)

    buttonFour.grid(row=2, column=0)
    buttonFive.grid(row=2, column=1)
    buttonSix.grid(row=2, column=2)

    buttonSeven.grid(row=1, column=0)
    buttonEight.grid(row=1, column=1)
    buttonNine.grid(row=1, column=2)

    buttonZero.grid(row=4, column=0)
    buttondot.grid(row=4, column=1)

    buttonEquals.grid(row=5, column=0, columnspan=3) 
    buttonClear.grid(row=4, column=2)  

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def paper():

    def button_equals():

        fnum = inputScreen.get()
        firstNumber = int(fnum)
        inputScreen.insert(0, int(firstNumber) * 1.6)
        a = inputScreen.get()
        
        user = simpledialog.askstring(title="Competition", prompt="Enter your first & last name to enter the competition?:")
        
        columns = ['Users','Score']
        PATH = '/Users/sebastianlarsen/Desktop/Eksamen/Python/Scoreboard.csv'
        filepath = Path(PATH)
        if not filepath.exists():
            with open(filepath, 'w'):
                filepath.touch()
      
        with open('/Users/sebastianlarsen/Desktop/Eksamen/Python/Scoreboard.csv', 'r') as f:
            reader = [row for row in csv.DictReader(f)]

        with open('/Users/sebastianlarsen/Desktop/Eksamen/Python/Scoreboard.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            is_edited = False
            for row in reader:
                if row['Users'] == user:
                    prev_score = row['Score'].strip() or 0
                    score = float(a) + float(prev_score)
                    row['Score'] = round(score, 2)
                    is_edited = True
                writer.writerow(row)
            if not is_edited:
                score1 = float(a)
                writer.writerow({'Users': user, 'Score': round(score1, 2)})


    buttonOne = Button(calculator, text="1", padx=40, pady=20, command=lambda: button_click(1))
    buttonTwo = Button(calculator, text="2", padx=40, pady=20, command=lambda: button_click(2))
    buttonThree = Button(calculator, text="3", padx=40, pady=20, command=lambda: button_click(3))

    buttonFour = Button(calculator, text="4", padx=40, pady=20, command=lambda: button_click(4))
    buttonFive = Button(calculator, text="5", padx=40, pady=20, command=lambda: button_click(5))
    buttonSix = Button(calculator, text="6", padx=40, pady=20, command=lambda: button_click(6))

    buttonSeven = Button(calculator, text="7", padx=40, pady=20, command=lambda: button_click(7))
    buttonEight = Button(calculator, text="8", padx=40, pady=20, command=lambda: button_click(8))
    buttonNine = Button(calculator, text="9", padx=40, pady=20, command=lambda: button_click(9))

    buttonZero = Button(calculator, text="0", padx=40, pady=20, command=lambda: button_click(0))
    buttondot = Button(calculator, text=".", padx=43, pady=20, command=lambda: button_click('.'))

    buttonEquals = Button(calculator, text="Calculate Co2", padx=119, pady=20, command=button_equals)
    buttonClear = Button(calculator, text="Clear", padx=29, pady=20, command=button_clear)

    buttonOne.grid(row=3, column=0)
    buttonTwo.grid(row=3, column=1)
    buttonThree.grid(row=3, column=2)

    buttonFour.grid(row=2, column=0)
    buttonFive.grid(row=2, column=1)
    buttonSix.grid(row=2, column=2)

    buttonSeven.grid(row=1, column=0)
    buttonEight.grid(row=1, column=1)
    buttonNine.grid(row=1, column=2)

    buttonZero.grid(row=4, column=0)
    buttondot.grid(row=4, column=1)

    buttonEquals.grid(row=5, column=0, columnspan=3) 
    buttonClear.grid(row=4, column=2)  


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def glass():

    def button_equals():
        fnum = inputScreen.get()
        firstNumber = int(fnum)
        inputScreen.insert(0, int(firstNumber) * 0.3)
        a = inputScreen.get()
        
        user = simpledialog.askstring(title="Competition", prompt="Enter your first & last name to enter the competition?:")
        
        columns = ['Users','Score']
        PATH = '/Users/sebastianlarsen/Desktop/Eksamen/Python/Scoreboard.csv'
        filepath = Path(PATH)
        if not filepath.exists():
            with open(filepath, 'w'):
                filepath.touch()
      
        with open('/Users/sebastianlarsen/Desktop/Eksamen/Python/Scoreboard.csv', 'r') as f:
            reader = [row for row in csv.DictReader(f)]

        with open('/Users/sebastianlarsen/Desktop/Eksamen/Python/Scoreboard.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            is_edited = False
            for row in reader:
                if row['Users'] == user:
                    prev_score = row['Score'].strip() or 0
                    score = float(a) + float(prev_score)
                    row['Score'] = round(score, 2)
                    is_edited = True
                writer.writerow(row)
            if not is_edited:
                score1 = float(a)
                writer.writerow({'Users': user, 'Score': round(score1, 2)})


    buttonOne = Button(calculator, text="1", padx=40, pady=20, command=lambda: button_click(1))
    buttonTwo = Button(calculator, text="2", padx=40, pady=20, command=lambda: button_click(2))
    buttonThree = Button(calculator, text="3", padx=40, pady=20, command=lambda: button_click(3))

    buttonFour = Button(calculator, text="4", padx=40, pady=20, command=lambda: button_click(4))
    buttonFive = Button(calculator, text="5", padx=40, pady=20, command=lambda: button_click(5))
    buttonSix = Button(calculator, text="6", padx=40, pady=20, command=lambda: button_click(6))

    buttonSeven = Button(calculator, text="7", padx=40, pady=20, command=lambda: button_click(7))
    buttonEight = Button(calculator, text="8", padx=40, pady=20, command=lambda: button_click(8))
    buttonNine = Button(calculator, text="9", padx=40, pady=20, command=lambda: button_click(9))

    buttonZero = Button(calculator, text="0", padx=40, pady=20, command=lambda: button_click(0))
    buttondot = Button(calculator, text=".", padx=43, pady=20, command=lambda: button_click('.'))

    buttonEquals = Button(calculator, text="Calculate Co2", padx=119, pady=20, command=button_equals)
    buttonClear = Button(calculator, text="Clear", padx=29, pady=20, command=button_clear)

    buttonOne.grid(row=3, column=0)
    buttonTwo.grid(row=3, column=1)
    buttonThree.grid(row=3, column=2)

    buttonFour.grid(row=2, column=0)
    buttonFive.grid(row=2, column=1)
    buttonSix.grid(row=2, column=2)

    buttonSeven.grid(row=1, column=0)
    buttonEight.grid(row=1, column=1)
    buttonNine.grid(row=1, column=2)

    buttonZero.grid(row=4, column=0)
    buttondot.grid(row=4, column=1)

    buttonEquals.grid(row=5, column=0, columnspan=3) 
    buttonClear.grid(row=4, column=2)



calculator.mainloop()
""" mainloop() is an infinite loop used to run the application, wait for an event to occur and
process the event as long as the window is not closed. """

