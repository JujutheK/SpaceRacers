------------------------------------------------------------------
TO DO

+ Spaceship scaling needs to be better
------------------------------------------------------------------
Hi there, Hey there, Ho there! Welcome to SPACERACERS

This game started of with me thinking: Hey Julian, how cool would it be if I can programme a 2D solar system using real physics? And on top of that, how epic would it be if I can make satellite transfers within this solar system fun? 

This was with me conciously choosing to ignore any challenges associated the n-th body problem, and just giving it my good ol' best shot. Because hey, 2D is makes everything easier amiright? 

Well the end result is SpaceRacers, a two player game where both of you race against time to collect as many resources as possible within one terran year (or before the n-th body problem causes everything to go ass up) so that your nation can come out on top of earths resource scarcity. 


You control your ship using :
---------------------------------------------------
Player1 / Player2

key.W / key.UP = Accelerate

Key.S / key.DOWN = Accelerate backwards

Key.A / Key.LEFT = turn left

Key.D / Key.RIGHT = right turn

(Key.LSHIFT / Key.RSHIFT = Shoot)

---------------------------------------------------


Sounds Fun? Awesome!


 Let me take you through the file structure so you get a general overview of what is what (for breivity sake I ommit the SpaceRacers at the start of each line):

main: The game loop, game menu and interactions. Pretty basic code used to combine and call the other files.

physics: the physical formulas and constants as well as some generic settings. Mess around and find out. (Please don't, it will break the programme)

Objects: Data of all objects on the screen, includes planets, the sun, the spaceships and any collectables. I made this seperate so that I don't have to go into the physics file again, where everything is a bit, ergh how to say... finicky



Disclaimer: 
Boy oh boy was the camera a pain in my underside. Literal, espresso->depresso. I'll be honest, I used a lot of online sources and GPT to get that to work, and still spend days on it. Wasn't fun, can't recommend, but I wanted/needed it to work, since otherwise youd be staring a black screen with 8 colored pixels. Try and figure out where the spaceship is currently pointing when its got the size of a pixel (possible by thrusting into a direction). 
If I havent implement a panning lock(ie the camera cant move beyond a certain point) its probably because as hard as I tried, I didnt understand the logic.
If there is no second player, its because of the camera. Honestly, **** the camera. 