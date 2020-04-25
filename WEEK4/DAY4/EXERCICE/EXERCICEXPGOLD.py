from random import randint
month = int(input("Enter a Month (MM) "))
value = 0


def get_random_temp(month, value):
    if 12 <= month < 13 or 0 < month <= 2:
        value = randint(-10, 10)
        season = "Winter"
    elif 3 <= month <= 5:
        value = randint(11, 17)
        season = "Spring"
    elif 9 <= month <= 11:
        value = randint(18, 24)
        season = "Fall"
    elif 6 <= month <= 8:
        value = randint(25, 40)
        season = "Summer"

    print(f"i'ts {season}")
    return float(value)


def main():
    a = get_random_temp(month, value)
    print(f"The temperature right now is {a} degrees Celsius.")
    if a <= 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 <= a < 16:
        print("Quite chilly! Don’t forget your coat")
    elif 17 <= a < 23:
        print("You're only need a sweat shirt to can remove it :)")
    elif 24 <= a < 32:
        print("We are in Summer ! Go chill in the beach if you can")
    elif 33 <= a <= 40:
        print("Stay at home with a the Mazgan")


main()