# Nutrition Tracker

**Nutrition Tracker** is a project designed to track and log your exercise routines, calculate the calories burned during these activities, and store them in a structured format using APIs. The project integrates with the Nutritionix API to fetch exercise data and store the results in Google Sheets for easy tracking and analysis.

## Features

- Log your exercise activities (e.g., running, walking, cycling).
- Get real-time data on calories burned for each exercise session.
- Automatically store your workout details in Google Sheets for future reference.
- Display simple stats like exercise duration and calories burned.

## Technologies Used

- **Python**: Programming language used for backend processing.
- **Nutritionix API**: Provides exercise and nutrition data.
- **Google Sheets API**: Stores workout details (date, time, duration, calories).
- **dotenv**: For securely managing environment variables (API keys, tokens).

## Setup

### Requirements

1. Python 3.x
2. Create a `.env` file for your API credentials. You can get the keys from the Nutritionix website and create a project for Google Sheets API.

### Steps to Run the Project

1. **Install Dependencies**:
   Install the required Python libraries:
   ```bash
   pip install requests python-dotenv
