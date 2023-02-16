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
        # And to include label to render information to the user
        lb_title = ttk.Label(root,text=f'welcome{self.user_name}, ID: {self.user_id}')
        lb_title.pack()
        lb_title1 = ttk.Label(root, text=f'welcome{self.user_name}, ID: {self.user_id}')
        lb_title1.pack()
        # lb_title2 = ttk.Label(root, text=f'welcome{self.user_name}, ID: {self.user_id}')
        # lb_title2.pack()
        # lb_title3 = ttk.Label(root, text=f'welcome{self.user_name}, ID: {self.user_id}')
        # lb_title3.pack()
        # lb_title4 = ttk.Label(root, text=f'welcome{self.user_name}, ID: {self.user_id}')
        # lb_title4.pack()
        # lb_title5 = ttk.Label(root, text=f'welcome{self.user_name}, ID: {self.user_id}')
        # lb_title5.pack()
        #Frames by Categories
        """BILLING"""
       
        ##################
        # itemFrame = ttk.Frame(self.notebook)
        # itemTab = ttk.Frame(itemFrame)
        # itemTab.pack(side=tkinter.LEFT)
        # itemTreeview = ttk.Frame(itemFrame)
        # itemTreeview.pack(side=tkinter.LEFT)
        #
        # ######################## BILLING TREEVIEW
        # item_tree = ttk.Treeview(itemTreeview, height = 20 ,columns=(1, 2, 3, 4), show="headings")
        # item_tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        # ### SCROLLBAR
        # item_tree_scroll = ttk.Scrollbar(itemTreeview, orient="vertical", command=item_tree.yview)
        # item_tree_scroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
        # item_tree.configure(yscrollcommand=item_tree_scroll.set)
        # item_tree.heading(1, text="Column 1")
        # item_tree.heading(2, text="Column 2")
        # item_tree.heading(3, text="Column 3")
        # item_tree.heading(4, text="Column 4")
        # ################################# BILLING TAB ENTRIES
        # lb_ItemCode = ttk.Label(itemTab, text="Label 1")
        # lb_ItemCode.pack()
        # self.itemCodeEntry = ttk.Entry(itemTab)
        # self.itemCodeEntry.pack()
        # lb_ItemName = ttk.Label(itemTab, text="Label 2")
        # lb_ItemName.pack()
        # billing_left_frame_entry2 = ttk.Entry(itemTab)
        # billing_left_frame_entry2.pack()
        # lb_ItemDescription = ttk.Label(itemTab, text="Label 3")
        # lb_ItemDescription.pack()
        # itemDescriptionEntry = ttk.Entry(itemTab)
        # itemDescriptionEntry.pack()
        # billing_left_frame_button1 = ttk.Button(itemTab, text="Button 1")
        # billing_left_frame_button1.pack()
        # btn_UpdateItem = ttk.Button(itemTab, text="Button 2")
        # btn_UpdateItem.pack()
        # btn_ItemShow = ttk.Button(itemTab, text="Button 3")
        # btn_ItemShow.pack()
        # self.notebook.add(itemFrame, text="Billing")

###################################################################
        """ITEMS"""
        #### MAIN FRAME ######################################################################
        itemFrame = ttk.Frame(self.notebook)
        ##### TOP FRAME FOR LABELS (RENDER INFORMATION  #######################################
        itemTopTab = ttk.Frame(itemFrame)
        itemTopTab.pack(side=tkinter.TOP)
        #### LEFT FRAME FOR THE ENTRIES, LABELS AND BUTTONS ###############################
        itemTab = ttk.Frame(itemFrame)
        itemTab.pack(side=tkinter.LEFT)
        #### RIGHT FRAME FOR TREEVIEW AND SCROLLBAR ############################################
        itemTreeview = ttk.Frame(itemFrame)
        itemTreeview.pack(side=tkinter.RIGHT)
