# Python Project for Team Discovery Channel: Matthew Everett, Kevin Jeffers, Tait Loughridge, Katy Sage
#
from drivers import Driver_1, Driver_2, Driver_3, Driver_4
from karts import Standard_kart, Mushmellow_kart, Powerflower_kart, Drybomber_kart, Kart
from tracks import Track_1, Track_2, Track_3, Track_4, Tracks
from players import Players
from gameplay_functions import print_player_ranks, set_starting_line, set_finish_order
from track_events import change_ranks, catastrophic, bad, neutral, good, catastrophic_first, bad_first, neutral_first, good_outcomes, bad_outcomes, neutral_outcomes, catastrophic_outcomes, go_around_track
import random

print("""
Welcome to Definitely NOT Mario Kart

  ___
    _-_-  _/\______\\__
 _-_-__  / ,-. -|-  ,-.`-.
    _-_- `( o )----( o )-'
           `-'      `-'

A text-based racing game.

Choose your driver and get racing!""")

player1 = Players(1)

game_menu = """
    1: Pick a Driver
    2: Pick a Kart
    3: View your selections
    4: RACE!!!
    5: Exit
    """

# GAME MENU AND FUNCTIONS--------------------------------------------------------------------------

kart_menu = ("""
    1: Standard:      
            Speed: 6.5, Handling: 4
    2: Mushmellow:    
            Speed: 4.3, Handling: 6.9
    3: Powerflower:   
            Speed: 6.7, Handling: 4.3
    4: Dry Bomber:    
            Speed: 3.4, Handling: 9.8""")

driver_menu = ("""
    1: Veteran:   
            Speed: 5,  Knowledge: 10,  Alertness: 5
    2: Crafty:    
            Speed: 0,  Knowledge: 10,  Alertness: 10
    3: Cavalier:  
            Speed: 10,  Knowledge: 0,  Alertness: 5
    4: Joe:       
            Speed: 5,  Knowledge: 5,  Alertness: 5""")

track_menu = ("""
    1: Suzuka:    
            Difficulty: 3, Weather: 0, Speed: 8, Handling: 8
    2: Fuji:      
            Difficulty: 5, Weather: 8, Speed: 4, Handling: 3
    3: Inagawa:   
            Difficulty: 8, Weather: 5, Speed: 3, Handling: 5
    4: Tsukuba:   
            Difficulty: 9, Weather: 0, Speed: 7, Handling: 4""")

def game_startmenu():
    while True:
        print(game_menu)
        menu_choice = int(input("Please choose an option: "))
        if menu_choice == 1:
            print(driver_menu)
            driver_choice = int(input("Please choose an option: "))
            if driver_choice == 1:
                players_driver = Driver_1("Veteran", 5, 10, 5, 5)
            if driver_choice == 2:
                players_driver = Driver_2("Crafty", 0, 10, 10, 10)
            if driver_choice == 3:
                players_driver = Driver_3("Cavalier", 10, 0, 5, 5)
            if driver_choice == 4:
                players_driver = Driver_4("Joe", 5, 5, 5, 5)
        if menu_choice == 2:
            print(kart_menu)
            kart_choice = int(input("Please choose an option: "))
            if kart_choice == 1:
                players_kart = Standard_kart("Standard", 6.5, 4, 9, 6.5)
            if kart_choice == 2:
                players_kart = Mushmellow_kart("Mushmellow", 4.3, 6.9, 6.9, 8.7)
            if kart_choice == 3:
                players_kart = Powerflower_kart("Powerflower", 6.7, 4.3, 9, 8.7)
            if kart_choice == 4:
                players_kart = Drybomber_kart("Dry Bomber", 3.4, 9.8, 3.9, 9.5)
        # if menu_choice == 3:
        #     print(track_menu)
        #     track_choice = int(input("Please choose an option: "))
        #     if track_choice == 1:
        #         players_track = Track_1("Suzuka", 3, 0, 8, 8)
        #     if track_choice == 2:
        #         players_track = Track_2("Fuji", 5, 8, 4, 3)
        #     if track_choice == 3:
        #         players_track = Track_3("Inagawa", 8, 5, 3, 5)
        #     if track_choice == 4:
        #         players_track = Track_4("Tsukuba", 9, 0, 7, 4)
        if menu_choice == 3:
            print(players_driver.stats())
            print(players_kart.stats())
            # print(players_track.stats())
        if menu_choice == 4:
            game(players_driver, players_kart, player1)
        if menu_choice == 5:
            exit_prompt = input("Are you sure you want to quit? All game data will be lost. (Y or N): ").upper()
            if exit_prompt == "Y":
                break
            elif exit_prompt == "N":
                pass
            else:
                print("That was not a valid choice. Try again. ")
                exit_prompt = input("Are you sure you want to quit? All game data will be lost. (Y or N): ").upper()

