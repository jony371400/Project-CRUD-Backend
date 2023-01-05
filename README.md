# Project-CRUD-Backend
For testing CRUD with RESTful API

> Configuration DB
```
1. $ cd dbHandler.py
2. Create Database and Table
3. Testing
```

> Execute App
```
$ pip install sqlite3
$ pip install flask
$ python dbServer.py
```

> Testing
```
Use Browser or PostMan to test
```

```
Test
    HTTP Method
        [Get]
    API
        $ http://127.0.0.1:5000/

Create
    HTTP Method
        [POST]
    API
        $ http://127.0.0.1:5000/API
    DATA
        {
            "ID" : 1,
            "NAME" : "Johnny"
        } 

Read
    HTTP Method
        [GET]
    API
        $ http://127.0.0.1:5000/API

Update
    HTTP Method
        [PUT]
    API
        $ http://127.0.0.1:5000/API
    DATA
        {
            "ID" : 1,
            "NAME" : "Johnny"
        }   
    
Delete
    HTTP Method
        [DELETE]
    API
        $ http://127.0.0.1:5000/API
    DATA
        {
            "ID" : 1
        } 
```

> SQL
```
INSERT INTO Customers (ID, NAME) VALUES (5 , 'Johnny');
select * from Customers;
UPDATE Customers SET NAME = 'Johnny2' WHERE ID = 5;
DELETE FROM Customers WHERE ID = 5;
```