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
############################################################################################

##############################################################################################
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
        """This return in where the messagebox to let know to the user their user ID number alocated by the DB """
        insertedSupplier_id = cursor.fetchone()[0]

        # Commit the changes to the database
        conn.commit()
        #possibilite to have the ID of the last inserted Supplier
        return insertedSupplier_id
              # Close the cursor and connection
        # cursor.close()
        # conn.close()
        print("Supplier data been created successfully in inventory_suppliers TABLE  ")

    def checkSupplier(self):
        pass

    def allSuppliers(self):
        conn.autocommit = True
        # Creating a cursor object
        cursor = conn.cursor()
        # INSERT
        cursor.execute("SELECT * FROM inventory_suppliers ORDER BY id ASC; ")

        # Get the last inserted id
        """This return all the data from inventory_suppliers TABLE """
        dataSuppliers = cursor.fetchall()

        # Commit the changes to the database
        conn.commit()
        return dataSuppliers

    def a_Supplier(self):
        pass

    # A function to update only the last 3 columns of a row
    def updateSupplier(self, id, Agent=None, Phone=None, Email=None):
        # SQL query with placeholders for the columns to update
        query = "UPDATE inventory_suppliers SET supplier_company_agent = %s, supplier_agent_phone = %s, supplier_agent_email = %s WHERE id = %s;"

        # Select the current values for the other columns
        select_query = "SELECT supplier_company_agent, supplier_agent_phone, supplier_agent_email FROM inventory_suppliers WHERE id = %s;"

        # Collect the values for the SQL queries
        update_values = []
        if Agent is not None:
            update_values.append(Agent)
        else:
            update_values.append(None)
        if Phone is not None:
            update_values.append(Phone)
        else:
            update_values.append(None)
        if Email is not None:
            update_values.append(Email)
        else:
            update_values.append(None)
        update_values.append(id)

        # Execute the SQL queries
        cursor = conn.cursor()
        cursor.execute(select_query, (id,))
        existing_values = cursor.fetchone()
        query_values = tuple(update_values)
        if None in query_values:
            query_values = tuple(v if v is not None else existing_values[i] for i, v in enumerate(query_values))
        cursor.execute(query, query_values)
        conn.commit()
        cursor.close()
############################################################################################

##############################################################################################
class ClientDB:
    def in_newClient(self, id, companyName, companyAgent, agentPhone, agentEmail):
        conn.autocommit = True
        # Creating a cursor object
        cursor = conn.cursor()
        # INSERT
        cursor.execute(
        f"INSERT INTO  inventory_clients (id, client_company_name, client_company_agent, client_agent_phone, client_agent_email) VALUES('{id}', '{companyName}', '{companyAgent}', '{agentPhone}', '{agentEmail}') RETURNING id ")

        # Get the last inserted id
        """This return in  where the messagebox to let know to the user their user ID number alocated by the DB """
        insertedClient_id = cursor.fetchone()[0]

        # Commit the changes to the database
        conn.commit()
        # possibilite to have the ID of the last inserted Supplier

        return insertedClient_id
        # Close the cursor and connection
        # cursor.close()
        # conn.close()
        print("Client data been created successfully in inventory_clients TABLE  ")


    def checkClient(self):
        pass

    def allClients(self):
        conn.autocommit = True
        # Creating a cursor object
        cursor = conn.cursor()
        # INSERT
        cursor.execute("SELECT * FROM inventory_clients ORDER BY id ASC; ")

        # Get the last inserted id
        """This return all the data from inventory_clients TABLE """
        dataClients = cursor.fetchall()

        # Commit the changes to the database
        conn.commit()
        return dataClients

    def a_Client(self):
        pass

    def updateClient(self, id, Agent = None, Phone = None, Email = None):
        # SQL query with placeholders for the columns to update
        query = "UPDATE inventory_clients SET client_company_agent = %s, client_agent_phone = %s, client_agent_email = %s WHERE id = %s;"

        # Select the current values for the other columns
        select_query = "SELECT supplier_company_agent, supplier_agent_phone, supplier_agent_email FROM inventory_suppliers WHERE id = %s;"

        # Collect the values for the SQL queries
        update_values = []
        if Agent is not None:
            update_values.append(Agent)
        else:
            update_values.append(None)
        if Phone is not None:
            update_values.append(Phone)
        else:
            update_values.append(None)
        if Email is not None:
            update_values.append(Email)
        else:
            update_values.append(None)
        update_values.append(id)

        # Execute the SQL queries
        cursor = conn.cursor()
        cursor.execute(select_query, (id,))
        existing_values = cursor.fetchone()
        query_values = tuple(update_values)
        if None in query_values:
            query_values = tuple(v if v is not None else existing_values[i] for i, v in enumerate(query_values))
        cursor.execute(query, query_values)
        conn.commit()
        cursor.close()
