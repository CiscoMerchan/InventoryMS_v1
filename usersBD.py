import psycopg2
# data = input("data: ")
# connection establishment
conn = psycopg2.connect(
    database="vitralum",
    user='postgres',
    password='Albita110621',
    host='localhost',
    port='5432'
)

class UserDb:
    conn.autocommit = True
    # Creating a cursor object
    cursor = conn.cursor()

    ############All the data from the table to render in the treeviw####

    def userAll(self):
        conn.autocommit = True
        # Creating a cursor object
        cursor = conn.cursor()
        # INSERT
        cursor.execute("SELECT * FROM _users ORDER BY user_id ASC; ")

        # Get the last inserted id
        """This return all the data in _users TABLE """
        dataUsers = cursor.fetchall()

        # Commit the changes to the database
        conn.commit()
        return dataUsers
    ########################################## INSERT AND VERIFICATION #####################################
    " This function is to INSERT Users values INTO _users TABLES   "
    def user_data_collection(self, firstname, lastname, email):
        conn.autocommit = True
        # Creating a cursor object
        cursor = conn.cursor()
        # INSERT
        cursor.execute(
            f"INSERT INTO  _users (user_first_name, user_lastname, user_email) VALUES('{firstname}', '{lastname}', '{email}') RETURNING user_id ")

        # Get the last inserted id
        """This return in user_window.py where the messagebox to let know to the user their user ID number alocated by the DB """
        self.last_insert_id = cursor.fetchone()[0]

        # Commit the changes to the database
        conn.commit()
        # Close the cursor and connection
        # cursor.close()
        # conn.close()
        print("User data been created successfully in _users TABLE  ")


    """RETURN OF THE USER ID FROM THE NAME AND LASTNAME ENTERED _users TABLES   """
    # The porpuse of this funtion is that after the data is Inserted back to fetch the entered data and returned
    # to the GUI but this time from the DB and not from the entered data directly entered ba the User
    def users_return(self):
            conn.autocommit = True
            # Creating a cursor object
            cursor = conn.cursor()
            # INSERT
            sql = (f"SELECT user_id, user_first_name, user_lastname, user_email FROM _users ")
            # executing above query
            cursor.execute(sql)
            try:
                result = cursor.fetchall()
                return result
                print(result)
            # print("User data been created successfully !!");
            except:
                print(f"User ID successfully in _users TABLE")
            # Commit the changes to the database
            conn.commit()
            # Close the cursor and connection
            cursor.close()
            # conn.close()
    """Callback function that take User ID and Name, verify is the data is in the DB and will return as callback
    True or False"""
    def user_check(self,_user_name, _user_id, callback):
        # try:
            conn.autocommit = True
            # Creating a cursor object
            cursor = conn.cursor()
            # SELECT QUERY
            sql = (f"SELECT * FROM _users WHERE user_id = '{_user_id}' AND user_first_name ='{_user_name}' ")
            # executing above query
            cursor.execute(sql)
            self.result = cursor.fetchone()
            # If a result is returned, return True
            # if result[0] == int(_user_id) and result[1] == _user_name:
            print("BD.OK")
            if self.result:
             callback(True)
             return self.result
             print(str(result)+'dbOK')
            # If no result is returned, return False
            # else:
            #     callback(False)
                # print(str(result) + 'dbNO')
            # Catch and print any errors that occur while connecting to the database
            """$$ Once the except is active it take over the TRY: *** To check """
        # except (Exception, psycopg2.Error) as error:
        #     # callback(False)
        #     print("Error while connecting to PostgreSQL", error)
    # Close the cursor and connection even if an error occurs
    #     finally:
    #         # Close the cursor and connection
    #     cursor.close()
    #     conn.close()
#         print("db close")
#############################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$###############################

###########################################  UPDATE ###################################################

    def updateUser(self, id , email):
        # try:
        conn.autocommit = True
        # Creating a cursor object
        cursor = conn.cursor()
        # SELECT QUERY
        print(f"before sql {id}  {email}")
        sql = (f"UPDATE _users SET user_email = '{email}' WHERE user_id = {int(id)}")
        print(f"after sql {id}  {email}")
        # executing above query
        cursor.execute(sql)
        print(f"after execution sql sql {id}  {email}")
        cursor.fetchone()

        # If a result is returned, return True
        # if result[0] == int(_user_id) and result[1] == _user_name:
        print("BD.OK")
        # if self.result:
        #     callback(True)
        #     return self.result
        #     print(str(result) + 'dbOK')
        # If no result is returned, return False
        # else:
        #     callback(False)
        # print(str(result) + 'dbNO')
        # Catch and print any errors that occur while connecting to the database
        """$$ Once the except is active it take over the TRY: *** To check """
    # except (Exception, psycopg2.Error) as error:
    #     # callback(False)
    #

class SupplierDB:
    """Insert new supplier in inventory_suppliers TABLE """
    def in_newSupplier(self, id,companyName,companyAgent,agentPhone,agentEmail):
        conn.autocommit = True
        # Creating a cursor object
        cursor = conn.cursor()
        # INSERT
        cursor.execute(
            f"INSERT INTO  inventory_suppliers (id, supplier_company_name, supplier_company_agent, supplier_agent_phone, supplier_agent_email) VALUES('{id}', '{companyName}', '{companyAgent}', '{agentPhone}', '{agentEmail}') RETURNING id ")

        # Get the last inserted id
        """This return in user_window.py where the messagebox to let know to the user their user ID number alocated by the DB """
        insertedSupplier_id = cursor.fetchone()[0]

        # Commit the changes to the database
        conn.commit()
        #possibilite to have the ID of the last inserted Supplier
        return insertedSupplier_id
              # Close the cursor and connection
        # cursor.close()
        # conn.close()
        print("Supplier data been created successfully in inventory_suppliers TABLE  ")



    # The porpuse of this funtion is that after the data is Inserted back to fetch the entered data and returned
    # to the GUI but this time from the DB and not from the entered data directly entered ba the User

    def checkSupplier(self):
        pass

    def allSuppliers(self):
        conn.autocommit = True
        # Creating a cursor object
        cursor = conn.cursor()
        # INSERT
        cursor.execute("SELECT * FROM inventory_suppliers ORDER BY id ASC; ")

        # Get the last inserted id
        """This return all the data in _users TABLE """
        dataSuppliers = cursor.fetchall()

        # Commit the changes to the database
        conn.commit()
        return dataSuppliers

    def a_Supplier(self):
        pass

    def updateSupplier(self):
        pass

class ClientDB:
    def in_newClient(self):
        pass

    def checkClient(self):
        pass

    def allClients(self):
        pass

    def a_Client(self):
        pass

    def updateClient(self):
        pass

class ItemDB:
    def in_newItem(self):
        pass

    def checkItem(self):
        pass

    def allItems(self):
        pass

    def a_item(self):
        pass

    def updateItem(self):
        pass

class BillingDB:
    ######### IN = Ingress in inventory#############
    def IN_in_newBill(self):
        pass

    def INcheckBill(self):
        pass

    def INallBill(self):
        pass

    def IN_a_Bill(self):
        pass

    def INupdateBill(self):
        pass
############## OUT = Discharge from inventory #########
    def OUT_in_newBill(self):
        pass

    def OUTcheckBill(self):
        pass

    def OUTallBill(self):
        pass

    def OUT_a_Bill(self):
        pass

    def OUTupdateBill(self):
        pass


class SearchDB:
    pass