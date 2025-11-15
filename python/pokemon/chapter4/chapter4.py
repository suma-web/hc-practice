# class Pokemon (
#     val name: String,
#     val type1: String,
#     val type2: String,
#     val hp: Int
# ){
#     fun attack() {
#         println("$name のこうげき!")
#     }
    
#     // ピカチュウの攻撃
#     fun thunderboltAttack() { 
#         println("$name の10万ボルト!")
#     }
    
#     // ゼニガメの攻撃
#     fun watergunAttack() {
#         println("$name のみずでっぽう!") }
#     }
# }

class Pokemon:
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    def attack(self):
        print(f"{self.name}のこうげき!")
    
    def thunderboltAttack(self):
        print(f"{self.name}の10万ボルト!")
    
    def watergunAttack(self):
        print(f"{self.name}のみずでっぽう!")

# if(poke.name == "ピカチュウ") {
#     poke.thunderboltAttack()
# }
# else if(poke.name == "ゼニガメ") {
#     poke.watergunAttack()
# }
# ...

poke = Pokemon()
if poke.name == "ピカチュウ":
    poke.thunderboltAttack()
elif poke.name == "ゼニガメ":
    poke.watergunAttack()

# class Pikachu: Pokemon()
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__()

# open class Pokemon(...)
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__()

# class Pikachu(
#     _name: String,
#     _type1: String,
#     _type2: String,
#     _hp: Int
# ): Pokemon(_name, _type1, _type2, _hp)
class Pikachu:
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
    
    def attack(self):
        print(f"{self.name}のこうげき")

class Pikachu(Pokemon):
    def __init__(self, name, type1, type2, hp):
        super().__init__(name, type1, type2, hp)

# fun main() {
#     val pika = Pikachu("ピカチュウ", "でんき", "", 100)
    
#     println(pika.name)     // ピカチュウ
#     println(pika.attack()) // ピカチュウ のこうげき! 
# }

def main():
    pika = Pikachu("ピカチュウ", "でんき", "", 100)

    print(pika.name)
    print(pika.attack())

# class Pikachu(
#     _name: String,
#     _type1: String,
#     _type2: String,
#     _hp: Int
# ): Pokemon(_name, _type1, _type2, _hp) {

#     override fun attack() {
#         println("$name の10万ボルト!")
#     }
# }
class Pikachu:
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
    
    def attack(self):
        print(f"{self.name}のこうげき")

class Pikachu(Pokemon):
    def __init__(self, name, type1, type2, hp):
        super().__init__(name, type1, type2, hp)

    def attack(self):
        print(f"{self.name}の10万ボルト!")

# fun main() {
#     val pika = Pikachu("ピカチュウ", "でんき", "", 100)
    
#     println(pika.attack()) // ピカチュウ の10万ボルト! 
# }
def main():
    pika = Pikachu("ピカチュウ", "でんき", "", 100)
    print(pika.attack())

# open class Pokemon(...) {
#     open fun attack() {
#         ...
#     }
# }
class Pokemon:
   def attack(self):
       ...

# class Pikachu(
#     _name: String,
#     _type1: String,
#     _type2: String,
#     _hp: Int
# ): Pokemon(_name, _type1, _type2, _hp) {

#     override fun attack() {
#         super.attack()    // 親クラスのメソッド呼び出し
#         println("$name の10万ボルト!")
#     }
# }
class Pokemon:
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    def attack(self):
        print(f"{self.name}のこうげき")

class Pikachu(Pokemon):
    def __init__(self, name, type1, type2, hp):
        super().__init__(name, type1, type2, hp)

    def attack(self):
        super().attack()
        print(f"{self.name}の10万ボルト!")

# val poke: Pikachu = Pikachu("ピカチュウ", "でんき", "", 100)
poke = Pikachu("ピカチュウ", "でんき", "", 100)

# val poke: Pokemon = Pikachu("ピカチュウ", "でんき", "", 100)
poke = Pikachu("ピカチュウ", "でんき", "", 100)