from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Main():
    def __init__(self):
        self.click_reg = 0
        self.click_auth = 0
        self.reg_btn = 0
        self.root = Tk()
        self.root["bg"] = "white"
        self.root.title("Program Gygole")
        self.root.geometry("400x400")
        self.enabled = IntVar()
        self.mode_theme = 0
        self.load_complete = 0


        
        
        self.btn_reg = Button(self.frame, text="Registration", command=self.registration, bg="white")
        self.btn_reg.pack(anchor=NW, fill=X)

        self.btn_auth = Button(self.frame, text="Authorization", command=self.authorization, bg="white")
        self.btn_auth.pack(anchor=NW, fill=X)

            

        self.dark_btn = Checkbutton(text="Dark Mode", variable=self.enabled, command=self.theme_mode, bg="white")
        self.dark_btn.pack(anchor=SW)
        
            


        

        

    
        
        
    def save_name_and_pass(self, name, password):
        with open("base.txt", "a") as save_n_p:
            save_n_p.write(name + ":" + password + "\n")

    def check_base(self, name, password):
        with open("base.txt", "r") as file:
            for line in file:
                stored_name, stored_password = line.strip().split(":")
                if name == stored_name and password == stored_password:
                    return True
        return False

    def registration(self):
        if self.click_reg == self.click_auth:
            
            self.regist_name = Label(text="Name:", bg="white")
            self.regist_name.pack(anchor=W, pady=6)

            self.enter_name = Entry()
            self.enter_name.pack(anchor=W, pady=6)

            self.reg_pass = Label(text="Password:", bg="white")
            self.reg_pass.pack(anchor=W, pady=6)

            self.enter_pass = Entry()
            self.enter_pass.pack(anchor=W, pady=10)

            
            

            def save_info():
                name = self.enter_name.get()
                password = self.enter_pass.get()
                self.save_name_and_pass(name, password)
                self.reg_btn += 1
                if self.reg_btn == 1:
                    succes_reg = Label(text=f"Successful new account: {name}", bg="white", fg="gray22")
                    succes_reg.pack(anchor=SW, pady=5)
                    self.reg_btn -= 1
                
            self.reg_acc = Button(text="Registration Account", command=save_info, background="white")
            self.reg_acc.pack(anchor=SW)
            

            self.click_reg += 2

    def authorization(self):
        if self.click_auth == 0:
            self.click_auth += 1
            if self.click_auth > self.click_reg:
                self.names_auth = Label(text="Name Account:", bg="white")
                self.names_auth.pack(anchor=W, pady=6)

                self.enter_auth_name = Entry()
                self.enter_auth_name.pack(anchor=W, pady=6)

                self.pass_auth = Label(text="Password Account:", bg="white")
                self.pass_auth.pack(anchor=W, pady=6)

                self.enter_auth_pass = Entry()
                self.enter_auth_pass.pack(anchor=W, pady=6)

                def login():
                    name = self.enter_auth_name.get()
                    password = self.enter_auth_pass.get()
                    if self.check_base(name, password):
                        messagebox.showinfo("Login", "Successful login!")
                    
                        
                    else:
                        messagebox.showerror("Login", "FAILED")
                        

                self.auth_acc = Button(text="Authorization Account", command=login, bg="white")
                self.auth_acc.pack(anchor=SW)
        
    def theme_mode(self):

        
        
            
        
        if self.enabled.get() == 1:

            
            self.root["bg"] = "gray22"

            self.dark_btn["text"] = "Dark Mode"
            self.mode_theme = 0

            self.dark_btn["bg"] = "gray22"
            self.dark_btn["fg"] = "white"

            self.btn_reg["bg"] = "gray22"
            self.btn_reg["fg"] = "white"

            self.btn_auth["bg"] = "gray22"
            self.btn_auth["fg"] = "white"

            

            if hasattr(self, "regist_name"):
                self.regist_name["bg"] = "gray22"
                self.regist_name["fg"] = "white"

                self.enter_name["bg"] = "gray22"
                self.enter_name["fg"] = "white"

                self.reg_pass["bg"] = "gray22"
                self.reg_pass["fg"] = "white"

                self.enter_pass["bg"] = "gray22"
                self.enter_pass["fg"] = "white"

                self.reg_acc["bg"] = "gray22"
                self.reg_acc["fg"] = "white"

                
                

                

            if hasattr(self, "names_auth"):

                self.names_auth["bg"] = "gray22"
                self.names_auth["fg"] = "white"

                self.enter_auth_name["bg"] = "gray22"
                self.enter_auth_name["fg"] = "white"

                self.pass_auth["bg"] = "gray22"
                self.pass_auth["fg"] = "white"

                self.enter_auth_pass["bg"] = "gray22"
                self.enter_auth_pass["fg"] = "white"

                self.auth_acc["bg"] = "gray22"
                self.auth_acc["fg"] = "white"
               

                

                
            
                

                

            
        elif self.enabled.get() == 0:

            self.root["bg"] = "white"

            self.dark_btn["text"] = "White mode"
            self.mode_theme = 1

            

                

            
            

            self.dark_btn["bg"] = "white"
            self.dark_btn["fg"] = "gray22"

            self.btn_reg["bg"] = "white"
            self.btn_reg["fg"] = "gray22"


            self.btn_auth["bg"] = "white"
            self.btn_auth["fg"] = "gray22"

            

            if hasattr(self, "regist_name"):
                self.regist_name["bg"] = "white"
                self.regist_name["fg"] = "gray22"

                self.enter_name["bg"] = "white"
                self.enter_name["fg"] = "gray22"

                self.reg_pass["bg"] = "white"
                self.reg_pass["fg"] = "gray22"

                self.enter_pass["bg"] = "white"
                self.enter_pass["fg"] = "gray22"

                self.reg_acc["bg"] = "white"
                self.reg_acc["fg"] = "gray22"

                
                
               
                

            if hasattr(self, "names_auth"):
                self.names_auth["bg"] = "white"
                self.names_auth["fg"] = "gray22"

                self.enter_auth_name["bg"] = "white"
                self.enter_auth_name["fg"] = "gray22"

                self.pass_auth["bg"] = "white"
                self.pass_auth["fg"] = "gray22"

                self.enter_auth_pass["bg"] = "white"
                self.enter_auth_pass["fg"] = "gray22"

                self.auth_acc["bg"] = "white"
                self.auth_acc["fg"] = "gray22"

                

            

                    

                

                

            

        

    def run(self):
        self.root.mainloop()

cl = Main()
cl.run()
