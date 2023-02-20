import logicStateDriver
from time import monotonic
class boardState():
    def __init__(self, theBoard):
        self.theBoard = theBoard
        self.logicDriver = logicStateDriver.logicState()
        self.timePressed = monotonic()
    def debounce(self):
        if monotonic() - self.timePressed > 0.2:
            return True
        else:
            return False 
    def buttonPressed(self, event):
        if self.debounce():
            self.logicDriver.parseInput(event.number)
        self.timePressed = monotonic()    