###### TEST For Labels at the top of the treevieww to render information#########
        lb_title = ttk.Label(itemTopTab, text='Itemfgsf Name')
        lb_title.pack()
        lb_title = ttk.Label(itemTopTab, text='Itemfgsf ')
        lb_title.pack(side=tkinter.RIGHT,padx=10)
        lb_title = ttk.Label(itemTopTab, text=' Name')
        lb_title.pack(side=tkinter.LEFT, padx=10)
        lb_title = ttk.Label(itemTopTab, text='Item Name')
        lb_title.pack(padx=10)
        #####################################################
        ###############test insert in treeview
        lis = []
        for i in range(1,50):
            itemlist = (f'{i}', "object", "Object to create objects", "supplier", 100+(i*4), f"${2+i}", 5*i, "level 1")
            lis.append(itemlist)
        print(lis)
        # item_tree.insert('','end', text=itemlist[0], values=itemlist[0:])
        ######################## ITEM TREEVIEW

        item_tree = ttk.Treeview(itemTreeview, height=18, columns=("Item Code", "Name", "Description","Supplier", "Quantity","Price","Min. Stock", "Location"), show="headings")
        item_tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        # item_tree.insert('', 'end', text=itemlist[0], values=lis[0:])   # Insert data into the treeview
        for row in lis:
                item_tree.insert('', 'end', values=row)#  test Insert data into the treeview
        #Scrollbar for the treeview
        item_tree_scroll = ttk.Scrollbar(itemTreeview, orient="vertical", command=item_tree.yview)
        item_tree_scroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
        item_tree.configure(yscrollcommand=item_tree_scroll.set)
        ##### Heading of the treeview
        item_tree.heading(0, text="Item Code", anchor='center')
        item_tree.heading(1, text="Name", anchor='center')
        item_tree.heading(2, text="Description", anchor='center')
        item_tree.heading(3, text="Supplier ID", anchor='center')
        item_tree.heading(4, text="Quantity", anchor='center')
        item_tree.heading(5, text="Price", anchor='center')
        item_tree.heading(6, text="Min. Stock", anchor='center')
        item_tree.heading(7, text="Location", anchor='center')
        ##### Columns of the treeview
        item_tree.column(0, width=150, anchor='center')
        item_tree.column(1, width=150, anchor='center')
        item_tree.column(2, width=300, anchor='center')
        item_tree.column(3, width=150, anchor='center')
        item_tree.column(4, width=100, anchor='center')
        item_tree.column(5, width=100, anchor='center')
        item_tree.column(6, width=100, anchor='center')
        item_tree.column(2, width=150, anchor='center')

        ################################# ITEMS TAB, LABELS AND ENTRIES
        lb_ItemCode = ttk.Label(itemTab, text="Item Code:")
        lb_ItemCode.pack()
        self.itemCodeEntry = ttk.Entry(itemTab)
        self.itemCodeEntry.pack()
        lb_ItemName = ttk.Label(itemTab, text="Name:")
        lb_ItemName.pack()
        self.itemNameEntry = ttk.Entry(itemTab)
        self.itemNameEntry.pack()
        lb_ItemDescription = ttk.Label(itemTab, text="Description")
        lb_ItemDescription.pack()
        self.itemDescriptionEntry = ttk.Entry(itemTab)
        self.itemDescriptionEntry.pack()
        lb_ItemDescription = ttk.Label(itemTab, text="Description")
        lb_ItemDescription.pack()
        self.itemDescriptionEntry = ttk.Entry(itemTab)
        self.itemDescriptionEntry.pack()
        lb_ItemSupplierId = ttk.Label(itemTab, text="Supplier ID:")
        lb_ItemSupplierId.pack()
        self.itemSupplierIdEntry = ttk.Entry(itemTab)
        self.itemSupplierIdEntry.pack()
        lb_ItemQuantity = ttk.Label(itemTab, text="Quantity:")
        lb_ItemQuantity.pack()
        self.itemQuantityEntry = ttk.Entry(itemTab)
        self.itemQuantityEntry.pack()
        lb_ItemPrice = ttk.Label(itemTab, text="Price:")
        lb_ItemPrice.pack()
        self.itemPriceEntry = ttk.Entry(itemTab)
        self.itemPriceEntry.pack()
        lb_ItemMinStock = ttk.Label(itemTab, text="Min. Stock")
        lb_ItemMinStock.pack()
        self.itemMinStockEntry = ttk.Entry(itemTab)
        self.itemMinStockEntry.pack()
        lb_ItemLocation = ttk.Label(itemTab, text="Location:")
        lb_ItemLocation.pack()
        self.itemLocationEntry = ttk.Entry(itemTab)
        self.itemLocationEntry.pack()

        ###BUTTONS
        btn_InsertItem = ttk.Button(itemTab, text="Insert")
        btn_InsertItem.pack()
        btn_UpdateItem = ttk.Button(itemTab, text="Update")
        btn_UpdateItem.pack(side=tkinter.RIGHT)
        btn_ItemShow = ttk.Button(itemTab, text="Show")
        btn_ItemShow.pack()
        self.notebook.add(itemFrame, text="Items")




