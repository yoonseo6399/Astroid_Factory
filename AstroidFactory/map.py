import pygame
import items
import random


class Map:
    width = 1
    height = 1
    map = []  # [ 세로 [ 가로 ] ] 세로 한 줄마다 그에 해당하는 가로줄 ex) [[1,2],[3,4],[5,6]]<- 이러면 가로로 2칸 세로로 3칸 짜리인 맵. 숫자 있는 자리엔 광석과 현제 빌딩 상태 넣을 예정
    items = items.Items.createResource

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def createMap(self):
        for x in range(self.height):
            self.map.append([items.Blank()])
        for heiRow in range(self.height):  # height row of map
            for widRow in range(self.width):  # width row of map
                self.map[heiRow].insert(0, random.choice(self.items))
            self.map[heiRow].pop()

# class Vision:
#     width = 10
#     height = 6
#
#     Xpos = Map.width / 2
#     Ypos = Map.height / 2
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_W:  # 시야 위쪽
#                 if Ypos + (height / 2) <= Map.height:
#                     Ypos += 1
#             elif event.key == pygame.K_S:  # 아래
#                 if Ypos - (height / 2) >= 0:
#                     Ypos -= 1
#             elif event.key == pygame.K_A:  # 왼
#                 if Xpos - (width / 2) >= 0:
#                     Xpos -= 1
#             elif event.key == pygame.K_D:  # 오
#                 if Xpos + (width / 2) >= Map.height:
#                     Xpos += 1
