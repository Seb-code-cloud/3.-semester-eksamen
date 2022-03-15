#importing required Libaries
from tkinter import *
import vlc


Sounds_path = ["/Users/sebastianlarsen/Desktop/Eksamen/Python/Residual.mp3", "/Users/sebastianlarsen/Desktop/Eksamen/Python/Bulkywaste.mp3"
,"/Users/sebastianlarsen/Desktop/Eksamen/Python/Cardboard.mp3", "/Users/sebastianlarsen/Desktop/Eksamen/Python/Electronic.mp3"
,"/Users/sebastianlarsen/Desktop/Eksamen/Python/softplastic.mp3", "/Users/sebastianlarsen/Desktop/Eksamen/Python/Glass.mp3"
,"/Users/sebastianlarsen/Desktop/Eksamen/Python/Hazardous.mp3", "/Users/sebastianlarsen/Desktop/Eksamen/Python/Metal.mp3"
,"/Users/sebastianlarsen/Desktop/Eksamen/Python/Paper.mp3", "/Users/sebastianlarsen/Desktop/Eksamen/Python/Porcelain.mp3"
,"/Users/sebastianlarsen/Desktop/Eksamen/Python/Batteries.mp3", "/Users/sebastianlarsen/Desktop/Eksamen/Python/FluorescentLamps.mp3"
,"/Users/sebastianlarsen/Desktop/Eksamen/Python/Sanitaion.mp3", "/Users/sebastianlarsen/Desktop/Eksamen/Python/PVC.mp3"
,"/Users/sebastianlarsen/Desktop/Eksamen/Python/SmallCombustible.mp3"]


#Creating an instance of Tkniter frame
win = Tk()
win.title("Waste sorting station")
win.geometry("800x500")
win.configure(background="white")

def Residual_Waste():
	f1 = Frame(win, bg="black", width=500, height=350)
	f1.place(x=0, y=190)
	player = vlc.MediaPlayer(Sounds_path[0])
	player.play()

def Bulky_waste():
	f1 = Frame(win, bg="dark green", width=500, height=350)
	f1.place(x=0, y=190)
	player = vlc.MediaPlayer(Sounds_path[1])
	player.play()

def Cardboard():
	f1 = Frame(win, bg="yellow", width=500, height=350)
	f1.place(x=0, y=190)
	player = vlc.MediaPlayer(Sounds_path[2])
	player.play()

def Electornic_waste():
	f1 = Frame(win, bg="orange", width=500, height=350)
	f1.place(x=0, y=190)
	player = vlc.MediaPlayer(Sounds_path[3])
	player.play()

def Soft_plastic():
	f1 = Frame(win, bg="pink", width=500, height=350)
	f1.place(x=0, y=190)
	player = vlc.MediaPlayer(Sounds_path[4])
	player.play()
	
def Glass():
	f1 = Frame(win, bg="green", width=500, height=350)
	f1.place(x=0, y=190)
	player = vlc.MediaPlayer(Sounds_path[5])
	player.play()
	
def Hazardous_Waste():
	f1 = Frame(win, bg="red", width=500, height=350)
	f1.place(x=0, y=190)
	player = vlc.MediaPlayer(Sounds_path[6])
	player.play()
	
def Metal():
	f1 = Frame(win, bg="grey", width=500, height=350)
	f1.place(x=0, y=190)
	player = vlc.MediaPlayer(Sounds_path[7])
	player.play()
	
def Paper():
	f1 = Frame(win, bg="blue", width=500, height=350)
	f1.place(x=0, y=190)
	player = vlc.MediaPlayer(Sounds_path[8])
	player.play()
	
def Porcelain():
	f1= Frame(win, bg="turquoise", width=500, height=350)
	f1.place(x=0, y=190)
	player = vlc.MediaPlayer(Sounds_path[9])
	player.play()
	
def Batteries():
	f1 = Frame(win, bg="dark red", width=500, height=350)
	f1.place(x=0, y=190)
	player = vlc.MediaPlayer(Sounds_path[10])
	player.play()
	
def Fluorescent_Lamps():
	f1 = Frame(win, bg="dark orange", width=500, height=350)
	f1.place(x=0, y=190)
	player = vlc.MediaPlayer(Sounds_path[11])
	player.play()
	
def Sanitation():
	f1 = Frame(win, bg="dark blue", width=500, height=350)
	f1.place(x=0, y=190)
	player = vlc.MediaPlayer(Sounds_path[12])
	player.play()

def PVC_plast():
	f1 = Frame(win, bg="purple", width=500, height=350)
	f1.place(x=0, y=190)
	player = vlc.MediaPlayer(Sounds_path[13])
	player.play()

def Small_Combustible():
	f1 = Frame(win, bg="white", width=500, height=350)
	f1.place(x=0, y=190)
	player = vlc.MediaPlayer(Sounds_path[14])
	player.play()
	


b1 = Button(win, text="Residual Waste", command = Residual_Waste)
b2 = Button(win, text="Bulky Waste", command = Bulky_waste)
b3 = Button(win, text="Cardboard", command = Cardboard)
b4 = Button(win, text="Electornic Waste", command = Electornic_waste)
b5 = Button(win, text="Soft Plastic", command = Soft_plastic)
b6 = Button(win, text="Glass", command = Glass)
b7 = Button(win, text="Hazardous Waste", command = Hazardous_Waste)
b8 = Button(win, text="Metal", command = Metal)
b9 = Button(win, text="Paper", command = Paper)
b10 = Button(win, text="Porcelain", command = Porcelain)
b11 = Button(win, text="Batteries", command = Batteries)
b12 = Button(win, text="Fluorescent Lamps", command = Fluorescent_Lamps)
b13 = Button(win, text="Sanitation", command = Sanitation)
b14 = Button(win, text="PVC-plast", command = PVC_plast)
b15 = Button(win, text="Small Combustible", command = Small_Combustible)



b1.place(x=0, y=1)
b2.place(x=0, y=35)
b3.place(x=0, y=70)
b4.place(x=0, y=105)
b5.place(x=0, y=140)
b6.place(x=150, y=1)
b7.place(x=150, y=35)
b8.place(x=150, y=70)
b9.place(x=150, y=105)
b10.place(x=150, y=140)
b11.place(x=300, y=0)
b12.place(x=300, y=35)
b13.place(x=300, y=70)
b14.place(x=300, y=105)
b15.place(x=300, y=140)



win.mainloop()