############################################################################################

##############################################################################################
class ItemDB:
    def in_newItem(self, ItemCode, ItemName, ItemDescription, ItemSupplierId,
                   ItemQuantity, ItemPrice, User, Date, ItemMinStock, ItemLocation):

        conn.autocommit = True
        # Creating a cursor object
        cursor = conn.cursor()
        # INSERT
        cursor.execute(
        f"INSERT INTO  inventory_items ( code_id, item_name, item_description, supplier_id, item_available, item_price,"
        f"created_user_id, item_created_date, item_min_stock, item_location) "
        f"VALUES('{ItemCode}', '{ItemName}', '{ItemDescription}', '{ItemSupplierId}', '{ItemQuantity}', '{ItemPrice}',"
        f" {User},'{Date}','{ItemMinStock}', '{ItemLocation}') RETURNING code_id ")

        # Get the last inserted id
        """This return where the messagebox to let know to the user their  ID number alocated by the DB """
        insertedItem_Code = cursor.fetchone()[0]

        # Commit the changes to the database
        conn.commit()
        # possibilite to have the ID of the last inserted Supplier

        return insertedItem_Code
    # Close the cursor and connection
    # cursor.close()
    # conn.close()
    print("Supplier data been created successfully in inventory_items TABLE  ")

    def checkItem(self):
        pass

    def allItems(self):
        conn.autocommit = True
        # Creating a cursor object
        cursor = conn.cursor()
        # INSERT
        cursor.execute("SELECT * FROM inventory_items ORDER BY code_id ASC; ")

        # Get the last inserted id
        """This return all the data from inventory_items TABLE """
        dataItems = cursor.fetchall()

        # Commit the changes to the database
        conn.commit()
        return dataItems

    def a_item(self,itemID):
        passconn.autocommit = True
        # Creating a cursor object
        cursor = conn.cursor()
        # INSERT
        cursor.execute(f"SELECT item_available FROM inventory_items WHERE code_id = '{itemID}'; ")

        # Get the last inserted id
        """This return all the data from inventory_items TABLE """
        dataItems = cursor.fetchall()

        # Commit the changes to the database
        conn.commit()
        return dataItems

    def updateItem(self, code_id, description = None, Qty = None, price = None, updateBy = None, updateDate = None,
                   minStock = None,location = None):
        query = "UPDATE inventory_items SET item_description = %s, item_available = %s, item_price = %s, " \
                "updated_user_id = %s, item_updated_date = %s, item_min_stock = %s, item_location = %s" \
                " WHERE code_id = %s;"

        # Select the current values for the other columns
        select_query = "SELECT item_description, item_available, item_price, updated_user_id, item_updated_date," \
                       " item_min_stock, item_location FROM inventory_items WHERE code_id = %s;"

        # Collect the values for the SQL queries
        update_values = []
        if description  is not None:
            update_values.append(description)
        else:
            update_values.append(None)
        if Qty is not None:
            update_values.append(Qty)
        else:
            update_values.append(None)
        if price is not None:
            update_values.append(price)
        else:
            update_values.append(None)
        if updateBy is not None:
            update_values.append(updateBy)
        else:
            update_values.append(None)
        if updateDate is not None:
            update_values.append(updateDate)
        else:
            update_values.append(None)
        if minStock is not None:
            update_values.append(minStock)
        else:
            update_values.append(None)
        if location is not None:
            update_values.append(location)
        else:
            update_values.append(None)
        update_values.append(code_id)

        # Execute the SQL queries
        cursor = conn.cursor()
        cursor.execute(select_query, (code_id,))
        existing_values = cursor.fetchone()
        query_values = tuple(update_values)
        if None in query_values:
            query_values = tuple(v if v is not None else existing_values[i] for i, v in enumerate(query_values))
        cursor.execute(query, query_values)
        conn.commit()
        cursor.close()

    """This function is to use in Billing TAB(def insertBill():). To update the item quantity after
    operation (if entrace = +, if exit = -)"""
    def updateItemQty(self,itemID, BillType, BillQty):
        conn.autocommit = True
        # Creating a cursor object
        cursor = conn.cursor()
        # INSERT
        cursor.execute(f"SELECT item_available FROM inventory_items WHERE code_id = '{itemID}'; ")
        result = cursor.fetchone()[0]
        print(result)
        conn.commit()
        cursor.close()
        if BillType =="Entrance":
            newQty = result + int(BillQty)
        else:
            if int(BillQty) > result:
                print('not enogth')
                return False
            else:
                newQty = result - int(BillQty)
        conn.autocommit = True
        # Creating a cursor object
        cursor = conn.cursor()
        cursor.execute(f"UPDATE inventory_items SET item_available = '{newQty}' WHERE code_id = '{itemID}'; ")
        conn.commit()
        cursor.execute(f"SELECT item_available FROM inventory_items WHERE code_id = '{itemID}'; ")
        newResult = cursor.fetchone()[0]
        print(newResult)
        return newResult

