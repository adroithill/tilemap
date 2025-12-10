from PIL import Image
import pygame
import json
import tilemap
import os

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720),pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
dt = 0

# global setup
tileSize = 16
tileScale = 4
cameraPos = pygame.Vector2(0,0)
        
emptyTilemap=tilemap.oldTilemap(20,20,tilemap.parseTileset("Overworld_Tileset",tileSize),24,json.loads(open("data/tilemaps/mapleCrossing/layers/bottom.json").read()))
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if os.path.isfile("data/tilemaps/" + filename + "/data.json"): 
        print("found tilemap")
    else:
        print("found dir")
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Screen Clearer
    screen.fill(pygame.Color(0,0,0))

    # RENDERER
    emptyTilemap.drawTilemap(tileSize,screen,tileScale,cameraPos.x,cameraPos.y)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        cameraPos.y -= 300 * dt
    if keys[pygame.K_s]:
        cameraPos.y += 300 * dt
    if keys[pygame.K_a]:
        cameraPos.x -= 300 * dt
    if keys[pygame.K_d]:
        cameraPos.x += 300 * dt

    pygame.display.flip()
    
    #emptyTilemap.setTileAtPos(int(input("x")),int(input("y")),int(input("x")),int(input("y")),18)

    dt = clock.tick(60)/1000
pygame.quit()