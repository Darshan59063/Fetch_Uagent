# importing necessary libraries
import os
import requests
import win32api
from dotenv import load_dotenv
load_dotenv()

# We are using Ambee API keys to get weather information of specified latitude and longitude 
# which includes temperature report as well
AMBEE_API_KEY = os.environ.get("AMBEE_API_KEY")
lat = float(input("Input Latitude: "))   #Specifying Latitude
lng = float(input("Input Longitude: "))  #Specifying Longitude
mini_temp = float(input("Minimum Temperature: "))  #Specifying Minimum temperature threshold
maxi_temp = float(input("Maximum Temperature: "))  #Specifying Maximum temperature threshold


# Function for getting weather report 
def get_weather_data(AMBEE_API_KEY, lat, lng):  
    WEATHER_API_URL = 'https://api.ambeedata.com/weather/latest/by-lat-lng'
    params = {  
        "lat": lat,  
        "lng": lng,  
        "x-api-key": AMBEE_API_KEY  
    }  
    response = requests.get(WEATHER_API_URL, params=params)  
    data = response.json()  
    return data 


# Importing Fetch.ai uagents library for connecting with our specified weather_agent
from uagents import Agent, Context
weather_agent = Agent(name="Weather_Agent", seed="weather agent for temperature")

# Function which will call weather_agent at repeated intervals of 3 sec which will give alert if current temperature doesn't
# lie in specified range
@weather_agent.on_interval(period=3.0)
async def say_hello(ctx: Context):
    data = get_weather_data(AMBEE_API_KEY, lat, lng) 
    if data['message'] == 'success': 
        current_temperature =  data['data']['temperature']
        if mini_temp > current_temperature or current_temperature > maxi_temp:
            win32api.MessageBox(0, f'Latest Temperature of Latitude: {lat} and Longitude:{lng} is {current_temperature} which does not lie within {mini_temp} and {maxi_temp}', '⚠️ ALERT')
            ctx.logger.info(f'Temperature is {current_temperature} which is not within {mini_temp} and {maxi_temp}')
        else:
            ctx.logger.info(f'Temperature is {current_temperature}')
    else:
        print("Check whether specified Latitude and Longitude Coordinates are correct else Retry in sometime")

if __name__ == "__main__":
    weather_agent.run()

