####INTRODUCTION####
This python program will transform any set of alphanumeric characters into a set of Morse signals from a GUI.
With the help of an arduino and a circuit, the Morse signals are then showned through a speaker, whose volume is controled by a potentiometer, and a LED.

-->I use the word "code" as a synonym of (0, 1, 3, 5) which corresponds to (idle time, dash, dot, space).<--


####PYTHON CODE####	
1.GUI
	Although this was the final step, I'll start off with it for the sake of clarity.
	
	The user interface is a pop-up window, with a background image of the portuguese navy, and two inputs: "stream" - the string the user wants to code, 		and "com" - the com port that the user wants use off their arduino: i.e. if the user wants to use the port 9 then it should write "com9".
	The inputs then are processed by a function, with the very creative name of process(). 

 
2.Processing user input
	In the process() function, we call Alpha and Morse lists, which contain the alphanumeric elements and each element code respectively.
	len(Morse)=len(Alpha)
	We compare the values inserted by the user with the Alpha list, and for each match we use that same index to search for the respective code.
	The output is a list where each element is a code. Which, in turn, is sent over to the "data" variable in the .ino file.
	

####ARDUINO####
The .ino code has to be inside a folder with the same name.
The delay() function defines each code as a multiple of 1 = 1milisecond.
By default, the LED is connected to pin 13 and this is unchangeble in the GUI.

####PROJECTING THE CIRCUIT####
After the circuit schematic was designed, we use the softwares:  
	EAGLE 5.0.0 - to design the schematic and pcb boards
	5Spice - to simulate said circuit
While designing the PCB, use higher number of wires as the lower layer of the board that have fabricated runways.
(This way we reduce the amount of necessary wires in the upper layer - taking a leap of faith that the lower layers will most definitly work. 
There was a small conection between two lines next to each other in the upper layer, so we short-circuited it with the alloy in the lower layer.

The Arduino signal sends a maximum voltage of 5V, which, with a small resistance is good enough to power the LED.
Nevertheless, we need to use a power transistor to increase the current in speaker branch.

In figure[1] we see a schematic of the circuit. Or rather, the two independent circuits.
	R1 = 1kohms
	R2 = 1kohms
	R3 = 100ohms
	Q1 = 2SC1306
	D1 = 5mm, your favorite colour
	SP1 = any speaker with low resistance

In figure[2] T1 = Q1, from bottom to top we have the base, collector and emitter.

Since we are dealing with square waves, all that can be output to the speaker are pulses.

####WELDING/BREADBOARD####
After the circuit was design we implement it using PCB boards were used in this case but you can use breadboards aswell. 
If you are feeling ambitious you can go and buy a PCB board on your favorite electronics store.
I hereby declare that I'll not be held responsible if any kind of injury happens! 
Be wise with your welding iron. 
As expected it was used a lead and tin alloy.


####HOW TO ASSEMBLY####
On figure[2] we can see there are two jumpers: 
	JP2 is where we connect the ends of the speaker; 
	JP1:
		Top Left: 5V from the Arduino
		Top Right: Arduino Port in the pin 13
		Bottom Left: GND
		Bottom Right: Arduino Port of your choosing from GUI




 