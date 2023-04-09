# Here will be the frame to operate the inventory
import tkinter
from sys import path
from tkinter import ttk, messagebox, END, Text, Radiobutton

import tkcalendar as tkcalendar
from accesory import CreateToolTip
# Import DATABASE
from usersBD import UserDb, SupplierDB, ClientDB
#Acces to _users TABLE
client_collection = ClientDB()
user_collection = UserDb()
supplier_collection = SupplierDB()
from backend_user import User

ID = ""
LABELS = ("",12, '')
class SecondWindow:
    ##################################$$$$$$$$$$$$  SUPPLIER  $$$$$$$$$$$$$$$$#######################################
    """ When user click on Show button this will display the whole data from inventory_suppliers TABLE"""
    def showSupplier(self):
        # 1- first clear the data in treeview (otherwise the data in treeview will be repeated)
        for item in self.supplier_tree.get_children():
            self.supplier_tree.delete(item)
        # 2- fetch data from DB
        allsuppliers = supplier_collection.allSuppliers()

        for row in allsuppliers:
            # 3- INSERTION OF VALUES FROM DB TO TREEVIEEW
            self.supplier_tree.insert('', 'end', text=row[0], values=row[0:])

    """Insert new Supplier. button INSERT"""
    def insertSupplier(self):
        #Entries data
        sup_Id = self.supplierIdEntry.get()
        sup_Name = self.supplierNameEntry.get()
        sup_Agent = self.supplierAgentEntry.get()
        sup_Phone = self.supplierTelephoneEntry.get()
        sup_Email = self.supplierEmailEntry.get()

        # check if any entry case is empty
        if (sup_Id =='' or sup_Name  =='' or sup_Agent  =='' or
            sup_Phone  =='' or sup_Email  =='') :
            messagebox.showerror("Error","All the entry case must be filled!")
        # if all the data is correct
        else:
            messagebox.askyesno('Confirm', f"Do you want to add New Supplier \n\n\n Id: {sup_Id}\n\n"
                                           f"Company: {sup_Name} \n\n Agent: {sup_Agent} \n\n Telephone: {sup_Phone} \n\n"
                                           f"Email: {sup_Email}")
            supplier_collection.in_newSupplier(
                sup_Id,sup_Name,sup_Agent,sup_Phone,sup_Email
            )
            # this can be used to let know the user that the data of this id have been well inserted. With a messagebox
            print(supplier_collection.in_newSupplier)
            if supplier_collection.in_newSupplier:
                self.supplierIdEntry.delete(0, END)
                self.supplierNameEntry.delete(0, END)
                self.supplierAgentEntry.delete(0, END)
                self.supplierTelephoneEntry.delete(0, END)
                self.supplierEmailEntry.delete(0, END)

    """Update Supplier Agent, Telephone or/and Email . button UPDATE"""
    def update_supplier(self):
        sup_Id = self.supplierIdEntry.get()
        sup_Agent = self.supplierAgentEntry.get()
        sup_Phone = self.supplierTelephoneEntry.get()
        sup_Email = self.supplierEmailEntry.get()
        #supplier ID is mandatory
        if (sup_Id == "" or sup_Agent == "" or sup_Phone == "" or sup_Email == "") :
            messagebox.showerror("ERROR", "No empty case in: Supplieer ID, Agent Full name, Telephone and Email  entries" )
        else:
            #Confirme the change to update
            confirmeUpdate = messagebox.askokcancel("Confirmation", f" For the Supplier ID {sup_Id}, the new company details are: \n\n"
                                                f"Agent: {sup_Agent}\n\n Telephone: {sup_Phone} and\n\n Email: {sup_Email}" )
            if confirmeUpdate:
                supplier_collection.updateSupplier(sup_Id,sup_Agent,sup_Phone,sup_Email)
                #data have been updated
                messagebox.showinfo('Info', 'Data save ')
                #After the data have been updated clear the Entry widgets
                self.supplierIdEntry.delete(0, END)
                self.supplierNameEntry.delete(0, END)
                self.supplierAgentEntry.delete(0, END)
                self.supplierTelephoneEntry.delete(0, END)
                self.supplierEmailEntry.delete(0, END)
            else:
                messagebox.showwarning("Info", f"No change have been made for Suppplier id: {sup_Id}")
    #Funtion to clear the Entry boxes
    def clearSupplier(self):
        self.supplierIdEntry.delete(0, END)
        self.supplierNameEntry.delete(0, END)
        self.supplierAgentEntry.delete(0, END)
        self.supplierTelephoneEntry.delete(0, END)
        self.supplierEmailEntry.delete(0, END)
