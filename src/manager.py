
from tkinter.constants import BOTH, CENTER, END, LEFT, RIGHT, VERTICAL, Y
from tkinter import Button, Canvas, Entry, Frame, Label, Scrollbar, Tk, messagebox
from functools import partial

from src.constant import *
from src.account import Account
from src.JsonHandler import JSONFileEditor
from src.Encryptor import Encryptor
from src.generator import PasswordGenerator

class PasswordManager:

    def __init__(self):
        self.window = Tk()
        self.window.update()
        self.window.title("Password Manager")
        self.window.geometry(WINDOW_SIZE)
        self.window.config(bg=THEME_COLOR)
        self.secret_file = "secret.json"

    def home_window(self):
        self.signup_button_frame.grid_remove()
        self.button_frame.grid(row=0, column=0, columnspan=2, padx=80, pady=75)

    def login(self):
        self.button_frame.grid_remove()
        self.login_button_frame = Frame(self.window, bg=THEME_COLOR)
        self.login_button_frame.grid(row=0, column=0, columnspan=2, pady=50)

        self.user_id_label = Label(self.login_button_frame,
                                text="Enter your user id",
                                bg = THEME_COLOR,
                                font=(FONT,LABEL_FONT_SIZE))
        self.user_id_label.grid(row=0,column=0,sticky=LEFT,padx=20,pady=20)

        self.id_box_login = Entry(self.login_button_frame, width=30)
        self.id_box_login.grid(row=0, column=1,sticky=LEFT, padx=20, pady=20)
        self.id_box_login.focus()

        self.key_label = Label(self.login_button_frame,
                                text="Enter Master Password",
                                bg = THEME_COLOR,
                                font=(FONT,LABEL_FONT_SIZE))
        self.key_label.grid(row=1,column=0,sticky=LEFT,padx=20,pady=20)

        self.key_entry_box = Entry(self.login_button_frame, width=30, show="*")
        self.key_entry_box.grid(row=1, column=1,sticky=LEFT, padx=20, pady=20)

        self.check_btn = Button(self.login_button_frame, 
                                text="Submit",bg=BTN_COLOR,
                                command=self.check_master_password,
                                width=15)
        self.check_btn.grid(row=3,column=0, pady=10,padx=20)
        self.check_btn = Button(self.login_button_frame, 
                                text="Back",bg=BTN_COLOR,
                                command=partial(self.backToHome,self.login_button_frame),
                                width=15)
        self.check_btn.grid(row=3,column=1, pady=10,padx=20)
        

    def signup(self):
        self.button_frame.grid_remove()
        self.signup_button_frame = Frame(self.window, bg=THEME_COLOR)
        self.signup_button_frame.grid(row=0, column=0, columnspan=2, pady=50)

        self.emial_id_label = Label(self.signup_button_frame,
                                text="Enter your user id",
                                bg = THEME_COLOR,
                                font=(FONT,LABEL_FONT_SIZE))
        self.emial_id_label.grid(row=0,column=0,sticky=LEFT,padx=20,pady=20)

        self.id_box = Entry(self.signup_button_frame, width=30)
        self.id_box.grid(row=0, column=1,sticky=LEFT, padx=20, pady=20)
        self.id_box.focus()

        self.label1 = Label(self.signup_button_frame,
                                text="Create New Master Password",
                                bg = THEME_COLOR,
                                font=(FONT,LABEL_FONT_SIZE))
        self.label1.grid(row=1,column=0,sticky=LEFT,padx=20,pady=20)

        self.mp_entry_box = Entry(self.signup_button_frame, width=30, show="*")
        self.mp_entry_box.grid(row=1, column=1,sticky=LEFT, padx=20, pady=20)
        self.mp_entry_box.focus()


        self.label2 = Label(self.signup_button_frame,
                                text="Enter Master Password again",
                                bg = THEME_COLOR,
                                font=(FONT,LABEL_FONT_SIZE))
        self.label2.grid(row=2,column=0,sticky=LEFT,padx=20,pady=10)

        self.rmp_entry_box = Entry(self.signup_button_frame, width=30, show="*")
        self.rmp_entry_box.grid(row=2, column=1,sticky=LEFT, padx=20, pady=10)

        self.save_btn = Button(self.signup_button_frame, text="Create Account",bg=BTN_COLOR,
                          command=self.save_master_password,
                          width=13)
        self.save_btn.grid(row=3,column=0, pady=10,padx=20)

        back_btn = Button(self.signup_button_frame, text="Back",bg=BTN_COLOR,
                          command=partial(self.backToHome,self.signup_button_frame),
                          width=13)
        back_btn.grid(row=3,column=1, pady=10,padx=20)
        messagebox.showinfo(title="Alert", message="Master Password can not be reset later.")

    def welcome_new_user(self):
        self.button_frame = Frame(self.window, bg=THEME_COLOR)
        self.button_frame.grid(row=0, column=0, columnspan=2, padx=80, pady=75)

        welcome_label = Label(self.button_frame,
                                text="WELCOME",
                                bg = THEME_COLOR,
                                font=(FONT,FONT_SIZE_L))
        welcome_label.grid(row=0,column=0,columnspan=2, sticky="nesw",padx=20,pady=10)

        # Login Button
        self.login_btn = Button(
            self.button_frame,
            text="Login",
            command=self.login,
            bg=BTN_COLOR,
            width=15,  # Set the width to make the button larger
            height=2   # Set the height to make the button taller
        )
        self.login_btn.grid(row=1, column=0, padx=50, pady=50, sticky='e')  # Centered to the right

        # SignUp Button
        self.signup_btn = Button(
            self.button_frame,
            text="Sign Up",
            command=self.signup,
            bg=BTN_COLOR,
            width=15,  # Set the width to make the button larger
            height=2   # Set the height to make the button taller
        )
        self.signup_btn.grid(row=1, column=1, padx=10, pady=10, sticky='w')  # Centered to the left

        
      

    def save_master_password(self):
        password1 = self.mp_entry_box.get()
        password2 = self.rmp_entry_box.get()
        email_id  = self.id_box.get()
        if self.isFilePresent(email_id) == True:
            messagebox.showinfo(title="Error", message="Accoutn already exist. Try to Login")
            self.home_window()
            return
        if password1 == password2 and len(password1) > 0:
            self.account = Account(email_id=email_id,password=password1)
            messagebox.showinfo(title="Done", message="Accoutn created successfully")
            self.home_window()
        else:
            self.home_window()
            messagebox.showinfo(title="Error", message="Passwords do not match. Try Again")

    def check_master_password(self):
        user_id =   self.id_box_login.get()
        ms_key  =   self.key_entry_box.get()
        if len(user_id)  == 0:
            messagebox.showinfo(title="Error", message="User Id can not be empty!")
        elif len(ms_key) == 0:
            messagebox.showinfo(title="Error", message="Master Password can not be empty!")
        elif self.isFilePresent(user_id) == False:
            messagebox.showinfo(title="Error", message="Enter valid user name")
        else:
            fileHandler = JSONFileEditor(user_id)
            hash_key = fileHandler.get_value("key")
            if hash_key != Encryptor.hashCode(ms_key):
                messagebox.showinfo(title="Error", message="Invalid Password")
            else:
                self.user_account = Account(user_id,ms_key)
                self.password_vault_screen()
        
    def password_vault_screen(self):
        self.window.geometry(WINDOW_SIZE)
        self.login_button_frame.grid_remove()
        
        main_frame = Frame(self.window, bg=THEME_COLOR)
        main_frame.grid(row=0, column=0, columnspan=4, padx=40, pady=50)
        welcome_label = Label(main_frame,
                                text=f"WELCOME",
                                bg = THEME_COLOR,
                                font=(FONT,FONT_SIZE,FONT_STYLE))
        welcome_label.grid(row=0, column=1)

        website_label= Label(main_frame,
                                text="Website:",
                                bg = THEME_COLOR,
                                font=(FONT,LABEL_FONT_SIZE))
        website_label.grid(row=1,column=0,sticky=LEFT,padx=20,pady=10)
        email_label= Label(main_frame,
                                text="Userid:",
                                bg = THEME_COLOR,
                                font=(FONT,LABEL_FONT_SIZE))
        email_label.grid(row=2,column=0, sticky=LEFT,padx=20,pady=10)
        password_label= Label(main_frame,
                                text="Password:",
                                bg = THEME_COLOR,
                                font=(FONT,LABEL_FONT_SIZE))
        password_label.grid(row=3,column=0,sticky=LEFT,padx=20,pady=10)

        #Entries
        website_entry = Entry(main_frame, width=20)
        website_entry.grid(row=1, column=1,sticky=LEFT, padx=20, pady=20)
        website_entry.focus()

        email_entry = Entry(main_frame, width=40)
        email_entry.grid(row=2, column=1,columnspan=2,sticky=LEFT, padx=20, pady=20)
        email_entry.insert(0, f"{self.user_account.name}")
        
        password_entry = Entry(main_frame, width=20)
        password_entry.grid(row=3, column=1,sticky=LEFT, padx=20, pady=20)


        # Buttons
        search_button = Button(
            main_frame,
            text="Search",
            command=partial(self.findPassword,website_entry),
            width=10,bg=BTN_COLOR
        )
        search_button.grid(row=1, column=2, sticky='e')
        generate_password_button = Button(
            main_frame,
            text="Generate Key",
            command=partial(self.generateKey,password_entry),
            width=10,bg=BTN_COLOR
        )
        generate_password_button.grid(row=3, column=2, sticky='e')
    
        add_button = Button(
            main_frame,
            text="Add Password",
            command=partial(self.addPassword,website_entry,email_entry,password_entry),
            width=20,bg=BTN_COLOR
        )
        add_button.grid(row=4, column=0,columnspan=2)
        
        show_all = Button(
            main_frame,
            text="Show All",
            command=partial(self.showPasswords,main_frame),
            width=20,
            bg=BTN_COLOR
        )
        show_all.grid(row=4, column=2,columnspan=2)

    def copy_text(self, text):
        self.window.clipboard_clear()
        self.window.clipboard_append(text)
        messagebox.showinfo(title="Done", message="Password copied to clipboard")

    def isFilePresent(self, id)->bool:
        file_path = id+".json"
        try:
            with open(file_path, 'r') as file:
                return True
        except (FileNotFoundError):
            return False
    
    def findPassword(self,website_entry:Entry):
        website = website_entry.get()
        if len(website) ==0:
            messagebox.showinfo(title="Error", message=f"Website field can not be empty!")
            return
        password = self.user_account.getPassword(website)
        if password != None:
            email = password[0]
            password = password[1]
            message=f"Email: {email}\nPassword: {password}"
            messagebox.showinfo(title=website, message=message)
            self.copy_text(password)
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

    def addPassword(self, website_entry,email_entry,password_entry):
        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        account = self.user_account

        if account.getPassword(website) != None:
            response = messagebox.askquestion("Confirm", f"Details for {website} exists. Do you want to continue?")
            if response.lower()=="no":
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                return

        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        else:
            try:
                account.addPassword(website,email,password)
            except KeyError:
                account.updatePassword(website,email,password)
            else:
                 messagebox.showinfo(title="Done", message="Credential added successfully")
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                account.save()
    
    def showPasswords(self,main_frame:Frame=None):
        if main_frame is not None:
            main_frame.grid_remove()
        self.window.geometry(WINDOW_SIZE_L)
        password_dict = self.user_account.getAllPasswords()
        if len(password_dict)==0:
            messagebox.showinfo(title="Info", message="No Credential found")
        
        sorted_dict = dict(sorted(password_dict.items()))
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        canvas = Canvas(self.window, bg=THEME_COLOR, highlightthickness=0)
        canvas.grid(row=0, column=0, columnspan=4, padx=40, pady=50, sticky="nsew")

        v_scrollbar = Scrollbar(self.window, orient="vertical", command=canvas.yview)
        v_scrollbar.grid(row=0, column=4, sticky="ns")

        h_scrollbar = Scrollbar(self.window, orient="horizontal", command=canvas.xview)
        h_scrollbar.grid(row=1, column=0, columnspan=4, sticky="ew")

        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        second_frame = Frame(canvas, bg=THEME_COLOR)
        canvas.create_window((0, 0), window=second_frame, anchor="nw")

        lbl = Label(second_frame, text="WEBSITE",bg = THEME_COLOR,
                    font=(FONT,LABEL_FONT_SIZE))
        lbl.grid(row=0, column=0, padx=40, pady=10,sticky=LEFT)

        btn = Button(second_frame,
                     text="Back",
                     command=partial(self.backToLogin,canvas,v_scrollbar,h_scrollbar),
                     width=15,
                     bg=BTN_COLOR,
                     )
        btn.grid(row=0,column=1, pady=10,sticky=LEFT)
        if password_dict:
            for i, (website, details) in enumerate(sorted_dict.items(), start=1):
                platform_label = Label(second_frame, text=website, bg=THEME_COLOR, anchor="w")
                platform_label.grid(row=i, column=0, padx=40, pady=10, sticky="w")

                show_btn = Button(second_frame, text="show", 
                                command=partial(self.show_key, website, details[0],details[1]), 
                                bg=BTN_COLOR,
                                width=VAULT_BTN_WIDTH)
                show_btn.grid(row=i, column=1, pady=10,  sticky="w")
                copy_btn = Button(second_frame,
                                text="Copy Password", 
                                command=partial(self.copy_text, details[1]), 
                                width=VAULT_BTN_WIDTH,
                                bg=BTN_COLOR)
                copy_btn.grid(row=i, column=2, pady=10,padx=5,  sticky="w")

                remove_btn = Button(second_frame, text="Delete Password", 
                                    command=partial(self.remove_password, website,canvas,v_scrollbar,h_scrollbar),
                                    bg=BTN_COLOR,
                                    width=VAULT_BTN_WIDTH)
                remove_btn.grid(row=i, column=3, pady=10,padx=5, sticky="w")
            canvas.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))
        
    def backToLogin(self,second_frame:Canvas,v_s:Scrollbar,h_s:Scrollbar):
        second_frame.grid_remove()
        v_s.grid_remove()
        h_s.grid_remove()
        self.password_vault_screen()

    def backToHome(self, current_frame:Frame):
        current_frame.grid_remove()
        self.button_frame.grid(row=0, column=0, columnspan=2, padx=80, pady=75)


    def generateKey(self,password_entry):
         pg = PasswordGenerator(password_entry)
         pg.window.mainloop()

    def remove_password(self, website,second_frame:Canvas,v_s:Scrollbar,h_s:Scrollbar):
        self.user_account.removePassword(website)
        self.user_account.save()
        messagebox.showinfo(title="Password Removed", message=f"Password for {website} removed successfully")
        second_frame.grid_remove()
        v_s.grid_remove()
        h_s.grid_remove()
        self.showPasswords()

    def show_key(self,website, user_id, key):
        message=f"USER ID:  {user_id}\nPASSWORD: {key}"
        messagebox.showinfo(title=website, message=message)
        self.copy_text(key)

