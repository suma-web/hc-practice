# val name = "リザードン"
name = "リザードン"

# class Pokemon {
#     val name: String
    
#     constructor(_name: String) {
#         name = _name
#     }
# }
class Pokemon:
    def __init__(self, name):
        self.name = name

# val poke = Pokemon("ピカチュウ")
# print(poke.name)    // ピカチュウ
poke = Pokemon("ピカチュウ")
print(poke.name)

# class Pokemon constructor(_name: String) {
#     val name: String = _name
# }
class Pokemon:
    def __init__(self, name):
        self.name = name

# class Pokemon(val name: String)
class Pokemon:
    def __init__(self, name):
        self.name = name
    
# class Pokemon(
#     val name: String
#     val type1: String
#     val type2: String
#     val hp: Int
# ) {
#     fun attack() {
#         println("$name のこうげき！")
#     }
# }
class Pokemon:
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
    
    def attack(self):
        print(f'{self.name}のこうげき')

# class Pokemon constructor(_name: String, _type: String) {
#     val exText = "$_name は $_type タイプのポケモン。"
# }
class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        print(f'{self.name}は{self.type}タイプのポケモン')

# // ↓メソッド開始
# fun localFunction() {
#     val poke = Pokemon()    // インスタンス生成
#     ...
# }
# // ↑メソッドが終わる時に自動的にインスタンスが破棄される

def localFunction():
    poke = Pokemon()