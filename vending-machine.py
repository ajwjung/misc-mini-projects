# vending machine style -- enter what the code to pick what box you want dropped out
# vending machine returns a random style
# open the box - reveals random box
import random

# Random toy generator
def choices_no_replacement(population, weights, k=1):
    population = list(population)
    weights = list(weights)
    result = []
    for n in range(k):
        pos = random.choices(range(len(population)), weights, k=1)[0]
        result.append(population[pos])
        del population[pos], weights[pos]
    result = "".join(result)
    return result


# Toy variants and probabilities
yuki = {
    "Neon": 1/12, "Rock Sugar": 1/12, "Perlite": 1/12,
    "Milkshake-Pink": 1/12, "Milkshake-Blue": 1/12, "Saipan": 1/12,
    "Porcelain": 1/12, "Strawberry Ice Cream": 1/12, "Galaxy": 1/12,
    "Aurora": 1/12, "Gemstone-Pink": 1/12, "Gemstone-Blue": 1/12,
    "Luminous": 1/50, "Yoka Baby": 1/100
}

vending_machine = [["A1", "A2", "A3"],
                   ["B1", "B2", "B3"],
                   ["C1", "C2", "C3"]]

# Chance of getting certain variants
population = [name for name in yuki.keys()]
weights = [round(values, 3) for values in yuki.values()]

make_purchase = input("""Hello! Welcome to our POPMART vending machine!
Would you like to make a purchase today? Y/N: """).upper()
while True:
    if make_purchase == "Y":
        for line in vending_machine:
            print(*line)

        box = input("Please enter the code for the box you would like: ").upper()
        found = any(box in sub for sub in vending_machine)
        if found:
            print("""Dispensing now...\nThank you for your purchase!""")

            open_now = input("Open the blind box? Y/N: ").upper()
            if open_now == "Y":
                print(f"""Opening now...\nYou got a {choices_no_replacement(population, weights)} Yuki!""")
                purchase = input("Would you like to purchase another one? Y/N: ").upper()
                if purchase == "Y":
                    continue
                elif purchase == "N":
                    print("Have a nice day!")
                else:
                    continue
            elif open_now == "N":
                print("Okay, save it for later.\nHave a nice day!")
            else:
                print("Come again?")
        else:
            print("Error, please try again.")
            continue

    elif make_purchase == "N":
        print("Thank you, have a nice day! :)")
    break
