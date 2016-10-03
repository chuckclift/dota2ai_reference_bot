from flask import Flask
from app import app
import json

app = Flask(__name__)



@app.route("/")
@app.route("/index")
def index():
    data = """
<a href="/Dota2AIService/api/service/reset">reset</a><br>
<a href="/Dota2AIService/api/service/select">select</a><br>
<a href="/Dota2AIService/api/service/chat">chat</a><br>
<a href="/Dota2AIService/api/service/levelup">levelup</a><br>
<a href="/Dota2AIService/api/service/update">update</a>
"""
    return data 

@app.route("/Dota2AIService/api/service/test", methods=['POST'])
def test():
    return "reset"

@app.route("/Dota2AIService/api/service/reset", methods=['POST'])
def reset():
    return ""

@app.route("/Dota2AIService/api/service/select", methods=['POST'])
def select():
    return json.dumps({"hero":"npc_dota_hero_lina","command":"SELECT"}) 

@app.route("/Dota2AIService/api/service/chat", methods=['POST'])
def chat():
    return """ {"teamOnly":false,"text":"Humans are n00bs!","player":5}  """

@app.route("/Dota2AIService/api/service/levelup", methods=['POST'])
def levelup():
    return json.dumps({"abilityIndex":0} )

@app.route("/Dota2AIService/api/service/update", methods=['POST'])
def update():
    return move(4000, 4000) # json.dumps({ "x" : "4000", "y" : "4000", "z" : "380", "command" : "MOVE"})



##
##  Functions for generating the return values
##
def noop():
    return json.dumps({ "command" : "NOOP" })

def move(x, y):
    return json.dumps({ "x" : x, "y" : y, "z" : "380", "command" : "MOVE"})

def attack(target):
    return json.dumps({ "target" : target , "command" : "ATTACK"})

def aoe_spell(x, y, ability):
    return json.dumps({ "command" : "CAST" , "ability" : ability , "x": x, "y": y , "z" : "380"})
    
def target_spell( ability, target):
    return json.dumps({ "command":"CAST" , "ability" : ability, "target" : target})

def buy(item_name):
    return json.dumps({ "command" : "BUY" , 
                        "item" : item_name})

def sell(slot_number):
        return json.dumps({ "command" : "SELL", "slot" : slot_number })

def use(item_slot):
    return json.dumps({ "command" : "USE_ITEM" , "slot" : item_slot})
    
if __name__ == "__main__":
    app.run(debug=True, port=8080)
