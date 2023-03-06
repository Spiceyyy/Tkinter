from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.geometry("600x100")

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=10&API_KEY=F5A871A6-F72A-4BAF-ADFE-5E0A02F5537C

# Create Zipcode Lookup Function
def zipLookup():
    #zip.get()
    #zipLabel = Label(root, text=zip.get())
    #zipLabel.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=10&API_KEY=F5A871A6-F72A-4BAF-ADFE-5E0A02F5537C")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
    
        if category == "Good":
            weather_colour = "#0C0"
        elif category == "Moderate":
            weather_colour = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_colour = "#ff9900"
        elif category == "Unhealthy":
            weather_colour = "#FF0000"
        elif category == "Very Unhealthy":
            weather_colour = "#990066"
        elif category == "Hazardous":
            weather_colour = "#660000"
    
    
        root.configure(background=weather_colour)
        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background=weather_colour)
        myLabel.grid(row=1, column=0, columnspan=2)

    except Exception as e:
        api = "Error..."



zip = Entry(root)
zip.grid(row=0, column=0, sticky=W+E+N+S)

zipButton = Button(root, text="Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1, sticky=W+E+N+S)

root.mainloop()