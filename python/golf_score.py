import sys

golf_matches = []
players_points = []
result_point = []

def result(golf_matches_num, players_points_num):
    point = players_points_num - golf_matches_num
    if players_points_num == 1 and golf_matches_num == 5:
        return "コンドル"
    elif players_points_num == 1:
        return "ホールインワン"
    elif point > 3:
        return f"{point}ボギー"
    elif golf_matches_num == 3:
        result_name = ["パー","ボギー","2ボギー","3ボギー","イーグル","バーディ"]
        return result_name[point]
    elif golf_matches_num == 4:
        result_name = ["パー","ボギー","2ボギー","3ボギー","イーグル","バーディ"]
        return result_name[point]
    elif golf_matches_num == 5:
        result_name = ["パー","ボギー","2ボギー","3ボギー","コンドル","アルバトロス","イーグル","バーディ"]
        return result_name[point]


lines = [line.strip() for line in sys.stdin if line.strip()]

golf_matches = list(map(int, lines[0].split(",")))
players_points = list(map(int, lines[1].split(",")))

for gm, pp in zip(golf_matches, players_points):
    result_point.append(result(gm, pp))

print(*golf_matches, sep=", ")
print(*players_points, sep=", ")
print(*result_point, sep=", ")