#####################################################################################################################

    ##################################$$$$$$$$$$$$ CLIENTS $$$$$$$$$$$$$$$$#######################################
    """ When user click on Show button this will display the whole data from inventory_clients TABLE"""

    def showClient(self):
        # 1- first clear the data in treeview (otherwise the data in treeview will be repeated)
        for item in self.client_tree.get_children():
            self.client_tree.delete(item)
        # 2- fetch data from DB
        allclients = client_collection.allClients()

        for row in allclients:
            # 3- INSERTION OF VALUES FROM DB TO TREEVIEEW
            self.client_tree.insert('', 'end', text=row[0], values=row[0:])

    """Insert new Client. button INSERT"""

    def insertClient(self):
        # Entries data
        cli_Id = self.clientIdEntry.get()
        cli_Name = self.clientNameEntry.get()
        cli_Agent = self.clientAgentEntry.get()
        cli_Phone = self.clientTelephoneEntry.get()
        cli_Email = self.clientEmailEntry.get()     # check if any entry case is empty
        if (cli_Id == '' or cli_Name == '' or cli_Agent == '' or
                cli_Phone == '' or cli_Email == ''):
            messagebox.showerror("Error", "All the entry case must be filled!")
        # if all the data is correct
        else:
            messagebox.askyesno('Confirm', f"Do you want to add New Client \n\n\n Id: {cli_Id}\n\n"
                                           f"Company: {cli_Name} \n\n Agent: {cli_Agent} \n\n Telephone: {cli_Phone} \n\n"
                                           f"Email: {cli_Email}")
            client_collection.in_newClient(
                cli_Id, cli_Name, cli_Agent, cli_Phone, cli_Email
            )
            # this can be used to let know the user that the data of this id have been well inserted. With a messagebox
            print(client_collection.in_newClient)
            if client_collection.in_newClient:
                # data have been inserted
                messagebox.showinfo('Info', 'Data save ')
                # After the data have been inserted clear the Entry widgets
                self.clientIdEntry.delete(0, END)
                self.clientNameEntry.delete(0, END)
                self.clientAgentEntry.delete(0, END)
                self.clientTelephoneEntry.delete(0, END)
                self.clientEmailEntry.delete(0, END)

    """Update Client Agent, Telephone or/and Email . button UPDATE"""

    def update_client(self):
        cli_Id = self.clientIdEntry.get()
        cli_Name = self.clientNameEntry.get()
        cli_Agent = self.clientAgentEntry.get()
        cli_Phone = self.clientTelephoneEntry.get()
        cli_Email = self.clientEmailEntry.get()
        # supplier ID is mandatory
        if (cli_Id == "" or cli_Agent == "" or cli_Phone == "" or cli_Email == ""):
            messagebox.showerror("ERROR","No empty case in: Client ID, Agent Full name, Telephone and Email  entries")
        else:
            # Confirme the change to update
            confirmeUpdate = messagebox.askokcancel("Confirmation",
                                                    f" For the Client ID {cli_Id}, the new company details are: \n\n"
                                                    f"Agent: {cli_Agent}\n\n Telephone: {cli_Phone} and\n\n Email: {cli_Email}")
            if confirmeUpdate:
                client_collection.updateClient(cli_Id, cli_Agent, cli_Phone, cli_Email)
                # data have been updated
                messagebox.showinfo('Info', 'Data save ')
                # After the data have been updated clear the Entry widgets

                self.clientIdEntry.delete(0, END)
                self.clientNameEntry.delete(0, END)
                self.clientAgentEntry.delete(0, END)
                self.clientTelephoneEntry.delete(0, END)
                self.clientEmailEntry.delete(0, END)
            else:
                messagebox.showwarning("Info", f"No change have been made for Client id: {cli_Id}")

    #################################################################################################################

