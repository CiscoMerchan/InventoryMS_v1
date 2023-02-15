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
    #User INSERT data
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

            # User UPDATE data
    def userUpdate(self):
      pass
#######################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$########################################
    def __init__(self,root,*args):
        print('__init__')
        self.window = root
        self.user_id = args[0]   # id entered from loginGUI_1 class FirstWindow
        self.user_name = args[1] # name entered from loginGUI_1 class FirstWindow
        # get the width and height of the screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # set the size of the root window to the size of the screen
        root.geometry("%dx%d+0+0" % (screen_width, screen_height))
        self.window.title('Inventory.2')
################################ NoteBooK##################
        self.notebook = ttk.Notebook(self.window) #width = 950, height = 450
        # this lb_title is just to check that the value entered by the user in loginGUI_1 module is transfered to this module
        lb_title = ttk.Label(root,text=f'welcome{self.user_name}, ID: {self.user_id}')
        lb_title.pack()
        lb_title1 = ttk.Label(root, text=f'welcome{self.user_name}, ID: {self.user_id}')
        lb_title1.pack()
        lb_title2 = ttk.Label(root, text=f'welcome{self.user_name}, ID: {self.user_id}')
        lb_title2.pack()
        lb_title3 = ttk.Label(root, text=f'welcome{self.user_name}, ID: {self.user_id}')
        lb_title3.pack()
        lb_title4 = ttk.Label(root, text=f'welcome{self.user_name}, ID: {self.user_id}')
        lb_title4.pack()
        lb_title5 = ttk.Label(root, text=f'welcome{self.user_name}, ID: {self.user_id}')
        lb_title5.pack()
        #Frames by Categories
        """BILLING"""
       
        ##################
        itemFrame = ttk.Frame(self.notebook)
        itemTab = ttk.Frame(itemFrame)
        itemTab.pack(side=tkinter.LEFT)
        itemTreeview = ttk.Frame(itemFrame)
        itemTreeview.pack(side=tkinter.LEFT)
        
        ######################## BILLING TREEVIEW
        item_tree = ttk.Treeview(itemTreeview, height = 20 ,columns=(1, 2, 3, 4), show="headings")
        item_tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        item_tree_scroll = ttk.Scrollbar(itemTreeview, orient="vertical", command=item_tree.yview)
        item_tree_scroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
        item_tree.configure(yscrollcommand=item_tree_scroll.set)
        item_tree.heading(1, text="Column 1")
        item_tree.heading(2, text="Column 2")
        item_tree.heading(3, text="Column 3")
        item_tree.heading(4, text="Column 4")
        ################################# BILLING TAB ENTRIES
        lb_ItemCode = ttk.Label(itemTab, text="Label 1")
        lb_ItemCode.pack()
        self.itemCodeEntry = ttk.Entry(itemTab)
        self.itemCodeEntry.pack()
        billing_left_frame_label2 = ttk.Label(itemTab, text="Label 2")
        billing_left_frame_label2.pack()
        billing_left_frame_entry2 = ttk.Entry(itemTab)
        billing_left_frame_entry2.pack()
        billing_left_frame_label3 = ttk.Label(itemTab, text="Label 3")
        billing_left_frame_label3.pack()
        billing_left_frame_entry3 = ttk.Entry(itemTab)
        billing_left_frame_entry3.pack()
        billing_left_frame_button1 = ttk.Button(itemTab, text="Button 1")
        billing_left_frame_button1.pack()
        billing_left_frame_button2 = ttk.Button(itemTab, text="Button 2")
        billing_left_frame_button2.pack()
        billing_left_frame_button3 = ttk.Button(itemTab, text="Button 3")
        billing_left_frame_button3.pack()
        self.notebook.add(itemFrame, text="Billing")

