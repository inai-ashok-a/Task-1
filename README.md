
# FASTAPI WITH MYSQL CRUD ON USERS

In this project, we can see through the integeration between the fastapi and mysql and be able to read, write, update, and delete the data from mysql through the fastapi.

## Installations:

### Set up a virtual environment

It’s good practice to create isolated Python environments for your Python project. To ensure that you have virtualenv installed, run the command below:

    pip install virtualenv

Now, create a new directory called server-side-rendering-with-fastapi. Navigate to it and use the command below to create a virtual environment:
  
    python3 -m venv env
  
To activate the virtual environment in windows we just created, run the command below:

    env/Scripts/activate
    
If env has not activated check Get-ExecutionPolicy has bypass by using this command below:

    Get-ExecutionPolicy
    
If it is Restricted then enter the below commands to Bypass:

    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass -Force
    
Now you can check by:

     Get-ExecutionPolicy
     
 ## Working:
uvicorn is an ASGI (async server gateway interface) compatible web server. It's (simplified) the binding element that handles the web connections from the browser or api client and then allows FastAPI to serve the actual request.

uvicorn listens on a socket, receives the connection, does a bit processing and hands the request over to FastAPI, according to the ASGI interface.

You can start the uvicorn main.py file by the below command:

    uvicorn main:app --reload
    
 ### Request from Postman:
    
#### Getrequest to read the data in  the mysql database.
  
 ![image](https://user-images.githubusercontent.com/109514878/180304084-089b435a-264e-4cc0-b2b6-4c3c4463ae9d.png)
 
 
 ### Postrequest to insert the data in the mysql database.
 
 In order to insert the data to the mysql you should set Header Key as Content-Type and Header value as application/json.
 Then you can enter the detail in body as raw.
 
 ![image](https://user-images.githubusercontent.com/109514878/180305576-9733b52f-76d9-4040-ba97-58276f7e517b.png)


### Putrequest to update the details.

  ![image](https://user-images.githubusercontent.com/109514878/180305805-da75b0ff-345a-46f1-bf13-ed06b06e7bd0.png)

### Deleterequest to delete the data from table by entering id of the table.

  ![image](https://user-images.githubusercontent.com/109514878/180306238-61aae53f-5986-40e6-983e-183c17ef9327.png)

     
