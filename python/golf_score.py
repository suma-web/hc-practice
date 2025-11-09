import sys

golf_matches = []
players_points = []
result_point = []

score_map = {
    3: {  # par3
        0:  "パー",
        1:  "ボギー",
        -1: "バーディ",
        -2: "イーグル",
    },
    4: {  # par4
        0:  "パー",
        1:  "ボギー",
        -1: "バーディ",
        -2: "イーグル",
        -3: "アルバトロス",
    },
    5: {  # par5
        0:  "パー",
        1:  "ボギー",
        -1: "バーディ",
        -2: "イーグル",
        -3: "アルバトロス",
    },
}

def result(par, strokes):
    diff = strokes - par
    if strokes == 1:
        return "コンドル" if par >= 5 else "ホールインワン"

    name = score_map.get(par, {}).get(diff)
    if name is not None:
        return name
    
    if diff >= 2:
        return f"{diff}ボギー"

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