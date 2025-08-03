import requests
from flask import Flask, render_template, request

app = Flask(__name__)

CLIENT_ID = "08ed72be94b848e6baa5fcccece2f052"
CLIENT_SECRET = "19f7e78a53ab42ad95bc7fd83b4ff329"

def get_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
    return response.json().get("access_token")

@app.route("/", methods=["GET", "POST"])
def index():
    artistas = []
    if request.method == "POST":
        query = request.form.get("query")
        token = get_token()
        if token:
            url = f"https://api.spotify.com/v1/search?q={query}&type=artist&limit=10"
            headers = {"Authorization": f"Bearer {token}"}
            resp = requests.get(url, headers=headers)
            data = resp.json()
            artistas = data.get("artists", {}).get("items", [])
    return render_template("index.html", artistas=artistas)

if __name__ == "__main__":
    app.run(debug=True)
