import sqlite3 as sql
import subprocess as sp


def connect_create_cursor():
    global conn
    global cur
    conn=sql.connect("ClientInfo.db")
    cur = conn.cursor()

def close_save_database():
    conn.commit()
    conn.close()

def just_close_database(): #this will just close the connection without commiting.
    conn.close()
def menu():
    print("""
    
    
    

███╗   ██╗███████╗ █████╗ ████████╗    ████████╗ ██████╗ ██╗   ██╗ ██████╗██╗  ██╗     ██████╗██╗     ███████╗ █████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗ 
████╗  ██║██╔════╝██╔══██╗╚══██╔══╝    ╚══██╔══╝██╔═══██╗██║   ██║██╔════╝██║  ██║    ██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██║████╗  ██║██╔════╝ 
██╔██╗ ██║█████╗  ███████║   ██║          ██║   ██║   ██║██║   ██║██║     ███████║    ██║     ██║     █████╗  ███████║██╔██╗ ██║██║██╔██╗ ██║██║  ███╗
██║╚██╗██║██╔══╝  ██╔══██║   ██║          ██║   ██║   ██║██║   ██║██║     ██╔══██║    ██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██║██║╚██╗██║██║   ██║
██║ ╚████║███████╗██║  ██║   ██║          ██║   ╚██████╔╝╚██████╔╝╚██████╗██║  ██║    ╚██████╗███████╗███████╗██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝   ╚═╝          ╚═╝    ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                                                                                      


                                                                                            
ENTER ONE OF THE FOLLOWING NUMBERS:                                                                                                            
                                                                                                                                                             
1- ADD a client
2- REMOVE a client
3- Consult Information
4- UPDATE Client Info
5- Exit application
    """)
    prompt=int(input("""What would you like to do? Enter the number for the desired action:  """))
    sp.run('cls',shell=True)#this will clear the terminal , so the old output doesnt show with the new output.
    return prompt
def Add_Client():
    try:
        connect_create_cursor()#this will connect and create the cursor to interact with the database.
        again = 'y'
        while again == 'y':

            Client_Name = str(input("What is the client's name? "))
            Client_Name = Client_Name.upper()
            Phone_Number = str(input("What is the client's phone number? "))
            address = str(input("What is the client's home address? "))
            address = address.upper()
            dimension = float(input("What is the square footage of the house/building ?"))
            city = str(input("Which city is the client/building located? "))
            city = city.upper()
            start_date = str(input("When did the customer start or will start? "))
            price = float(input("What is the amount being charged? "))

            sqlentry = '''INSERT INTO clients(phone,name,address,dimension,city,price,startdate) 
                    VALUES(?,?,?,?,?,?,?)''' #these questions marks will be replaced by the variables' values of the next line
            cur.execute(sqlentry,(Phone_Number,Client_Name,address,dimension,city,price,start_date))#Here we used the SQL query from the variable and all these other variable is passed to statement, this is done this way to prevent sql injection,this is called parameterized query.

            again = input("Would like to add more clients?(y/n) ")
        close_save_database()#this will save data to database and close the connection.
        sp.run('cls', shell=True)  # this will clear the terminal , so the old output doesnt show with the new output.
    except KeyboardInterrupt:
        just_close_database()
        pass

    except:
        print("ERROR!!! you entered an invalid input, the process will restart")
        Add_Client()
def Delete_Client():
    pass
def Update_Client_Menu():
    update_info = int(input("""
    Which information would you like to MODIFY ?
    1- Client Name
    2- Phone
    3- Address 
    4- City
    5- House size
    6- Price
    7- ALL or more than 1 information
        
    Enter the number for the desired Modification: """))
    return update_info
def Update_Client():
    while True:

        if Update_Client_Menu() == 1: #This updates the client's name.
            connect_create_cursor()
            old_name = str(input("Current Name: ")).upper()
            new_name =str(input("New Name: ")).upper()
            cur.execute("SELECT name from clients;")
            confirm_name_exists = cur.fetchone()
            if old_name == confirm_name_exists[0]:
                cur.execute("UPDATE clients SET name = ? WHERE name = ? ;",(new_name,old_name) )
                close_save_database()
                break
            else:
                print("The Client's name specified could NOT be found,Please try again.")
def Consult_Client():
    connect_create_cursor()
    consult_name =str(input("Enter client's name or 'all' to see every client:")).upper()
    if consult_name != "ALL":
        cur.execute(f"SELECT * FROM clients WHERE name LIKE '{consult_name}%'")
        IDnumber = cur.fetchall() # Fetchall returns a list with all the rows, each row is a tuple within the list. Fetchone() will return just one row at a time.

        for clients in IDnumber:
            print(f"""
        ________________________________________________________________________________________________________________
         Name:{clients[1]} | Phone: {clients[2]} | Address:{clients[3]} | Price:""" + f'\033[0;32;40m{clients[6]}\033[0m\n' +
         f"""         ID: {clients[0]:<2}| Footage ^2: {clients[5]} | Started on: {clients[7]} | City: {clients[4]}
        ________________________________________________________________________________________________________________""",end='')
        input("Press 'Enter' to go back: ")
        sp.run('cls', shell=True)  # this will clear the terminal , so the old output doesnt show with the new output.

    if consult_name == "ALL":
        cur.execute(f"SELECT * FROM clients;")
        IDnumber = cur.fetchall()  # Fetchall returns a list with all the rows, each row is a tuple within the list. Fetchone() will return just one row at a time.

        for clients in IDnumber:
            print(f"""
                ________________________________________________________________________________________________________________
                 Name:{clients[1]} | Phone: {clients[2]} | Address:{clients[3]} | Price:""" + f'\033[0;32;40m{clients[6]}\033[0m\n' +
                  f"""                 ID: {clients[0]:<2}| Footage ^2: {clients[5]} | Started on: {clients[7]} | City: {clients[4]}
                ________________________________________________________________________________________________________________""",end='')
        input("""
        Press 'Enter' to go back: """)
        sp.run('cls', shell=True)  # this will clear the terminal , so the old output doesnt show with the new output.
    just_close_database()
#THE ACTUAL APPLICATION
def main():

    try:

        leave = 0
        while leave == 0:
            action= menu()
            if action == 1 : #ADD Client info.
                Add_Client()
            if action == 2 : # DELETE Client info.
                Delete_Client()
            if action == 3 : #Consult Client Info.
                Consult_Client()
            if action == 4:
                Update_Client()
            if action == 5 :
                leave = 1




    except:
        pass

# Start/Call the program.
if __name__== "__main__":
    main()
