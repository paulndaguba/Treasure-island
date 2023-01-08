print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
#Write your code below this line 👇

direction = input("You dey cross road. Where do you wan go? Make you type left or right. \n") 
if direction == 'left' :
    options = input("You reach one lake like that. One island dey middle of the lake. You go type which one you wan do, type wait to wait for a boat or type swim to swim across \n")
    if options == 'wait' :
        door = input("You don reach the island and you never die, Thank GOD for your life. You come see one house with 3 doors. One door na red, another one na yellow the last one come be blue. Which door you go choose? \n")
        if door == 'yellow' :
            print ("Confam!!! You don Win!!!") 
        elif door == 'red':
          print("Bandits don catch you. Game Over.")
        else :
          print ("Bandits don catch you. Game Over.")
    else :
        print("Shark don chop you. Game Over.")
else :
    print ("You don fall for lagoon. Game Over.")