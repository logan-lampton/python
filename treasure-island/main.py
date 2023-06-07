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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Welcome to Treasure Island.")
print("\nLike so many before you, the call of treasure has brought you to this dangerous slice of paradise. Good luck finding what you seek. Otherwise, you may just find death.")

direction = input("\nYou disembark your rickety ship and walk to the treeline of palms. You notice two paths through the dense growth of palms. Do you go left or right?\n").lower()

if direction == "left":
    print("\nYou walk through the twilight of the dense forest for a while before coming to a river and on the other side a strange wooden structure. This must be where the galley of the infamous Captain Torance ended up. It now looks to have been dismantled and repurposed into a new building of some sort.") 
    swim = input("\nYou approach the river. It looks like one you're strong enough to swim across. Do you swim or wait?\n").lower()
    if swim == "wait":
      print("\nSomething raises the hairs on the back of your neck and you wait. Good thing too. A crocodile swims past where you were about to swim and it looks rather hungry.\nWhile watching the scaly creature float by, you notice a rowboat hidden in the reeds nearby. You struggle as you pull it through the sand to the river and it seems old and in bad shape. But she floats well enough to get across the river safely.\nYou disembark and find yourself at the strange remains of the ship. Something seems off about this whole building, and not just the too perfect of angles of a ramshackle structure made out of materials not for the purpose of creating a building. You get a chill staring at that forsaken jumble of wood. It's at that point that you notice three doors, each a different color. Time for a difficult choice.")
      door = input("Which door do you open? Red, blue, or yellow?\n").lower()
      if door == "red":
        print("You open the door and know that it leads to a different place than this island somehow. You see a massive star on the other side. How is this possible? You don't have long to consider it as you instantly go blind and are immolated half a second later.\nBetter luck in your next life.")
      elif door == "blue":
        print("You open the door and know that it leads to a different place than this island somehow. The door opens to a black void. You have but a moment before a vaccum caused by the void sucks you and the nearby shrubs and debris into it. You find yourself floating in space for about a minute, with nothing but your thoughts. It's so cold. So empty. You suffocate.\nBetter luck in your next life.")
      elif door == "yellow":
        print("The door swings open surprisingly easily. Inside you find a lit sterile looking room. A treasure chest is in the center of the room. Congratulations. You have found the treasure. You somehow know that everything will be okay now. Now all the debts will be paid. Now all the nightmares will end. Right? Right?\nAt any rate, you win.")
    elif swim == "swim":
      print("\nYou make it halfway across the river before a shape emerges from the water to greet you. It is a crocodile twice your size. It's lipless mouth seems to be grinning. You don't survive. \nBetter luck in your next life.")
elif direction == "right":
    print("\nYou follow the path for several minutes into an increasingly dark forest. Snap. You step on something in the gloom. You rapidly descend into what you realize is a hidden spike trap. \n'Clever, it's how you would have done it,' is the last thing you think before the jagged spears at the bottom whisk you away to oblivion.\nBetter luck in your next life.")
