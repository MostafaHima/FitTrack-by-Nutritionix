import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# API credentials
APP_ID = os.getenv("NATURAL_APP_ID")
API_KEY = os.getenv("NATURAL_API_KEY")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

# Endpoints for APIs
nutural_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/63af58bc12d0333a6fd921b836f52de3/caloriTraking/workouts"

# Headers for Nutritionix API
nutural_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Headers for Sheety API
sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

# Get user input for exercises
exercise_text = input("Tell me which exercises you did: ")

# Parameters for Nutritionix API
nutural_paramters = {
    "query": exercise_text,
    "age": 23,
    "gender": "male",
    "weight_kg": 55,
    "height_cm": 180,
}

# Request exercise data from Nutritionix API
nutural_response = requests.post(
    url=nutural_endpoint,
    json=nutural_paramters,
    headers=nutural_headers
)

# Parse the response data
nutural_data = nutural_response.json()

# Get current date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Check if exercises are found in the API response
if "exercises" in nutural_data:
    for exercise in nutural_data["exercises"]:
        # Prepare data for Sheety API
        sheety_post = {
            "workout": {
                "date": today_date,
                "time": now_time,
                "exercise": exercise["user_input"].title(),  # Capitalize input
                "duration": float(exercise["duration_min"]),  # Convert duration to float
                "calories": exercise["nf_calories"]  # Calories burned
            }
        }

        # Send data to Sheety API
        sheety_response = requests.post(
            sheety_endpoint,
            json=sheety_post,
            headers=sheety_headers
        )

        # Print the response from Sheety API
        print("Response from Sheety API:", sheety_response.text)
else:
    # If no exercises are found, display a message
    print("No exercises found in the result.")
