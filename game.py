from config import *

class Moving_stuff:
	def __init__(self,x,enemies_vel, crossed):
		self.x = x
		self.enemies_vel = enemies_vel
		self.crossed = crossed

class Stationary_stuff:
	def __init__(self,x,y,crossed):
		self.x = x
		self.y = y
		self.crossed = crossed

def backgrnd():
	win.fill([0,150,255])
	py.draw.rect(win, (0,0,0),(x,y,width,height))	# Charecter
	static_boxes()  #static enemies
	moving_boxes()	#moving enemies
	displayScore() 	 #score stuff
	py.display.update()

def moving_boxes():
	global Moving_enemies
	py.draw.rect(win, (0,255,0),(Moving_enemies[0].x,66,80,70))
	py.draw.rect(win, (0,255,0),(Moving_enemies[1].x,211,80,70))
	py.draw.rect(win, (0,255,0),(Moving_enemies[2].x,361,80,70))
	py.draw.rect(win, (0,255,0),(Moving_enemies[3].x,511,80,70))
	py.draw.rect(win, (0,255,0),(Moving_enemies[4].x,661,80,70))

def static_boxes():
	global Stationary_enemies
	for i in range(len(Stationary_enemies)):
		py.draw.rect(win, (255,255,0),(Stationary_enemies[i].x,Stationary_enemies[i].y,75,75))


def play():	#stuff we can change: min_vel, max_vel, no_of_station_ene, player
	global y,x,width,height,player,vel
	x = 386
	if(player%2==0):
		y = 755
	else:
		y = 0
	height=40
	width=30
	run = True

	# making moving enemies
	global Moving_enemies, min_vel, max_vel
	Moving_enemies = []
	for i in range(5):
		temp_vel = min_vel + (random()*(max_vel - min_vel))
		temp = Moving_stuff(0,temp_vel,False)
		Moving_enemies.append(temp)

	# making static enemies
	global Stationary_enemies, no_of_station_ene
	Stationary_enemies = []
	for i in range(no_of_station_ene):
		static_x = random()*(800)
		static_y = random()*(800)
		temp = Stationary_stuff(static_x, static_y,False)
		Stationary_enemies.append(temp)

	while run:
		py.time.delay(100)
		keys = py.key.get_pressed()
		# TO EXIT GAME/level
		for event in py.event.get():
		    if event.type == py.QUIT:
		        run = False
		        exit()
		# MOVEMENT OF PLAYER
		if keys[py.K_LEFT] and x > vel:
		    x -= vel
		if keys[py.K_RIGHT] and x < 800 - width - vel:
		    x += vel
		if keys[py.K_UP] and y > vel:
			y -= vel
		if keys[py.K_DOWN] and y < 800 - height - vel :
			y += vel
		# print("x: "+str(x),"y: " + str(y))
		# Moving enemies
		for i in range(5):
			if( Moving_enemies[i].x > 800 ):
				Moving_enemies[i].x %= 800
			Moving_enemies[i].x  += Moving_enemies[i].enemies_vel
		backgrnd()
		
		# detecting collsions
		# moving
		global result
		if (661-40)<y and y<(661+70) and (Moving_enemies[4].x-30)<x and x<(Moving_enemies[4].x+80):
			run = False
			result = False
		elif (511-40)<y and y<(511+70) and (Moving_enemies[3].x-30)<x and x<(Moving_enemies[3].x+80):
			run = False
			result = False
		elif (361-40)<y and y<(361+70) and (Moving_enemies[2].x-30)<x and x<(Moving_enemies[2].x+80):
			run = False
			result = False
		elif (211-40)<y and y<(211+70) and (Moving_enemies[1].x-30)<x and x<(Moving_enemies[1].x+80):
			run = False
			result = False
		elif (66-40)<y and y<(66+70) and (Moving_enemies[0].x-30)<x and x<(Moving_enemies[0].x+80):
			run = False
			result = False
		# stationary
		for enemy in Stationary_enemies:
			if (enemy.x-30)<x and x<(enemy.x+75) and (enemy.y-40)<y and y<(enemy.y+75):
				run = False
				result = False

		# scoring 
		global score,score1,score2
		score -=0.01 	#time dependence
		if player == 0 :
			# moving enemies
			if y<(661) and Moving_enemies[4].crossed==False :
				Moving_enemies[4].crossed=True
				score += 10
			if y<511 and Moving_enemies[3].crossed==False :
				Moving_enemies[3].crossed=True
				score+=10
			if y<361 and Moving_enemies[2].crossed==False :
				Moving_enemies[2].crossed=True
				score+=10
			if y<211 and Moving_enemies[1].crossed==False :
				Moving_enemies[1].crossed=True
				score+=10
			if y<66 and Moving_enemies[0].crossed==False :
				Moving_enemies[0].crossed=True
				score+=0
			# stationary
			for enemy in Stationary_enemies :
				if (enemy.y > y) and enemy.crossed==False :
					enemy.crossed = True
					score += 5
			score1 = score
			
		elif player == 1 :
			# moving enemies
			if y>(661) and Moving_enemies[4].crossed==False :
				Moving_enemies[4].crossed=True
				score += 10
			if y>511 and Moving_enemies[3].crossed==False :
				Moving_enemies[3].crossed=True
				score+=10
			if y>361 and Moving_enemies[2].crossed==False :
				Moving_enemies[2].crossed=True
				score+=10
			if y>211 and Moving_enemies[1].crossed==False :
				Moving_enemies[1].crossed=True
				score+=10
			if y>66 and Moving_enemies[0].crossed==False :
				Moving_enemies[0].crossed=True
				score+=0
			# stationary
			for enemy in Stationary_enemies :
				if (enemy.y < y) and enemy.crossed==False :
					enemy.crossed = True
					score += 5
			score2 = score
			

		# win/lose condition
		result = False
		if player%2==0 and y<=vel:
			run = False
			result = True
		elif player%2==1 and y>=(800 - height - vel):
			run = False
			result = True



