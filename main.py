import pygame
import sys
import Game

pygame.init()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Kill And Win")
background_image = pygame.image.load("./assets/background.jpg")  
font = pygame.font.Font(None, 36)  



enter_text = font.render("Enter", True, (255, 0, 0)   )

enter_text_rect = enter_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2.24 + 150))

enter_button_rect = pygame.Rect(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 + 100, 100, 50)


pygame.mixer.init()  
button_sound = pygame.mixer.Sound("./sounds/epic-logo-6906.mp3") 
start=button_sound.play(loops=-1) 


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                if enter_button_rect.collidepoint(event.pos):
                   
                    new_window = True
                    while new_window:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                new_window = False
                                running = False
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:  
                                    if easy_button_rect.collidepoint(event.pos):
                                       Game.Start_Game(10)
                                       pygame.quit()
                                    elif hard_button_rect.collidepoint(event.pos):
                                        Game.Start_Game(5)
                                        pygame.quit()

                        window.fill(WHITE)

                        
                        start.pause()
                        Text_Reader_Sound = pygame.mixer.Sound('./sounds/Sound_Reader.mp3')  
                        Text_Reader_Sound.play(loops=0, maxtime=0, fade_ms=0)

                        lorem_text = font.render("kill and win : is a Game to win 10G of Drug and kill 10 skeleton ", True, BLACK)
                        lorem_text_rect = lorem_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100))
                        lorem_textt = font.render("upper Arrow to go forward , down Arrow to go backward ", True, BLACK)
                        lorem_textt_rect = lorem_textt.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 60))
                        lorem_texttt = font.render(" and Enter to hit  ", True, BLACK)
                        lorem_texttt_rect = lorem_texttt.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 20))

                        window.blit(lorem_text, lorem_text_rect)
                        window.blit(lorem_textt,lorem_textt_rect)
                        window.blit(lorem_texttt,lorem_texttt_rect)


                        easy_button_rect = pygame.Rect(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 + 50, 100, 50)
                        hard_button_rect = pygame.Rect(WINDOW_WIDTH // 2 + 10, WINDOW_HEIGHT // 2 + 50, 100, 50)
                        pygame.draw.rect(window, BLACK, easy_button_rect, 2)
                        pygame.draw.rect(window, BLACK, hard_button_rect, 2)

                        
                        easy_text = font.render("Easy", True, BLACK)
                        easy_text_rect = easy_text.get_rect(center=(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 + 75))
                        window.blit(easy_text, easy_text_rect)

                        hard_text = font.render("Hard", True, BLACK)
                        hard_text_rect = hard_text.get_rect(center=(WINDOW_WIDTH // 2 + 60, WINDOW_HEIGHT // 2 + 75))
                        window.blit(hard_text, hard_text_rect)

                        pygame.display.flip()

    window.blit(background_image, (0, 0))

    window.blit(enter_text, enter_text_rect)


    pygame.draw.rect(window, WHITE, enter_button_rect)
    pygame.draw.rect(window, BLACK, enter_button_rect, 2)
    window.blit(enter_text, enter_text_rect)

    pygame.display.flip()
pygame.quit()
sys.exit()
