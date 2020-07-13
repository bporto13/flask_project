# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import get_player_info
from model import get_player_team
from model import get_player_home
from model import get_player_number
from model import get_player_position 
from model import get_player_gif
from datetime import datetime


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/') 
@app.route('/home')
def index():
    return render_template("home.html", time=datetime.now())

@app.route('/results', methods=['GET','POST'])
def results():
    if request.method == "POST":
        # print(request.form["player"])
        player_name = request.form["player"]
        player_status = request.form["status"]
        stat1Choice = request.form["box1"]
        stat2Choice = request.form["box2"]
        stat3Choice = request.form["box3"]
        player_info = get_player_info(player_status,player_name,)
        player_team = get_player_team(player_info,stat1Choice, stat2Choice,stat3Choice)
        player_jersey = get_player_number(player_info,stat1Choice, stat2Choice,stat3Choice)
        player_born = get_player_home(player_info,stat1Choice, stat2Choice,stat3Choice)
        player_position = get_player_position(player_info, stat1Choice, stat2Choice,stat3Choice)
        player_gif = get_player_gif(player_info)
       

        return render_template("results.html", time=datetime.now(), player_info=player_info, player_status = player_status,player_team=player_team, player_jersey=player_jersey, player_born = player_born, player_position = player_position, player_gif=player_gif)
    else:
        return "ERROR"