# GAME AND GAME FUNCTIONS BELOW HERE---------------------------------------------------------------

# create functions for each track to order events
# laps(tracks(track_events))
def game(players_driver, players_kart, player1):
    print("""
    Welcome to Suzuka!! 
    """)
    set_starting_line(players_driver, players_kart, player1)
    # set lap count based on user input
    lap_count = int(input("How many laps would you like to race? \n"))
    if lap_count == 0:
        print("That's no fun! Please enter a number over 1 and under 100.")
    elif lap_count >= 100:
        print("Whoa, that's a little far! Let's take it easy at first. Please enter a number between 1 and 100.")
    else:
        pass
    # loop game for length of lap count
    laps = 1
    while laps != (lap_count + 1):
        if laps == lap_count:
            input("Ready for the next lap? <Enter to continue>\n")
            print("Final Lap!!!\n")
            go_around_track(player1)
            laps += 1
            input("Ready to see your final results? <Enter to continue>")
        elif laps < lap_count:
            input("Ready for the lap? <Enter to continue>\n")
            print("Lap %d!!\n" % laps)
            go_around_track(player1)
            laps += 1
        else:
            pass
    print("""\nFINISH!!
                          .oo`             :y/`                            
                   ```.:+syyy+            .yyyyo/-.``                      
       ``.--:///////::+yyyyyyy:          `syyyyyyy:::////+/::-..``         
   `.://:syyyyys.     `syyyyyyy.         +yyyyyyy/      /yyyyyy+://-.`     
  :+:.   :yyyyyyo`     -yso/-.ss`       :y/.:+syo`     -yyyyyys`  `./o`    
  -o`     +ysssoo::://+o+`    -y+      .yo`   `-s++/::-+ossssy.     :o`    
   /+ `.:+s:``   `oyyyyyy:     +h:    `oy.    `oyyyyyy-    `.+o/-` .s.     
   `o+oyyyys`     .syyyyys.`.-+syy.   /yyo/-``/yyyyyy+      :yyyys+o:      
    .syyyyyy+```..-+o+//:--oyyyyyyo` -yyyyyyy/-:://+o:...``.syyyyyy/       
     -yyyso/-/ssyyyy/      /yyyyyyy/.syyyyyys.     `syyyyso-:/oyyyo`       
      /s-`   `syyyyyy-     `oyyso:+ysy:+oyyy:`     +yyyyyy/   `./y.        
      `o:     -yyyyyyo::://::-.`  `sy/  ``-::://::/syyyyyo`     o:         
       .s.`-:///:-..`````         -yyo`         ````..--://::. /+          
        -+/-``                   `ss:y/                    `.:+o`          
         `                       oy. +y-                                   
                                /y:  `ss.                                  
                               -y+    .yo`                                 
                              `ss`     :y/                                 
                              `:.       --                                                                                                         
\n""")
    if player1.rank == 1:
        print("Congrats! You WON!!")
    elif player1.rank == 2:
        print("Second: Not great, not horrible.")
    elif player1.rank == 3:
        print("Third: try harder.")
    elif player1.rank == 4:
        print("Fourth ... oof.")
    set_finish_order()

    play_again = input("Would you like to play again? (Y or N) ").upper()
    if play_again == "Y":
        pass
    elif play_again == "N":
        quit()
    else:
        print("That was not a valid choice. Try again. ")

game_startmenu()