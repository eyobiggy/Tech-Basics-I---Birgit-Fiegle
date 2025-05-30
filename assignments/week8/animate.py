import pygame
import random

pygame.init()
X = 1200
Y = 700

scrn = pygame.display.set_mode((X, Y))

scrn.fill((0,0,0))

pygame.display.set_caption('Space Cat Floating On A Sandwich')

imp = pygame.image.load("cat.webp").convert_alpha()
imp2 = pygame.image.load("cat2.png").convert_alpha()
imp2 = pygame.transform.scale(imp2, (300, 370))

imp_bg = pygame.image.load("space.jpg").convert_alpha()

clock = pygame.time.Clock()

class Background:
    def __init__(self, image):
        self.image = imp_bg

    def draw(self):
        scrn.blit(self.image, (0, 0))



class Cat:
    def __init__(self, cat_x, cat_y,speed_x, speed_y,image):
        self.cat_x = cat_x
        self.cat_y = cat_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.image = image

    def move(self):
        self.cat_x += self.speed_x
        self.cat_y += self.speed_y
        if self.cat_x > X:
            self.cat_x = 0
        if self.cat_x < -self.image.get_width():
            self.cat_x = 1200

        if self.cat_y > Y:
            self.cat_y = 0
        if self.cat_y < -self.image.get_height():
            self.cat_y = 0



    def draw(self):
        scrn.blit(self.image, (self.cat_x, self.cat_y))

class Spin:
    def __init__(self, x, y, image, size):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, size)
        self.speed = random.randint(2,20)
        self.angle = 0

    def move(self):
        self.angle += self.speed

    def draw(self, screen):
        rotated = pygame.transform.rotate(self.image, self.angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        screen.blit(rotated, rect)

cat1 = Cat(20, 20, random.randint(1,5), random.randint(1,5),imp)
cat2 = Spin(570,470, imp2, (300,300))
cat3 = Spin(230,500, imp, (120, 120))
cat4 = Cat(1000,680,random.randint(-5,-1),random.randint(1,5),imp2)

background = Background(imp_bg)

status = True
while (status):

    scrn.fill((0,0,0))

    background.draw()

    cat1.move()
    cat2.move()
    cat3.move()
    cat4.move()

    cat1.draw()
    cat2.draw(scrn)
    cat3.draw(scrn)
    cat4.draw()

    pygame.display.update()
    clock.tick(60)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False

pygame.quit()



# I used ChatGBT to:
# learn how to make images sizeable
# learn how to make an image rotate
# solve mistakes: make the cats reappear at the right spot, let them rotate at random speeds