import Main

users = "root"
def main():
    print(Main)
    if users == "root":
        print(f"Hello {users}")

class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def userAut(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        if self.age == "root" and self.age >= 18:
            print("Добро пожаловать")

def main():
    users = User(" ", 0)
    users.userAut()

if __name__ == "__main__":
    main()