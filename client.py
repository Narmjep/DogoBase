import requests

# GET params
# Headers
headers = {'Content-Type': 'application/json' , 'Accept': 'application/json'}

bellaJsonData = {
        "id": 1,
        "name": "Bella",
        "gender": "female"
}

query = {
        "id": 1,
}

query1 = {
        "name": "Bella",
}

query2 = {
        "gender": "female"
}

query3 = {
        "id": 2,
        "name": "Bella",
        "gender": "female"
}

query4 = {
        "id": 1,
        "name": "Bella",
        "gender": "female"
}

sql_query = {'query':"SELECT * FROM dog_model WHERE name = 'Bella'"}

if __name__ == '__main__':
    # Adding dogs
    print("Adding a random dog")
    print(requests.post('http://localhost:5000/api/create' , headers=headers , json={}).text)
    print('-------------------------------')

    print("Adding bella")
    print(requests.post('http://localhost:5000/api/create' , headers=headers, json=bellaJsonData).text)
    print('-------------------------------')

    print("Adding bella again. Id will be overwritten.")
    print(requests.post('http://localhost:5000/api/create' , headers=headers, json=bellaJsonData).text)
    print('-------------------------------')

    print("Look for dog with id 1")
    print(requests.get('http://localhost:5000/api/search/1' , headers=headers).text)
    print('-------------------------------')

    print("Look for dog with id 1 (using params)")
    print(requests.get('http://localhost:5000/api/search' , headers=headers, json=query).text)
    print('-------------------------------')

    print("Look for alls dogs with the name Bella")
    print(requests.get('http://localhost:5000/api/search' , headers=headers, json=query1).text)
    print('-------------------------------')

    print("Looking for all female dogs")
    print(requests.get('http://localhost:5000/api/search' , headers=headers, json=query2).text)
    print('-------------------------------')

    print("Looking for bella with id 2")
    print(requests.get('http://localhost:5000/api/search' , headers=headers, json=query3).text)
    print('-------------------------------')

    print("Looking for bella with id 1 (does not exist)")
    print(requests.get('http://localhost:5000/api/search' , headers=headers, json=query4).text)
    print('-------------------------------')

    print("Looking for all dogs (sql)")
    print(requests.get('http://localhost:5000/api/search/*' , headers=headers).text)
    print('-------------------------------')


    print("Run SQL query")
    print(requests.get('http://localhost:5000/api/sql' , headers=headers, json=sql_query).text)