# librerias requeridas
import requests, json
from flask import Flask, render_template, request

app = Flask("temperature_app")

def parametros_api(city_name):
    api_key = "" # colocar su api key de openweathermap
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
    response = requests.get(complete_url)
    x = response.json()
    
    if x["cod"] != "404":
        city = x['name']
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"] 
        data = [city,current_temperature,current_pressure,current_humidity,weather_description]
    else:
        data = "Ciudad no encontrada "

    return data

 
@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method=="GET":
        return render_template("index.html")

    if request.method=="POST":
        city_name = request.form['city_name']
        weather_data = parametros_api(city_name)

        return render_template("index.html",
                                data=weather_data, len = len(weather_data))

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

