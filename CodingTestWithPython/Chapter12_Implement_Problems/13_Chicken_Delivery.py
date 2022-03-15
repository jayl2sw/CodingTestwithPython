# 맵의 크기, 남김
n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

houses = []
chicken = []

for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            houses.append([i, j])
        elif array[i][j] == 2:
            chicken.append([i, j])

print(houses)

chicken_combination = []



k = len(chicken)
def Combination(idx, list):
    if len(list) == m:
        chicken_combination.append(list[:])
        return

    for i in range(idx, k):
        Combination(i + 1, list + [chicken[i]])

Combination(0, [])

print(chicken_combination)

def distance(list1, list2):
    return abs(list1[0] - list2[0]) + abs(list1[1] - list2[1])

min_total = int(1e9)

for locations in chicken_combination:
    location_total = 0
    for house in houses:
        house_min = int(1e9)
        for location in locations:
            distance_var = distance(location, house)
            if house_min >= distance_var:
                house_min = distance_var
        location_total += house_min



    if min_total > location_total:
        min_total = location_total


print(min_total)
