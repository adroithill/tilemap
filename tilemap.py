from PIL import Image
import pygame


class oldTilemap:
    def __init__(self,xSize:int,ySize:int,tileset:list,defaultTile:int=24,tilemap:list[int]=None,extraData:dict=None):
        self.xSize = xSize
        self.ySize = ySize
        self.tilemap = []
        self.tileset = tileset
        for i in range(xSize*ySize):
            self.tilemap.append(defaultTile)
        if tilemap: self.tilemap = tilemap
        if extraData: self.extraData = extraData
        print("WARNING USING DEREPRICATED CLASS")
    
    def drawTilemap(self,size,screen,scale=1,localCameraX=0.0,localCameraY=0.0):
        for i in range(self.xSize*self.ySize):
            tileSprite = self.tileset[self.tilemap[i]].sprite
            tileSprite = pygame.transform.scale_by(tileSprite, scale)
            x = i % self.xSize
            y = i // self.xSize
            pos_x = x * size * scale
            pos_y = y * size * scale
            screen.blit(tileSprite, (pos_x-localCameraX, pos_y-localCameraY))
            
    def debug_displayTilemap(self):
        for i in range(self.ySize):
            for j in range(self.xSize):
                print(self.tilemap[j+(i*(self.xSize-1))], end="")
            print("")
    
    def setTileAtPos(self,x,y,tileSetX,tileSetY,tileSetWidthTiles):
        self.tilemap[x+(y*(self.xSize))] = tileSetX+(tileSetY*(tileSetWidthTiles-1))

class tile:
    def __init__(self,image,extra=None):
        self.sprite = image
        self.extraData=extra

def parseTileset(tilesetName:str,tileSize:int):
    width, height = Image.open("data/sprites/tiles/"+tilesetName+".png").size
    tileset=pygame.image.load("data/sprites/tiles/"+tilesetName+".png").convert_alpha()
    localTiles = []
    for i in range(height//tileSize):
        for j in range(width//tileSize):
            tileSprite = pygame.Surface((tileSize,tileSize)).convert_alpha()
            tileSprite.blit(tileset, (0,0), (0+(j*tileSize),0+(i*tileSize),tileSize,tileSize))
            tileSprite.set_colorkey(pygame.Color(0,0,0))
            localTiles.append(tile(tileSprite))
    return localTiles

class tilemap:
    def __init__(self,locationInTilemaps:str):
        pass