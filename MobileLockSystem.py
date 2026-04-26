# Create a class Mobile
# Create private variable for password
# Add method set_password(pwd)
# Password must be at least 4 characters
# Add method unlock(pwd)
# Check password and print result
# Add method change_password(old_pwd, new_pwd)
# Change only if old password is correct
# New password must follow rules

class Mobile:
    def __init__(self):
        self.__password = None
    def set_password(self, pwd):
        if len(pwd) >= 4:
            self.__password = pwd
            print("Password set successfully")
        else:
            print("Password must be at least 4 characters")
    def unlock(self, pwd):
        if self.__password is None:
            print("No password set")
        elif pwd == self.__password:
            print("Mobile Unlocked")
        else:
            print("Incorrect Password")
    def change_password(self, old_pwd, new_pwd):
        if self.__password is None:
            print("No password set")
        elif old_pwd != self.__password:
            print("Old password is incorrect")
        elif len(new_pwd) < 4:
            print("New password must be at least 4 characters")
        else:
            self.__password = new_pwd
            print("Password changed successfully")
class Mobile:
    def __init__(self):
        self.__password = None
    def set_password(self, pwd):
        if len(pwd) >= 4:
            self.__password = pwd
            print("Password set successfully")
        else:
            print("Password must be at least 4 characters")
    def unlock(self, pwd):
        if self.__password is None:
            print("No password set")
        elif pwd == self.__password:
            print("Mobile Unlocked")
        else:
            print("Incorrect Password")
    def change_password(self, old_pwd, new_pwd):
        if self.__password is None:
            print("No password set")
        elif old_pwd != self.__password:
            print("Old password is incorrect")
        elif len(new_pwd) < 4:
            print("New password must be at least 4 characters")
        else:
            self.__password = new_pwd
            print("Password changed successfully")
m1 = Mobile()
pwd = input("Set your password: ")
m1.set_password(pwd)
unlock_pwd = input("Enter password to unlock: ")
m1.unlock(unlock_pwd)
old_pwd = input("Enter old password: ")
new_pwd = input("Enter new password: ")
m1.change_password(old_pwd, new_pwd)
unlock_pwd1 = input("Enter password to unlock again: ")
m1.unlock(unlock_pwd1)