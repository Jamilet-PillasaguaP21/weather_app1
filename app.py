from flask import Flask, render_template
import requests #pip install requests
from dotenv import load_dotenv, dotenv_values

config = dotenv_values('.env')

app = Flask(__name__) 

def get_weather_data(city):
    API_KEY = config['API_KEY']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=es&units=metric'
    r = requests.get(url).json()
    print(r)
    return r

@app.route('/jami')
def jami():
    get_weather_data('Guayaquil')
    return get_weather_data('Guayaquil')


@app.route('/about')
def about():
    return render_template('mi_curriculo.html')

@app.route('/clima')
def clima():
    return 'clima'

if __name__ == '__main__':
    app.run(debug=True)