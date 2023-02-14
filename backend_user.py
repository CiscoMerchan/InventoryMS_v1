"""Backend_user Module. this module comunicate between the GUI and the DB"""
# from sys import path
# path.append['InventoryMS_v1/inventoryGUI_2.py']
from usersBD import UserDb
# from inventoryGUI_2 import SecondWindow
# object from inventoryGUI_2 module
# user_data = SecondWindow.get_user_data()
userdb = UserDb()
class User:
    def __init__(self, *args):
        self.name = user_data[0]
        self.lastname = user_data[1]
        self.email = user_data[2]
        self.admin = user_data[3]
    def insert(self):
        userdb.user_data_collection(self.name,self.lastname,self.email)
        print('send to db')