# Here will be the frame to operate the inventory
import tkinter
from sys import path
from tkinter import ttk, messagebox, END
from accesory import CreateToolTip
from usersBD import UserDb
collection = UserDb()
from backend_user import User


LABELS = ("",12, '')
class SecondWindow:
#######################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$########################################
    """User data operation"""
    #User Insert data
    def insert_user_data(self):
        Name = self.userNameEntry.get()
        LastName = self.userLastNameEntry.get()
        Email = self.userEmailEntry.get()
        Admin = self.cb_Admin.get() ###To change
        print(Admin)
        print('en incert data')
        """Before INSERT data into the database this is a message to confirme the entered data"""
        confirmation = messagebox.askyesno("Confirmation", f"the new User is : {Name} {LastName}\n {Email}?")
        """If the data is correct the data will be insert into _users table and will return the id number of the user """
        """if the user click 'NO' the data in the entries case will be deleted and the user will rewrite thier data"""
        if confirmation == False:
            print('cofirmacion falsa')
            Name.delete(0, END) #self.userNameEntry.delete(0, END)
            LastName.delete(0, END)#self.userLastNameEntry.delete(0, END)
            Email.delete(0, END) # self.userEmailEntry.delete(0, END)
        else:
            # Data colleted and insert
            print('else')
            collection.user_data_collection(
                Name.lower(), LastName.lower(),Email
            )
            # return of the user id number
            messagebox.showinfo(f"Your user ID: {str(collection.last_insert_id)}",
                                f"Welcome to Inventory {Name} {LastName} this is your User ID: {str(collection.last_insert_id)}. \n This number is your ID and is necessary to use")
            print('ultimo mensaje')
            if True:
                print('now deleted data')
                self.userNameEntry.delete(0, END)
                self.userLastNameEntry.delete(0, END)
                self.userEmailEntry.delete(0, END)
#######################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$########################################
    def __init__(self,root,*args):
        print('__init__')
        self.window = root
        self.user_id = args[0]   # id entered from loginGUI_1 class FirstWindow
        self.user_name = args[1] # name entered from loginGUI_1 class FirstWindow
        # self.window.geometry("500x800")
        self.window.title('Inventory.2')
################################ NoteBooK##################
        self.notebook = ttk.Notebook(self.window) #width = 950, height = 450
        # this lb_title is just to check that the value entered by the user in loginGUI_1 module is transfered to this module
        lb_title = ttk.Label(root,text=f'welcome{self.user_name}, ID: {self.user_id}')
        lb_title.pack()
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

        frameUser = ttk.Frame(self.notebook)
        #Label and entry
        lb_Title = ttk.Labelframe(frameUser,text= "User")
        lb_Title.grid(row=0)
        lb_UserName = ttk.Label(frameUser, text="* Name:", font=LABELS)
        lb_UserName.grid(row=1)#pack(padx=15, pady=5, anchor='w')
        self.userNameEntry = ttk.Entry(frameUser, textvariable="Name")
        self.userNameEntry.grid(row=2)#pack( padx=15, pady=5,anchor='w')
        lb_UserLastName = ttk.Label(frameUser, text="* Lastname:", font=LABELS)
        lb_UserLastName.grid(row=3) # pack(padx=15, pady=5, anchor='w')
        self.userLastNameEntry = ttk.Entry(frameUser, textvariable="LastName")
        self.userLastNameEntry.grid(row=4)#pack(padx=15, pady=5, anchor='w')
        lb_UserEmail = ttk.Label(frameUser, text="Email:", font=LABELS)
        lb_UserEmail.grid(row=5) # pack(padx=15, pady=5, anchor='w')
        self.userEmailEntry = ttk.Entry(frameUser, textvariable="Email")
        self.userEmailEntry.grid(row=6) #pack(padx=15, pady=5, anchor='w')
        lb_Mandatory = ttk.Label(frameUser, text="* case madatory", font=('',8,'bold'))
        lb_Mandatory.grid(row=7)#pack(padx=15, pady=5, anchor='w')
        self.cb_Admin = ttk.Checkbutton(frameUser,text='Admin', variable="Admin", onvalue=1, offvalue = 0)
        self.cb_Admin.grid(row=8) #.pack(padx=15, pady=5, anchor='w')
        CreateToolTip(self.cb_Admin, text=' \n If new user will be part of Admin check the box \n')
        btn_Insert = ttk.Button(frameUser,text='Insert', command= lambda : self.insert_user_data())
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
    # user_id= UserDb.user_check()[0]
    # user_name = UserDb.user_check()[1]
    # print(user_id, user_name)
    root = tkinter.Tk()
    window = SecondWindow(root,6,"Alba") #6,"Alba" is to activate the page, when finished delete only root left

    root.mainloop()

if __name__ == '__main__':
    app()

