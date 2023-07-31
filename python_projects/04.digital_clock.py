from datetime import datetime
import os
import time
import keyboard

# for clearing the screen and move the curser to the top left
def clear_screen():
    #Clears the screen and moves the cursor to the top left corner.
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[0;0H", end='')

# changing terminal clor
def set_background_color(color):
    #Sets the background color of the terminal.
    print(f"\033[48;5;{color}m", end='')
# this class is for numbers 
# eache line contains the corresponding line in the digital format of the number
class Line:
    l1 = ["  ===== " ,
          " //||   " ,
          " ====   " ,
          " ====   " ,
          "   //|| " ,
          " ====== " ,
          "   //   " ,
          " ====== " ,
          "  ===== " ,
          "  ====  " ]
    l2 = [" ||   ||" ,
          "   ||   " ,
          "//  ||  " ,
          "     || " ,
          "  // || " ,
          " ||     " ,
          "  //    " ,
          "     // " ,
          " ||   ||" ,
          " ||  || " ]
    l3 = [" ||   ||" ,
          "   ||   " ,
          "    //  " ,
          " ====|| " ,
          " //  || " ,
          " ====== " ,
          "  ====  " ,
          "    //  " ,
          "  ===== " ,
          "  ====  " ]
    l4 = [" ||   ||" ,
          "   ||   " ,
          "   //   " ,
          "     || " ,
          " =======" ,
          "     || " ,
          " ||  || " ,
          "   //   " ,
          " ||   ||" ,
          "    //  " ]
    l5 = ["  ===== " ,
          " ====== " ,
          "  ===== " ,
          " ====   " ,
          "     || " ,
          " ====== " ,
          "  ====  " ,
          " =====  " ,
          "  ===== " ,
          "   //   " ]

set_background_color(30)
# starting program and run it in an endless loop
while True:
    # getting time for now
    now = datetime.now()
    # clear the screen
    clear_screen()
    #seperating and printting each digit of the clock
    print("*******************************************************************")
    print("* " , Line.l1[int(now.hour/10)] , Line.l1[now.hour%10] , "   " , Line.l1[int(now.minute/10)] , Line.l1[now.minute%10] , "   " , Line.l1[int(now.second/10)] , Line.l1[now.second%10] , " *")
    print("* " , Line.l2[int(now.hour/10)] , Line.l2[now.hour%10] , " @ " , Line.l2[int(now.minute/10)] , Line.l2[now.minute%10] , " @ " , Line.l2[int(now.second/10)] , Line.l2[now.second%10] , " *")
    print("* " , Line.l3[int(now.hour/10)] , Line.l3[now.hour%10] , "   " , Line.l3[int(now.minute/10)] , Line.l3[now.minute%10] , "   " , Line.l3[int(now.second/10)] , Line.l3[now.second%10] , " *")
    print("* " , Line.l4[int(now.hour/10)] , Line.l4[now.hour%10] , " @ " , Line.l4[int(now.minute/10)] , Line.l4[now.minute%10] , " @ " , Line.l4[int(now.second/10)] , Line.l4[now.second%10] , " *")
    print("* " , Line.l5[int(now.hour/10)] , Line.l5[now.hour%10] , "   " , Line.l5[int(now.minute/10)] , Line.l5[now.minute%10] , "   " , Line.l5[int(now.second/10)] , Line.l5[now.second%10] , " *")
    print("*******************************************************************")
    print("Enter 'q' to quit : ")
    #to quit the program
    if keyboard.is_pressed("q"):
        break
    # break and then refresh
    time.sleep(.5)
    