###################################################################
        """ITEMS"""

        itemFrame = ttk.Frame(self.notebook)
        itemTab = ttk.Frame(itemFrame) 
        itemTab.pack(side=tkinter.LEFT)
        itemTreeview = ttk.Frame(itemFrame)
        itemTreeview.pack(side=tkinter.LEFT) 
 ###############test insert in treeview
        itemlist= ('345454', "object", "supplier", 100, f"${20}", 5, "level 1")
        # item_tree.insert('','end', text=itemlist[0], values=itemlist[0:])
        ######################## ITEM TREEVIEW
        item_tree = ttk.Treeview(itemTreeview, height=20, columns=("Code", "Name","Supplier", "Quantity","Price","Min. Stock", "Location"), show="headings")
        item_tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        item_tree.insert('', 'end', text=itemlist[0], values=itemlist[0:])   # Insert data into the treeview

        #Scrollbar for the treeview
        item_tree_scroll = ttk.Scrollbar(itemTreeview, orient="vertical", command=item_tree.yview)
        item_tree_scroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
        item_tree.configure(yscrollcommand=item_tree_scroll.set)

        item_tree.heading(0, text="Code", anchor='center')
        item_tree.heading(1, text="Name", anchor='center')
        item_tree.heading(2, text="Supplier", anchor='center')
        item_tree.heading(3, text="Quantity", anchor='center')
        item_tree.heading(4, text="Price", anchor='center')
        item_tree.heading(5, text="Min. Stock", anchor='center')
        item_tree.heading(6, text="Location", anchor='center')
        item_tree.column(0, width=100, anchor='center')
        item_tree.column(1, width=100, anchor='center')
        item_tree.column(2, width=100, anchor='center')
        item_tree.column(3, width=100, anchor='center')
        item_tree.column(4, width=100, anchor='center')
        item_tree.column(5, width=100, anchor='center')
        item_tree.column(6, width=100, anchor='center')

        ################################# ITEMS TAB ENTRIES
        lb_ItemCode = ttk.Label(itemTab, text="Code:")
        lb_ItemCode.pack()
        self.itemCodeEntry = ttk.Entry(itemTab)
        self.itemCodeEntry.pack()
        billing_left_frame_label2 = ttk.Label(itemTab, text="Label 2")
        billing_left_frame_label2.pack()
        billing_left_frame_entry2 = ttk.Entry(itemTab)
        billing_left_frame_entry2.pack()
        billing_left_frame_label3 = ttk.Label(itemTab, text="Label 3")
        billing_left_frame_label3.pack()
        billing_left_frame_entry3 = ttk.Entry(itemTab)
        billing_left_frame_entry3.pack()
        billing_left_frame_button1 = ttk.Button(itemTab, text="Button 1")
        billing_left_frame_button1.pack()
        billing_left_frame_button2 = ttk.Button(itemTab, text="Button 2")
        billing_left_frame_button2.pack()
        billing_left_frame_button3 = ttk.Button(itemTab, text="Button 3")
        billing_left_frame_button3.pack()
        self.notebook.add(itemFrame, text="Items")




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
###################### USER TABS##########################
        # frameUser = ttk.Frame(self.notebook)
        # #Label and entry
        # lb_Title = ttk.Labelframe(frameUser,text= "User")
        # lb_Title.grid(row=0)