##################################################################################
        """SUPPLIERS"""

        #### MAIN FRAME ######################################################################
        supplierFrame = ttk.Frame(self.notebook)
        ##### TOP FRAME FOR LABELS (RENDER INFORMATION  #######################################
        supplierTopTab = ttk.Frame(supplierFrame)
        supplierTopTab.pack(side=tkinter.TOP)
        #### LEFT FRAME FOR THE ENTRIES, LABELS AND BUTTONS ###############################
        supplierTab = ttk.Frame(supplierFrame)
        supplierTab.pack(side=tkinter.LEFT)
        #### RIGHT FRAME FOR TREEVIEW AND SCROLLBAR ############################################
        supplierTreeview = ttk.Frame(supplierFrame)
        supplierTreeview.pack(side=tkinter.RIGHT)
        ###### TEST For Labels at the top of the treevieww to render information#########
        lb_title = ttk.Label(supplierTopTab, text='Itemfgsf Name')
        lb_title.pack()
        lb_title = ttk.Label(supplierTopTab, text='Itemfgsf ')
        lb_title.pack(side=tkinter.RIGHT, padx=10)
        lb_title = ttk.Label(supplierTopTab, text=' Name')
        lb_title.pack(side=tkinter.LEFT, padx=10)
        lb_title = ttk.Label(supplierTopTab, text='Item Name')
        lb_title.pack(padx=10)
        #####################################################
        ###############test insert in treeview
        lis = []
        for i in range(1, 50):
            suplist = (
            25*i, f"Company {i}", f"Name {i}", i*45, f"email{i}")
            lis.append(suplist)
        print(lis)
        # supplier_tree.insert('','end', text=itemlist[0], values=itemlist[0:])
        ######################## ITEM TREEVIEW

        supplier_tree = ttk.Treeview(supplierTreeview, height=18, columns=(
         "Supplier ID", "Company Name", "Agent", "Telephone", "Email"), show="headings")
        supplier_tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        # supplier_tree.insert('', 'end', text=itemlist[0], values=lis[0:])   # Insert data into the treeview
        for row in lis:
            supplier_tree.insert('', 'end', values=row)  # test Insert data into the treeview
        # Scrollbar for the treeview
        supplier_tree_scroll = ttk.Scrollbar(supplierTreeview, orient="vertical", command=supplier_tree.yview)
        supplier_tree_scroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
        supplier_tree.configure(yscrollcommand=supplier_tree_scroll.set)
        ##### Heading of the treeview
        supplier_tree.heading(0, text="Supplier ID", anchor='center')
        supplier_tree.heading(1, text="Company Name", anchor='center')
        supplier_tree.heading(2, text="Agent", anchor='center')
        supplier_tree.heading(3, text="Telephone", anchor='center')
        supplier_tree.heading(4, text="Email", anchor='center')

        ##### Columns of the treeview
        supplier_tree.column(0, width=150, anchor='center')
        supplier_tree.column(1, width=300, anchor='center')
        supplier_tree.column(2, width=300, anchor='center')
        supplier_tree.column(3, width=100, anchor='center')
        supplier_tree.column(4, width=250, anchor='center')


        ################################# SUPPLIERS TAB, LABELS AND ENTRIES

        lb_SupplierId = ttk.Label(supplierTab, text="Supplier ID:")
        lb_SupplierId.pack()
        self.supplierIdEntry = ttk.Entry(supplierTab)
        self.supplierIdEntry.pack()
        lb_SupplierName = ttk.Label(supplierTab, text="Company Name:")
        lb_SupplierName.pack()
        self.supplierNameEntry = ttk.Entry(supplierTab)
        self.supplierNameEntry.pack()
        lb_SupplierAgent = ttk.Label(supplierTab, text="Agent Full Name:")
        lb_SupplierAgent.pack()
        self.supplierAgentEntry = ttk.Entry(supplierTab)
        self.supplierAgentEntry.pack()
        lb_SupplierTelephone = ttk.Label(supplierTab, text="Telephone:")
        lb_SupplierTelephone.pack()
        self.supplierTelephoneEntry = ttk.Entry(supplierTab)
        self.supplierTelephoneEntry.pack()
        lb_SupplierEmail = ttk.Label(supplierTab, text="Email:")
        lb_SupplierEmail.pack()
        self.supplierEmailEntry = ttk.Entry(supplierTab)
        self.supplierEmailEntry.pack()

        ###BUTTONS
        btn_InsertSupplier = ttk.Button(supplierTab, text="Insert", command="")
        btn_InsertSupplier.pack()
        btn_UpdateSupplier = ttk.Button(supplierTab, text="Update", command="")
        btn_UpdateSupplier.pack(side=tkinter.RIGHT)
        btn_SupplierShow = ttk.Button(supplierTab, text="Show", command="")
        btn_SupplierShow.pack()
        self.notebook.add(supplierFrame, text="Supplier")
