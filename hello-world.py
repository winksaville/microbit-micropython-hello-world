from microbit import *
for i in range(1,3):
    display.scroll(i) # Display a number, the loop index
    display.scroll("HELLO WORLD 1/2 SPEED.", delay=300) # half speed scroll

display.scroll("Done!", loop=True); # loops forever scrolling at full speed "Done!"

