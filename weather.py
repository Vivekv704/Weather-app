# import requests

# def get_weather(city_name):

#     apikey = "fd46ead4a61c918476efc691c4d8e4f7"
#     url = "https://api.openweathermap.org/data/2.5/weather"

#     params = {
#         'q' : city_name,
#         'appid' :apikey,
#         'units' : 'matrics'
#     }

#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         data = response.json()
#         # print(data)
#         temprature = data['main']['temp']
#         sunrise = data['sys']['sunrise']
#         sunset = data['sys']['sunset']
#         place = data['name']

#         print("Temprature ", temprature)
#         print("Sunrise ", sunrise)
#         print("Sunset ", sunset)
#         print("This is weather of ",place)
#     else:
#         print("Error:", response.status_code)
# city_name = input("Enter the city name: ")
# get_weather(city_name)



from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    city = request.args.get('city')
    api_key = 'fd46ead4a61c918476efc691c4d8e4f7'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    weather_data = {
        'place': data['name'],
        'temperature': data['main']['temp'],
        'sunrise': data['sys']['sunrise'],
        'sunset': data['sys']['sunset']
    }
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
