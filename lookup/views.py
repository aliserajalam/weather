from django.shortcuts import render
from my_secrets import secrets

def index(request):
    import json
    import requests

    api_key = secrets.API_KEY
    print(api_key)

    if request.method == "POST":
        
        zipcode = request.POST['zipcode']

        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=0&API_KEY=" + api_key)
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"
        
        if api[0]['Category']['Name'] == "Good":
            category_colour = "good"
            category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
        elif api[0]['Category']['Name'] == "Moderate":
            category_colour = "moderate"
            category_description = "(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_colour = "USG"
            category_description = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_colour = "unhealthy"
            category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_colour = "veryunhealthy"
            category_description = "(201 - 300) Health alert: everyone may experience more serious health effects"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_colour = "hazardous"
            category_description = "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."


    else:  
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=0&API_KEY=" + api_key)
        
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"
        
        if api[0]['Category']['Name'] == "Good":
            category_colour = "good"
            category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
        elif api[0]['Category']['Name'] == "Moderate":
            category_colour = "moderate"
            category_description = "(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_colour = "USG"
            category_description = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_colour = "unhealthy"
            category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_colour = "veryunhealthy"
            category_description = "(201 - 300) Health alert: everyone may experience more serious health effects"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_colour = "hazardous"
            category_description = "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."
                    
            

    return render(request, 'index.html', {
        'api': api,
        'category_description': category_description,
        'category_colour': category_colour
    })

def about(request):
    return render(request, 'about.html', {})