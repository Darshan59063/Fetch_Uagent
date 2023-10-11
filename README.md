# Temperature Alert Agent
## TeamID - Hack-230421

Welcome to the Temperature Alert Agent Project! In this README, we'll guide you through the process of setting up your Ambee API key and running the main.py file using a virtual environment. This project allows you to input latitude, longitude, minimum temperature, and maximum temperature for a region and then fetch the current temperature for that location. Sends an alert/notification to the user when the current temperature in their chosen location goes below the minimum or above the maximum threshold they've set.

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

## Step 4: Install Dependencies

1. Ensure you have a requirements.txt file with a list of project's dependencies, including any necessary libraries or packages.
2. Install the required dependencies by running the following command:

   bash
      pip install -r requirements.txt

## Step 5: Run the Program

1. Run the main.py file to execute your program. The program will prompt you to enter the latitude, longitude, minimum temperature, and maximum temperature for the region.

   bash
   python .\main.py 
