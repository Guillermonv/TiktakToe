

class Game():

    def __init__(self, gameId, player, player2=None, started=None, duration=None, winner=None, board=None):
        self.gameId = gameId;
        self.player = player
        self.player2 = player2
        self.started = started
        self.duration= duration
        self.winner= winner
        self.board= board

    def getGameId(self):
     return (self.gameId)

    def setGameId(self, gameId):
        self.gameId = gameId

    def getPlayer(self):
     return self.player

     def setPlayer(self,player):
       self.player= player

    def getPlayer2(self):
     return self.player2

     def setPlayer(self,player2):
       self.player2= player2