import sqlite3
from sqlite3 import Error

from flask import Flask
from flask import abort
from flask import render_template
from flask import make_response
from flask import request
from flask import redirect
from datetime import datetime

app = Flask(__name__)

if __name__ == '__main__':
   app.run()

@app.route("/")
def home():
    if not 'wins' in request.cookies:
        print("No cookies found")
        resp = make_response(render_template("background.html"))
        resp.set_cookie("wins", "0")
        resp.set_cookie("winStreak", "0")
        resp.set_cookie("playedToday", "false")
        resp.set_cookie("loginTime", str(datetime.now()))
        resp.set_cookie("results", "none")
    
    if request.cookies.get("playedToday") == "true":
        print("Already played today")
        print(timeCheck(request.cookies.get("loginTime")))
        if timeCheck(request.cookies.get("loginTime")) == True:
            print("Time to play")
            resp = make_response(render_template("background.html"))
            resp.set_cookie("playedToday", "false")
            resp.set_cookie("results", "none")
            resp.set_cookie("loginTime", str(datetime.now()))
        else:
            print("Checking win or lose")
            if request.cookies.get("results") == "win":
                print("win")
                return redirect("/win")
            elif request.cookies.get("results") == "lose":
                print("lose")
                return redirect("/lose")
    elif request.cookies.get("playedToday") == "false":
        print("Not played today")
        resp = make_response(render_template("background.html"))
    return resp

@app.route("/win")
def winGet():
    wins = int(request.cookies.get("wins"))
    winStreak = int(request.cookies.get("winStreak"))
    if request.cookies.get("playedToday") == "false":
        wins = wins + 1
        winStreak = winStreak + 1
    resp = make_response(render_template("finish.html", wins=wins, winStreak=winStreak, results="Congratulations, my trickster, you may celebrate."))
    resp.set_cookie("wins", str(wins))
    resp.set_cookie("winStreak", str(winStreak))
    resp.set_cookie("playedToday", "true")
    resp.set_cookie("results", "win")
    return resp

@app.route("/lose")
def loseGet():
    wins = int(request.cookies.get("wins"))
    winStreak = int(request.cookies.get("winStreak"))
    winStreak = 0
    resp = make_response(render_template("finish.html", wins=wins, winStreak=winStreak, results="Apologies, my trickster, you have been bested."))
    resp.set_cookie("wins", str(wins))
    resp.set_cookie("winStreak", str(winStreak))
    resp.set_cookie("playedToday", "true")
    resp.set_cookie("results", "lose")
    return resp

@app.route("/newPersona")
def guessPersona():
    persona = {}
    conn = None
    try:
        conn = sqlite3.connect("./Persona5WordleDatabase.db")
        conn.row_factory = sqlite3.Row
        sql = """
            Select Persona.Name, Persona.Arcana, Persona.Inherit, Persona.Physical, Persona.Gun, Persona.Fire, Persona.Ice, Persona.Wind, Persona.Electric, Persona.Nuclear, Persona.Psychic, Persona.Bless, Persona.Curse
            From Persona
            ORDER BY RANDOM()
            LIMIT 1
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        persona.update({"Name":row["Name"]})
        persona.update({"Arcana":row["Arcana"]})
        persona.update({"Inherit":row["Inherit"]})
        persona.update({"Physical":row["Physical"]})
        persona.update({"Gun":row["Gun"]})
        persona.update({"Fire":row["Fire"]})
        persona.update({"Ice":row["Ice"]})
        persona.update({"Wind":row["Wind"]})
        persona.update({"Electric":row["Electric"]})
        persona.update({"Psychic":row["Psychic"]})
        persona.update({"Nuclear":row["Nuclear"]})
        persona.update({"Bless":row["Bless"]})
        persona.update({"Curse":row["Curse"]})

    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)
    finally:
        if conn:
            conn.close()
    return persona

@app.route("/getPersona/<name>")
def getUserPersona(name):
    persona = {}
    try:
        conn = sqlite3.connect("./Persona5WordleDatabase.db")
        conn.row_factory = sqlite3.Row
        sql = """
            Select Persona.Name, Persona.Arcana, Persona.Inherit, Persona.Physical, Persona.Gun, Persona.Fire, Persona.Ice, Persona.Wind, Persona.Electric, Persona.Nuclear, Persona.Psychic, Persona.Bless, Persona.Curse
            From Persona
            Where Persona.Name = ?
        """
        cursor = conn.cursor()
        cursor.execute(sql, [name])
        row = cursor.fetchone()
        persona.update({"Name":row["Name"]})
        persona.update({"Arcana":row["Arcana"]})
        persona.update({"Inherit":row["Inherit"]})
        persona.update({"Physical":row["Physical"]})
        persona.update({"Gun":row["Gun"]})
        persona.update({"Fire":row["Fire"]})
        persona.update({"Ice":row["Ice"]})
        persona.update({"Wind":row["Wind"]})
        persona.update({"Electric":row["Electric"]})
        persona.update({"Psychic":row["Psychic"]})
        persona.update({"Nuclear":row["Nuclear"]})
        persona.update({"Bless":row["Bless"]})
        persona.update({"Curse":row["Curse"]})

    except Error as e:
        print(f"Error opening the database{e}")
        abort(500)
    except Error as e:
        print(f"Persona does not exist in database{e}")
        abort(200)
    finally:
        if conn:
            conn.close()
    return persona

def timeCheck(loginTime):
    loginYear = int(loginTime.split("-")[0])
    loginMonth = int(loginTime.split("-")[1])
    loginDay = int(loginTime.split("-")[2].split(" ")[0])
    
    now = datetime.now()
    nowYear = now.year
    nowMonth = now.month
    nowDay = now.day
    print(nowYear, nowMonth, nowDay)
    print(loginYear, loginMonth, loginDay)

    if nowYear != loginYear:
        return True
    elif nowMonth != loginMonth:
        return True
    elif nowDay != loginDay:
        return True
    else:
        return False