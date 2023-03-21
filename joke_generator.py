import requests

# Get a random joke from the API
url = "https://official-joke-api.appspot.com/random_joke"

# Make a request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the data from the response
    data = response.json()
    # Print the joke
    print(data['setup'])
    print(data['punchline'])
else:
    print("Sorry, something went wrong. Please try again later.")