#######################################$$$$$$$$$$$$$  USER   $$$$$$$$$$$$$$$$$########################################
    """User data operation"""
    #User INSERT data
    def insert_user_data(self):
        Name = self.userNameEntry.get()
        LastName = self.userLastNameEntry.get()
        Email = self.userEmailEntry.get()
        # Admin = self.cb_Admin.get() ###To change
        # print(Admin)
        '''Check that all the necessary cases contains data'''
        if Name=='' or LastName =='' or Email=='' :
            messagebox.showerror('Error!', "Name, Lastname and Email must be entered")
        else:
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
                user_collection.user_data_collection(
                    Name.lower(), LastName.lower(),Email
                )
                # return of the user id number
                messagebox.showinfo(f"Your user ID: {str(user_collection.last_insert_id)}",
                                    f"Welcome to Inventory {Name} {LastName} this is your User ID: {str(user_collection.last_insert_id)}. \n This number is your ID and is necessary to use")
                print('ultimo mensaje')
                if True:
                    print('now deleted data')
                    self.userNameEntry.delete(0, END)
                    self.userLastNameEntry.delete(0, END)
                    self.userEmailEntry.delete(0, END)

            # User UPDATE data   THIS CODE  IS NOT WORKING
    def userUpdate(self):
        idUser = self.userIdEntry.get()
        Email = self.userEmailEntry.get()
        print(idUser)
        print(Email)
        # check is the case id and email are fill. Only email can be updated in user DB
        if idUser == ''  or Email == '':
            messagebox.showerror('Opp! Error Update', 'For Update User "email", ID and email case must be filled! ')
        else:
            print("A confirmar")
            # messsage to confirme with the user if the data to Update is correct
            confirmation = messagebox.askyesno(
                "User Update", f"For User ID: {idUser} Do you wan to update the email to: {Email}   ")
            if confirmation :

                user_collection.updateUser(id=idUser, email=Email)
                if True:
                    messagebox.showinfo('Message', f'User email is Updated')
                    self.userNameEntry.delete(0,END)
                    self.userEmailEntry.delete(0, END)
                else:
                    messagebox.showerror('Ops!', "Error, the User email hasn't been updated")
    # User Tab, Show button - update Treeview
    def show(self):
        #1- first clear the data in treeview (otherwise the data in treeview will be repeated)
        for item in self.user_tree.get_children():
            self.user_tree.delete(item)
        #2- fetch data from DB
        allusers = user_collection.userAll()

        for row in allusers:
            #3- INSERTION OF VALUES FROM DB TO TREEVIEEW
            self.user_tree.insert('', 'end', text=row[0], values=row[0:])
