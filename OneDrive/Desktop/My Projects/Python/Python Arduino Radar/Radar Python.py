import pygame

import serial

import os

import math



GREEN = (0,255,0)

DORG = (0, 100, 0)

DARR = (100,0,0)

RED = (255,0,0)

BLUE = (0,0,255)



while True:

	try:

		ser = serial.Serial('COM3', 9600)

		break

	except:

		print("ERROR. NO CONNECTION MADE.")

		os.system('pause')



pygame.init()



size = (900, 700)

gameDisplay = pygame.display.set_mode(size)

pygame.display.set_caption("UltraBoi")



quit = False



def calcPoints(radius, angle):



	x = math.cos(math.radians(angle)) * radius

	y = math.sin(math.radians(angle)) * radius



	return (x,y)





listoflines = []



listofgreen = []

listofred = []



listoflines.append(((50, 600), (850, 600)))

for i in range(12):

	j = i + 1

	ang = j * 15

	x, y = calcPoints(400, ang)

	listoflines.append(((450 - x, 600 - y), (450, 600)))



def draw(pos, distance):



	gameDisplay.fill((0,0,0))



	for line in listoflines:

		pygame.draw.line(gameDisplay, GREEN, line[0], line[1])



	for line in listofgreen:

		pygame.draw.line(gameDisplay, DORG, line[0], line[1])

		line[2] -= 1



		if line[2] < 0:

			listofgreen.remove(line)



	for line in listofred:

		pygame.draw.line(gameDisplay, DARR, line[0], line[1])

		line[2] -= 1



		if line[2] < 0:

			listofred.remove(line)



	if distance * 6 > 400:

		distance = 66



	x1, y1 = calcPoints(400, 180 - pos)

	x2, y2 = calcPoints(distance * 6, 180 - pos)

	pygame.draw.line(gameDisplay, GREEN, (450, 600), (450 - x2, 600 - y2))

	

	pygame.draw.line(gameDisplay, RED, (450 - x1, 600 - y1), (450 - x2, 600 - y2))



	listofgreen.append([(450, 600), (450 - x2, 600 - y2), 360])



	listofred.append([(450 - x1, 600 - y1), (450 - x2, 600 - y2), 360])



while quit == False:



	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			quit = True



	rawdata = ser.readline()

	distance = int(rawdata.decode('utf-8').split(' ')[0])

	pos = int(rawdata.decode('utf-8').split(' ')[1])



	print(distance)



	draw(pos, distance)



	pygame.display.update()
