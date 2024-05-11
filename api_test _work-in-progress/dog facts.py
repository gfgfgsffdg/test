import requests

#holds the response from the API
response = None
#holds the fact from the response
fact = None

#send a GET request to the API and store the response
response = requests.get("https://dogapi.dog/api/v2/facts")
#check if the response was successful
if response.status_code == 200:
    #convert the response into a dictionary
    data = response.json()
    #store the fact from the dictionary
    fact = data['data']
    #store the text from the fact
    body_text = fact[0]['attributes']['body']
    #print the text from the fact
    print(body_text)