# bill = ItemDB()
#
# res = bill.updateItemQty('03',"Entance",130)
# print(res)
############################################################################################


############################################################################################

##############################################################################################
class BillingDB:
    ######### IN = Ingress in inventory#############
    def in_newBill(self,bill_id, entrance_or_exit, company_id, item_id, itemname, bill_quantity,
                        bill_price, bill_discount, bill_date, bill_date_created, bill_description, user_id ):
        conn.autocommit = True
        # Creating a cursor object
        cursor = conn.cursor()
        # INSERT
        cursor.execute(
            f"INSERT INTO  inventory_transaction (bill_id, entrance_or_exit, company_id, item_id, itemname,"
            f" bill_quantity, bill_price, bill_discount, bill_date, bill_date_created, bill_description, user_id  ) "
            f"VALUES('{bill_id}', '{entrance_or_exit}', '{company_id}', '{item_id}', '{itemname}', '{bill_quantity}',"
            f" '{bill_price}', '{bill_discount}', '{bill_date}', '{bill_date_created}', '{bill_description}', '{user_id}') RETURNING user_id ")

        # Get the last inserted id
        """This return where the messagebox to let know to the user their  ID number alocated by the DB """
        insertedIBilling_Code = cursor.fetchone()[0]

        # Commit the changes to the database
        conn.commit()
        # possibilite to have the ID of the last inserted Billing

        return insertedIBilling_Code
        # Close the cursor and connection
        # cursor.close()
        # conn.close()

    print("Supplier data been created successfully in inventory_transaction TABLE  ")

    #This function returns all the data from inventory_transaction TABLE
    def allBill(self):
        conn.autocommit = True
        # Creating a cursor object
        cursor = conn.cursor()
        # INSERT
        cursor.execute("SELECT * FROM inventory_transaction ORDER BY bill_id ASC; ")

        # Get the last inserted id
        """This return all the data from inventory_transaction TABLE """
        dataBills = cursor.fetchall()

        # Commit the changes to the database
        conn.commit()
        return dataBills

############################################################################################

##############################################################################################
class SearchDB:
    pass