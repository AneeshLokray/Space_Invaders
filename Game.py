import pygame
from pygame import mixer
from pygame.locals import *
import random
import json
import os  

pygame.mixer.pre_init(44100, -16, 2, 512) 
mixer.init()
pygame.init()


clock = pygame.time.Clock()
fps = 60
scores = {}

screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')


font30 = pygame.font.SysFont('Constantia', 30)
font40 = pygame.font.SysFont('Constantia', 40)
font20 = pygame.font.SysFont('Constantia', 20)
font60 = pygame.font.SysFont('Constantia', 60)

explosion_fx = pygame.mixer.Sound("img/explosion.wav")
explosion_fx.set_volume(0.25)

explosion2_fx = pygame.mixer.Sound("img/explosion2.wav")
explosion2_fx.set_volume(0.25)

laser_fx = pygame.mixer.Sound("img/laser.wav")
laser_fx.set_volume(0.25)


rows = 5
cols = 5
alien_cooldown = 1000  
last_alien_shot = pygame.time.get_ticks()
countdown = 3
last_count = pygame.time.get_ticks()
game_over = 0  
score = 0
username = ""  


red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
black = (0, 0, 0)


bg = pygame.image.load("img/bg.png")

def draw_bg():
    screen.blit(bg, (0, 0))


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_start = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        
        speed = 8

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += speed


        if key[pygame.K_SPACE] and pygame.time.get_ticks() - self.last_shot > 500:
            laser_fx.play()
            bullet = Bullets(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.last_shot = pygame.time.get_ticks()

    
        self.mask = pygame.mask.from_surface(self.image)

        pygame.draw.rect(screen, red, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
        if self.health_remaining > 0:
            pygame.draw.rect(screen, green, (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.health_start)), 15))
        elif self.health_remaining <= 0:
            explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
            explosion_group.add(explosion)
            self.kill()
            return -1

        return 0



class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, alien_group, True):
            self.kill()
            explosion_fx.play()
            explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
            explosion_group.add(explosion)
            global score
            score += 10  
            if score % 100 == 0:  
                spaceship.health_remaining = min(spaceship.health_remaining + 1, spaceship.health_start)


class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/alien" + str(random.randint(1, 5)) + ".png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_counter = 0
        self.move_direction = 1

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 75:
            self.move_direction *= -1
            self.move_counter *= self.move_direction


class Alien_Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/alien_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y += 2
        if self.rect.top > screen_height:
            self.kill()
        if pygame.sprite.spritecollide(self, spaceship_group, False, pygame.sprite.collide_mask):
            self.kill()
            explosion2_fx.play()
            spaceship.health_remaining -= 1
            explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
            explosion_group.add(explosion)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 6):
            img = pygame.image.load(f"img/exp{num}.png")
            if size == 1:
                img = pygame.transform.scale(img, (20, 20))
            if size == 2:
                img = pygame.transform.scale(img, (40, 40))
            if size == 3:
                img = pygame.transform.scale(img, (160, 160))
            
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

    def update(self):
        explosion_speed = 3
        
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()


spaceship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()

def create_aliens():   
    for row in range(rows):
        for item in range(cols):
            alien = Aliens(100 + item * 100, 100 + row * 70)
            alien_group.add(alien)

create_aliens()


spaceship = Spaceship(int(screen_width / 2), screen_height - 100, 5)
spaceship_group.add(spaceship)

pygame.mixer.music.load("img/stranger_things.mp3")
pygame.mixer.music.play(-1)  


