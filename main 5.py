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




choice = input("Would you like to make a left or a right?")

if (choice == "right"):
   print("You have fallen into a pit. Game Over!")
#insert art
elif (choice =="left"):
   print("...You have reached a river.")
  
   print('''
                   _.._
   _________....-~    ~-.______
~~~                            ~~~~-----...___________..--------
                                           |   |     |
                                           | |   |  ||
                                           |  |  |   |
                                           |'. .' .`.|
___________________________________________|0oOO0oO0o|____________
 -          -         -       -      -    / '  '. ` ` \    -    -
      --                  --       --   /    '  . `   ` \    --
---            ---          ---       /  '                \ ---
     ----               ----        /       ' ' .    ` `    \  ----
-----         -----         ----- /   '   '        `      `   \
     .-~~-.          ------     /          '    . `     `    `  \
    (_^..^_)-------           /  '    '      '      `
Lester||||AMC       --------/     '     '   '
''')
choice2 = input("\nWould you like to swim across the river or wait for the tide to lower? swim or wait?\n")

if (choice2 == "swim"):
  print("\nYou have been attacked by pirranahs. Game Over!\n")

  print('''
*******************************************************************************
    
        ,---,
  _    _,-'    `--,
 ( `-,'            `\
  \           ,    o \
  /   ,       ;       \
 (_,-' \       `, _  ""/
     pb `-,___ =='__,-'
              ````

 
 *******************************************************************************
 ''')


elif (choice2 == "wait"):
  print("\nYou have reached three doors!\n")

choice3 = input("\nIn front of you are: a pink door, a green door, and a blue door. Which door would you like to enter?\n")

if (choice3 == "blue"):
  print("...YOU HAVE FOUND THE HIDDEN TREASURE! YOU WIN!!!")
elif (choice3 == "green"):
  print("Youve been attacked by hungry beasts!! Game Over!!")
  print('''
                
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
  ''')
elif (choice3 == "pink"):
  print(" Youve been burned by fire! Game Over!!")
  print('''
         (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''') 
else:
  print("GAME OVER!!!")