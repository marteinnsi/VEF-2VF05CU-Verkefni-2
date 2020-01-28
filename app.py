from flask import Flask
app = Flask(__name__)

@app.route("/")
def route_index():
    return app.send_static_file("html/index.html")

@app.route("/kennitala/<int:kt>")
def route_kennitala(kt):
    if len(str(kt)) == 10:
        tversumma = 0
        while kt:
            tversumma += kt % 10
            kt //= 10
        return str(tversumma)
    else:
        return "Kennitala á að vera 10 stafir."

if __name__ == "__main__":
    app.run(threaded=True, port=5000)