username_entered = False
while not username_entered:
    screen.fill((0, 0, 0))  
    draw_text("Enter Your Username:", font30, white, 150, 300)
    
    username_rendered = font30.render(username, True, white)
    screen.blit(username_rendered, (150, 350))

    pygame.display.update()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                username_entered = True
            elif event.key == pygame.K_BACKSPACE:
                username = username[:-1]
            else:
                username += event.unicode

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text, text_color, button_color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(button_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.SysFont('Arial', 30)

    def draw(self, screen):
        pygame.draw.rect(screen, white, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


def play_again():
    global game_over, score, spaceship
    game_over = 0
    score = 0
    spaceship.health_remaining = spaceship.health_start
    spaceship = Spaceship(int(screen_width / 2), screen_height - 100, 3)
    spaceship_group.empty()  
    spaceship_group.add(spaceship)  
    alien_group.empty()  
    alien_bullet_group.empty()  
    bullet_group.empty()  
    create_aliens()
   
    save_high_scores(scores)

def quit_game():
    global run
    run = False
    
    save_high_scores(scores)


play_again_button = Button(screen_width // 2 - 100, screen_height // 2 + 50, 200, 50, "Play Again", black, white)
quit_button = Button(screen_width // 2 - 100, screen_height // 2 + 150, 200, 50, "Quit", black, white)
leaderboard_button = Button(screen_width // 2 - 100, screen_height // 2 + 250, 200, 50, "Leaderboard", black, white)


def save_high_scores(scores):
    file_name = "highest_scores.txt"
    try:
        updated_scores = {}
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                for line in file:
                    username, score = line.strip().split(":")
                    score = int(score)
                    
                    if username in scores and scores[username] > score:
                        updated_scores[username] = scores[username]
                    else:
                        updated_scores[username] = score
        
        for username, score in scores.items():
            if username not in updated_scores:
                updated_scores[username] = score

        
        with open(file_name, "w") as file:
            for username, score in updated_scores.items():
                file.write(f"{username}:{score}\n")
    except Exception as e:
        print("Error saving high scores:", e)



def load_high_scores():
    scores = {}
    file_name = "highest_scores.txt"
    
    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as file:
                for line in file:
                    username, score = line.strip().split(":")
                    scores[username] = int(score)
            
            sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
            
            top_ten_scores = dict(list(sorted_scores.items())[:10])
            return top_ten_scores
        except Exception as e:
            print("Error loading high scores:", e)
    return scores  



def display_leaderboard():
    run = True
    while run:
        screen.fill(black)
        draw_text("Leaderboard", font40, white, int(screen_width / 2 - 100), 50)
        draw_text("Username    Score", font30, white, 50, 150)
        y = 200
        scores = load_high_scores()
        for username, score in scores.items():
            draw_text(f"{username:<12}  {score}", font30, white, 50, y)
            y += 50
        
        
        pygame.draw.rect(screen, white, (50, screen_height - 100, 100, 50))
        draw_text("Back", font30, black, 65, screen_height - 90)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 50 <= mouse_x <= 150 and screen_height - 100 <= mouse_y <= screen_height - 50:
                    run = False  

    return

run = True
while run:
    clock.tick(fps)

    draw_bg()
    alien_group.draw(screen)
    if countdown == 0:   
        time_now = pygame.time.get_ticks()
        if time_now - last_alien_shot > alien_cooldown and len(alien_bullet_group) < 5 and len(alien_group) > 0:
            attacking_alien = random.choice(alien_group.sprites())
            alien_bullet = Alien_Bullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom)
            alien_bullet_group.add(alien_bullet)
            last_alien_shot = time_now

        
        if len(alien_group) == 0:
            create_aliens()

        if game_over == 0:
            game_over = spaceship.update()

            bullet_group.update()
            alien_group.update()
            alien_bullet_group.update()
        else:
            if game_over == -1:
                scores[username] = score  
                save_high_scores(scores)  
                draw_text('GAME OVER!', font60, white, int(screen_width / 2 - 150), int(screen_height / 3))
                play_again_button.draw(screen)
                quit_button.draw(screen)
                leaderboard_button.draw(screen)


    if countdown > 0:
        draw_text('GET READY!', font40, white, int(screen_width / 2 - 110), int(screen_height / 2 + 50))
        draw_text(str(countdown), font40, white, int(screen_width / 2 - 10), int(screen_height / 2 + 100))
        count_timer = pygame.time.get_ticks()
        if count_timer - last_count > 1000:
            countdown -= 1
            last_count = count_timer

    explosion_group.update()

    spaceship_group.draw(screen)
    bullet_group.draw(screen)
    alien_bullet_group.draw(screen)
    explosion_group.draw(screen)

    draw_text("Score: " + str(score), font30, white, 10, 10)
    
    draw_text("Player: " + username, font20, white, 10, screen_height - 30)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            if play_again_button.rect.collidepoint(event.pos):
                play_again()
            
            elif quit_button.rect.collidepoint(event.pos):
                quit_game()
            elif leaderboard_button.rect.collidepoint(event.pos):
                display_leaderboard() 

    pygame.display.update()

pygame.quit()