#######################################################################
        """CLIENT"""

        #### MAIN FRAME ######################################################################
        clientFrame = ttk.Frame(self.notebook)
        ##### TOP FRAME FOR LABELS (RENDER INFORMATION  #######################################
        clientTopTab = ttk.Frame(clientFrame)
        clientTopTab.pack(side=tkinter.TOP)
        #### LEFT FRAME FOR THE ENTRIES, LABELS AND BUTTONS ###############################
        clientTab = ttk.Frame(clientFrame)
        clientTab.pack(side=tkinter.LEFT)
        #### RIGHT FRAME FOR TREEVIEW AND SCROLLBAR ############################################
        clientTreeview = ttk.Frame(clientFrame)
        clientTreeview.pack(side=tkinter.RIGHT)
        ###### TEST For Labels at the top of the treevieww to render information#########
        lb_title = ttk.Label(clientTopTab, text='Itemfgsf Name')
        lb_title.pack()
        lb_title = ttk.Label(clientTopTab, text='Itemfgsf ')
        lb_title.pack(side=tkinter.RIGHT, padx=10)
        lb_title = ttk.Label(clientTopTab, text=' Name')
        lb_title.pack(side=tkinter.LEFT, padx=10)
        lb_title = ttk.Label(clientTopTab, text='Item Name')
        lb_title.pack(padx=10)
        #####################################################
        ###############test insert in treeview
        lis = []
        for i in range(1, 50):
            suplist = (
            25*i, f"Company {i}", f"Name {i}", i*45, f"email{i}")
            lis.append(suplist)
        print(lis)
        # client_tree.insert('','end', text=itemlist[0], values=itemlist[0:])
        ######################## ITEM TREEVIEW

        client_tree = ttk.Treeview(clientTreeview, height=18, columns=(
         "Client ID", "Company Name", "Agent", "Telephone", "Email"), show="headings")
        client_tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        # client_tree.insert('', 'end', text=itemlist[0], values=lis[0:])   # Insert data into the treeview
        for row in lis:
            client_tree.insert('', 'end', values=row)  # test Insert data into the treeview
        # Scrollbar for the treeview
        client_tree_scroll = ttk.Scrollbar(clientTreeview, orient="vertical", command=client_tree.yview)
        client_tree_scroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
        client_tree.configure(yscrollcommand=client_tree_scroll.set)
        ##### Heading of the treeview
        client_tree.heading(0, text="Client ID", anchor='center')
        client_tree.heading(1, text="Company Name", anchor='center')
        client_tree.heading(2, text="Agent", anchor='center')
        client_tree.heading(3, text="Telephone", anchor='center')
        client_tree.heading(4, text="Email", anchor='center')

        ##### Columns of the treeview
        client_tree.column(0, width=150, anchor='center')
        client_tree.column(1, width=300, anchor='center')
        client_tree.column(2, width=300, anchor='center')
        client_tree.column(3, width=100, anchor='center')
        client_tree.column(4, width=250, anchor='center')


        ################################# CLIENTS TAB, LABELS AND ENTRIES

        lb_SupplierId = ttk.Label(clientTab, text="Supplier ID:")
        lb_SupplierId.pack()
        self.clientIdEntry = ttk.Entry(clientTab)
        self.clientIdEntry.pack()
        lb_SupplierName = ttk.Label(clientTab, text="Company Name:")
        lb_SupplierName.pack()
        self.clientNameEntry = ttk.Entry(clientTab)
        self.clientNameEntry.pack()
        lb_SupplierAgent = ttk.Label(clientTab, text="Agent Full Name:")
        lb_SupplierAgent.pack()
        self.clientAgentEntry = ttk.Entry(clientTab)
        self.clientAgentEntry.pack()
        lb_SupplierTelephone = ttk.Label(clientTab, text="Telephone:")
        lb_SupplierTelephone.pack()
        self.clientTelephoneEntry = ttk.Entry(clientTab)
        self.clientTelephoneEntry.pack()
        lb_SupplierEmail = ttk.Label(clientTab, text="Email:")
        lb_SupplierEmail.pack()
        self.clientEmailEntry = ttk.Entry(clientTab)
        self.clientEmailEntry.pack()

        ###BUTTONS
        btn_InsertSupplier = ttk.Button(clientTab, text="Insert", command="")
        btn_InsertSupplier.pack()
        btn_UpdateSupplier = ttk.Button(clientTab, text="Update", command="")
        btn_UpdateSupplier.pack(side=tkinter.RIGHT)
        btn_SupplierShow = ttk.Button(clientTab, text="Show", command="")
        btn_SupplierShow.pack()
        self.notebook.add(clientFrame, text="Client")

