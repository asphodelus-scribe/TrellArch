import boardStateDriver
from time import sleep
from board import SCL, SDA
import busio
from adafruit_neotrellis.neotrellis import NeoTrellis
i2c_bus = busio.I2C(SCL, SDA)   
theTrellis = NeoTrellis(i2c_bus)
boardDriver = boardStateDriver.boardState([(0,0,0)]*16)
for i in range(16):
    theTrellis.activate_key(i, NeoTrellis.EDGE_RISING)
    theTrellis.callbacks[i] = boardDriver.buttonPressed
while True:
    sleep(0.02)
    for i in range(len(boardDriver.theBoard)):
        theTrellis.pixels[i] = boardDriver.theBoard[i]
    theTrellis.sync()

# trellis > color > trinket
# gnd     > blk   > gnd
# int     > wht   > 3
# vin     > red   > USB
# sda     > blu   > 0 
# scl     > ylw   > 2