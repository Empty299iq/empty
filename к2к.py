import time

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Рівень голоду (0 - ситий, 10 - дуже голодний)
        self.happiness = 5  # Рівень щастя (0 - нещасливий, 10 - дуже щасливий)
        self.energy = 5  # Рівень енергії (0 - виснажений, 10 - енергійний)
        self.alive = True

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1
            print(f"{self.name} поїв і тепер голод зменшився до {self.hunger}.")
        else:
            print(f"{self.name} не голодний!")

    def play(self):
        if self.energy > 0:
            self.happiness += 1
            self.hunger += 1
            self.energy -= 1
            print(f"{self.name} грає! Щастя: {self.happiness}, голод: {self.hunger}, енергія: {self.energy}.")
        else:
            print(f"{self.name} занадто втомлений, щоб грати.")

    def sleep(self):
        self.energy += 2
        self.hunger += 1
        print(f"{self.name} спить. Енергія: {self.energy}, голод: {self.hunger}.")

    def status(self):
        print(f"Ім'я: {self.name}")
        print(f"Голод: {self.hunger}/10")
        print(f"Щастя: {self.happiness}/10")
        print(f"Енергія: {self.energy}/10")

    def check_alive(self):
        if self.hunger >= 10:
            print(f"{self.name} помер від голоду...")
            self.alive = False
        elif self.happiness <= 0:
            print(f"{self.name} став нещасливим і залишив вас...")
            self.alive = False
        elif self.energy <= 0:
            print(f"{self.name} помер від виснаження...")
            self.alive = False

def main():
    name = input("Введіть ім'я вашого Тамагочі: ")
    pet = Tamagotchi(name)

    print(f"Вашого вихованця звуть {pet.name}. Подбайте про нього!")
    time.sleep(1)

    while pet.alive:
        print("\nДії:")
        print("1 - Годувати")
        print("2 - Грати")
        print("3 - Спати")
        print("4 - Переглянути статус")
        print("5 - Вийти")
        choice = input("Виберіть дію: ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            pet.status()
        elif choice == "5":
            print(f"Ви залишили {pet.name}.")
            break
        else:
            print("Невірний вибір!")

        pet.check_alive()

    print("Гра закінчена.")

if __name__ == "__main__":
    main()

