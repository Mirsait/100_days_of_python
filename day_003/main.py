print('''
                                   ___
                               ,-""   `.
                             ,'  _   e )`-._
                            /  ,' `-._<.===-'
                           /  /
                          /  ;
              _          /   ;
 (`._    _.-"" ""--..__,'    |
 <_  `-""                     \
  <`-                          :
   (__   <__.                  ;
     `-.   '-.__.      _.'    /
        \      `-.__,-'    _,'
         `._    ,    /__,-'
            ""._\__,'< <____
                 | |  `----.`.
                 | |        \ `.
                 ; |___      \-``
                 \   --<
                  `.`.<
             hjw    `-'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
is_win = False
direction = input("Where do you wanna go? Left of Right?\n").lower()
if direction == "left":

    action = input("You went to river. You can wait the boot or swim across. Swim or Wait?\n").lower()
    if action == "wait":
        print("You waited the boot and went across the river.")

        color = input("You see three big doors. Yellow, Blue and Red. Which door?\n").lower()
        if color == "yellow":
            is_win = True

if is_win:
    print("You win!")
else:
    print("Game over!")


