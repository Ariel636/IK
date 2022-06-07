import pygame
pygame.init()

win = pygame.display.set_mode((500,500))

rad = 15
a = 14
b = 14

x = 10
y = 400
width = 100
height = 10
run = True
score = 0 
score_font = pygame.font.SysFont("comicsansms", 35)
while run:
	pygame.time.delay(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	key = pygame.key.get_pressed()
	if key[pygame.K_RIGHT]:
            x+=5
	if key[pygame.K_LEFT]:
            x+=5
	if b >= 500:
		b = 0
		a = random.randint(0,500)
	b += 10
	if a >=x and a <=x+width and b ==y:
		b = 0 
		a = random.randint(0,500)
		score += 1
	win.fill((0,0,0))
	value = score_font.render("Your Score: " + str(score), True, pygame.Color("Yellow"))
	pygame.draw.circle(win,(244,233,222),(a,b),rad)
	pygame.draw.rect(win, (244,122,14), (x,y,width,height))
	win.blit(value, [0, 0])
	pygame.display.update()
