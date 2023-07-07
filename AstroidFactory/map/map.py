import pygame

class Map:
    width = 100
    height = 60
    map = [[]]

class Vision:
    width = 10
    height = 6

    Xpos = 0
    Ypos = 0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # 시야 위쪽
                if Ypos+(height/2) >= Map.height:
                    print()
                else:
                    Ypos += 1
            elif event.key == pygame.K_RIGHT: # 아래
                if Ypos-(height/2) <= 0:
                    print()
                else:
                    Ypos -= 1
            elif event.key == pygame.K_SPACE: # 왼
                if Xpos-(width/2) <= 0:
                    print()
                else:
                    Xpos -= 1
            elif event.key == pygame.K_SPACE: # 오
                if Xpos+(width/2) >= Map.height:
                    print()
                else:
                    Xpos += 1
