print('''                  .--------------------------------...
               ,'-------------------------------,'   |
              /                                /     |
             /________________________________/    ,'|
             |               ..               |  ,'  |
             |___________-==/88\==-___________|,' /) |.
             |  \    \     ((  ))     /    /  |  (/  |-. .
             |   \    \     \{}/     /    /   |    .' .  .
          . '|    \    \     )(     / _  /    |    ,   .  .
         . . |\    \    \    \/    _.( ~-.   /|\ ,' .   . .
       ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
        .  `    .     .       .  ,'\. ~-  . , .  .  .   .
           .  `   .     ,   .      , ~~-.' .  .    .''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")
direction = input("Chosse between left or right :")
is_alive = True
if direction.lower() == "left":
    direction = input("Chosse between swim or wait :")
    if direction.lower() == "wait":
        direction = input("Chosse between the door (red|blue|yellow) :")
        if direction.lower() == "red":
            is_alive = False
            message = "Burned by fire"
        elif direction.lower() == "blue":
            is_alive = False
            message = "Eaten by beasts"
        elif direction.lower() == "yellow":
            print("You Win !!!")
        elif direction.lower() != "yellow" or direction.lower() != "red" or direction.lower() != "blue":
            is_alive = False
    else:
        is_alive = False
        message = "Attacked by trout"
else:
    is_alive = False
    message = "You fall into a hole"

if is_alive:
    print('''                         ,----------_____....----.--------,
                _____.....-----~~~~~             |_______/ `
               |                                 |      /  |
               |          1 0 0 0 $              |     /
               |                                  |   /   /
                |                                 | _/   /
                |            / Y E A R            |,'|~~
               ,|                                ,'  |
             ,'_|_____________________________:,' /) |.
             |  \    \                /    /  |  (/  |_. .
             |   \    \     {}       /    /   |    .' .  .
          . '|    \    \            / _  /    |    ,   .  .
         . . |\    \    \          _.( ~-.   /|\ ,' .   . .
       ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
        .  `    .     .       .  ,'\. ~-  . , .  .  .   .
           .  `   .     ,   .      , ~~-.' .  .    .''')
else:
    print('''     |     '       /  |    |             /  |
     /__      ___ (  /     /__   Y  __  (  _/
     \\--`-'-|`---\\ |     \`--`-'-|`---\\/
      |' _/   ` __/ /       |'__/   ` __/ |
      '._  W    ,--'        '-.   w   ,--/
         |_:_._/              |'_._._/  /
                              |________/''')
    print(f"Game over \n {message}")