#######################################################################################################
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
       
        #################
        #### MAIN FRAME ######################################################################
        BillingFrame = ttk.Frame(self.notebook)
        ##### TOP FRAME FOR LABELS (RENDER INFORMATION  #######################################
        BillingTopTab = ttk.Frame(BillingFrame)
        BillingTopTab.pack(side=tkinter.TOP)
        #### LEFT FRAME FOR THE ENTRIES, LABELS AND BUTTONS ###############################
        BillingTab = ttk.Frame(BillingFrame)
        BillingTab.pack(side=tkinter.LEFT)
        #### RIGHT FRAME FOR TREEVIEW AND SCROLLBAR ############################################
        BillingTreeview = ttk.Frame(BillingFrame)
        BillingTreeview.pack(side=tkinter.RIGHT)
        ###### TEST For Labels at the top of the treevieww to render information#########
        lb_title = ttk.Label(BillingTopTab, text='User ID selected : ')
        lb_title.pack()
        lb_title = ttk.Label(BillingTopTab, text='Itemfgsf ')
        lb_title.pack(side=tkinter.RIGHT, padx=10)
        lb_title = ttk.Label(BillingTopTab, text=' Name')
        lb_title.pack(side=tkinter.LEFT, padx=10)
        lb_title = ttk.Label(BillingTopTab, text='Item Name')
        lb_title.pack(padx=10)
        #####################################################
        ###############test insert in treeview
        lis = []
        for i in range(1, 50):
            itemlist = (
            f'{i}', "object", "17/02/2023", "supplier", 100 + (i * 4), f"${2 + i}", 5 * i, "level 1",
            f'{i*2}%', 'trhsfghsfgbhsfgbafcvarvfvafvafva afvgasfavbsf asfdvasfv ', f'ID{i}')
            lis.append(itemlist)
        print(lis)
        # item_tree.insert('','end', text=itemlist[0], values=itemlist[0:])
        ######################## ITEM TREEVIEW

        Billing_tree = ttk.Treeview(BillingTreeview, height=18, columns=(
            "Reference ID", "Type of Transaction", "Date", "Company ID", "Item ID", "Item Name", "Quantity", "Price",
            "Discount", "Description", "UserID"), show="headings")
        Billing_tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        # item_tree.insert('', 'end', text=itemlist[0], values=lis[0:])   # Insert data into the treeview
        for row in lis:
            Billing_tree.insert('', 'end', values=row)  # test Insert data into the treeview
        # Scrollbar for the treeview
        Billing_tree_scroll = ttk.Scrollbar(BillingTreeview, orient="vertical", command=Billing_tree.yview)
        Billing_tree_scroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
        Billing_tree.configure(yscrollcommand=Billing_tree_scroll.set)
        ##### Heading of the treeview
        Billing_tree.heading(0, text="Reference ID", anchor='center')
        Billing_tree.heading(1, text="Type of Transacation", anchor='center')
        Billing_tree.heading(2, text="Date", anchor='center')
        Billing_tree.heading(3, text="Company ID", anchor='center')
        Billing_tree.heading(4, text="Item ID", anchor='center')
        Billing_tree.heading(5, text="Item Name", anchor='center')
        Billing_tree.heading(6, text="Quantity", anchor='center')
        Billing_tree.heading(7, text="Price", anchor='center')
        Billing_tree.heading(8, text="Discount", anchor='center')
        Billing_tree.heading(9, text="Description", anchor='center')
        Billing_tree.heading(10, text="User ID", anchor='center')
        ##### Columns of the treeview
        Billing_tree.column(0, width=80, anchor='center')
        Billing_tree.column(1, width=80, anchor='center')
        Billing_tree.column(2, width=80, anchor='center')
        Billing_tree.column(3, width=80, anchor='center')
        Billing_tree.column(4, width=70, anchor='center')
        Billing_tree.column(5, width=100, anchor='center')
        Billing_tree.column(6, width=60, anchor='center')
        Billing_tree.column(7, width=50, anchor='center')
        Billing_tree.column(8, width=60, anchor='center')
        Billing_tree.column(9, width=300, anchor='center')
        Billing_tree.column(10, width=50, anchor='center')

        ################################# ITEMS TAB, LABELS AND ENTRIES
        inStock = tkinter.IntVar() #If this radiobutton check = 1. else = 0 RADIOBUTTON
        outStock = tkinter.IntVar() #If this radiobutton check = 1 else = 0 RADIOBUTTON
        inStock = tkinter.Radiobutton(BillingTab, text="In", variable=inStock, command="")
        inStock.pack(side=tkinter.TOP)
        outStock = tkinter.Radiobutton(BillingTab, text="Out", variable=outStock, command="")
        outStock.pack()

        date = tkcalendar.DateEntry(BillingTab, width=10)
        date.pack()
        lb_ItemCode = ttk.Label(BillingTab, text="Reference Number:")
        lb_ItemCode.pack()
        self.BillingCodeEntry = ttk.Entry(BillingTab)
        self.BillingCodeEntry.pack()
        lb_ItemName = ttk.Label(BillingTab, text="Company ID:")
        lb_ItemName.pack()
        self.BillingNameEntry = ttk.Entry(BillingTab)
        self.BillingNameEntry.pack()
        lb_ItemDescription = ttk.Label(BillingTab, text="Item ID:")
        lb_ItemDescription.pack()
        self.BillingDescriptionEntry = ttk.Entry(BillingTab)
        self.BillingDescriptionEntry.pack()
        lb_ItemDescription = ttk.Label(BillingTab, text="Item Name:")
        lb_ItemDescription.pack()
        self.BillingDescriptionEntry = ttk.Entry(BillingTab)
        self.BillingDescriptionEntry.pack()
        lb_ItemSupplierId = ttk.Label(BillingTab, text="Quantity:")
        lb_ItemSupplierId.pack()
        self.BillingSupplierIdEntry = ttk.Entry(BillingTab)
        self.BillingSupplierIdEntry.pack()
        lb_ItemQuantity = ttk.Label(BillingTab, text="Price:")
        lb_ItemQuantity.pack()
        self.BillingQuantityEntry = ttk.Entry(BillingTab)
        self.BillingQuantityEntry.pack()
        lb_ItemPrice = ttk.Label(BillingTab, text="Discount:")
        lb_ItemPrice.pack()
        self.BillingPriceEntry = ttk.Entry(BillingTab)
        self.BillingPriceEntry.pack()
        lb_ItemMinStock = ttk.Label(BillingTab, text="Description:")
        lb_ItemMinStock.pack()
        self.BillingMinStockEntry = tkinter.Text(BillingTab, width = 20, height = 3)
        self.BillingMinStockEntry.pack()



        ###BUTTONS
        btn_InsertItem = ttk.Button(BillingTab, text="Insert")
        btn_InsertItem.pack()
        btn_UpdateItem = ttk.Button(BillingTab, text="Update")
        btn_UpdateItem.pack(side=tkinter.RIGHT)
        btn_ItemShow = ttk.Button(BillingTab, text="Show")
        btn_ItemShow.pack()
        ####
        self.notebook.add(BillingFrame, text="Billing")
                  ## END BILLING ###
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

        item_tree = ttk.Treeview(itemTreeview, height=18, columns=("Item Code","Name", "Description","Supplier",
                                                                   "Quantity","Price","Min. Stock", "Location"), show="headings")
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
        # Insert button
        btn_InsertItem = ttk.Button(itemTab, text="Insert", command=lambda: self.insertItem())
        btn_InsertItem.pack(side=tkinter.TOP)
        btn_InsertItem.bind("<Return>", lambda event: self.insertItem()(btn_InsertItem["Insert"]))
        # Update button
        btn_UpdateItem = ttk.Button(itemTab, text="Update", command=lambda: self.update_Item())
        btn_UpdateItem.pack(side=tkinter.TOP)
        btn_UpdateItem.bind("<Return>", lambda event: self.update_Item()(btn_UpdateItem["Update"]))
        # Show button
        btn_ItemShow = ttk.Button(itemTab, text="Show", command=lambda: self.showItem())
        btn_ItemShow.pack(side=tkinter.LEFT)
        btn_ItemShow.bind("<Return>", lambda event: self.showSupplier()(btn_InsertItem["Show"]))
        # Clear button
        btn_ItemClear = ttk.Button(itemTab, text="Clear", command=lambda: self.clearItem())
        btn_ItemClear.pack()
        btn_ItemClear.bind("<Return>", lambda event: self.clearItem()(btn_ItemClear["Clear"]))
        # END
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

        lb_title = ttk.Label(supplierTopTab, text='Selection:', font=('',16,'bold'))
        lb_title.pack()
        lb_1Title = ttk.Label(supplierTopTab, text='Id: ', font=('',12,'bold'))
        lb_1Title.pack(side=tkinter.LEFT )
        lb_titleSupId = ttk.Label(supplierTopTab, text='', background='white', font=('',14,'bold'))
        lb_titleSupId.pack(side=tkinter.LEFT )
        lb_2Title = ttk.Label(supplierTopTab, text='     Name:', font=('',12,'bold'))
        lb_2Title.pack(side=tkinter.LEFT)
        lb_titleSupName = ttk.Label(supplierTopTab, text='',background='white')
        lb_titleSupName.pack(side=tkinter.LEFT)
        lb_3Title = ttk.Label(supplierTopTab, text='     Agent:', font=('',12,'bold'))
        lb_3Title.pack(side=tkinter.LEFT)
        lb_titleSupAgent = ttk.Label(supplierTopTab, text='',background='white')
        lb_titleSupAgent.pack(side=tkinter.LEFT)
        lb_4Title = ttk.Label(supplierTopTab, text='     Telephone:', font=('',12,'bold'))
        lb_4Title.pack(side=tkinter.LEFT)
        lb_titleSupPhone = ttk.Label(supplierTopTab, text='',background='white')
        lb_titleSupPhone.pack(side=tkinter.LEFT)
        lb_4Title = ttk.Label(supplierTopTab, text='     Email:', font=('', 12, 'bold'))
        lb_4Title.pack(side=tkinter.LEFT)
        lb_titleSupEmail = ttk.Label(supplierTopTab, text='', background='white')
        lb_titleSupEmail.pack(side=tkinter.LEFT)
        #####################################################


        ######################## ITEM TREEVIEW

        self.supplier_tree = ttk.Treeview(supplierTreeview, height=18, columns=(
         "Supplier ID", "Company Name", "Agent", "Telephone", "Email"), show="headings")
        self.supplier_tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        """Display in the treeview all the data from the inventory_suppliers TABLE """
        # fetch data from DB
        allsuppliers = supplier_collection.allSuppliers()

        for row in allsuppliers:
            # - INSERTION OF VALUES FROM DB TO TREEVIEEW
            self.supplier_tree.insert('', 'end', text=row[0], values=row[0:])
        # Scrollbar for the treeview
        supplier_tree_scroll = ttk.Scrollbar(supplierTreeview, orient="vertical", command=self.supplier_tree.yview)
        supplier_tree_scroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.supplier_tree.configure(yscrollcommand=supplier_tree_scroll.set)
        ##### Heading of the treeview
        self.supplier_tree.heading(0, text="Supplier ID", anchor='center')
        self.supplier_tree.heading(1, text="Company Name", anchor='center')
        self.supplier_tree.heading(2, text="Agent", anchor='center')
        self.supplier_tree.heading(3, text="Telephone", anchor='center')
        self.supplier_tree.heading(4, text="Email", anchor='center')

        ##### Columns of the treeview
        self.supplier_tree.column(0, width=150, anchor='center')
        self.supplier_tree.column(1, width=300, anchor='center')
        self.supplier_tree.column(2, width=300, anchor='center')
        self.supplier_tree.column(3, width=100, anchor='center')
        self.supplier_tree.column(4, width=250, anchor='center')
        ####Select items from the treeview###
        ######################################
        """this methods is to select,fetch and return data from the clicked row in the treeview """

        def treeview_select(event):
            # FETCH SELECTED ROW
            select_SupplierId = event.widget.selection()[0]
            # FETCH ALL VALUES OF THE ROW
            select_SupplierIdValue = event.widget.item(select_SupplierId)['values']
            """Configuration of the labes at the topframe. When the user clicks one of the row in the treeview the data 
            from the clicked row will be display at the top. thE VALUE ARE INDEXED"""

            """Rendering the selected row in the treeview into the Entry widgets"""
            # Supplier ID
            self.supplierIdEntry.delete(0, END)
            self.supplierIdEntry.insert(0, select_SupplierIdValue[0])
            # SUPPLIER NAME
            self.supplierNameEntry.delete(0, END)
            self.supplierNameEntry.insert(0, select_SupplierIdValue[1])
            # AGENT SUPPLIER
            self.supplierAgentEntry.delete(0, END)
            self.supplierAgentEntry.insert(0, select_SupplierIdValue[2])
            # SUPPLIER PHONE
            self.supplierTelephoneEntry.delete(0, END)
            self.supplierTelephoneEntry.insert(0, select_SupplierIdValue[3])
            # SUPPLIER EMAIL
            self.supplierEmailEntry.delete(0, END)
            self.supplierEmailEntry.insert(0, select_SupplierIdValue[4])
            """Render selected row in the treeviw at the TopFrame"""
            #Supplier ID
            lb_titleSupId.config(text=select_SupplierIdValue[0])
            #Supplier Name
            lb_titleSupName.config(text=select_SupplierIdValue[1])
            #Supplier Agent
            lb_titleSupAgent.config(text=select_SupplierIdValue[2])
            #Supplier Phone
            lb_titleSupPhone.config(text=select_SupplierIdValue[3])
            #Supplier Email
            lb_titleSupEmail.config(text=select_SupplierIdValue[4])
            return select_SupplierIdValue

        self.supplier_tree.bind('<<TreeviewSelect>>', treeview_select)
        #######################################################

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
        #Insert button
        btn_InsertSupplier = ttk.Button(supplierTab, text="Insert", command=lambda : self.insertSupplier())
        btn_InsertSupplier.pack(side=tkinter.TOP)
        btn_InsertSupplier.bind("<Return>", lambda event: self.insertSupplier()(btn_InsertSupplier["Insert"]))
        #Update button
        btn_UpdateSupplier = ttk.Button(supplierTab, text="Update", command=lambda : self.update_supplier())
        btn_UpdateSupplier.pack(side=tkinter.TOP)
        btn_UpdateSupplier.bind("<Return>", lambda event: self.update_supplier()(btn_UpdateSupplier["Update"]))
        #Show button
        btn_SupplierShow = ttk.Button(supplierTab, text="Show", command= lambda : self.showSupplier())
        btn_SupplierShow.pack(side=tkinter.LEFT)
        btn_SupplierShow.bind("<Return>", lambda event: self.showSupplier()(btn_InsertSupplier["Show"]))
        #Clear button
        btn_SupplierClear = ttk.Button(supplierTab, text="Clear", command=lambda: self.clearSupplier())
        btn_SupplierClear.pack()
        btn_SupplierClear.bind("<Return>", lambda event: self.clearSupplier()(btn_SupplierClear["Clear"]))
        #END
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
        lb_title = ttk.Label(clientTopTab, text='Selection:', font=('', 16, 'bold'))
        lb_title.pack()
        lb_1Title = ttk.Label(clientTopTab, text='Id: ', font=('', 12, 'bold'))
        lb_1Title.pack(side=tkinter.LEFT)
        lb_titleCliId = ttk.Label(clientTopTab, text='', background='white', font=('', 14, 'bold'))
        lb_titleCliId.pack(side=tkinter.LEFT)
        lb_2Title = ttk.Label(clientTopTab, text='     Name:', font=('', 12, 'bold'))
        lb_2Title.pack(side=tkinter.LEFT)
        lb_titleCliName = ttk.Label(clientTopTab, text='', background='white')
        lb_titleCliName.pack(side=tkinter.LEFT)
        lb_3Title = ttk.Label(clientTopTab, text='     Agent:', font=('', 12, 'bold'))
        lb_3Title.pack(side=tkinter.LEFT)
        lb_titleCliAgent = ttk.Label(clientTopTab, text='', background='white')
        lb_titleCliAgent.pack(side=tkinter.LEFT)
        lb_4Title = ttk.Label(clientTopTab, text='     Telephone:', font=('', 12, 'bold'))
        lb_4Title.pack(side=tkinter.LEFT)
        lb_titleCliPhone = ttk.Label(clientTopTab, text='', background='white')
        lb_titleCliPhone.pack(side=tkinter.LEFT)
        lb_4Title = ttk.Label(clientTopTab, text='     Email:', font=('', 12, 'bold'))
        lb_4Title.pack(side=tkinter.LEFT)
        lb_titleCliEmail = ttk.Label(clientTopTab, text='', background='white')
        lb_titleCliEmail.pack(side=tkinter.LEFT)
        #####################################################

        ######################## ITEM TREEVIEW

        self.client_tree = ttk.Treeview(clientTreeview, height=18, columns=(
         "Client ID", "Company Name", "Agent", "Telephone", "Email"), show="headings")
        self.client_tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        """Display in the treeview all the data from the inventory_suppliers TABLE """
        # fetch data from DB
        allclients = client_collection.allClients()

        for row in allclients:
            # - INSERTION OF VALUES FROM DB TO TREEVIEEW
            self.client_tree.insert('', 'end', text=row[0], values=row[0:])
        # Scrollbar for the treeview
        client_tree_scroll = ttk.Scrollbar(clientTreeview, orient="vertical", command=self.client_tree.yview)
        client_tree_scroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.client_tree.configure(yscrollcommand=client_tree_scroll.set)
        ##### Heading of the treeview
        self.client_tree.heading(0, text="Client ID", anchor='center')
        self.client_tree.heading(1, text="Company Name", anchor='center')
        self.client_tree.heading(2, text="Agent", anchor='center')
        self.client_tree.heading(3, text="Telephone", anchor='center')
        self.client_tree.heading(4, text="Email", anchor='center')

        ##### Columns of the treeview
        self.client_tree.column(0, width=150, anchor='center')
        self.client_tree.column(1, width=300, anchor='center')
        self.client_tree.column(2, width=300, anchor='center')
        self.client_tree.column(3, width=100, anchor='center')
        self.client_tree.column(4, width=250, anchor='center')

        ####Select items from the treeview###
        ######################################
        """this methods is to select,fetch and return data from the clicked row in the treeview """

        def treeview_select(event):
            # FETCH SELECTED ROW
            select_ClientId = event.widget.selection()[0]
            # FETCH ALL VALUES OF THE ROW
            select_ClientIdValue = event.widget.item(select_ClientId)['values']
            """Configuration of the labes at the topframe. When the user clicks one of the row in the treeview the data 
            from the clicked row will be display at the top. thE VALUE ARE INDEXED"""

            """Rendering the selected row in the treeview into the Entry widgets"""
            # CLIENT ID
            self.clientIdEntry.delete(0, END)
            self.clientIdEntry.insert(0, select_ClientIdValue[0])
            # CLIENT NAME
            self.clientNameEntry.delete(0, END)
            self.clientNameEntry.insert(0, select_ClientIdValue[1])
            # AGENT CLIENT
            self.clientAgentEntry.delete(0, END)
            self.clientAgentEntry.insert(0, select_ClientIdValue[2])
            # CLIENT PHONE
            self.clientTelephoneEntry.delete(0, END)
            self.clientTelephoneEntry.insert(0, select_ClientIdValue[3])
            # CLIENT EMAIL
            self.clientEmailEntry.delete(0, END)
            self.clientEmailEntry.insert(0, select_ClientIdValue[4])
            """Render selected row in the treeviw at the TopFrame"""
            # Client ID
            lb_titleCliId.config(text=select_ClientIdValue[0])
            # Client Name
            lb_titleCliName.config(text=select_ClientIdValue[1])
            # Client Agent
            lb_titleCliAgent.config(text=select_ClientIdValue[2])
            # Client Phone
            lb_titleCliPhone.config(text=select_ClientIdValue[3])
            # Client Email
            lb_titleCliEmail.config(text=select_ClientIdValue[4])
            return select_ClientIdValue

        self.client_tree.bind('<<TreeviewSelect>>', treeview_select)
        #######################################################

        ################################# CLIENTS TAB, LABELS AND ENTRIES

        lb_ClientId = ttk.Label(clientTab, text="Supplier ID:")
        lb_ClientId.pack()
        self.clientIdEntry = ttk.Entry(clientTab)
        self.clientIdEntry.pack()
        lb_ClientName = ttk.Label(clientTab, text="Company Name:")
        lb_ClientName.pack()
        self.clientNameEntry = ttk.Entry(clientTab)
        self.clientNameEntry.pack()
        lb_ClientAgent = ttk.Label(clientTab, text="Agent Full Name:")
        lb_ClientAgent.pack()
        self.clientAgentEntry = ttk.Entry(clientTab)
        self.clientAgentEntry.pack()
        lb_ClientTelephone = ttk.Label(clientTab, text="Telephone:")
        lb_ClientTelephone.pack()
        self.clientTelephoneEntry = ttk.Entry(clientTab)
        self.clientTelephoneEntry.pack()
        lb_ClientEmail = ttk.Label(clientTab, text="Email:")
        lb_ClientEmail.pack()
        self.clientEmailEntry = ttk.Entry(clientTab)
        self.clientEmailEntry.pack()

        ###BUTTONS
        btn_InsertClient = ttk.Button(clientTab, text="Insert", command=lambda : self.insertClient())
        btn_InsertClient.pack()
        btn_UpdateClient = ttk.Button(clientTab, text="Update", command=lambda : self.update_client())
        btn_UpdateClient.pack(side=tkinter.RIGHT)
        btn_ClientShow = ttk.Button(clientTab, text="Show", command=lambda : self.showClient())
        btn_ClientShow.pack()
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

        lb_title = ttk.Label(userTopTab, text='Selection:', font=('',16,'bold'))
        lb_title.pack()
        lb_1Title = ttk.Label(userTopTab, text='User Id: ', font=('',12,'bold'))
        lb_1Title.pack(side=tkinter.LEFT )
        lb_titleUser = ttk.Label(userTopTab, text='', background='white', font=('',14,'bold'))
        lb_titleUser.pack(side=tkinter.LEFT )
        lb_2Title = ttk.Label(userTopTab, text='     Name:', font=('',12,'bold'))
        lb_2Title.pack(side=tkinter.LEFT)
        lb_titleName = ttk.Label(userTopTab, text='',background='white')
        lb_titleName.pack(side=tkinter.LEFT)
        lb_3Title = ttk.Label(userTopTab, text='     Lastname:', font=('',12,'bold'))
        lb_3Title.pack(side=tkinter.LEFT)
        lb_titleLastName = ttk.Label(userTopTab, text='',background='white')
        lb_titleLastName.pack(side=tkinter.LEFT)
        lb_4Title = ttk.Label(userTopTab, text='     Email:', font=('',12,'bold'))
        lb_4Title.pack(side=tkinter.LEFT)
        lb_titleEmail = ttk.Label(userTopTab, text='',background='white')
        lb_titleEmail.pack(side=tkinter.LEFT)

        #####################################################

        ######################## USER TREEVIEW

        self.user_tree = ttk.Treeview(userTreeview, height=18, columns=(
            "User ID", "Name", "Last Name", "Email"), show="headings")
        self.user_tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

        """Display in the treeview all the data from the _users TABLE """
        allusers = user_collection.userAll()
        for row in allusers:

            # INSERTION OF VALUES FROM DB TO TREEVIEEW
            self.user_tree.insert('', 'end', text=row[0], values=row[0:])   # Insert data into the treeview
        ##############################SCROLL BAR ###########################
        user_tree_scroll = ttk.Scrollbar(userTreeview, orient="vertical", command=self.user_tree.yview)
        user_tree_scroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.user_tree.configure(yscrollcommand=user_tree_scroll.set)
        ##### Heading of the treeview
        self.user_tree.heading(0, text="User ID", anchor='center')
        self.user_tree.heading(1, text="Name", anchor='center')
        self.user_tree.heading(2, text="Last Name", anchor='center')
        self.user_tree.heading(3, text="Email", anchor='center')

        ##### Columns of the treeview
        self.user_tree.column(0, width=150, anchor='center')
        self.user_tree.column(1, width=300, anchor='center')
        self.user_tree.column(2, width=300, anchor='center')
        self.user_tree.column(3, width=350, anchor='center')
        ####################################
        ####Select items from the treeview###
        ######################################
        """this methods is to select,fetch and return data from the clicked row in the treeview """
        def treeview_select(event):
            # FETCH SELECTED ROW
            select_userId = event.widget.selection()[0]
            # FETCH ALL VALUES OF THE ROW
            select_userIdValue = event.widget.item(select_userId)['values']
            """Configuration of the labes at the topframe. When the user clicks one of the row in the treeview the data 
            from the clicked row will be display at the top. thE VALUE ARE INDEXED"""
            #USER ID
            lb_titleUser.config(text= select_userIdValue[0] )
            # USER NAME
            lb_titleName.config(text= select_userIdValue[1] )
            #USER LASTNAME
            lb_titleLastName.config(text= select_userIdValue[2] )
            #USER EMAIL
            lb_titleEmail.config(text=select_userIdValue[3])

            return select_userIdValue
        self.user_tree.bind('<<TreeviewSelect>>', treeview_select)
        #######################################################
        ################################# USER TAB, LABELS AND ENTRIES
        lb_UserId = ttk.Label(userTab, text="ID:")
        lb_UserId.pack()
        self.userIdEntry = ttk.Entry(userTab)
        self.userIdEntry.pack()
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
        # Insert data into the DB
        btn_InsertUser = ttk.Button(userTab, text="Insert", command=lambda : self.insert_user_data())
        btn_InsertUser.pack()
        # Update a particular row
        btn_UpdateUser = ttk.Button(userTab, text="Update", command=lambda : self.userUpdate())
        btn_UpdateUser.pack(side=tkinter.RIGHT)
        # Refresh data display in treeview
        btn_UserShow = ttk.Button(userTab, text="Show", command=lambda : self.show())
        btn_UserShow.pack()
        ######
        self.notebook.add(userFrame, text="User")

###########################################################################


        """SEARCH"""
        frameSearch = ttk.Frame(self.notebook)
        lb_frameSearch = ttk.Label(frameSearch, text ="Search")
        lb_frameSearch.pack(padx = 5, pady =5)
        frameSearch.pack(expand=1,fill="both")

        # Notebook Widget


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
    window = SecondWindow(root,6,"Alba") #6,"Alba" is to activate the page, when finished delete only root left

    root.mainloop()

if __name__ == '__main__':
    app()

