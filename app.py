from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city):
    api_key = "f74df3f9c4bfc90f69fb7c6c43fa4baa"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return {
            "city": data.get('name'),
            "temperature": data['main'].get('temp'),
            "description": data['weather'][0].get('description').capitalize()
        }

    except Exception as e:
        return {"error": str(e)}

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        weather = get_weather(city)
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
