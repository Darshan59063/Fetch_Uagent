# Temperature Alert Agent

Welcome to the fetch_temperature_agent project! In this README, we'll guide you through the process of setting up your Ambee API key and running the main.py file using a virtual environment. This project allows you to input latitude, longitude, minimum temperature, and maximum temperature for a region and then fetch the current temperature for that location.

## Step 1: Obtain Your Ambee API Key

1. Visit the [Ambee website](https://www.ambee.com/) to obtain your API key.
2. Once you have your API key, copy it to your clipboard.

## Step 2: Create a .env File

1. Create a `.env` file in your project directory.
2. Open the `.env` file using a text editor.
3. Add the following line to the `.env` file and replace `"your_api_key"` with your actual Ambee API key:

   ```dotenv
   AMBEE_API_KEY="your_api_key"

## Step 3: Set Up a Virtual Environment

1. Open your terminal and navigate to your project directory.
2. Create a virtual environment by running the following command in bash terminal:

   ```bash
   python -m venv venv
   
3. Activate the virtual environment:
   * On Windows:
        ```bash
        .\venv\Scripts\activate

   * On macOS and Linux:
        ```bash
        source venv/bin/activate
4. Run the main.py file
