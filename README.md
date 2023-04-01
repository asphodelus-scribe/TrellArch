# TrellArch
A rudimentary 16 bit variable system emulating functional code paradigms in python on an Adafruit NeoTrellis.
For a full schematic diagram of process flow and register labels, see readme.png
The NeoTrellis is a 4x4 board of buttons with controllable 8-bit color backlights on each button.
The first button pressed determines which routine to be run, and all further inputs control process flow.
If a routine has a numerical output, it will be displayed on the board by lighting up the index of button corresponding to the output
until any other button is pressed, otherwise the program returns to the command input state.
A given output x is expressed as x=16n+a where n is an integer. Only the residual value a is displayed on the board. 
Future versions will use the color of button a to indicate the factor n, allowing for an exact decoding of the output value.
Currently completed processes are: write integer to memory, read integer from memory, write contents of one memory location to another, 

