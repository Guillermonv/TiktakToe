import  datetime
from random import randrange

class Validator:

    finish = False
    endedAt = None
    ocuppedCell = False
    draw = False
    def gameValidator(self, row, col):
        obj = self
        if ((obj[row][col] == 'X') or(obj[row][col] == 'O')):
            Validator.ocuppedCell = True
        else:
            Validator.ocuppedCell = False
            obj[row][col] = 'X'
        return obj;

    def computer(self):
        obj = self
        row = 0
        col = 0
        if Validator.finish is not True:
            while (obj[col][row] == 'O') or (obj[col][row] == 'X'):
                row = randrange(3)
                col = randrange(3)
        print("computer is here")
        obj[col][row] = 'O'
        return obj

    def drawValidate(self):
        obj = self
        if ((obj[0][0] == 'O' or obj[0][0] == 'X') and
            (obj[0][1] == 'O' or obj[0][1] == 'X') and
            (obj[0][2] == 'O' or obj[0][2] == 'X') and
            (obj[1][0] == 'O' or obj[1][0] == 'X') and
            (obj[1][1] == 'O' or obj[1][1] == 'X') and
            (obj[1][2] == 'O' or obj[1][2] == 'X') and
            (obj[2][0] == 'O' or obj[2][0] == 'X') and
            (obj[2][1] == 'O' or obj[2][1] == 'X') and
            (obj[2][2] == 'O' or obj[2][2] == 'X')):
            Validator.draw = True
        else:
            Validator.draw = False


    def isFinishValidator(self):
        obj = self
        print(obj)
        if((obj[0][0] == 'X' and obj[0][1] == 'X' and obj[0][2] == 'X')or
           (obj[1][0] == 'X' and obj[1][1] == 'X' and obj[1][2] == 'X')or
           (obj[2][0] == 'X' and obj[2][1] == 'X' and obj[2][2] == 'X')or
           (obj[0][0] == 'X' and obj[1][0] == 'X' and obj[2][0] == 'X')or
           (obj[0][1] == 'X' and obj[1][1] == 'X' and obj[2][1] == 'X')or
           (obj[0][2] == 'X' and obj[1][2] == 'X' and obj[2][2] == 'X')or
           (obj[0][0] == 'O' and obj[1][0] == 'O' and obj[2][0] == 'O')or
           (obj[1][0] == 'O' and obj[1][1] == 'O' and obj[2][1] == 'O')or
           (obj[0][2] == 'O' and obj[1][2] == 'O' and obj[2][2] == 'O')or
           (obj[0][0] == '0' and obj[0][1] == '0' and obj[0][2] == 'O')or
           (obj[1][0] == '0' and obj[1][1] == '0' and obj[1][2] == 'O')or
           (obj[2][0] == 'O' and obj[2][1] == 'O' and obj[2][2] == 'O')or
           (obj[0][0] == 'O' and obj[1][1] == 'O' and obj[2][2] == 'O')or
           (obj[0][0] == 'X' and obj[1][1] == 'X' and obj[2][2] == 'X')):
            Validator.finish = True
            Validator.endedAt = datetime.datetime.now()
        else:
            Validator.finish = False
        return self

    def isFinish(self):
      return self.finish

    def getEndedAt(self):
        return self.finish