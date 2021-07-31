from random import randint


choice = ["ქვა", "მაკრატელი", "ქაღალდი"]
computer = choice[randint(0,2)]

palyer = False

while True:

    palyer = input("ქვა, მაკრატელი, ქაღალდი - ")

    if palyer == "ქვა" and computer == "მაკრატელი":
        print(f"თქვენ მოიგეთ, კომპიუტერმა აირჩია {computer}")
    elif palyer == "მაკრატელი" and computer == "ქაღალდი":
        print(f"თქვენ მოიგეთ, კომპიუტერმა აირჩია {computer}")
    elif palyer == "ქაღალდი" and computer == "ქვა":
        print(f"თქვენ მოიგეთ კომპიუტერმა აირჩია {computer}")
    elif palyer == "მაკრატელი" and computer == "ქვა":
        print(f"თქვენ წააგეთ, კომპიუტერმა აირჩია {computer}")
    elif palyer == "ქაღალდი" and computer == "მაკრატელი":
        print(f"თქვენ წააგეთ, კომპიუტერმა აირჩია {computer}")
    elif palyer == "ქვა" and computer == "ქაღალდი":
        print(f"თქვენ წააგეთ, კომპიუტერმა აირჩია {computer}")
    elif palyer == computer:
        print(f"ფრე, კომპიუტერმა აირჩია {computer} ")
    else:
        print("შეიყვანეთ სწორი მოქმედება !")
    player = False
    computer = choice[randint(0, 2)]
