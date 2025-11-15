# abstract class Pokemon {
#     abstract val name: String
#     abstract val type1: String
#     abstract val type2: String
#     abstract val hp: Int
    
#     abstract fun attack()
# }

from abc import ABC, abstractmethod


class Pokemon:
    @abstractmethod
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    @abstractmethod
    def attack(self):
        pass

# abstract class Pokemon {
#     abstract var name: String
#     abstract val type1: String
#     abstract val type2: String
#     abstract val hp: Int
    
#     abstract fun attack()
# }

from abc import ABC, abstractmethod


class Pokemon:
    @abstractmethod
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    @abstractmethod
    def attack(self):
        pass

# abstract class Pokemon {
#     abstract var name: String
#     abstract val type1: String
#     abstract val type2: String
#     abstract val hp: Int
    
#     abstract fun attack()

#     fun changeName(newName: String) {
#         // 不適切な名前はエラー
#         if(name == "うんこ") {
#             print("不適切な名前です")
#             return
#         }
#         this.name = newName
#     }
# }

# val newName = getUserInput() // ユーザーの入力を受け取る
# pokemon.name = newName       // changeName()を使わずに名前を変えてしまった！

from abc import ABC, abstractmethod


class Pokemon:
    @abstractmethod
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    @name.setter
    def name(self, new_name):
        if self.name == "うんこ":
            print("不適切な名前です")
        self._name = new_name

    @abstractmethod
    def attack(self):
        pass

new_name = input()
pokemon = Pokemon()
pokemon.name = new_name


# abstract class Pokemon {
#     private var name: String = ""    // 外部からアクセス不可能
# }

from abc import ABC, abstractmethod


class Pokemon:
    @abstractmethod
    def __init__(self, name, type1, type2, hp):
        self._name = ""

# abstract class Pokemon {
#     private var name: String = ""
#     abstract val type1: String
#     abstract val type2: String
#     abstract val hp: Int
    
#     abstract fun attack()

#     fun changeName(newName: String) {
#         // 不適切な名前はエラー
#         if(name == "うんこ") {
#             print("不適切な名前です")
#             return
#         }
#         this.name = newName
#     }
    
#     fun getName(): String {
#         return this.name
#     }
# }

from abc import ABC, abstractmethod


class Pokemon:
    @abstractmethod
    def __init__(self, name, type1, type2, hp):
        self._name = ""
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    def attack(self):
        pass

    def change_name(self, new_name):
        if new_name == "うんこ":
            print("不適切な名前です")
        self._name = new_name
    
    def get_name(self):
        self._name = new_name
        return self._name

    @abstractmethod
    def attack(self):
        pass

# class Pikachu(
#     override val type1: String,
#     override val type2: String,
#     override val hp: Int
# ) : Pokemon() {

#     override fun attack() {
#         println("${super.getName()} の10万ボルト!")
#     }
# }

class Pikachu(Pokemon):
    def __init__(self, name, type1, type2, hp):
        super().__init__(type1, type2, hp)

    def attack(self):
        super().attack()
        print(f"{super().get_name()}の10万ボルト")

# pokemon.changeName("テキセツ")
# pokemon.getName()     // テキセツ

# pokemon.changeName("うんこ")   // 「不適切な名前です」と表示される
# pokemon.getName()     // テキセツ のまま

pokemon = Pokemon()

pokemon.change_name("テキセツ")
pokemon.get_name()

pokemon.change_name("うんこ")
pokemon.get_name()

# interface NameService {
#     fun changeName(newName: String)
#     fun getName(): String
# }

from abc import ABC, abstractmethod

class NameService(ABC):

    @abstractmethod
    def change_name(self, new_name):
        pass

    @abstractmethod
    def get_name(self):
        pass

# abstract class Pokemon: NameService {
#     private var name: String = ""
#     abstract val type1: String
#     abstract val type2: String
#     abstract val hp: Int
    
#     abstract fun attack()

#     override fun changeName(newName: String) {
#         // 不適切な名前はエラー
#         if(name == "うんこ") {
#             print("不適切な名前です")
#             return
#         }
#         this.name = newName
#     }
    
#     override fun getName(): String {
#         return this.name
#     }
# }

class NameService(ABC):
    @abstractmethod
    def change_name(self, new_name):
        pass

    @abstractmethod
    def get_name(self):
        pass

class Pokemon(NameService):
    def __init__(self):
        self.__name = ""
        

    def change_name(self, new_name):
        if new_name == "うんこ":
            print("不適切な名前です")
            return
        self.__name = new_name

    def get_name(self):
        super().__init__()
        return self.__name
    
    @abstractmethod
    def attack(self):
        pass

# class Player(): NameService {
#     override fun changeName(newName: String) {
#         ...
#     }
    
#     override fun getName(): String {
#         ...
#     }
# }

class Player(NameService):
    def change_name(self, new_name):
        super().__init__()

    def get_name(self):
        super().__init__()
