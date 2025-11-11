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

# class Pokemon {
#     val name: String = “リザードン”
#     val type1: String = “ほのお”
#     val type2: String = “ひこう”
#     val hp: Int = 100
    
#     // 追加
#     fun attack() {
#         println("$name のこうげき！")
#     }
# }

class Pokemon:
    def __init__(self):
        name = "リザードン"
        type1 = "ほのお"
        type2 = "ひこう"
        hp = 100

    def attack(self):
        print(f"{self.name}のこうげき!")


# val poke = Pokemon()
poke = Pokemon()

# fun main() {
#     val poke = Pokemon()

#     println(poke.name)   // リザードン
#     println(poke.type1)  // ほのお
#     poke.attack()        // リザードン のこうげき！
# }

def main():
    poke = Pokemon()
    print(poke.name)   # リザードン
    print(poke.type1)  # ほのお
    poke.attack()      # リザードン のこうげき！

if __name__ == "__main__":
    main()