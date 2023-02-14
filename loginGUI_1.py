"""Module Firstwindow: Login, user entries: Name and ID number to get into the Inventory
 after verification in the DB """
import time
import tkinter
from tkinter import Label, Entry, Button, Frame, Toplevel, messagebox
from tkinter import ttk
from _userDB import UserDb

userdb = UserDb()


class FirstWindow:

    def __init__(self, root):
        self.root = root
        self.root = Toplevel()
        self.root.title('"Inventory System/Account Login"(Welcome to v.2)')
        self.root.destroy()
        # screen_width = root.winfo_screenwidth()
        # screen_height = root.winfo_screenheight()
        ################

        TopLoginForm = Frame(root, bd=1, width=300, height=30, )  # width=300, height=30,
        TopLoginForm.pack()  # side='top'
        lbl_text = Label(TopLoginForm, text="Administrator Login", font=('arial', 12))  #
        lbl_text.pack()
        MidLoginForm = Frame(root, width=300)
        MidLoginForm.pack(side='top')
        lbl_username = Label(root, text="Username:", font=('arial', 12), bd=15)
        lbl_username.pack()

        self.username = Entry(root, font=('arial', 12), width=15)
        self.username.pack()
        self.username.focus_set()  # initial focus
        self.username.bind('<Return>', self.check_user)
        lbl_password = Label(root, text="Id:", font=('arial', 12), bd=15)
        lbl_password.pack()
        #

        self.password = Entry(root, font=('arial', 12), width=15, show="*")
        self.password.pack()
        self.password.bind('<Return>', self.check_user)
        lbl_result = Label(root, text="", font=('arial', 12))
        lbl_result.pack()
        btn_login = Button(root, text="Login", font=('arial', 12), width=15, command=self.check_user)
        btn_login.pack()
        btn_login.bind('<Return>', self.check_user)

    #############

    # Check if user is in the DB
    def check_user(self):
        # Checking name and id from user with a callback function
        result = userdb.user_check(self.username.get(), self.password.get(), self.openWin)
        return result

    # Callback function
    def openWin(self, check_user):
        user_id = self.password.get()
        user_name = self.username.get()

        if check_user == False:
            print('false')
            # message no working may self.result from db ( to try)
            messagebox.showerror('Opss!', 'Name or/Id are not valide\n Try again or Insert new User ')


        else:
            print('seconwin')
            from v2_page2 import SecondWindow
            # No Working FirstWindow not destroy
            self.root.destroy()
            # SecondWindow take has argument user log id ( I can used to take data from the database and aswell to registre
            # in every oparation the user id
            SecondWindow(self.root, user_id, user_name)


def app():
    root = tkinter.Tk()
    window = FirstWindow(root)
    root.mainloop()


if __name__ == '__main__':
    app()



