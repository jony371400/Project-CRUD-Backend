import sqlite3

#######################################################################
# Build
#######################################################################
# def CreateTable():
#     cursorObj.execute('CREATE TABLE Customers (ID INT , NAME INT);')
#     cursorObj.execute('CREATE TABLE Orders (ID INT , CODE INT);')
#     print("Create Table Success!")


# def InsertDATA():
#     cursorObj.execute("INSERT INTO Customers (ID , NAME) VALUES (1, 1 )")
#     cursorObj.execute("INSERT INTO Customers (ID , NAME) VALUES (2, 2 )")
#     cursorObj.execute("INSERT INTO Customers (ID , NAME) VALUES (3, 3 )")
#     cursorObj.execute("INSERT INTO Customers (ID , NAME) VALUES (4, 4 )")

#     cursorObj.execute("INSERT INTO Orders (ID , CODE) VALUES (2, 1 )")
#     cursorObj.execute("INSERT INTO Orders (ID , CODE) VALUES (4, 2 )")
#     cursorObj.execute("INSERT INTO Orders (ID , CODE) VALUES (6, 3 )")
#     cursorObj.execute("INSERT INTO Orders (ID , CODE) VALUES (8, 4 )")

#     print("Insert Success!")

#######################################################################
# Function
#######################################################################
def ReadData():    
    con = sqlite3.connect('mydatabase.db')
    cursorObj = con.cursor()

    # # Select Customers Table
    # print('Select Customers Table')
    # cursor = cursorObj.execute("SELECT ID, NAME FROM Customers")
    # for row in cursor:
    #     print("ID = ", row[0], "NAME = ", row[1])

    # # Select Orders Table
    print('Select Orders Table')
    cursor = cursorObj.execute("SELECT ID, CODE FROM Orders")
    for row in cursor:
        print("ID = ", row[0], "CODE = ", row[1])
    
    con.commit()
    con.close()

    return cursor

#######################################################################
# DB Jpin
#######################################################################
def InnerJoin():
    con = sqlite3.connect('mydatabase.db')
    cursorObj = con.cursor()

    print('Inner Join')
    cursor = cursorObj.execute(
        "SELECT Customers.ID , Customers.NAME , Orders.CODE FROM Customers INNER JOIN Orders ON Customers.ID = Orders.ID;")
    for row in cursor:
        print("ID = ", row[0], "NAME = ", row[1], "CODE = ", row[2])

    con.commit()
    con.close()


def FullJoin():
    con = sqlite3.connect('mydatabase.db')
    cursorObj = con.cursor()

    print('Full Join')
    cursor = cursorObj.execute("SELECT Customers.ID , Customers.NAME , Orders.CODE FROM Customers LEFT JOIN Orders ON Customers.ID = Orders.ID \
                              union \
                              SELECT Orders.ID , Customers.NAME , Orders.CODE FROM Orders LEFT JOIN Customers ON Orders.ID = Customers.ID;")
    for row in cursor:
        print("ID = ", row[0], "NAME = ", row[1], "CODE = ", row[2])


def LeftJoin():
    con = sqlite3.connect('mydatabase.db')
    cursorObj = con.cursor()

    print('Left Join')
    cursor = cursorObj.execute(
        "SELECT Customers.ID , Customers.NAME , Orders.CODE  FROM Customers LEFT JOIN Orders ON Customers.ID = Orders.ID;")
    for row in cursor:
        print("ID = ", row[0], "NAME = ", row[1], "CODE = ", row[2])
    con.commit()
    con.close()


def RightJoin():
    con = sqlite3.connect('mydatabase.db')
    cursorObj = con.cursor()

    print('Right Join')
    cursor = cursorObj.execute("SELECT Orders.ID , Customers.NAME , Orders.CODE  FROM Orders LEFT JOIN Customers ON Customers.ID = Orders.ID;")
    for row in cursor:
        print("ID = ", row[0], "NAME = ", row[1], "CODE = ", row[2])

    con.commit()
    con.close()


#######################################################################
# TEST
#######################################################################
# print("Connect Success!")
# con = sqlite3.connect('mydatabase.db')
# cursorObj = con.cursor()

# CreateTable()
# InsertDATA()
# ReadData()
# InnerJoin()
# FullJoin()
# LeftJoin()
# RightJoin()

# con.commit()
# con.close()