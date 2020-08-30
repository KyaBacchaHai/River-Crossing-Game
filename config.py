import pygame as py
from random import random
py.init()

win = py.display.set_mode((800,800))
x,y,width,height,vel,player = 50,50,30,40,5,0
min_vel,max_vel = 5, 10	#moving enemies
no_of_station_ene = 5; #static enemies
score1=0
score2=0
Moving_enemies = []
Stationary_enemies = []
font = py.font.Font('freesansbold.ttf', 19) 
score1, score2 = 0,0

def got_hit():
	win.fill((0,0,0))
	text = "got hit"
	text = font.render(text ,1,(255,255,255))
	win.blit(text, (350,400))
	py.display.update()
	py.time.delay(1000)

def succ():
	win.fill((0,0,0))
	text = "success, next level"
	text = font.render(text ,1,(255,255,255))
	win.blit(text, (350,400))
	py.display.update()
	py.time.delay(1000)
