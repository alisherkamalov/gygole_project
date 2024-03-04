from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class Main():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("720x580")
        self.root.title("Gygole")
        self.root["bg"] = "white"
        
        self.load = Loading_and_reg_auth()
        self.load.loading(self.root)
        
        self.root.mainloop()

class Loading_and_reg_auth():
    def loading(self, root):
        self.style = ttk.Style()
        self.style.configure("My.TFrame", background="white")
        self.root = root
        self.load = 0
        self.reg_btn = 0
        
        self.frame = ttk.Frame(root, padding=[1], style="My.TFrame")
        self.frame.pack(anchor="n", pady=200)

        self.photo = Image.open("logo4.jpg")
        self.photo1 = ImageTk.PhotoImage(self.photo)
        self.label_photo = ttk.Label(self.frame, image=self.photo1, background="white")
        self.label_photo.pack(anchor="n", pady=[0,10])

        self.loading_label = ttk.Label(self.frame, text="Loading", font=("Helvetica",20), background="white", foreground="gray22", wraplength=500)
        self.loading_label.pack(anchor="s", pady=[10,0])
        
        self.move_load(0)  

    def move_load(self, count=0):
        self.canvas = Canvas(self.frame, bg="white", highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=True, padx=10)

        rectangle = self.canvas.create_rectangle(30, 10, 50, 20, outline="gray22", fill="gray22")

        def animate():
            nonlocal count
            if count < 20:
                self.canvas.move(rectangle, 15, 0)
            elif count < 40:
                self.canvas.move(rectangle, -15, 0)
            elif count < 60:
                self.canvas.move(rectangle, 15, 0)
            elif count < 80:
                self.canvas.move(rectangle, -15, 0)
            else:
                self.canvas.move(rectangle, 0, 0) 

            count += 1
            if count < 100:
                self.root.after(50, animate)
            else:
                self.execute_after_animation()

        animate()

    def execute_after_animation(self):
        self.loading_label.destroy()
        self.frame.pack_configure(pady=10)
        self.load = 3  
        self.canvas.destroy()

        self.registration_and_authorization_button()  

    def registration_and_authorization_button(self):
        self.click_reg = 0
        self.click_auth = 0
        self.style2 = ttk.Style()
        self.style2.configure("My.TButton", background="white", foreground="gray22")

        if self.load == 3:  
            self.reg_btn = ttk.Button(self.frame, text="Registration", style="My.TButton", command=self.registration)
            self.reg_btn.pack(side="left", padx=[0,20], pady=15)

            self.auth_btn = ttk.Button(self.frame, text="Authorization", style="My.TButton", command=self.authorization)
            self.auth_btn.pack(side="right", padx=[20,0],pady=15)
            
            self.exit_btn = ttk.Button(self.root, text="Exit", command=self.exit_app, style="My.TButton")
            self.exit_btn.pack(side=TOP)

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
        self.style3 = ttk.Style()
        self.style3.configure("My.TLabel", background="white", foreground="gray22")

        self.frame2 = ttk.Frame(self.root, padding=[1], relief=SOLID, style="My.TLabel")
        self.frame2.pack(anchor="n", pady=25)
            
            
        self.name_reg = ttk.Label(self.frame2, text="Name:", style="My.TLabel")
        self.name_reg.pack(anchor="w", pady=10, padx=10)
            
        self.name_reg_en = ttk.Entry(self.frame2, width=30)
        self.name_reg_en.pack(anchor="w", pady=10, padx=10)
            
        self.pass_reg = ttk.Label(self.frame2, text="Password:", style="My.TLabel")
        self.pass_reg.pack(anchor="w", pady=10, padx=10)
            
            
        self.pass_reg_en = ttk.Entry(self.frame2, width=30)
        self.pass_reg_en.pack(anchor="w", pady=10, padx=10)
            
        
            
        self.reg_btn.pack_configure(anchor="center", padx=[75,0])

        
        
        self.auth_btn.destroy()

        def save_info():
                name = self.name_reg_en.get()
                password = self.pass_reg_en.get()
                self.save_name_and_pass(name, password)
                self.reg_btn = 1
                if self.reg_btn == 1:
                    messagebox.showinfo("Save_info", f"Successful new account: {name}")
                    self.reg_btn = 2


        self.reg_acc = ttk.Button(self.frame2, text="sign up", command=save_info)
            
        self.reg_acc.pack(anchor="sw", pady=15, padx=10)
        self.reg_btn = 1
        
        self.exit_btn.destroy()

    def authorization(self):
        self.style4 = ttk.Style()
        self.style4.configure("My.TLabel", background="white", foreground="gray22")

        if self.click_auth == self.click_reg:
            
            self.frame2 = ttk.Frame(self.root, padding=[1], relief=SOLID, style="My.TLabel")
            self.frame2.pack(anchor="n", pady=25)
            
            self.name_reg = ttk.Label(self.frame2, text="Name:", style="My.TLabel")
            self.name_reg.pack(anchor="w", pady=10, padx=10)
            
            self.name_reg_en = ttk.Entry(self.frame2, width=30)
            self.name_reg_en.pack(anchor="w", pady=10, padx=10)
            
            self.pass_reg = ttk.Label(self.frame2, text="Password:", style="My.TLabel")
            self.pass_reg.pack(anchor="w", pady=10, padx=10)
            
            self.pass_reg_en = ttk.Entry(self.frame2, width=30)
            self.pass_reg_en.pack(anchor="w", pady=10, padx=10)



            def login():
                name = self.name_reg_en.get()
                password = self.pass_reg_en.get()
                if self.check_base(name, password):
                    messagebox.showinfo("Login", "Successful login!")
                    self.frame2.pack_forget()
                    self.auth_btn.destroy()

                    name_user = ttk.Label(self.root, text=f"Account: {name}", style="My.TLabel", font=("Helvetica", 25))
                    name_user.pack(anchor="nw")
                    

                    




                else:
                    messagebox.showerror("Login", "FAILED")
            
            self.reg_acc = ttk.Button(self.frame2, text="sign in", command=login)
            self.reg_acc.pack(anchor="sw", pady=10, padx=10)

            self.click_auth = 2
            
            
            self.auth_btn.pack_configure(anchor="n", pady=10, padx=[0,65])

            

            self.back_auth = ttk.Button(self.frame2, text="Back", command=self.back_auth_btn)
            self.back_auth.pack(anchor="sw", pady=10, padx=10)
            self.reg_btn.destroy()
            self.exit_btn.destroy()

    

    def back_auth_btn(self):
        self.frame2.pack_forget()
        self.auth_btn.destroy()
        self.registration_and_authorization_button()
        
    def exit_app(self):
        self.root.destroy()
            
if __name__ == "__main__":
    app = Main()
