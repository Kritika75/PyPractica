import pygame
import math
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Explorer")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PLANET_COLOURS = [BLUE, RED, GREEN]

clock = pygame.time.Clock()

SUN_RADIUS = 50
PLANETS = [
    {"radius": 15, "distance": 100, "colour": BLUE, "speed": 0.01},
    {"radius": 20, "distance": 200, "colour": RED, "speed": 0.007},
    {"radius": 25, "distance": 300, "colour": GREEN, "speed": 0.005}
]

spaceship = pygame.Rect(WIDTH // 2 - 20, HEIGHT // 2 + 200, 40, 40)
SPACESHIP_SPEED = 5

angles = [0 for _ in PLANETS]

def draw_solar_system():
    """Draw the sun, planets and spaceship"""
    screen.fill(BLACK)
    pygame.draw.circle(screen, YELLOW, (WIDTH // 2, HEIGHT // 2), SUN_RADIUS)
    
    for i, planet in enumerate(PLANETS):
        angle = angles[i]
        x = WIDTH // 2 + math.cos(angle) * planet["distance"]
        y = HEIGHT // 2 + math.sin(angle) * planet["distance"]
        pygame.draw.circle(screen, planet["colour"], (int(x), int(y)), planet["radius"])
        
    pygame.draw.rect(screen, WHITE, spaceship)
    
def update_planet_positions():
    for i, planet in enumerate(PLANETS):
        angles[i] += planet["speed"]
        
def handle_spaceship_movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and spaceship.top > 0:
        spaceship.y -= SPACESHIP_SPEED
    if keys[pygame.K_DOWN] and spaceship.bottom < HEIGHT:
        spaceship.y += SPACESHIP_SPEED
    if keys[pygame.K_LEFT] and spaceship.left > 0:
        spaceship.x -= SPACESHIP_SPEED
    if keys[pygame.K_RIGHT] and spaceship.right < WIDTH:
        spaceship.x += SPACESHIP_SPEED
        
def display_planet_info():
    font = pygame.font.SysFont(None, 36)
    for i, planet in enumerate(PLANETS):
        angle = angles[i]
        x = WIDTH // 2 + math.cos(angle) * planet["distance"]
        y = HEIGHT // 2 + math.sin(angle) * planet["distance"]
        if spaceship.collidepoint(int(x), int(y)):
            text = font.render(f"Planet {i + 1}", True, WHITE)
            screen.blit(text, (20, 20))
            
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    handle_spaceship_movement()
    update_planet_positions()
    draw_solar_system()
    display_planet_info()
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
sys.exit()