def intro(): 
	global win
	white = (255, 255, 255) 
	green = (0, 255, 0) 
	blue = (0, 0, 119) 

	# create a font object. 
	# 1st parameter is the font file 
	# which is present in py. 
	# 2nd parameter is size of the font 
	global font
	font = py.font.Font('freesansbold.ttf', 19) 
	keys = py.key.get_pressed()
	# create a text suface object, 
	# on which text is drawn on it. 
	text = font.render('Press SPACE To Play:', True, green, blue)
	name_of_game = font.render('River Crossing Game', True, green, blue)
	instructions1 = font.render('The objective of the game is to cross the river collisions with any objects', True, green, blue)
	instructions2 = font.render('in the path would result in losing the instantly, there are two players in', True, green, blue)
	instructions3 = font.render('the game. The level of the game will get harder as each consequtive level is', True, green, blue)
	instructions4 = font.render('completed. First the player1 goes then the player2. The game automatically displays', True, green, blue)
	instructions5 = font.render('the respective scores once both the players lose. The scoring is based on how', True, green, blue)
	instructions6 = font.render('fast the level is completed along with how many obsticles have been crossed.', True, green, blue)
	instructions7 = font.render('On crossing the stationary obsticles you get 5 points and 10 for moving obsticles.', True, green, blue)

	# create a rectangular object for the 
	# text surface object 
	textRect = text.get_rect()
	name_of_gameRect = name_of_game.get_rect()
	instructions1Rect = instructions1.get_rect()
	instructions2Rect = instructions2.get_rect()
	instructions3Rect = instructions3.get_rect()
	instructions4Rect = instructions4.get_rect()
	instructions5Rect = instructions5.get_rect()
	instructions6Rect = instructions6.get_rect()
	instructions7Rect = instructions7.get_rect()
	# set the center of the rectangular object. 
	textRect.center = (400, 400 + 150) 
	name_of_gameRect.center = (400, 400 - 150)
	instructions1Rect.center = (400, 400 - 150 + 64)
	instructions2Rect.center = (400, 400 - 150 + 64 + 19)
	instructions3Rect.center = (400, 400 - 150 + 64 + 2*19)
	instructions4Rect.center = (400, 400 - 150 + 64 + 3*19)
	instructions5Rect.center = (400, 400 - 150 + 64 + 4*19)
	instructions6Rect.center = (400, 400 - 150 + 64 + 5*19)
	instructions7Rect.center = (400, 400 - 150 + 64 + 6*19)
	while True : 
		# completely fill the surface object 
		win.fill((0,150,255)) 
		# copying the text surface object 
		# to the display surface object 
		# at the center coordinate. 
		win.blit(text, textRect) 
		win.blit(name_of_game, name_of_gameRect)
		win.blit(instructions1, instructions1Rect)
		win.blit(instructions2, instructions2Rect)
		win.blit(instructions3, instructions3Rect)
		win.blit(instructions4, instructions4Rect)
		win.blit(instructions5, instructions5Rect)
		win.blit(instructions6, instructions6Rect)
		win.blit(instructions7, instructions7Rect)
		# iterate over the list of Event objects 
		# that was returned by py.event.get() method. 
		for event in py.event.get() :
			if event.type == py.QUIT :
				exit() 
		py.display.update()
		keys = py.key.get_pressed()
		if keys[py.K_SPACE]:
			start_game()
			break

## score
def displayScore():
	global score1, score2
	white = (255,255,255)
	text1 = font.render("Player 1: "+ str(score1), 1, white)
	text2 = font.render("Player 2: "+ str(score2), 1, white)
	win.blit(text1, (650, 50))
	win.blit(text2, (650, 100))


def start_game():
	global player,result, min_vel, max_vel, no_of_station_ene, score, font
	global score1, score2
	player = 0
	result = True
	score = 0 
	while result :
		play()
		if (result):
			succ()
		min_vel +=2
		max_vel += 3
		no_of_station_ene +=2
	score1 = score
	player,result,min_vel,max_vel,no_of_station_ene = 1,True,5,10,5
	got_hit()
	win.fill((0,0,0))
	score = 0
	text = font.render( "Player 1 was hit, Player2 will now play",1,(255,255,255))
	win.blit(text, (250,400))
	py.display.update()
	py.time.delay(2000)
	while result :
		play()
		if (result):
			succ()
		min_vel +=2
		max_vel += 3
		no_of_station_ene +=2
	score2 = score 
	got_hit()
	if( score1>score2 ):
		text = "Player 1 wins"
	elif(score2>score1):
		text = "Player 2 wins"
	else :
		text = "the game was draw"
	win.fill((0,0,0))
	text = font.render(text ,1,(255,255,255))
	win.blit(text, (350,400))
	py.display.update()
	py.time.delay(2000)


intro()