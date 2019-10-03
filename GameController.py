from flask import Flask
from pymongo import MongoClient
from flask import jsonify
from flask import abort
import datetime
from datetime import timedelta


from Domain import Board
from Service import GameService
from Util import Validator

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.local
collection = db["tiktaktoe"]
app = Flask(__name__)


@app.route("/")
def home_page():
    return "Welcome Darconf"


@app.route("/game/tiktaktoe/create/<gameId>/<player>",  methods=["POST"])
def startGame(gameId,player):
    a = [3][0]

    Obj = GameService.Game(gameId, player)

    mydict = {"gameId": Obj.getGameId(),
              "player": Obj.getPlayer(),
              "started": datetime.datetime.now(),
              "duration": None,
              "winner": "TBD",
              "board": Board.Board.emptyboard}

    collection.insert_one(mydict)
    return "Game Created, its " + player + " turn" ,201


@app.route("/game/tiktaktoe/play/<gameId>/<col>/<row>", methods=["PUT"])
def play(gameId, col, row):
    s = collection.find_one({'gameId': gameId})
    if s:
        output = s['board']
    else:
        return abort(400, 'No Such Game')
    outputBoard = Validator.Validator.gameValidator(output,int( col),int (row))

    if Validator.Validator.draw is True:
        duration = Validator.Validator.endedAt - s['started']
        collection.find_one_and_update({"gameId": gameId},
                                       {"$set": {"duration": str(duration), "winner": "Draw"}})
        return "Draw"

    Validator.Validator.isFinishValidator(output)
    collection.find_one_and_update({"gameId": gameId},
                                   {"$set": {"board": outputBoard}})
    if Validator.Validator.finish is True:
        duration = Validator.Validator.endedAt - s['started']
        print("Days " + str(duration.days) + " Hours " + str(duration.days*24) + " Minutes  " + str(duration.days*3600)
                      + " Seconds " + str(duration.seconds))
        collection.find_one_and_update({"gameId": gameId},
                                       {"$set": {"duration": str(duration), "winner": s['player']}})
        return "Player " + s['player'] + " has Win"

    if Validator.Validator.finish is True:
        duration = Validator.Validator.endedAt - s['started']
        collection.find_one_and_update({"gameId": gameId},
                                       {"$set": {"duration": str(duration),"winner":"Computer"}})
    outputBoard = Validator.Validator.computer(output)
    Validator.Validator.isFinishValidator(output)
    collection.find_one_and_update({"gameId": gameId},
                                   {"$set": {"board": outputBoard}})
    if Validator.Validator.draw is True:
        duration = Validator.Validator.endedAt - s['started']
        collection.find_one_and_update({"gameId": gameId},
                                       {"$set": {"duration": str(duration), "winner": "Draw"}})
        return "Draw"

        return "Computer has win"
    if Validator.Validator.draw is True:
        duration = Validator.Validator.endedAt - s['started']
        collection.find_one_and_update({"gameId": gameId},
                                       {"$set": {"duration": str(duration), "winner": "Draw"}})
        return "Draw"
    if Validator.Validator.ocuppedCell is True:
        return "Celda ocupada"

    return "its " + s['player'] + " turn";


@app.route("/game/tiktaktoe/history", methods=["GET"])
def getall():
    output = []
    for s in collection.find():
        output.append({'player': s['player'], 'started': s['started'],
                       'duration': s['duration'],'board': s['board'],'winner':s['winner']})
    return jsonify({'result': output})



"""
@app.route("/company/<company>")
def getbyproperty(name):
    s = mycol.find_one({'company': company})
    if s:
        output = {'company': s['company'], 'location': s['location'], 'size': s['size']}
    else:
        output = "No such company"
    return jsonify({'result': output})
"""
@app.route("/game/tiktaktoe/<player>", methods=["DELETE"])
def delperson(player):
 collection.delete_one({'player': player})
 return "borrado"


if __name__ == '__main__':
    app.run(debug=True)