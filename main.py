import pygame

W, H = 10,20
TILE = 45
GAME_RES = 800, 600
FPS = 60

pygame.init()
game_sc = pygame.display.set_mode(GAME_RES)
clock = pygame.time.Clock()

grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(W) for y in range(H)]

while True:
    game_sc.fill(pygame.Color('black'))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exist()
            
    [pygame.draw.rect(game_SC, (40, 40, 40), i_rect, 1) for i_rect in grid]
    
    
    pygame.display.flip()
    clock.tick()