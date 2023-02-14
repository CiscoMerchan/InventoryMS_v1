# Here will be the frame to operate the inventory
import tkinter
from tkinter import Label, Entry,Button, Frame,Toplevel, messagebox, Tk
from tkinter import ttk
import time
from _userDB import UserDb
from accesories import CreateToolTip
userdb = UserDb()
LABELS = ("",12, '')
class SecondWindow:


    def __init__(self,window, user_id, user_name):
        self.window = window
        self.user_id = user_id
        self.user_name = user_name
        # self.window.geometry("500x800")
        self.window.title('Inventory.2')
################################ NoteBooK##################
        self.notebook = ttk.Notebook(self.window) #width = 950, height = 450

        #Frames by Categories
        """BILLING"""
        frameBilling = ttk.Frame(self.notebook)
        lb_frameBilling = ttk.Label(frameBilling, text="Billing")
        lb_frameBilling.pack(padx=20, pady=5, anchor='w')
        frameBilling.pack(expand=1,fill="both")

###################################################################
        """ITEMS"""
        frameItem = ttk.Frame(self.notebook)
        lb_frameItem = ttk.Label(frameItem, text="Items")
        lb_frameItem.pack(padx=5, pady=5, anchor='w')
        frameItem.pack(expand=1,fill="both")





##################################################################################
        frameSupplier = ttk.Frame(self.notebook)
        lb_frameSupplier = ttk.Label(frameSupplier, text="Supplier")
        lb_frameSupplier.pack(padx=5, pady=5)
        frameSupplier.pack(expand=1,fill="both")

#######################################################################
        """CLIENT"""
        frameClient = ttk.Frame(self.notebook)
        lb_frameClient = ttk.Label(frameClient, text="Client")
        lb_frameClient.pack(padx = 5, pady =5)
        frameClient.pack(expand=1,fill="both")

###############################################################
        """USER"""

        self.U_NAME = tkinter.StringVar()  # in USER frame, get the user name.
        self.U_LASTNAME = tkinter.StringVar()  # in USER frame, get the user lastname.
        self.U_EMAIL = tkinter.StringVar()  # in USER frame, get the user email.
        self.U_ADMIN = tkinter.StringVar()  # in USER frame, if checked get the user status as Admin.
        print(self.U_ADMIN)
        frameUser = ttk.Frame(self.notebook)
        #Label and entry
        lb_Title = ttk.Labelframe(frameUser,text= "User")
        lb_Title.grid(row=0)
        lb_UserName = ttk.Label(frameUser, text="* Name:", font=LABELS)
        lb_UserName.grid(row=1)#pack(padx=15, pady=5, anchor='w')
        userNameEntry = ttk.Entry(frameUser)
        userNameEntry.grid(row=2)#pack( padx=15, pady=5,anchor='w')
        lb_UserLastName = ttk.Label(frameUser, text="* Lastname:", font=LABELS)
        lb_UserLastName.grid(row=3) # pack(padx=15, pady=5, anchor='w')
        userLastNameEntry = ttk.Entry(frameUser)
        userLastNameEntry.grid(row=4)#pack(padx=15, pady=5, anchor='w')
        lb_UserEmail = ttk.Label(frameUser, text="Email:", font=LABELS)
        lb_UserEmail.grid(row=5) # pack(padx=15, pady=5, anchor='w')
        userEmailEntry = ttk.Entry( frameUser)
        userEmailEntry.grid(row=6) #pack(padx=15, pady=5, anchor='w')
        lb_Mandatory = ttk.Label(frameUser, text="* case madatory", font=('',8,'bold'))
        lb_Mandatory.grid(row=7)#pack(padx=15, pady=5, anchor='w')
        cb_Admin = ttk.Checkbutton(frameUser,text='Admin', variable=self.U_ADMIN, onvalue=True,offvalue=False)
        cb_Admin.grid(row=8) #.pack(padx=15, pady=5, anchor='w')
        CreateToolTip(cb_Admin, text=' \n If new user will be part of Admin check the box \n')
        btn_Insert = ttk.Button(frameUser,text='Insert')
        btn_Insert.grid(row=9, column=0)
        btn_Show = ttk.Button(frameUser, text='Show')
        btn_Show.grid(row=9, column=1)
        btn_Update = ttk.Button(frameUser, text='Update')
        btn_Update.grid(row=10, column=0, columnspan= 2)


        frameUser.pack(expand=1,fill="both")




        ###########################################################################


        """SEARCH"""
        frameSearch = ttk.Frame(self.notebook)
        lb_frameSearch = ttk.Label(frameSearch, text ="Search")
        lb_frameSearch.pack(padx = 5, pady =5)
        frameSearch.pack(expand=1,fill="both")

        # Notebook Widget

        self.notebook.add(frameBilling, text = "Billing" )
        self.notebook.add(frameItem, text = "Items")
        self.notebook.add(frameSupplier, text = "Supplier")
        self.notebook.add(frameClient, text = "Client")
        self.notebook.add(frameUser, text = "User" )
        self.notebook.add(frameSearch, text = "Search", state="disabled")# $Note: $to improuve that depending and the user
        # notebook widget can be 'disabled', 'normal' 'hidden' $ maybe  with boolean in _user TABLE can be add it and
        # depending on True  or False some widget can be used by the user.






        # .enable_traversal() function allows the user to pass from one tab to another just click Control+Tab(forward) and
        # backward by clikc Shift+Control+Tab
        self.notebook.enable_traversal()
        """ $Note: padx=35 lateral distance from the frame, pady=105 distance from the to to the frame, anchor='w' """
        self.notebook.pack(expand=2,fill="both")#padx=25, pady=150, anchor='w'
        # label = Label(self.window, text=f'Welcowme"{user_name}" to Inventory.2 (UserID: "{user_id}"')
        # label.pack()




def app():
    root = tkinter.Tk()
    window = SecondWindow(root, 1, "Alba")

    root.mainloop()

if __name__ == '__main__':
    app()

