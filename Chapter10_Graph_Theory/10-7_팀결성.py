# 학생 수, 연산의 개수 input

def find_team(team, a):
    if team[a] != a:
        team[a] = find_team(team, team[a])
    return team[a]

def get_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)
    if a < b:
        team[b] = a
    else:
        team[a] = b

n, m = map(int, input().split())
team = [0] * (n + 1)

result = ''
for i in range(0, n+1):
    team[i] = i

for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        get_team(team, a, b)

    else:
        if find_team(team, a) == find_team(team, b):
            result += "Y"
        else:
            result += "N"

print(result)

