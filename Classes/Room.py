import pygame

class Room:
    def __init__(self, name, image_path, position, width, height):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.position = position
        self.width = width
        self.height = height

    def draw(self, screen,color):
        screen.blit(self.image, self.position)
        font = pygame.font.Font(None, 24)  
        text = font.render(self.name, True, color) 
        text_rect = text.get_rect(center=(self.position[0] + self.width // 2, self.position[1] + self.height // 2))  
        screen.blit(text, text_rect)  
        

    def contains_point(self, point):
        x, y = point
        room_x, room_y = self.position
        return room_x <= x <= room_x + self.width and room_y <= y <= room_y + self.height 
