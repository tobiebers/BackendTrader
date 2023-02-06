from flask import Flask, request, render_template
import random

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.template_folder = 'templates'


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        Kapital = float(request.form["Kapital"])
        Hebel = int(request.form["Hebel"])
        Trades = int(request.form["Trades"])
        Winrate = int(request.form["Winrate"])
        Tp = float(request.form["Tp"])
        Sl = float(request.form["Sl"])

        Liste = []
        Listeplott = []

        winner = Winrate/100 * Trades
        loser = Trades - winner

        winner = int(winner)
        loser = int(loser)

        for i in range(winner):
            Liste.append(Tp)

        for i in range(loser):
            Liste.append(Sl)

        counterWinner = 0
        counterWinner = int(counterWinner)
        counterLooser = 0
        counterLooser = int(counterLooser)
        counterGesamt = 0
        counterGesamt = int(counterGesamt)

        for i in range(Trades):
            trade = random.choice(Liste)
            if trade == Tp:
                Liste.remove(trade)
                counterWinner = counterWinner + 1
                counterGesamt = counterGesamt + 1
                WL = Kapital / 100 * trade
                Kapital = Kapital + WL * Hebel
                Kapital = round(Kapital, 2)
                Listeplott.append(Kapital)
            elif trade == Sl:
                Liste.remove(trade)
                counterLooser = counterLooser + 1
                counterGesamt = counterGesamt + 1
                WL = Kapital / 100 * trade
                Kapital = Kapital - WL * Hebel
                Kapital = round(Kapital, 2)
                Listeplott.append(Kapital)

        return render_template("result.html", Kapital=Kapital, counterWinner=counterWinner, counterLooser=counterLooser)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
