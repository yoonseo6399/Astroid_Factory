import map
import Bulidings
import item

gameMap = map.Map(5, 4)
gameMap.createMap()
inventory = [[]]
for i in gameMap.map:        # a에서 안쪽 리스트를 꺼냄
    for j in i:    # 안쪽 리스트에서 요소를 하나씩 꺼냄
        print(j.name, end=' ')
    print()
