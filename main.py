from pygame import *
from random import *
class GameDobrui(sprite.Sprite):
    def __init__(self, picture, x, y, speed, widht, height):
        super().__init__()
        self.image = transform.scale(image.load(picture), (widht, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameDobrui):
    def update_l(self):
        keys_pressed = key.get_pressed()
        global a
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_s] and self.rect.y < 500 - 86:
            self.rect.y += 10

    def update_r(self):
        keys_pressed = key.get_pressed()
        global a
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_DOWN] and self.rect.y < 500 - 86:
            self.rect.y += 10


a = randint(1,500)
b = randint(1, 500)
c = randint(1, 2)


font.init()

font = font.Font(None, 40)



window = display.set_mode((500, 500))
display.set_caption('  ')
background = transform.scale(image.load('background.jpg'), (500, 500))

player1 = Player("player1.png", 50, 250, 86, 25, 80)
player2 = Player("player2.png", 400, 250, 86, 25, 80)
FPS = 300
clock = time.Clock()

ball = GameDobrui("Ball.png", 200, 250, 0, 50, 50)

game = True

win_pl_1 = font.render('Левый игрок выйграл', 1, (255,0, 105))
win_pl_2 = font.render('Правый игрок выйграл', 1, (255,0, 105))


player1_point = 0
player2_point = 0



finish = False
speed_x = 1
speed_y = 1


while game == True:
    point = font.render(str(player1_point) + ':' + str(player2_point), 1, (255, 255, 255))
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 450:
            speed_y *= -1
        if ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
            speed_x *= -1

        if ball.rect.x < 25:
            player2_point += 1
            ball.rect.x = 200
            ball.rect.y = 250

        if ball.rect.x > 425:
            player1_point += 1
            ball.rect.x = 200
            ball.rect.y = 250


        if player1_point > 5:
            finish = True
            window.blit(win_pl_1,(100, 250))

        if player2_point > 5:
            finish = True
            window.blit(win_pl_2,(100, 250))




        window.blit(point, (25, 25))
        player1.reset()
        player1.update_l()

        player2.reset()
        player2.update_r()

        ball.reset()

        clock.tick(FPS)
        display.update()