#         lb_UserName = ttk.Label(frameUser, text="* Name:", font=LABELS)
#         lb_UserName.grid(row=1)#pack(padx=15, pady=5, anchor='w')
#         self.userNameEntry = ttk.Entry(frameUser, textvariable="Name")
#         self.userNameEntry.grid(row=2)#pack( padx=15, pady=5,anchor='w')
#         lb_UserLastName = ttk.Label(frameUser, text="* Lastname:", font=LABELS)
#         lb_UserLastName.grid(row=3) # pack(padx=15, pady=5, anchor='w')
#         self.userLastNameEntry = ttk.Entry(frameUser, textvariable="LastName")
#         self.userLastNameEntry.grid(row=4)#pack(padx=15, pady=5, anchor='w')
#         lb_UserEmail = ttk.Label(frameUser, text="Email:", font=LABELS)
#         lb_UserEmail.grid(row=5) # pack(padx=15, pady=5, anchor='w')
#         self.userEmailEntry = ttk.Entry(frameUser, textvariable="Email")
#         self.userEmailEntry.grid(row=6) #pack(padx=15, pady=5, anchor='w')
#         lb_Mandatory = ttk.Label(frameUser, text="* case madatory", font=('',8,'bold'))
#         lb_Mandatory.grid(row=7)#pack(padx=15, pady=5, anchor='w')
#         self.cb_Admin = ttk.Checkbutton(frameUser,text='Admin', variable="Admin", onvalue=1, offvalue = 0)
#         self.cb_Admin.grid(row=8) #.pack(padx=15, pady=5, anchor='w')
#         CreateToolTip(self.cb_Admin, text=' \n If new user will be part of Admin check the box \n')
#         btn_Insert = ttk.Button(frameUser,text='Insert', command= lambda : self.insert_user_data())
#         btn_Insert.grid(row=9, column=0)
#         btn_Show = ttk.Button(frameUser, text='Show')
#         btn_Show.grid(row=9, column=1)
#         btn_Update = ttk.Button(frameUser, text='Update')
#         btn_Update.grid(row=10, column=0, columnspan= 2)
#
#
#         frameUser.pack(expand=1,fill="both")
#
# ####################### USER TREE VIEW   ####################################################
#         tabUser = ttk.Notebook(self.window)
#         userTree = ttk.Frame(tabUser)
#
#         userTitle = ttk.Labelframe(frameUser, text="Users", borderwidth=3)
#         frameUser.grid_propagate(0)
#         userTitle.grid(row=0,column=1,padx=8,pady=4,sticky="N")
#         userTree.grid_anchor(anchor='center')
#         # ************************************ TREE VIEW *******************************************
#
#         tree = ttk.Treeview(frameUser, columns=('Item', 'ID', 'Name', 'last Name', 'Email', 'Quantity'), height=20)
#         tree.place(x=30, y=95)
#         vsb = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
#         vsb.place(x=60 + 1000 + 5, y=0, height=200 + 220, bordermode='outside')
#
#         tree.configure(yscrollcommand=vsb.set)
#         tree.heading('#0', text='Users')
#         tree.heading('#1', text='ID')
#         tree.heading('#2', text='Name')
#         tree.heading('#3', text='Last Name')
#         tree.heading('#4', text='Email')
#         tree.heading('#5', text='Level')
#         tree.column('#1', stretch=tkinter.YES)
#         tree.column('#2', stretch=tkinter.YES)
#         tree.column('#0', stretch=tkinter.YES)
#         tree.column('#3', stretch=tkinter.YES)
#         tree.column('#4', stretch=tkinter.YES)
#         tree.column('#5', stretch=tkinter.YES)
#         tree.grid(row=11, columnspan=4, sticky='nsew')
#         # tabcontrol1.pack(expand=0, fill="both")
#         frameUser.pack(expand=1, fill="both")

        #### TEST

        # frameUser = ttk.Frame(self.notebook)
        #
        # # Label and entry
        # lb_Title = ttk.Labelframe(frameUser, text="User")
        # lb_Title.grid(row=0, column=0, sticky='nsew')
        #
        # lb_UserName = ttk.Label(frameUser, text="* Name:", font=LABELS)
        # lb_UserName.grid(row=1, column=0)
        # self.userNameEntry = ttk.Entry(frameUser, textvariable="Name")
        # self.userNameEntry.grid(row=2, column=0)
        #
        # lb_UserLastName = ttk.Label(frameUser, text="* Lastname:", font=LABELS)
        # lb_UserLastName.grid(row=3, column=0)
        # self.userLastNameEntry = ttk.Entry(frameUser, textvariable="LastName")
        # self.userLastNameEntry.grid(row=4, column=0)
        #
        # lb_UserEmail = ttk.Label(frameUser, text="Email:", font=LABELS)
        # lb_UserEmail.grid(row=5, column=0)
        # self.userEmailEntry = ttk.Entry(frameUser, textvariable="Email")
        # self.userEmailEntry.grid(row=6, column=0)
        #
        # lb_Mandatory = ttk.Label(frameUser, text="* case mandatory", font=('', 8, 'bold'))
        # lb_Mandatory.grid(row=7, column=0)
        # self.cb_Admin = ttk.Checkbutton(frameUser, text='Admin', variable="Admin", onvalue=1, offvalue=0)
        # self.cb_Admin.grid(row=8, column=0)
        # CreateToolTip(self.cb_Admin, text=' \n If new user will be part of Admin check the box \n')
        #
        # btn_Insert = ttk.Button(frameUser, text='Insert', command=lambda: self.insert_user_data())
        # btn_Insert.grid(row=9, column=0)
        # btn_Show = ttk.Button(frameUser, text='Show')
        # btn_Show.grid(row=9, column=1)
        # btn_Update = ttk.Button(frameUser, text='Update')
        # btn_Update.grid(row=10, column=0, columnspan=2)
        #
        # ##
        # tabUser = ttk.Notebook(self.window)
        #
        # userTreeView = ttk.Frame(tabUser)
        # tabUser.add(userTreeView, text="Users")
        # tabUser.pack(side="left", fill="both", expand=True)
        #
        # userTitle = ttk.Labelframe(userTreeView, text="Users")
        # userTitle.grid(row=0, column=0, sticky='nsew')
        #
        # tree = ttk.Treeview(userTreeView, columns=('Item', 'ID', 'Name', 'Last Name', 'Email', 'Level'))
        # tree.grid(row=1, column=0, sticky='nsew')
        #
        # # tree.heading('#0', text='Users')
        # tree.heading('#0', text='ID')
        # tree.heading('#1', text='Name')
        # tree.heading('#2', text='Last Name')
        # tree.heading('#3', text='Email')
        # tree.heading('#4', text='Level')
        #
        # tree.column('#1', stretch=tkinter.YES)
        # tree.column('#2', stretch=tkinter.YES)
        # tree.column('#0', stretch=tkinter.YES)
        # tree.column('#3', stretch=tkinter.YES)
        # tree.column('#4', stretch=tkinter.YES)
        # # tree.column('#5', stretch=tkinter.YES)
        #
        # # Add vertical scrollbar
        # vsb = ttk.Scrollbar(userTreeView, orient="vertical", command=tree.yview)
        # vsb.grid(row=1, column=1, sticky='ns')
        # tree.configure(yscrollcommand=vsb.set)

        ###########################################################################


        """SEARCH"""
        frameSearch = ttk.Frame(self.notebook)
        lb_frameSearch = ttk.Label(frameSearch, text ="Search")
        lb_frameSearch.pack(padx = 5, pady =5)
        frameSearch.pack(expand=1,fill="both")

        # Notebook Widget

        # self.notebook.add(frameBilling, text = "Billing" )
        # self.notebook.add(frameItem, text = "Items")
        self.notebook.add(frameSupplier, text = "Supplier")
        self.notebook.add(frameClient, text = "Client")
        # self.notebook.add(frameUser, text = "User" )
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

