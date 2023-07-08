import pygame
import Buildings.items


class Map:
    width = 100
    height = 60
    map = [[]]#[ 세로 [ 가로 ] ] 세로 한 줄마다 그에 해당하는 가로줄 ex) [[1,2],[3,4],[5,6]]<- 이러면 가로로 2칸 세로로 3칸 짜리인 맵. 숫자 있는 자리엔 광석과 현제 빌딩 상태 넣을 예정

    def __int__(self,width,height):
        self.width = width
        self.height = height
    def createMap(self):
        for heiRow in range(0,self.width-1): #height row of map
            for widRow in range(0,self.height-1): #width row of map
                #대충 랜덤하게 광석 넣기 일단 아무것도 없는 blank 넣을게요
                map[heiRow][widRow] = items.Blank


class Vision:
    width = 10
    height = 6

    X_pos = map.width/2
    Y_pos = map.height/2
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_W: # 시야 위쪽
                if Ypos+(height/2) <= Map.height:
                    Ypos += 1
            elif event.key == pygame.K_S: # 아래
                if Ypos-(height/2) >= 0:
                    Ypos -= 1
            elif event.key == pygame.K_A: # 왼
                if X_pos-(width/2) >= 0:
                    X_pos -= 1
            elif event.key == pygame.K_D: # 오
                if X_pos+(width/2) >= Map.height:
                    X_pos += 1
