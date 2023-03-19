from tkinter import *
from tkinter import ttk
import tkinter.font as font


DIAGONALE_GD = "diagonale_gauche_droite"
DIAGONALE_DG = "diagonale_droite_gauche"
LIGNE_HORIZONTAL = "ligne_horizontale"
LIGNE_VERTICAL = "ligne_verticale"



class Jeu:

	def __init__(self):
		
		self.gameMap = [ 
					["P","B","G","N","I","Z","Y","I"],
					["B","H","Y","A","W","Q","U","A"],
					["H","R","D","T","P","O","V","W"],
					["L","J","G","Z","I","M","R","F"],
					["E","X","B","N","K","W","T","Y"],
					["X","T","S","L","G","Y","H","O"],
					["V","J","A","R","O","Y","F","P"],
					["P","M","H","E","I","M","A","U"]]


	
		self.gameWindow = Tk()
		self.gameWindow.title("Mot Croisé") 
		self.gameWindow.geometry("1200x650+400+250")
		self.gameWindow.minsize(width = 1200, height = 650) 
		self.gameWindow.maxsize(width = 1200, height = 650) 
		self.gameWindow.configure(bg="#45458B")

		
		self.valideBtn = Button(self.gameWindow, text = "Valider", bg = "green", fg = "white")
		self.valideBtn.place(x = 800, y = 150)


		
		self.leaveBtn = Button(self.gameWindow,text="Quitter",bg = "red",fg = "white",command=self.gameWindow.destroy, font = font.Font(size=15))
		self.leaveBtn.place(x = 900, y = 420) 


		
		self.MotLabel = Label(self.gameWindow,text = "")


		
		self.mot = Mot(self.MotLabel)


		
		posy = 40 
		for x in range(len(self.gameMap)): 
			posx = 40 
			for y in range(len(self.gameMap[0])):
				lettre = Lettre(self.gameMap[x][y],x,y,self) 
				lettre.boutton.place(x=posx, y=posy) 
				self.gameMap[x][y] = lettre
				posx+=75 
			posy += 75 


		
		self.ClearLettersBtn = Button(self.gameWindow,text = "Clear", command = None)
		self.ClearLettersBtn.place(x = 800, y = 420)

		def clear(self):
			for listeLettre in self.gameMap:
				for lettre in listeLettre:
					if lettre.isClicked:
						lettre.isClicked = False
						lettre.boutton.confgure(bg = "#9090EE",activebackground="#A3A3FE")


		self.gameWindow.mainloop()



class Lettre:

	def __init__(self,lettre,x,y,game):

		self.index = -1
		self.mot = game.mot
		self.gameWindow = game.gameWindow
		self.gameMap = game.gameMap 
		self.isClicked = False 
		self.x = x 
		self.y = y 
		self.lettre = lettre
		self.boutton = Button(self.gameWindow,text="".join(lettre),
			width = 3, height = 1, font = font.Font(size=20),
			bg="#9090EE", activebackground="#A3A3FE", bd=0,
			command=self.clicked)


	def clicked(self): 

		if self.isClicked:
			self.boutton.configure(bg = "#9090EE",activebackground="#A3A3FE")
			self.isClicked = False
			self.mot.mot = [self.mot.mot[i] for i in range(len(self.mot.mot)) if self != self.mot.mot[i]]
		
		else: 
			
			if self.x+1 < len(self.gameMap[0]) and self.gameMap[self.x+1][self.y].isClicked:
				self.mot.ajouterLettre(self)
				self.index = len(self.mot.mot)-1
				self.boutton.configure(bg = "red",activebackground="red")
				self.isClicked = True
				print(f"la lettre {self.lettre} est cliqué en haut de la lettre {self.gameMap[self.x+1][self.y].lettre}")

			
			elif self.x-1 > 0 and self.gameMap[self.x-1][self.y].isClicked:
				self.mot.ajouterLettre(self)
				self.index = len(self.mot.mot)-1
				self.boutton.configure(bg = "red",activebackground="red")
				self.isClicked = True
				print(f"la lettre {self.lettre} est cliqué en bas de la lettre {self.gameMap[self.x-1][self.y].lettre}")

			
			elif self.y+1 < len(self.gameMap) and self.gameMap[self.x][self.y+1].isClicked:
				self.mot.ajouterLettre(self)
				self.index = len(self.mot.mot)-1
				self.boutton.configure(bg = "red",activebackground="red")
				self.isClicked = True
				print(f"la lettre {self.lettre} est cliqué à gauche de la lettre {self.gameMap[self.x][self.y+1].lettre}")

			
			elif self.y-1 > 0 and self.gameMap[self.x][self.y-1].isClicked:
				self.mot.ajouterLettre(self)
				self.index = len(self.mot.mot)-1
				self.boutton.configure(bg = "red",activebackground="red")
				self.isClicked = True
				print(f"la lettre {self.lettre} est cliqué à droite de {self.gameMap[self.x][self.y-1].lettre}")

			else:
				self.mot.ajouterLettre(self)
				self.boutton.configure(bg = "red",activebackground="red")
				self.isClicked = True
				

		print(f"le mot est {self.mot.afficherMot()}")

class Mot:

	def __init__(self,displayLabel):
		self.mot = []
		self.displayLabel = displayLabel
		self.direction = None

	def ajouterLettre(self, lettre):
		self.mot.append(lettre)

	def afficherMot(self):
		return "".join(self.mot[i].lettre for i in range(len(self.mot)))
		

	