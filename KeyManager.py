from src.manager import *


if __name__ == '__main__':
    manager = PasswordManager()
    manager.welcome_new_user()
    manager.window.mainloop()