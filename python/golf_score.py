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
    else:
        return None


try:
    lines = [line.strip() for line in sys.stdin if line.strip()]
    golf_matches = list(map(int, lines[0].split(",")))
    players_points = list(map(int, lines[1].split(",")))

    if len(golf_matches) != 18 or len(players_points) != 18:
        raise ValueError(f"ホール数が18ではありません（規定打数={len(golf_matches)}ホール, プレイヤー={len(players_points)}ホール）")

except ValueError:
    print("数字を入力してください")
    sys.exit(1)
except IndexError:
    print("入力ファイルの形式が正しくありません（一行目に規定打数、二行目にプレイヤーの打数を記述してください）")
    sys.exit(1)
except TypeError:
    print("入力の型を確認してください")
    sys.exit(1)

for gm, pp in zip(golf_matches, players_points):
    result_point.append(result(gm, pp))

print(*golf_matches, sep=", ")
print(*players_points, sep=", ")
print(*result_point, sep=", ")