###############################################################
        """USER"""

        #### MAIN FRAME ######################################################################
        userFrame = ttk.Frame(self.notebook)
        ##### TOP FRAME FOR LABELS (RENDER INFORMATION  #######################################
        userTopTab = ttk.Frame(userFrame)
        userTopTab.pack(side=tkinter.TOP)
        #### LEFT FRAME FOR THE ENTRIES, LABELS AND BUTTONS ###############################
        userTab = ttk.Frame(userFrame)
        userTab.pack(side=tkinter.LEFT)
        #### RIGHT FRAME FOR TREEVIEW AND SCROLLBAR ############################################
        userTreeview = ttk.Frame(userFrame)
        userTreeview.pack(side=tkinter.RIGHT)
        ###### TEST For Labels at the top of the treevieww to render information#########
        lb_title = ttk.Label(userTopTab, text='Itemfgsf Name')
        lb_title.pack()
        lb_title = ttk.Label(userTopTab, text='Itemfgsf ')
        lb_title.pack(side=tkinter.RIGHT, padx=10)
        lb_title = ttk.Label(userTopTab, text=' Name')
        lb_title.pack(side=tkinter.LEFT, padx=10)
        lb_title = ttk.Label(userTopTab, text='Item Name')
        lb_title.pack(padx=10)
        #####################################################
        ###############test insert in treeview
        lis = []
        for i in range(1, 50):
            suplist = (
                 i, f"Name {i}", f"Last Name {i}",f"email{i}")
            lis.append(suplist)
        print(lis)
        # user_tree.insert('','end', text=itemlist[0], values=itemlist[0:])
        ######################## ITEM TREEVIEW

        user_tree = ttk.Treeview(userTreeview, height=18, columns=(
            "User ID", "Name", "Last Name", "Email"), show="headings")
        user_tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        # user_tree.insert('', 'end', text=itemlist[0], values=lis[0:])   # Insert data into the treeview
        for row in lis:
            user_tree.insert('', 'end', values=row)  # test Insert data into the treeview
        # Scrollbar for the treeview
        user_tree_scroll = ttk.Scrollbar(userTreeview, orient="vertical", command=user_tree.yview)
        user_tree_scroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
        user_tree.configure(yscrollcommand=user_tree_scroll.set)
        ##### Heading of the treeview
        user_tree.heading(0, text="User ID", anchor='center')
        user_tree.heading(1, text="Name", anchor='center')
        user_tree.heading(2, text="Last Name", anchor='center')
        user_tree.heading(3, text="Email", anchor='center')

        ##### Columns of the treeview
        user_tree.column(0, width=150, anchor='center')
        user_tree.column(1, width=300, anchor='center')
        user_tree.column(2, width=300, anchor='center')
        user_tree.column(3, width=350, anchor='center')


        ################################# CLIENTS TAB, LABELS AND ENTRIES

        lb_UserName = ttk.Label(userTab, text="Name:")
        lb_UserName.pack()
        self.userNameEntry = ttk.Entry(userTab)
        self.userNameEntry.pack()
        lb_SupplierName = ttk.Label(userTab, text="Last Name:")
        lb_SupplierName.pack()
        self.userLastNameEntry = ttk.Entry(userTab)
        self.userLastNameEntry.pack()
        lb_UserEmail = ttk.Label(userTab, text="Email:")
        lb_UserEmail.pack()
        self.userEmailEntry = ttk.Entry(userTab)
        self.userEmailEntry.pack()


        ###BUTTONS
        btn_InsertUser = ttk.Button(userTab, text="Insert", command="")
        btn_InsertUser.pack()
        btn_UpdateUser = ttk.Button(userTab, text="Update", command="")
        btn_UpdateUser.pack(side=tkinter.RIGHT)
        btn_UserShow = ttk.Button(userTab, text="Show", command="")
        btn_UserShow.pack()
        self.notebook.add(userFrame, text="User")

###########################################################################


        """SEARCH"""
        frameSearch = ttk.Frame(self.notebook)
        lb_frameSearch = ttk.Label(frameSearch, text ="Search")
        lb_frameSearch.pack(padx = 5, pady =5)
        frameSearch.pack(expand=1,fill="both")

        # Notebook Widget

        # self.notebook.add(frameBilling, text = "Billing" )
        # self.notebook.add(frameItem, text = "Items")
        # self.notebook.add(frameSupplier, text = "Supplier")
        # self.notebook.add(frameClient, text = "Client")
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