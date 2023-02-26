# Here will be the frame to operate the inventory
import tkinter
from sys import path
from tkinter import ttk, messagebox, END, Text, Radiobutton, Listbox,StringVar, IntVar
import tkcalendar as tkcalendar
from datetime import datetime
from accesory import CreateToolTip
# Import DATABASE
from usersBD import UserDb, SupplierDB, ClientDB, ItemDB, BillingDB
#Acces to _users TABLE
client_collection = ClientDB()
user_collection = UserDb()
supplier_collection = SupplierDB()
item_collection = ItemDB()
billing_collection = BillingDB()
from backend_user import User

ID = ""
LABELS = ("",12, '')
class SecondWindow:
    ##################################$$$$$$$$$$$$  Billing  $$$$$$$$$$$$$$$$#######################################


    """ When user click on Show button this will display the whole data from inventory_suppliers TABLE"""
    #fuction call  by Show Button
    def showBill(self):
        # 1- first clear the data in treeview (otherwise the data in treeview will be repeated)
        for bill in self.billing_tree.get_children():
            self.billing_tree.delete(bill)
        # 2- fetch data from DB
        allbills = billing_collection.allBill()

        for row in allbills:
            # 3- INSERTION OF VALUES FROM DB TO TREEVIEEW
            self.billing_tree.insert('', 'end', text=row[0], values=row[0:])

    """Insert new Bill. button INSERT"""
    def insertBill(self):

        # logged user Name
        username_in_the_system = self.user_name
        # logged user ID
        username_in_the_systemID = int(self.user_id)
        # print(self.get_billType())
        ### Entries data
        # This catch the choice in radiobutton
        billType = self.BILLING.get()
        print(billType)
        # Bill reference number
        billCode = self.BillCodeEntry.get()
        # Name of the company Client or Supplier
        billCompanyId = self.BillCompanyIdEntry.get()
        # Item ID
        billItemId = self.BillItemIdEntry.get()
        # Item name
        billItemName = self.BillItemNameEntry.get()
        # Qty of the item to in or out of the stock
        billQty = self.BillQtyEntry.get()
        #Item price
        billPrice = self.BillPriceEntry.get()
        #If didcount on the item price
        billDiscount = self.BillDiscountEntry.get()
        #description on the bill transaction
        billDescription = self.BillDescriptionEntry.get("1.0", "end")
        # date that the bill is inserted
        dateIn = datetime.today().strftime('%m/%d/%Y')
        # date when the order was made
        billDate = self.date.get_date()

        # """FIRST CHECK. this function check if the billCode already exist in the DB   """
        # checkBillCode = billing_collection.checkId(billCode)
        # if checkBillCode == False:
        #     messagebox.showerror('ERROR',"The Reference Number for")
        # check if any entry case is empty
        if (billCode == '' or billCompanyId == '' or billItemId == '' or billItemName == '' or billQty == '' or
            billPrice == '' or  billDiscount == ''  ):
            #maybe to specify in the message with Entry case are mandatory
            messagebox.showerror("Error", "All the entry case must be filled!")
        # if all the data is correct
        else:
            """update_result is avariable that takes parameters to update the item quantity and at the same time,
            check if there is more than the bill quantity, in case there is not enough items it will return false 
            and let know the user that the operation is not possible"""
            update_result = item_collection.updateItemQty(itemID=billItemId,BillType=billType, BillQty=billQty)
            #if the billQty is > that the item quantity
            if update_result == False:
                 messagebox.showerror('ERROR', f"Sorry the quantity of the bill: {billCode} is superior to "
                                                  f"the quantity in the store!")

            else:
                print(str(update_result)+ " Item quantity updated successfully")
                confirmation = messagebox.askyesno('Confirm',
                                f"{username_in_the_system} Do you want to create the Bill Reference: {billCode}\n\n"
                                f"Item name: {billItemName} \n\n to/from Company ID: {billCompanyId} \n\n "
                                f"Item: {billItemName} \n\n Quantity: { billQty} \n\n "
                                f"Price: {billPrice} \n\n Discount:{billDiscount} \n\n "
                                )
                if confirmation:
                    billing_collection.in_newBill(billCode,billType,billCompanyId,billItemId, billItemName, int(billQty),
                                                  billPrice, billDiscount, dateIn, billDate, billDescription,
                                                  username_in_the_systemID )
                    messagebox.showinfo("Bill Done", f"Bill number: '{billCode}' Save!")
            # this can be used to let know the user that the data of this id have been well inserted. With a messagebox
                    print(billing_collection.in_newBill)
                    if billing_collection.in_newBill:
                        self.BillCodeEntry.delete(0,END)
                        self.BillCompanyIdEntry.delete(0,END)
                        self.BillItemIdEntry.delete(0,END)
                        self.BillItemNameEntry.delete(0,END)
                        self.BillQtyEntry.delete(0,END)
                        self.BillPriceEntry.delete(0,END)
                        self.BillDiscountEntry.delete(0,END)
                        self.BillDescriptionEntry.delete('1.0','end')

    """Update Item description, Qty, price, updateBy, updateDate, minStock or/ and location . button UPDATE"""

    def update_Item(self):
        pass
    #     # logged user Name
    #     username_in_the_system = self.user_name
    #     # logged user ID
    #     username_in_the_systemID = int(self.user_id)
    #
    #     # Entries data
    #     itemCode = self.itemCodeEntry.get()
    #     itemDescription = self.itemDescriptionEntry.get()
    #     itemQty = self.itemQuantityEntry.get()
    #     itemPrice = self.itemPriceEntry.get()
    #     dateUpdate = datetime.today().strftime('%m/%d/%Y')
    #     itemMinStock = self.itemMinStockEntry.get()
    #     itemLocation = self.itemLocationEntry.get()
    #     #  Item code ID is mandatory
    #     if (
    #             itemCode == "" or itemDescription == "" or itemQty == "" or itemPrice == "" or
    #             itemMinStock == "" or itemLocation == ""):
    #         print(itemCode, itemDescription, itemQty, itemPrice, dateUpdate, itemMinStock, itemLocation)
    #         messagebox.showerror("ERROR",
    #                              "No empty case in: Item code, Description , Quantity, Price, Min.Stock or Location  entries")
    #     else:
    #         # Confirme the change to update
    #         confirmeUpdate = messagebox.askokcancel("Confirmation",
    #                                                 f" {username_in_the_system}: You are Updating Item {itemCode} the :"
    #                                                 f"\n\nDescription: {itemDescription}, \n\n Quantity: {itemQty} \n\n"
    #                                                 f"Price: {itemPrice}\n\n Min. Stock: {itemMinStock} \n\n "
    #                                                 f"Location: {itemLocation}")
    #         if confirmeUpdate:
    #             item_collection.updateItem(itemCode, itemDescription, itemQty, itemPrice, username_in_the_systemID,
    #                                        dateUpdate, itemMinStock, itemLocation)
    #             # data have been updated
    #             messagebox.showinfo('Info', 'Update save ')
    #             # After the data have been updated clear the Entry widgets
    #             self.itemCodeEntry.delete(0, END)
    #             self.itemNameEntry.delete(0, END)
    #             self.itemDescriptionEntry.delete(0, END)
    #             self.itemSupplierIdEntry.delete(0, END)
    #             self.itemQuantityEntry.delete(0, END)
    #             self.itemPriceEntry.delete(0, END)
    #             self.itemMinStockEntry.delete(0, END)
    #             self.itemLocationEntry.delete(0, END)
    #         else:
    #             messagebox.showwarning("Info", f"No change have been made for Item code id: {itemCode}")

    # Funtion to clear the Entry boxes
    def clearBill(self):
        self.BillCodeEntry.delete(0, END)
        self.BillCompanyIdEntry.delete(0, END)
        self.BillItemIdEntry.delete(0, END)
        self.BillItemNameEntry.delete(0, END)
        self.BillQtyEntry.delete(0, END)
        self.BillPriceEntry.delete(0, END)
        self.BillDiscountEntry.delete(0, END)
        self.BillDescriptionEntry.delete('1.0', 'end')

    #######################Listbox ###############################################################################
    """In this area will have 3 function to render at the topFrame a listbox with name and id for: 
        - Items
        - Suppliers
        - Clients
    THis will help the user to find in one placethe necessary item id and the company name (Supplier or Client) to
    used as input in the billing form. """

    """Item"""
    # this function will render in the BillingTopTab item name and id
    def update_itemListabox(self, event):
        if self.itemlistbox.curselection():
            self.selected_item = self.itemlistbox.get(self.itemlistbox.curselection())
            item_id = [item[1] for item in self.items if item[0] == self.selected_item][0]
            self.entry_item_id.delete(0, tkinter.END)
            self.entry_item_id.insert(0, item_id)
        else:
            self.selected_item = None
    """Supplier"""

    # this function will render in the BillingTopTab Supplier name and id
    def update_SupplierListabox(self, event):
        if self.suplistbox.curselection():
            self.selected_sup = self.suplistbox.get(self.suplistbox.curselection())
            sup_id = [item[1] for item in self.sups if item[0] == self.selected_sup][0]
            self.entry_sup_id.delete(0, tkinter.END)
            self.entry_sup_id.insert(0, sup_id)
        else:
            self.selected_sup = None

    """Clients"""

    # this function will render in the BillingTopTab Client name and id
    def update_ClientListabox(self, event):
        if self.clientlistbox.curselection():
            self.selected_client = self.clientlistbox.get(self.clientlistbox.curselection())
            client_id = [item[1] for item in self.clients if item[0] == self.selected_client][0]
            self.entry_client_id.delete(0, tkinter.END)
            self.entry_client_id.insert(0, client_id)
        else:
            self.selected_client = None


    ########################################################################################################

    ##################################$$$$$$$$$$$$  ITEMS  $$$$$$$$$$$$$$$$#######################################
    """ When user click on Show button this will display the whole data from inventory_suppliers TABLE"""

    def showItem(self):
        # 1- first clear the data in treeview (otherwise the data in treeview will be repeated)
        for item in self.item_tree.get_children():
            self.item_tree.delete(item)
        # 2- fetch data from DB
        allitems = item_collection.allItems()

        for row in allitems:
            # 3- INSERTION OF VALUES FROM DB TO TREEVIEEW
            self.item_tree.insert('', 'end', text=row[0], values=row[0:])

    """Insert new Supplier. button INSERT"""

    def insertItem(self):
        # logged user Name
        username_in_the_system = self.user_name
        # logged user ID
        username_in_the_systemID = int(self.user_id)

        # Entries data
        itemCode = self.itemCodeEntry.get()
        itemName = self.itemNameEntry.get()
        itemDescription = self.itemDescriptionEntry.get()
        itemSupId = self.itemSupplierIdEntry.get()
        itemQty = self.itemQuantityEntry.get()
        itemPrice = self.itemPriceEntry.get()
        dateIn = datetime.today().strftime('%m/%d/%Y')
        itemMinStock = self.itemMinStockEntry.get()
        itemLocation = self.itemLocationEntry.get()

        # check if any entry case is empty
        if (itemCode == '' or itemName == '' or itemDescription == '' or itemSupId =='' or itemQty == '' or
                itemPrice == '' or itemMinStock == '' or itemLocation == ""):
            messagebox.showerror("Error", "All the entry case must be filled!")
        # if all the data is correct
        else:
            messagebox.askyesno('Confirm', f"{username_in_the_system} Do you want to add New Item \n\n\n Code: {itemCode}\n\n"
                                           f"Item name: {itemName} \n\n Item Description: {itemDescription} \n\n "
                                           f"Item Supplier ID: {itemSupId} \n\n Quantity: {itemQty} \n\n "
                                           f"Price: {itemPrice} \n\n Item Min.Stock{itemMinStock} \n\n "
                                           f"Item Location: {itemLocation}")
            item_collection.in_newItem(
                itemCode, itemName, itemDescription, itemSupId, int(itemQty), itemPrice,username_in_the_systemID,
                dateIn, int(itemMinStock), itemLocation
            )
            # this can be used to let know the user that the data of this id have been well inserted. With a messagebox
            print(supplier_collection.in_newSupplier)
            if supplier_collection.in_newSupplier:

                self.itemCodeEntry.delete(0, END)
                self.itemNameEntry.delete(0, END)
                self.itemDescriptionEntry.delete(0, END)
                self.itemSupplierIdEntry.delete(0, END)
                self.itemQuantityEntry.delete(0, END)
                self.itemPriceEntry.delete(0, END)
                self.itemMinStockEntry.delete(0, END)
                self.itemLocationEntry.delete(0, END)

    """Update Item description, Qty, price, updateBy, updateDate, minStock or/ and location . button UPDATE"""

    def update_Item(self):
        # logged user Name
        username_in_the_system = self.user_name
        # logged user ID
        username_in_the_systemID = int(self.user_id)

        # Entries data
        itemCode = self.itemCodeEntry.get()
        itemDescription = self.itemDescriptionEntry.get()
        itemQty = self.itemQuantityEntry.get()
        itemPrice = self.itemPriceEntry.get()
        dateUpdate = datetime.today().strftime('%m/%d/%Y')
        itemMinStock = self.itemMinStockEntry.get()
        itemLocation = self.itemLocationEntry.get()
        #  Item code ID is mandatory
        if (
             itemCode == "" or itemDescription == "" or itemQty == "" or itemPrice == "" or
             itemMinStock == "" or itemLocation == ""):
            print( itemCode,itemDescription,itemQty,itemPrice,dateUpdate,itemMinStock,itemLocation)
            messagebox.showerror("ERROR",
                                 "No empty case in: Item code, Description , Quantity, Price, Min.Stock or Location  entries")
        else:
            # Confirme the change to update
            confirmeUpdate = messagebox.askokcancel("Confirmation",
                                                    f" {username_in_the_system}: You are Updating Item {itemCode} the :"
                                                    f"\n\nDescription: {itemDescription}, \n\n Quantity: {itemQty} \n\n"
                                                    f"Price: {itemPrice}\n\n Min. Stock: {itemMinStock} \n\n "
                                                    f"Location: {itemLocation}")
            if confirmeUpdate:
                item_collection.updateItem(itemCode,itemDescription,itemQty,itemPrice,username_in_the_systemID,
                                           dateUpdate,itemMinStock,itemLocation)
                # data have been updated
                messagebox.showinfo('Info', 'Update save ')
                # After the data have been updated clear the Entry widgets
                self.itemCodeEntry.delete(0, END)
                self.itemNameEntry.delete(0, END)
                self.itemDescriptionEntry.delete(0, END)
                self.itemSupplierIdEntry.delete(0, END)
                self.itemQuantityEntry.delete(0, END)
                self.itemPriceEntry.delete(0, END)
                self.itemMinStockEntry.delete(0, END)
                self.itemLocationEntry.delete(0, END)
            else:
                messagebox.showwarning("Info", f"No change have been made for Item code id: {itemCode}")

    # Funtion to clear the Entry boxes
    def clearItem(self):
        self.itemCodeEntry.delete(0, END)
        self.itemNameEntry.delete(0, END)
        self.itemDescriptionEntry.delete(0, END)
        self.itemSupplierIdEntry.delete(0, END)
        self.itemQuantityEntry.delete(0, END)
        self.itemPriceEntry.delete(0, END)
        self.itemMinStockEntry.delete(0, END)
        self.itemLocationEntry.delete(0, END)



    ##################################################################################################################

    ##################################$$$$$$$$$$$$  SUPPLIER  $$$$$$$$$$$$$$$$#######################################
    """ When user click on Show button this will display the whole data from inventory_suppliers TABLE"""
    def showSupplier(self):
        # 1- first clear the data in treeview (otherwise the data in treeview will be repeated)
        for item in self.item_tree.get_children():
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
        BillingTreeview.pack(side=tkinter.LEFT)
        ###### TEST For Labels at the top of the treevieww to render information#########
        """TopFrame to search id and name of: Item, Supplier/Client to make use in the billing form"""
        """Item id and name"""
        # self.items = []
        # for row in item_collection.Item_Name_Id():
        #     self.items.append((row[1], row[0]))
        #
        # self.itemlistbox = tkinter.Listbox(BillingTopTab, width=20, height = 1)
        # for item in self.items:
        #     self.itemlistbox.insert(tkinter.END, item[0])
        #
        # lb_itemName = ttk.Label(BillingTopTab, text='Item name').pack()
        #
        # self.itemlistbox.pack(anchor='w')
        # self.itemlistbox.bind("<<ListboxSelect>>", self.update_itemListabox)
        # lb_itemID = ttk.Label(BillingTopTab, text='Item Id').pack()
        # self.entry_item_id = ttk.Entry(BillingTopTab, width=10)
        # # self.entry_item_id.pack()#side=tkinter.LEFT
        # self.entry_item_id.grid(row=2, column=0, sticky='sw')
        # """Supplier id and name"""
        # self.sups = []
        # for row in supplier_collection.Supplier_Name_Id():
        #     self.sups.append((row[1], row[0]))
        #
        # self.suplistbox = tkinter.Listbox(BillingTopTab, width=20, height=1)
        # for item in self.sups:
        #     self.suplistbox.insert(tkinter.END, item[0])
        #
        # lb_supName = ttk.Label(BillingTopTab, text='Supplier name').pack()
        #
        # self.suplistbox.pack(side=tkinter.RIGHT)
        # self.suplistbox.bind("<<ListboxSelect>>", self.update_SupplierListabox)
        # lb_itemID = ttk.Label(BillingTopTab, text='Supplier Id').pack()
        # self.entry_sup_id = ttk.Entry(BillingTopTab, width=10)
        # self.entry_sup_id.pack(side=tkinter.RIGHT)  # side=tkinter.LEFT
        self.items = []
        for row in item_collection.Item_Name_Id():
            self.items.append((row[1], row[0]))

        self.itemlistbox = tkinter.Listbox(BillingTopTab, width=20, height=1)
        for item in self.items:
            self.itemlistbox.insert(tkinter.END, item[0])
        self.itemlistbox.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

        lb_itemName = ttk.Label(BillingTopTab, text='Item name')
        lb_itemName.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

        # to render the id in the self.entry_item_id
        self.itemlistbox.bind("<<ListboxSelect>>", self.update_itemListabox)

        lb_itemID = ttk.Label(BillingTopTab, text='Item Id')
        lb_itemID.grid(column=0, row=1, sticky=tkinter.W)

        self.entry_item_id = ttk.Entry(BillingTopTab, width=10)
        self.entry_item_id.grid(column=1, row=1, sticky=tkinter.E)

        """Supplier id and name"""
        self.sups = []
        for row in supplier_collection.Supplier_Name_Id():
            self.sups.append((row[1], row[0]))

        self.suplistbox = tkinter.Listbox(BillingTopTab, width=20, height=1)
        for item in self.sups:
            self.suplistbox.insert(tkinter.END, item[0])
        self.suplistbox.grid(column=4, row=0, sticky=tkinter.W, padx=5, pady=5)

        lb_supName = ttk.Label(BillingTopTab, text='Supplier name')
        lb_supName.grid(column=3, row=0, sticky=tkinter.W, padx=5, pady=5)

        # to render the id in the  self.entry_sup_id
        self.suplistbox.bind("<<ListboxSelect>>", self.update_SupplierListabox)

        lb_supID = ttk.Label(BillingTopTab, text='Supplier Id')
        lb_supID.grid(column=3, row=1, sticky=tkinter.W, padx=5, pady=5)

        self.entry_sup_id = ttk.Entry(BillingTopTab, width=10)
        self.entry_sup_id.grid(column=4, row=1, sticky=tkinter.E, padx=5, pady=5)

        """Client id and name"""
        self.clients= []
        for row in client_collection.Client_Name_Id():
            self.clients.append((row[1], row[0]))

        self.clientlistbox = tkinter.Listbox(BillingTopTab, width=20, height=1)
        for item in self.clients:
            self.clientlistbox.insert(tkinter.END, item[0])
        self.clientlistbox.grid(column=6, row=0, sticky=tkinter.W, padx=5, pady=5)

        lb_clientName = ttk.Label(BillingTopTab, text='Client name')
        lb_clientName.grid(column=5, row=0, sticky=tkinter.W, padx=5, pady=5)

        # to render the id in the  self.entry_client_id
        self.clientlistbox.bind("<<ListboxSelect>>", self.update_ClientListabox)

        lb_clientID = ttk.Label(BillingTopTab, text='Client Id')
        lb_clientID.grid(column=5, row=1, sticky=tkinter.W, padx=5, pady=5)

        self.entry_client_id = ttk.Entry(BillingTopTab, width=10)
        self.entry_client_id.grid(column=6, row=1, sticky=tkinter.E, padx=5, pady=5)

        #####################################################

        ######################## Billing TREEVIEW

        self.billing_tree = ttk.Treeview(BillingTreeview, height=18, columns=(
            "Reference ID", "Entrance/Exit", "Company ID", "Item ID", "Item Name", "Quantity", "Price",
            "Discount","Date","Created Date", "Description", "UserID"), show="headings")
        self.billing_tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        # fetch data from DB
        allbills = billing_collection.allBill()

        for row in allbills:
            # INSERTION OF VALUES FROM DB TO TREEVIEEW
            """To change the bg on the treeview"""
            # self.billing_tree.tag_configure('oddrow', background='gray')
            self.billing_tree.insert('', 'end', text=row[0], values=row[0:] , tags = ('oddrow',))
            # self.billing_tree.tag_configure('oddrow', background='gray')
        # Scrollbar for the treeview
        billing_tree_scroll = ttk.Scrollbar(BillingTreeview, orient="vertical", command=self.billing_tree.yview)
        billing_tree_scroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.billing_tree.configure(yscrollcommand=billing_tree_scroll.set)
        ##### Heading of the treeview
        self.billing_tree.heading(0, text="Reference ID", anchor='center')
        self.billing_tree.heading(1, text="Entrance/Exit", anchor='center')
        self.billing_tree.heading(2, text="Company ID", anchor='center')
        self.billing_tree.heading(3, text="Item ID", anchor='center')
        self.billing_tree.heading(4, text="Item Name", anchor='center')
        self.billing_tree.heading(5, text="Quantity", anchor='center')
        self.billing_tree.heading(6, text="Price", anchor='center')
        self.billing_tree.heading(7, text="Discount", anchor='center')
        self.billing_tree.heading(8, text="Date", anchor='center')
        self.billing_tree.heading(9, text="Created Date", anchor='center')
        self.billing_tree.heading(10, text="Description", anchor='center')
        self.billing_tree.heading(11, text="User ID", anchor='center')
        ##### Columns of the treeview
        self.billing_tree.column(0, width=80, anchor='center')
        self.billing_tree.column(1, width=80, anchor='center')
        self.billing_tree.column(2, width=80, anchor='center')
        self.billing_tree.column(3, width=80, anchor='center')
        self.billing_tree.column(4, width=80, anchor='center')
        self.billing_tree.column(5, width=80, anchor='center')
        self.billing_tree.column(6, width=60, anchor='center')
        self.billing_tree.column(7, width=60, anchor='center')
        self.billing_tree.column(8, width=70, anchor='center')
        self.billing_tree.column(9, width=80, anchor='center')
        self.billing_tree.column(10, width=250, anchor='center')
        self.billing_tree.column(11, width=50, anchor='center')

        ###############################################################
        ####Select items from the treeview###
        ###############################################################
        """this methods is to select,fetch and return data from the clicked row in the treeview """

        def treeview_select(event):
            # FETCH SELECTED ROW
            select_BillId = event.widget.selection()[0]  # FETCH ALL VALUES OF THE ROW
            print(select_BillId)
            select_BillIdValue = event.widget.item(select_BillId)['values']
            print(select_BillIdValue)
            """Configuration of the labes at the topframe. When the user clicks one of the row in the treeview the data 
            from the clicked row will be display at the top. thE VALUE ARE INDEXED"""

            """Rendering the selected row in the treeview into the Entry widgets"""
            # Bill CODE
            self.BillCodeEntry.delete(0, END)
            self.BillCodeEntry.insert(0, select_BillIdValue[0])
            # Bill company id
            self.BillCompanyIdEntry.delete(0, END)
            self.BillCompanyIdEntry.insert(0, select_BillIdValue[2])
            # Bill item id
            self.BillItemIdEntry.delete(0, END)
            self.BillItemIdEntry.insert(0, select_BillIdValue[3])
            # Bill item name
            self.BillItemNameEntry.delete(0, END)
            self.BillItemNameEntry.insert(0, select_BillIdValue[4])
            # Bill QUANTITY
            self.BillQtyEntry.delete(0, END)
            self.BillQtyEntry.insert(0, select_BillIdValue[5])
            # Bill PRICE
            self.BillPriceEntry.delete(0, END)
            self.BillPriceEntry.insert(0, select_BillIdValue[6])
            # Bill Discount
            self.BillDiscountEntry.delete(0, END)
            self.BillDiscountEntry.insert(0, select_BillIdValue[7])
            # ITEM LOCATION
            self.BillDescriptionEntry.delete('1.0', 'end')
            self.BillDescriptionEntry.insert('1.0', select_BillIdValue[9])
        self.billing_tree.bind('<<TreeviewSelect>>', treeview_select)
            ############################################

        ################################# BILLING TAB, RADIOBUTTON, LABELS AND ENTRIES
        ###############RADIOBUTTON#################################################
        self.BILLING = tkinter.StringVar() #RADIOBUTTON VARIABLE
        self.BILLING.set('Entrance') #THE DEFAULT

        self.inStock = tkinter.Radiobutton(BillingTab, text="Entrance", variable=self.BILLING, value = 'Entrance', command=lambda : self.insertBill())
        self.inStock.pack( anchor='w', padx=15)#anchor='w'
        self.outStock = tkinter.Radiobutton(BillingTab, text="Exit", variable=self.BILLING,value = 'Exit', command=lambda : self.insertBill())
        self.outStock.pack(anchor='w', padx=15)#side=tkinter.TOP,
        self.selected_value = None

        ##############################################################################
        ################LABELS & ENTRIES############################################
        self.date = tkcalendar.DateEntry(BillingTab, width=10)
        self.date.pack()
        lb_BillCode = ttk.Label(BillingTab, text="Reference Number:")
        lb_BillCode.pack()
        self.BillCodeEntry = ttk.Entry(BillingTab)
        self.BillCodeEntry.pack()
        lb_CompanyId = ttk.Label(BillingTab, text="Company ID:")
        lb_CompanyId.pack()
        self.BillCompanyIdEntry = ttk.Entry(BillingTab)
        self.BillCompanyIdEntry.pack()
        lb_BillItemId = ttk.Label(BillingTab, text="Item ID:")
        lb_BillItemId.pack()
        self.BillItemIdEntry = ttk.Entry(BillingTab)
        self.BillItemIdEntry.pack()
        lb_BillItemName = ttk.Label(BillingTab, text="Item Name:")
        lb_BillItemName.pack()
        self.BillItemNameEntry = ttk.Entry(BillingTab)
        self.BillItemNameEntry.pack()
        lb_BillQty = ttk.Label(BillingTab, text="Quantity:")
        lb_BillQty.pack()
        self.BillQtyEntry = ttk.Entry(BillingTab)
        self.BillQtyEntry.pack()
        lb_BillPrice = ttk.Label(BillingTab, text="Price:")
        lb_BillPrice.pack()
        self.BillPriceEntry = ttk.Entry(BillingTab)
        self.BillPriceEntry.pack()
        lb_BillDiscount = ttk.Label(BillingTab, text="Discount:")
        lb_BillDiscount.pack()
        self.BillDiscountEntry = ttk.Entry(BillingTab)
        self.BillDiscountEntry.pack()
        lb_BillDescription = ttk.Label(BillingTab, text="Description:")
        lb_BillDescription.pack()
        self.BillDescriptionEntry = tkinter.Text(BillingTab, width = 18, height = 1)
        self.BillDescriptionEntry.pack()
    #######################################################################


        ###BUTTONS
        #INSERT BUTTON
        btn_InsertBill = ttk.Button(BillingTab, text="Insert", command = lambda : self.insertBill())
        btn_InsertBill.pack(side=tkinter.TOP)
        btn_InsertBill.bind("<Return>", lambda event: self.insertBill()(btn_InsertBill["Insert"]))
        #UPDATE BUTTON
        btn_UpdateBill = ttk.Button(BillingTab, text="Update", command = lambda : "")
        btn_UpdateBill.pack(side=tkinter.TOP)
        btn_UpdateBill.bind("<Return>", lambda event: self.updateBill()(btn_InsertBill["Update"]))
        # SHOW BUTTON
        btn_BillShow = ttk.Button(BillingTab, text="Show",command = lambda : self.showBill())
        btn_BillShow.pack(side=tkinter.LEFT)
        btn_BillShow.bind("<Return>", lambda event: self.showBill()(btn_BillShow["Show"]))
        # Clear button
        btn_BillClear = ttk.Button(BillingTab, text="Clear", command=lambda: self.clearBill())
        btn_BillClear.pack(side=tkinter.BOTTOM)
        btn_BillClear.bind("<Return>", lambda event: self.clearBill()(btn_BillClear["Clear"]))
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


        lb_title = ttk.Label(itemTopTab, text='Selection:', font=('',16,'bold'))
        lb_title.pack()
        lb_1Title = ttk.Label(itemTopTab, text='Code Id: ', font=('',12,'bold'))
        self.spinbox_id = tkinter.IntVar()
        entry = ttk.Entry(itemTopTab, textvariable=self.spinbox_id)
        entry.pack()

        # lb_1Title.pack(side=tkinter.LEFT )
        # lb_titleItemId = ttk.Label(itemTopTab, text='', background='white', font=('',14,'bold'))
        # lb_titleItemId.pack(side=tkinter.LEFT )

        # """Items Spinbox"""
        # self.items = []
        # # c.execute("SELECT code_id, item_name FROM inventory_items")
        # for row in item_collection.Item_Name_Id():
        #     self.items.append((row[1], row[0]))
        #
        # self.spinbox_ItemName = tkinter.StringVar()
        # self.spinbox = ttk.Spinbox(itemTopTab, textvariable=self.spinbox_ItemName, values=[item[0] for item in self.items],
        #                            command=self.update_spinbox)
        # self.spinbox.pack()


        # lb_2Title = ttk.Label(itemTopTab, text='     Name:', font=('',12,'bold'))
        # lb_2Title.pack(side=tkinter.LEFT)
        # lb_titleItemName = ttk.Label(itemTopTab, text='',background='white')
        # lb_titleItemName.pack(side=tkinter.LEFT)
        lb_3Title = ttk.Label(itemTopTab, text='     Description:', font=('',12,'bold'))
        lb_3Title.pack(side=tkinter.LEFT)
        lb_titleItemDescription = ttk.Label(itemTopTab, text='',background='white')
        lb_titleItemDescription.pack(side=tkinter.LEFT)
        lb_4Title = ttk.Label(itemTopTab, text='     Supplier ID:', font=('',12,'bold'))
        lb_4Title.pack(side=tkinter.LEFT)
        lb_titleItemSupId = ttk.Label(itemTopTab, text='',background='white')
        lb_titleItemSupId.pack(side=tkinter.LEFT)
        lb_4Title = ttk.Label(itemTopTab, text='     Quantity:', font=('', 12, 'bold'))
        lb_4Title.pack(side=tkinter.LEFT)
        lb_titleQty = ttk.Label(itemTopTab, text='', background='white')
        lb_titleQty.pack(side=tkinter.LEFT)
        lb_4Title = ttk.Label(itemTopTab, text='     Price:', font=('', 12, 'bold'))
        lb_4Title.pack(side=tkinter.LEFT)
        lb_titlePrice = ttk.Label(itemTopTab, text='', background='white')
        lb_titlePrice.pack(side=tkinter.LEFT)
        lb_4Title = ttk.Label(itemTopTab, text='     Created by:', font=('', 12, 'bold'))
        lb_4Title.pack(side=tkinter.LEFT)
        lb_titleCreateBy = ttk.Label(itemTopTab, text='', background='white')
        lb_titleCreateBy.pack(side=tkinter.LEFT)
        lb_4Title = ttk.Label(itemTopTab, text='     Created date:', font=('', 12, 'bold'))
        lb_4Title.pack(side=tkinter.LEFT)
        lb_titleCreateDate = ttk.Label(itemTopTab, text='', background='white')
        lb_titleCreateDate.pack(side=tkinter.LEFT)
        lb_4Title = ttk.Label(itemTopTab, text='     Update by:', font=('', 12, 'bold'))
        lb_4Title.pack(side=tkinter.LEFT)
        lb_titleUpdateBy = ttk.Label(itemTopTab, text='', background='white')
        lb_titleUpdateBy.pack(side=tkinter.LEFT)
        lb_4Title = ttk.Label(itemTopTab, text='     Update date:', font=('', 12, 'bold'))
        lb_4Title.pack(side=tkinter.LEFT)
        lb_titleUpdateDate = ttk.Label(itemTopTab, text='', background='white')
        lb_titleUpdateDate.pack(side=tkinter.LEFT)
        lb_4Title = ttk.Label(itemTopTab, text='     Min. Stock:', font=('', 12, 'bold'))
        lb_4Title.pack(side=tkinter.LEFT)
        lb_titleMinStock = ttk.Label(itemTopTab, text='', background='white')
        lb_titleMinStock.pack(side=tkinter.LEFT)
        lb_4Title = ttk.Label(itemTopTab, text='     Location:', font=('', 12, 'bold'))
        lb_4Title.pack(side=tkinter.LEFT)
        lb_titleLocation = ttk.Label(itemTopTab, text='', background='white')
        lb_titleLocation.pack(side=tkinter.LEFT)
        #####################################################

        #####################################################
        ############### insert in treeview
        self.item_tree = ttk.Treeview(itemTreeview, height=18, columns=("Item Code","Name", "Description","Supplier ID",
                                                                   "Quantity","Price","Created by", "Created Date",
                                                                   "Update by", "Update date","Min. Stock", "Location"
                                                                   ), show="headings")
        self.item_tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        # fetch data from DB
        allitems = item_collection.allItems()

        for row in allitems:
            # INSERTION OF VALUES FROM DB TO TREEVIEEW
            self.item_tree.insert('', 'end', text=row[0], values=row[0:])
        #Scrollbar for the treeview
        item_tree_scroll = ttk.Scrollbar(itemTreeview, orient="vertical", command=self.item_tree.yview)
        item_tree_scroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.item_tree.configure(yscrollcommand=item_tree_scroll.set)
        ##### Heading of the treeview
        self.item_tree.heading(0, text="Item Code", anchor='center')
        self.item_tree.heading(1, text="Name", anchor='center')
        self.item_tree.heading(2, text="Description", anchor='center')
        self.item_tree.heading(3, text="Supplier ID", anchor='center')
        self.item_tree.heading(4, text="Quantity", anchor='center')
        self.item_tree.heading(5, text="Price", anchor='center')
        self.item_tree.heading(6, text="Created by", anchor='center')
        self.item_tree.heading(7, text="Created date", anchor='center')
        self.item_tree.heading(8, text="Update by", anchor='center')
        self.item_tree.heading(9, text="Update date", anchor='center')
        self.item_tree.heading(10, text="Min. Stock", anchor='center')
        self.item_tree.heading(11, text="Location", anchor='center')
        ##### Columns of the treeview
        self.item_tree.column(0, width=80, anchor='center')
        self.item_tree.column(1, width=100, anchor='nw')
        self.item_tree.column(2, width=200, anchor='nw')
        self.item_tree.column(3, width=80, anchor='center')
        self.item_tree.column(4, width=80, anchor='center')
        self.item_tree.column(5, width=50, anchor='center')
        self.item_tree.column(6, width=80, anchor='center')
        self.item_tree.column(7, width=80, anchor='center')
        self.item_tree.column(8, width=80, anchor='center')
        self.item_tree.column(9, width=80, anchor='center')
        self.item_tree.column(10, width=80, anchor='center')
        self.item_tree.column(11, width=100, anchor='nw')

        ####Select items from the treeview###
        ######################################
        """this methods is to select,fetch and return data from the clicked row in the treeview """

        def treeview_select(event):
            # FETCH SELECTED ROW
            select_ItemId = event.widget.selection()[0]       # FETCH ALL VALUES OF THE ROW
            print(select_ItemId)
            select_ItemIdValue = event.widget.item(select_ItemId)['values']
            print(select_ItemIdValue)
            """Configuration of the labes at the topframe. When the user clicks one of the row in the treeview the data 
            from the clicked row will be display at the top. thE VALUE ARE INDEXED"""

            """Rendering the selected row in the treeview into the Entry widgets"""
            # ITEM CODE
            self.itemCodeEntry.delete(0, END)
            self.itemCodeEntry.insert(0, select_ItemIdValue[0])
            # ITEM NAME
            self.itemNameEntry.delete(0, END)
            self.itemNameEntry.insert(0, select_ItemIdValue[1])
            # ITEM DESCRIPTION
            self.itemDescriptionEntry.delete(0, END)
            self.itemDescriptionEntry.insert(0, select_ItemIdValue[2])
            # ITEM SUPPLIER ID
            self.itemSupplierIdEntry.delete(0, END)
            self.itemSupplierIdEntry.insert(0, select_ItemIdValue[3])
            # ITEM QUANTITY
            self.itemQuantityEntry.delete(0, END)
            self.itemQuantityEntry.insert(0, select_ItemIdValue[4])
            # ITEM PRICE
            self.itemPriceEntry.delete(0, END)
            self.itemPriceEntry.insert(0, select_ItemIdValue[5])
            # ITEM MIN. STOCK
            self.itemMinStockEntry.delete(0, END)
            self.itemMinStockEntry.insert(0, select_ItemIdValue[10])
            # ITEM LOCATION
            self.itemLocationEntry.delete(0, END)
            self.itemLocationEntry.insert(0, select_ItemIdValue[11])
            ############################################
            """Render selected row in the treeviw at the TopFrame"""
            ############################################
            # Code ID
            # entry.config(text=select_ItemIdValue[0])
            # Item Name
            # lb_titleItemName.config(text=select_ItemIdValue[1])
            # Item Description
            lb_titleItemDescription.config(text=select_ItemIdValue[2])
            # Supplier ID
            lb_titleItemSupId.config(text=select_ItemIdValue[3])
            # Quantity
            lb_titleQty.config(text=select_ItemIdValue[4])
            # Price
            lb_titlePrice.config(text=select_ItemIdValue[5])
            # Created by
            lb_titleCreateBy.config(text=select_ItemIdValue[6])
            # Created date
            lb_titleCreateDate.config(text=select_ItemIdValue[7])
            # Updated by
            lb_titleUpdateBy.config(text=select_ItemIdValue[8])
            # Updated date
            lb_titleUpdateDate.config(text=select_ItemIdValue[9])
            #Min.Stock
            lb_titleMinStock.config(text=select_ItemIdValue[10])
            # Location
            lb_titleLocation.config(text=select_ItemIdValue[11])
            return select_ItemIdValue

        self.item_tree.bind('<<TreeviewSelect>>', treeview_select)
        #######################################################
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
        # lb_ItemDescription = ttk.Label(itemTab, text="Description")
        # lb_ItemDescription.pack()
        # self.itemDescriptionEntry = ttk.Entry(itemTab)
        # self.itemDescriptionEntry.pack()
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
        btn_ItemShow.bind("<Return>", lambda event: self.showItem()(btn_InsertItem["Show"]))
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
        lb_Supplier_Details = ttk.Label(supplierTab, text='Contact Details').pack(anchor='w', pady=10, padx=5)
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
        lb_Client_Details = ttk.Label(clientTab, text= 'Contact Details').pack(anchor='w',pady=10, padx=5)

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

