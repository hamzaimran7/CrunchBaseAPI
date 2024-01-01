from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/searches/organizations")
def make_request(payload: dict):
    api_url = "https://crunchbase-crunchbase-v1.p.rapidapi.com/searches/organizations"
    api_key = "YOUR_RAPIDAPI_KEY"  # Replace with your actual RapidAPI key

    headers = {
        'Content-Type': 'application/json',
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': "crunchbase-crunchbase-v1.p.rapidapi.com",
    }

    # Make the request to Crunchbase API using the 'requests' library
    response = requests.post(api_url, json=payload, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Return the JSON response directly
        return response.json()
    else:
        # If the request was not successful, return an error message with status code and reason
        return {"error": f"Error: {response.status_code}, {response.reason}"}
