Hi there, Hey there, Ho there! Welcome to SPACERACERS

This game started of with me thinking: Hey Julian, how cool would it be if I can programme a 2D solar system using real physics? And on top of that, how epic would it be if I can make satellite transfers within this solar system fun? 

This was with me conciously choosing to ignore any challenges associated the n-th body problem, and just giving it my good ol' best shot. Because hey, 2D is makes everything easier amiright? 

Well the end result is SpaceRacers, a two player game where both of you race against time to collect as many resources as possible within one terran year (or before the n-th body problem causes everything to go ass up) so that your nation can come out on top of earths resource scarcity. 


You control your ship using:
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


