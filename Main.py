from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

class Main():
    
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title("Theme mode")
        self.root["bg"] = "white"
        self.enabled = IntVar()
        self.mode_theme = 0
        

    def check_button(self):
        self.btn = Checkbutton(text="Dark Mode", variable=self.enabled, command=self.dark_theme, background="white", foreground="gray22")
        self.btn.pack(anchor=NW)

    def bomb(self):
        self.bimba = Label(text=f"BOMB", bg="white", fg="gray22")
        self.bimba.pack(anchor=CENTER, pady=110, padx=1)
        
    def dark_theme(self):
        if self.mode_theme == 0:
            self.btn["text"] = "White mode"
            self.mode_theme = 1
        
        elif self.mode_theme == 1:
            self.btn["text"] = "Dark Mode"
            self.mode_theme = 0

        if self.enabled.get() == 1:
            self.root["bg"] = "gray22"
            self.btn.config(background="gray22", foreground="white")
            self.bimba["bg"] = "gray22"
            self.bimba["fg"] = "white"
                      

            

        elif self.enabled.get() == 0:
            self.root["bg"] = "white"
            self.btn.config(background="white", foreground="gray22")
            self.bimba["bg"] = "white"
            self.bimba["fg"] = "gray22" 

    def boom(self):
        showinfo(message="BOOM")

    

            
            
        
        

    
    
    

        
                
                
    
        

            
        


        
    
            
        
        



    def run(self):

        self.root.mainloop()

cl = Main()
cl.check_button()
cl.bomb()
cl.boom()
cl.dark_theme()
cl.run()
    