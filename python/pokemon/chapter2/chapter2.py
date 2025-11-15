# class Pokemon {
#     val name: String = “リザードン”
#     val type1: String = “ほのお”
#     val type2: String = “ひこう”
#     val hp: Int = 100
# }

class Pokemon:
    def __init__(self):
        name = "リザードン"
        type1 = "ほのお"
        type2 = "ひこう"
        hp = 100

# # val poke = Pokemon()

poke = Pokemon()

# fun main() {
#     val poke = Pokemon()

#     println(poke.name)   // リザードン
#     println(poke.type1)  // ほのお
#     poke.attack()        // リザードン のこうげき！
# }

class Pokemon:
    def __init__(self):
        self.name = "リザードン"
        self.type1 = "ほのお"
        self.type2 = "ひこう"
        self.hp = 100

    def attack(self):
        print(f"{self.name} のこうげき！")

def main():
    poke = Pokemon()
    print(poke.name)
    print(poke.type1)
    poke.attack()

if __name__ == "__main__":
    main()

# val poke: Pokemon = Pokemon()
poke: "Pokemon" = Pokemon()

# val pokemon1Name = "ヒトカゲ"
# val pokemon2Name = "ゼニガメ"
# ...
# val pokemon100Name = "ミュウ"

# val pokemon1Type1 = "ほのお"
# ...
# 以下延々と続く

pokemon1Name = "ヒトカゲ"
pokemon2Name = "ゼニガメ"
pokemon100Name = "ミュウ"
pokemon1Type1 = "ほのお"

# val pokemonName = listOf("ヒトカゲ", "ゼニガメ", ... "ミュウ")
# val pokemonType1 = ...
pokemonName = ["ヒトカゲ","ゼニガメ","...","ミュウ"]
pokemonType1 = ["ほのお","みず","...","エスパー"]

# val pokeMp = ...
pokeMp = []

# fun main() {
#     val pokemons: List<Pokemon> = createPokemon100() // ポケモンのインスタンスを100匹分作る処理とする
    
#     println(pokemons[0].name)    // 1匹目のポケモンの名前
#     println(pokemons[9].type1)    // 10匹目のポケモンのタイプ1
#     println(pokemons[99].attack()) // 100匹目のポケモンの攻撃
# }
class Pokemon:
    def __init__(self, name, type1, type2="なし", hp=100):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    def attack(self):
        print(f"{self.name} のこうげき！")


def create_pokemon_100():
    pokemons = []
    for i in range(1, 101):
        pokemons.append(
            Pokemon(
                name=f"ポケモン{i}",
                type1="タイプA",
                type2="タイプB",
                hp=100
            ))
    return pokemons


def main():
    pokemons = create_pokemon_100()
    print(pokemons[0].name)
    print(pokemons[9].type1)
    pokemons[99].attack()


if __name__ == "__main__":
    main()

# class Pokemon {
#     val name: String = "リザードン"
#     val type1: String = "ほのお"
#     val type2: String = "ひこう"
#     val hp: Int = 100
#     val mp: Int = 10 // 追加
    
#     fun attack() {
#         println("$name のこうげき!")
#     }
# }
# fun main() {
#     val poke = Pokemon()

#     println(poke.mp)   // 10
# }

class Pokemon:
    def __init__(self):
        self.name = "リザードン"
        self.type1 = "ほのお"
        self.type2 = "ひこう"
        self.hp = 100
        self.mp = 10
    
    def attack(self):
        print(f"{self.name}のこうげき!")

def main():
    poke = Pokemon()
    print(poke.mp)

if __name__ == "__main__":
    main()