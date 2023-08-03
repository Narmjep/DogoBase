# DogoBase

DogoBase is a very simple database for storing dog data that provides an easy-to-use [api](#dogobase-api).
- The [DogoBase](DogoBase) folder contains the code for the dogobase server which hosts the api.
- The [RandomNameGenerator](RandomNameGenerator) folder contains the code for the random name generator used by the dogobase server, which also provides an [api](#randomnamegenerator-api).
- The [client](client.py) is a python script that demonstrates how to use the dogobase api.
- The scripts [run.bash](run.bash), [run.bat](run.bat) and [run.ps1](run.ps1) are used to run both servers, each in a seperate terminal window.

The apis are developed using [*flask*](https://flask.palletsprojects.com/en/1.1.x/). Make sure to install the [required packages](requirements.txt).

## **DogoBase API**

To run the server locally, run the [server.py](DogoBase/server.py) file. The server will be hosted on port 5000 by default. Make sure however that the random name generator server is **also** running ([RandomNameGenerator](#randomnamegenerator-api))! The database file will be created inside the [data](RandomNameGenerator/data) folder.

## 1. Get data

 - To get a dog with a specific id, send a GET request to **/api/search/{id}**.
 - To search for a dog with a specific id, name and/or gender send a GET request to **/api/search** with a json parameter `{'id':... , 'name':... , 'gender':...}`

## 2. Add data

- To create a new dog and add it to the database make a POST request to **api/create** with a json paramter `{'id':... , 'name':... , 'gender':...}`. If any of the parameters are missing, the server will generate a random value for it. If the id is already in use, the server will assign a new one to the dog. The server will return the newly created dog as a json object.

## 3. SQL

- To execute any SQL query, send a POST request to **/api/sql** with a json parameter `{'query':...}`. The server will return the result of the query as a json object.

## **RandomNameGenerator API**

To run the server locally, run the [server.py](RandomNameGenerator/server.py) file. The server will be hosted on port 5001 by default.

 - To get a random name, send a GET request to **/**. The server will return the name as text,

 - To get a random male name send a GET request to **/male**.

 - To get a random female name send a GET request to **/female/**.
