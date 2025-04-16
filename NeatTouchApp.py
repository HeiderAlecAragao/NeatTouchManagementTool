import sqlite3 as sql
def menu():
    print("""
1- ADD a client
2- REMOVE a client
3- Consult Information
4- Exit application
    """)
    prompt=int(input("What would you like to do? Enter the number for the desired action:  "))
    return prompt
def Add_Client():
    try:
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
            cur.execute(sqlentry,(Phone_Number,Client_Name,address,dimension,city,start_date,price))#Here we used the SQL query from the variable and all these other variable is passed to statement, this is done this way to prevent sql injection,this is called parameterized query.

            again = input("Would like to add more clients?(y/n) ")
    except:
        print("ERROR!!! you entered an invalid input, the process will restart")
        Add_Client()

def Delete_Client():
    pass

def Consult_Client():
    #pass
    consult_name =str(input("What client would you like to consult about?")).upper()

    cur.execute(f"SELECT * from clients where phone LIKE '{consult_name}%'")
    IDnumber =cur.fetchall()
    print(IDnumber)
#THE ACTUAL APPLICATION
def main():
    global conn
    global cur
    try:

        conn =sql.connect("ClientInfo.db") # Connecting to the database and closing should probably be done on the main body
        cur = conn.cursor()
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



        conn.commit()
        conn.close()
    except:
        pass

# Start/Call the program.
if __name__== "__main__":
    main()
