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

    def update(self):
        pass

