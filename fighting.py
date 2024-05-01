import pygame
import random
import math
import tkinter as tk
from tkinter import messagebox
import sys
from Classes import Characters
class BloodIndicator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x + 30, self.y), 10)
        pygame.draw.circle(screen, (255, 0, 0), (self.x + 50 , self.y), 10)
        pygame.draw.circle(screen, (255, 0, 0), (self.x + 70, self.y), 10)

def Start_Game(numOfSkeleton, time_limit):
    # Initialization
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("kill and win")
    background_image = pygame.image.load("./assets/floor_black.jpg")
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(background_image, (0, 0))
    font = pygame.font.Font(None, 36)
    timer_start = pygame.time.get_ticks()

    # Create player (Pablo) and enemy objects
    player = Characters.Player("./assets/pablo.png", 100, 100, 100, 0.1)
    enemies = []
    blood_indicators = []

    # Load enemy image based on the number of skeletons
    enemy_img = "./assets/normal enemy.png" if numOfSkeleton > 1 else "./assets/last enemy.png" 
    if numOfSkeleton == 1:
        print("box is  displyed")
        Characters.YellowObject.drawBox("./assets/Box.png",screen,500,100)

    # Create enemy objects
    for _ in range(numOfSkeleton):
        enemy = Characters.YellowObject(enemy_img, 80, random.randint(300, 700), random.randint(50, 500), 0.1)
        enemy.hits = 0
        enemies.append(enemy)
        blood_indicator = BloodIndicator(enemy.x, enemy.y - 30)
        blood_indicators.append(blood_indicator)

    # Attack cooldowns
    player_attack_cooldown = 0
    enemy_attack_cooldowns = [0] * numOfSkeleton

    # Main loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Ask user if they want to exit the game
                root = tk.Tk()
                root.withdraw()
                response = messagebox.askyesno("Exit", "Do you want to exit the game?")
                if response:
                    running = False
                    pygame.quit()
                    sys.exit()

        # Player input handling
        keys = pygame.key.get_pressed()
        player.handle_input(keys)
        player.CheckEdge()
        # Player attack handling
        if keys[pygame.K_SPACE] and player_attack_cooldown == 0:
            player_attack_cooldown = 30  # Cooldown in frames
            for enemy in enemies:
                if player.hit(enemy):
                    sword_sound = pygame.mixer.Sound("./sounds/swing-whoosh-weapon-1-189819.mp3")
                    sword_sound.play()
                    enemy.hits += 1 
                    if enemy.hits >= 3:  
                        enemies.remove(enemy)
                        blood_indicators.pop()
                        if len(enemies) == 0 and numOfSkeleton == 1:
                            pygame.mixer.stop() 
                            laughing_sound = pygame.mixer.Sound("./sounds/evil-laugh-49831.mp3")
                            laughing_sound.play(loops=-1)
                            print("Congratulations! You have defeated the final enemy!")
                            running = True
                            screen.fill((255, 255, 255))
                            win_font = pygame.font.Font(None, 72)
                            win_text = win_font.render("You Win!", True, (0, 0, 0))
                            text_rect = win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                            screen.blit(win_text, text_rect)
                            pygame.display.flip()
                            root = tk.Tk()
                            root.withdraw()
                        elif len(enemies)==0:
                            response = messagebox.askyesno("Next", "Do you want to proceed to the next level?")
                            if response:
                                number = random.randint(1, 2)
                                Start_Game(number, time_limit)
                            else:
                                pygame.quit()
                                sys.exit()

        # Update player attack cooldown
        if player_attack_cooldown > 0:
            player_attack_cooldown -= 1


        for i, (enemy, blood_indicator) in enumerate(zip(enemies, blood_indicators)):
            enemy.sense_and_move(player)
            enemy.move()

            # Enemy attack handling
            if enemy_attack_cooldowns[i] == 0:
                if enemy.hit(player):
                    player.health -= 5
                    if player.health <= 0:
                        print("Player is dead!")
                        running = False
                        root = tk.Tk()
                        root.withdraw()
                        response = messagebox.askyesno("Game Over", "Do you want to restart the game?")
                        if response:
                            pygame.quit()
                            sys.exit()
                            # number = random.randint(1, 2)
                            # Start_Game(number, time_limit)  # Restart the game
                        else:
                            pygame.quit()
                            sys.exit()
                    enemy_attack_cooldowns[i] = 15  # Cooldown in frames

            # Update enemy attack cooldown
            if enemy_attack_cooldowns[i] > 0:
                enemy_attack_cooldowns[i] -= 1

            # Update blood indicator position
            blood_indicator.x = enemy.x
            blood_indicator.y = enemy.y - 30

        # Render objects on screen
        screen.blit(background_image, (0, 0))
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        for blood_indicator in blood_indicators:
            blood_indicator.draw(screen)

        timer_seconds = (pygame.time.get_ticks() - timer_start) // 1000
        timer_text = font.render(f"Time: {time_limit - timer_seconds}", True, (255, 255, 255))
        screen.blit(timer_text, (10, 10))
        for i in range(player.health // 5):
            pygame.draw.circle(screen, (255, 0, 0), (30 + 15 * i, SCREEN_HEIGHT - 30), 5)

        # Check if time is up
        if timer_seconds >= time_limit:
            running = False
            root = tk.Tk()
            root.withdraw()
            response = messagebox.askyesno("Time Up", "Time's up! Do you want to play again?")
            if response:
                pygame.quit()
                sys.exit() 
            else:
                pygame.quit()
                sys.exit()

        # Update display
        pygame.display.flip()
  
    # Quit game
    pygame.quit()

