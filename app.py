from flask import Flask, render_template, abort
app = Flask(__name__)

frettir = {
    1: ("Rannsóknir segja að bananar séu gulir", "Já það var skemmtilegt"),
    2: ("Team Fortress 2 kosinn besti leikur 2020", "Og það kom engum að óvart"),
    3: ("Nýtt ilmvatn frá Google", ".-."),
    4: ("Appelsínur og epli", "Eru góð"),
}

@app.route("/")
def route_index():
    return render_template("index.html")

@app.route("/kennitala/<int:kt>")
def route_kennitala(kt):
    tversumma = 0
    while kt:
        tversumma += kt % 10
        kt //= 10
    return str(tversumma)

@app.route("/frett/<int:id>")
def route_frett(id):
    if id in frettir:
        return render_template("frett.html", frett_id=id, frettir=frettir)
    else:
        abort(404)
        

@app.errorhandler(404)
def route_404(resource):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(threaded=True, port=5000)