import sqlite3
from sqlite3 import Error

from flask import Flask
from flask import abort
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("background.html")
if __name__ == '__main__':
   app.run()

@app.route("/login")
def login():
    conn = None
    try:
        conn = sqlite3.connect("./Persona5WordleDatabase.db")
        conn.row_factory = sqlite3.Row
        sql = """
            Select User.Username, User.Password
            From User
        """
    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)

@app.route("/signin", methods = ["POST"])
def signin(username, password):
    conn = None
    try:
        conn = sqlite3.connect("./Persona5WordleDatabase.db")
        conn.row_factory = sqlite3.Row
        sql = """
            Select User.Username, User.Password
            From User
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        if username == {"Username":row["Username"]}:
            abort(1000)
        elif password == {"Password":row["Password"]}:
            abort(1000)
        
        


    except Error as e:
        print(f"Error opening the database {e}")
        abort(500)

@app.route("/newPersona")
def guessPersona():
    persona = {}
    conn = None
    try:
        conn = sqlite3.connect("./Persona5WordleDatabase.db")
        conn.row_factory = sqlite3.Row
        sql = """
            Select Persona.Name, Persona.Arcana, Persona.Inherit, Elements.Physical, Elements.Gun, Elements.Fire, Elements.Ice, Elements.Wind, Elements.Electric, Elements.Nuclear, Elements.Psychic, Elements.Bless, Elements.Curse
            From Persona, Elements
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
            Select Persona.Name, Persona.Arcana, Persona.Inherit, Elements.Physical, Elements.Gun, Elements.Fire, Elements.Ice, Elements.Wind, Elements.Electric, Elements.Nuclear, Elements.Psychic, Elements.Bless, Elements.Curse
            From Persona, Elements
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
        print(f"Persona doesn't exist {e}")
        abort(500)
    finally:
        if conn:
            conn.close()
    return persona