"""# Create the user frame with grid geometry manager
frameUser = ttk.Frame(self.notebook)
frameUser.grid(row=0, column=0, sticky="nsew")

# Place the user input widgets in the left side of the frame using grid geometry manager
lb_Title = ttk.Labelframe(frameUser, text="User")
lb_Title.grid(row=0, column=0, padx=8, pady=4, sticky="nsew")

lb_UserName = ttk.Label(lb_Title, text="* Name:", font=LABELS)
lb_UserName.grid(row=0, column=0, padx=8, pady=4, sticky="w")
self.userNameEntry = ttk.Entry(lb_Title, textvariable="Name")
self.userNameEntry.grid(row=0, column=1, padx=8, pady=4, sticky="w")

lb_UserLastName = ttk.Label(lb_Title, text="* Lastname:", font=LABELS)
lb_UserLastName.grid(row=1, column=0, padx=8, pady=4, sticky="w")
self.userLastNameEntry = ttk.Entry(lb_Title, textvariable="LastName")
self.userLastNameEntry.grid(row=1, column=1, padx=8, pady=4, sticky="w")

lb_UserEmail = ttk.Label(lb_Title, text="Email:", font=LABELS)
lb_UserEmail.grid(row=2, column=0, padx=8, pady=4, sticky="w")
self.userEmailEntry = ttk.Entry(lb_Title, textvariable="Email")
self.userEmailEntry.grid(row=2, column=1, padx=8, pady=4, sticky="w")

lb_Mandatory = ttk.Label(lb_Title, text="* case mandatory", font=('', 8, 'bold'))
lb_Mandatory.grid(row=3, column=0, padx=8, pady=4, sticky="w")
self.cb_Admin = ttk.Checkbutton(lb_Title, text='Admin', variable="Admin", onvalue=1, offvalue=0)
self.cb_Admin.grid(row=3, column=1, padx=8, pady=4, sticky="w")
CreateToolTip(self.cb_Admin, text=' \n If new user will be part of Admin check the box \n')

btn_Insert = ttk.Button(lb_Title, text='Insert', command=lambda: self.insert_user_data())
btn_Insert.grid(row=4, column=0, padx=8, pady=4, sticky="w")

btn_Show = ttk.Button(lb_Title, text='Show')
btn_Show.grid(row=4, column=1, padx=8, pady=4, sticky="w")

btn_Update = ttk.Button(lb_Title, text='Update')
btn_Update.grid(row=5, column=0, columnspan=2, padx=8, pady=4, sticky="w")

# Create treeview

tree = ttk.Treeview(frameTreeView, columns=('Item', 'ID', 'Name', 'Last Name', 'Email', 'Level'))
tree.heading('#0', text='Users')
tree.heading('#1', text='ID')
tree.heading('#2', text='Name')
tree.heading('#3', text='Last Name')
tree.heading('#4', text='Email')
tree.heading('#5', text='Level')
tree.column('#1', stretch=tkinter.YES)
tree.column('#2', stretch=tkinter.YES)
tree.column('#0', stretch=tkinter.YES)
tree.column('#3', stretch=tkinter.YES)
tree.column('#4', stretch=tkinter.YES)
tree.column('#5', stretch=tkinter.YES)

# Add vertical scrollbar
vsb = ttk.Scrollbar(frameTreeView, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(side='right', fill='y')

"""