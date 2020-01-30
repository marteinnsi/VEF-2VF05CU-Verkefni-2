from flask import Flask, render_template, abort
app = Flask(__name__)

frettir = {
    1: ("Marteinn", "marteinn@localhost", "Bananar gulir samkvæmt nýjustu rannsóknum", "Nýjustu rannsóknir MIT telja banana gula.", "banani.png"),
    2: ("Martienn", "marteinn@localhost", "Appelsínur eru ekki gular", "Sigmundur telur appelsínur appelsínugular.", "appelsina.png"),
    3: ("Marteinn", "marteinn@localhost", "Team Fortress 2 kosinn besti leikur 2020", "Þessar fréttir koma náttúruega engum á óvart en þær eru samt skemmtilegar.", "tf2.png"),
    4: ("Marteinn", "marteinn@localhost", "Breath of the Wild gefinn út á PS2", "Frægi leikurinn Breath of the Wild hefur verið gefinn út á PlayStation 2", "ps2.png"),
    5: ("Marteinn", "marteinn@localhost", "Danir vinna heimsmeistaramót", "Danir unnu heimsmeistarabót í boccia", "danir.jpg"),
    6: ("Marteinn", "marteinn@localhost", "Dungeon Defenders: Awakened kemur út í ár, 2020", "Vinsæla tölvuleikjaserían Dungeon Defenders á von á nýjum leik snemma árið 2020.", "defenders.png")
}


@app.route("/")
def route_index():
    return render_template("index.html", frettir=frettir)


@app.route("/kennitala/<int:kt>")
def route_kennitala(kt):
    tversumma = 0
    while kt:
        tversumma += kt % 10
        kt //= 10
    return render_template("kennitala.html", tversumma=tversumma)


@app.route("/frett/<int:id>")
def route_frett(id):
    if id in frettir:
        return render_template("frett.html", frett=frettir[id])
    else:
        abort(404)


@app.errorhandler(404)
def route_404(resource):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
