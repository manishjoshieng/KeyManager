from tkinter import *
from tkinter import messagebox
from secrets import choice
from tkinter.constants import END
from src.constant import *
from src.passwordGenerator import KeyGenerator

class PasswordGenerator:

    def __init__(self, entryBox: Entry = None):
        self.window = Tk()
        self.window.title("Key Generator")
        self.window.geometry(WINDOW_SIZE)  # Adjusted the window height
        self.window.config(bg=THEME_COLOR)
        self.box = entryBox

        self.size_label = Label(self.window,
                                text="Enter the key size: ",
                                bg = THEME_COLOR,
                                font=(FONT,LABEL_FONT_SIZE))
        self.size_label.grid(row=0,column=0,sticky=LEFT,padx=20,pady=10)

        self.size_input = Entry(self.window,width=10)
        self.size_input.insert(0,"8")
        self.size_input.grid(row=0, column=1,sticky=LEFT, padx=20, pady=10)

        self.excl_chars = Label(self.window, 
                                text="Enter chars to exclude:",
                                bg=THEME_COLOR,
                                font=(FONT, LABEL_FONT_SIZE),
                                anchor="w")
        self.excl_chars.grid(row=1, column=0, sticky=LEFT, padx=20, pady=10)

    
        self.excld_entry_box = Entry(self.window, width=10)
        self.excld_entry_box.grid(row=1, column=1, padx=20, pady=10,sticky="w")
        if self.box is None:
            self.generated_key = Label(self.window,
                                    text="Password:",
                                    bg = THEME_COLOR,
                                    font=(FONT,LABEL_FONT_SIZE))
            self.generated_key.grid(row=2,column=0,sticky=LEFT,padx=20,pady=10)

            # Entry box for password
            self.password_entry_box = Entry(self.window, text="", width=35, show="*")
            self.password_entry_box.grid(row=2, column=1, padx=20,pady=10)

        # Checkboxes for including character types
        self.include_numbers = False
        self.include_uppercase = False
        self.include_lowercase = False
        self.include_special_chars = False

        self.numbers_checkbox = Checkbutton(
            self.window, 
            text="Include Numbers", 
            bg=THEME_COLOR,
            font=(FONT,15,FONT_STYLE),
            command=self._include_number
           )
        self.numbers_checkbox.grid(row=3, column=0,sticky=LEFT,pady=10)

        
        
        self.uppercase_checkbox = Checkbutton(
            self.window, 
            text="Include Uppercase", 
            bg=THEME_COLOR,
            font=(FONT,15,FONT_STYLE),
            command=self._include_uppercase,
            )
        self.uppercase_checkbox.grid(row=3, column=1,sticky=LEFT)

        
        self.lowercase_checkbox = Checkbutton(
            self.window, 
            text="Include Lowercase", 
            bg=THEME_COLOR,
            font=(FONT,15,FONT_STYLE),
            command=self._include_lowercase,
            )
        self.lowercase_checkbox.grid(row=4, column=0,sticky=LEFT)
        

        self.special_chars_checkbox = Checkbutton(
            self.window, 
            text="Include Special Chars", 
            bg=THEME_COLOR,
            font=(FONT,15,FONT_STYLE),
            command=self._include_special_chars,
           )
        self.special_chars_checkbox.grid(row=4, column=1,sticky=LEFT)
        

        # Frame for buttons
        self.button_frame = Frame(self.window,bg=THEME_COLOR)
        self.button_frame.grid(row=5, 
                               column=0, 
                               columnspan=2, 
                               padx=10, 
                               pady=10)

        # Generate Password Button
        generate_btn = Button(
            self.button_frame, 
            text="Generate Password",bg=BTN_COLOR,
            command=self.generate_random_password)
        generate_btn.grid(row=0, column=0, padx=10)

        # Copy Password Button
        copy_btn = Button(self.button_frame,
                          text="Copy Password", 
                          command=self.copy_password,
                          bg=BTN_COLOR)
        copy_btn.grid(row=0, column=1, padx=10)

    def _include_number(self):
        self.include_numbers = not (self.include_numbers)

    def _include_uppercase(self):
        self.include_uppercase = not self.include_uppercase

    def _include_lowercase(self):
        self.include_lowercase = not self.include_lowercase
    def _include_special_chars(self):
        self.include_special_chars = not self.include_special_chars

    def generate_random_password(self):
        if self.box is None:
            self.password_entry_box.delete(0, END)
        else:
            self.box.delete(0, END)
        try:
            try:
                password_length = int(self.size_input.get())
            except:
                messagebox.showinfo(title="Oops", message="Please enter value between 0 and 32")
                return
            if password_length==0 or password_length > 32:
                messagebox.showinfo(title="Oops", message="Please enter value between 0 and 32")
                return
            PG = KeyGenerator()
            
            if self.include_uppercase:
                PG.include_uppercase = True
            if self.include_lowercase:
                PG.include_lowercase =True
            if self.include_numbers:
                PG.include_number = True
            if self.include_special_chars:
                PG.include_special_chars =True

            excluded_chars = self.excld_entry_box.get()
            if  len(excluded_chars) > 0:
                PG.setExcludedChars(excluded_chars)

            password = PG.generatePassword(password_length)
            
            if self.box is not None:
                self.box.insert(0,password)
            else:
                self.password_entry_box.insert(0, password)
        except ValueError:
            self.feedback = Label(self.window, fg="red",
                                  text="Please enter number of characters")
            self.feedback.grid(row=6, column=0, columnspan=2, pady=5, padx=10, sticky="w")

    def copy_password(self):
        self.window.clipboard_clear()
        if self.box is not None:
            self.window.clipboard_append(self.box.get())
        else:
            self.window.clipboard_append(self.password_entry_box.get())
        messagebox.showinfo(title="Done", message="Password copied to clipboard")
         

if __name__ == "__main__":
    PasswordGenerator().window.mainloop()
