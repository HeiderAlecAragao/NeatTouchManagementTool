import sqlite3 as sql


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
    
    
    
 
 
$$\   $$\                       $$\           $$$$$$$$\                            $$\       
$$$\  $$ |                      $$ |          \__$$  __|                           $$ |      
$$$$\ $$ | $$$$$$\   $$$$$$\  $$$$$$\            $$ | $$$$$$\  $$\   $$\  $$$$$$$\ $$$$$$$\  
$$ $$\$$ |$$  __$$\  \____$$\ \_$$  _|           $$ |$$  __$$\ $$ |  $$ |$$  _____|$$  __$$\ 
$$ \$$$$ |$$$$$$$$ | $$$$$$$ |  $$ |             $$ |$$ /  $$ |$$ |  $$ |$$ /      $$ |  $$ |
$$ |\$$$ |$$   ____|$$  __$$ |  $$ |$$\          $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |
$$ | \$$ |\$$$$$$$\ \$$$$$$$ |  \$$$$  |         $$ |\$$$$$$  |\$$$$$$  |\$$$$$$$\ $$ |  $$ |
\__|  \__| \_______| \_______|   \____/          \__| \______/  \______/  \_______|\__|  \__|
                                                                                            
                                                                                            
                                                                                            
                                                                                                             
                                                                                                                                                             
1- ADD a client
2- REMOVE a client
3- Consult Information
4- Exit application
    """)
    prompt=int(input("""What would you like to do? Enter the number for the desired action:  """))
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
    except:
        print("ERROR!!! you entered an invalid input, the process will restart")
        Add_Client()

def Delete_Client():
    pass

def Consult_Client():
    connect_create_cursor()
    consult_name =str(input("What client would you like to consult about?")).upper()

    cur.execute(f"SELECT * FROM clients WHERE name LIKE '{consult_name}%'")
    IDnumber =cur.fetchall()
    Many_clients_Count = 0
    for clients in IDnumber:
        print(f"""
    ________________________________________________________________________________________________________________
     Name:{IDnumber[Many_clients_Count][1]} | Phone: {IDnumber[Many_clients_Count][2]} | Address:{IDnumber[Many_clients_Count][3]} | Price: {IDnumber[0][6]} 
     ID: {IDnumber[Many_clients_Count][0]:<10} | Footage ^2: {IDnumber[Many_clients_Count][5]} | Started on: {IDnumber[Many_clients_Count][7]} | City: {IDnumber[Many_clients_Count][4]}
    ________________________________________________________________________________________________________________
        \n""")
        Many_clients_Count=+1
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
            if action == 4 :
                leave = 1




    except:
        pass

# Start/Call the program.
if __name__== "__main__":
    main()
