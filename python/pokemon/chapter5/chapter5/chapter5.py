# abstract class Pokemon {
#     abstract val name: String
#     abstract val type1: String
#     abstract val type2: String
#     abstract val hp: Int
    
#     abstract fun attack()
# }

from abc import ABC, abstractmethod
class Pokemon(ABC):
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    @abstractmethod
    def attack(self):
        pass

# class Pikachu(
#     override val name: String,
#     override val type1: String,
#     override val type2: String,
#     override val hp: Int
# ) : Pokemon() {

#     override fun attack() {
#         println("$name の10万ボルト!")
#     }
# }

from abc import ABC, abstractmethod
class Pokemon(ABC):
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    @abstractmethod
    def attack(self):
        print(f"{self.name}の10万ボルト")

class Pikachu(Pokemon):
    def __init__(self, name, type1, type2, hp):
        super().__init__(name, type1, type2, hp)

    @abstractmethod
    def attack(self):
        print(f"{self.name}の10万ボルト!")

# fun main() {
#     val pika = Pikachu("ピカチュウ", "でんき", "", 100)

#     println(pika.attack()) // ピカチュウ の10万ボルト!
# }

def main():
    pika = Pikachu("ピカチュウ", "でんき", "", 100)
    print(pika.attack())

if __name__ == "__main__":
    main()

# class Pikachu(
#     override val name: String,
#     override val type1: String,
#     override val type2: String,
#     override val hp: Int
# ) : Pokemon() {

#     override fun attack() {
#         super.attack()
#         println("$name の10万ボルト!")
#     }
# }

class Pikachu(Pokemon):
    def __init__(self, name, type1, type2, hp):
        super().__init__(name, type1, type2, hp)

    @abstractmethod
    def attack(self):
        super().attack()
        print(f"{self.name}の10万ボルト!")


# class Pikachu(
#     val namae: String,     // 名前。 本来は `name` を使いたい
#     val taipu1: String,    // タイプ1。 本来は `type1` を使いたい 
#     val taipu2: String,    // タイプ2。 本来は `type2` を使いたい
#     val hitpoint: Int      // HP。 本来は `hp` を使いたい
# ): Pokemon(namae, taipu1, taipu2, hitpoint) {
#     // kougeki() じゃなくて attack() を使いたい
#     fun kougeki() { ... }
# }

class Pikachu:
    def __init__(self, namae, taipu1, taipu2, hitpoint):
        self.namae = namae
        self.taipu1 = taipu1
        self.taipu2 = taipu2
        self.hitpoint = hitpoint

    def kougeki(self):
        pass

# abstract class Test {
#     val value = 100    // 値を入れられる
    
#     fun greet() { print("Hello!") }
# }

from abc import ABC , abstractmethod

class Test(ABC):
    def __init__(self, value):
        self.value = 100

    def greet(self):
        print("Hello!")

# interface Test {
#     val value: Int    // 値を入れられない
    
#     fun greet() { print("Hello!") }  // メソッドは実装可能
# }

from abc import ABC, abstractmethod

class Test(ABC):
    @property
    @abstractmethod
    def value(self):
        pass

    def greet(self):
        print("Hello!")

# abstract class ParentA
# abstract class ParentB

# class Child: ParentA()         // 多重継承NG

from abc import ABC, abstractmethod

class ParentA(ABC):
    @abstractmethod
    # ...

class ParentB(ABC):
    @abstractmethod
    # ...

class Child(ParentA):
    # ...

# interface ParentA
# interface ParentB

# class Child: ParentA, ParentB // 多重継承OK

from abc import ABC , abstractmethod


class ParentA(ABC):
    @property
    @abstractmethod
    # ...

class ParentB(ABC):
    @property
    @abstractmethod
    # ...

class Child(ParentA, ParentB):
    # ...