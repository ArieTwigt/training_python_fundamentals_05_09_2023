from custom_modules.calc_functions import calc_pythagoras, calc_size_circle


calculation_type = input("Choose calculation A = Pythagoras, B = Circle:\n").lower()

if calculation_type == "a":
    side_a = float(input("Size of a:\n"))
    side_b = float(input("Size of b:\n"))

    c = calc_pythagoras(side_a, side_b)

    print(c)
elif calculation_type == "b":

    diameter = float(input("Voer diameter in:\n"))

    size = calc_size_circle(diameter)

    print(f"De oppervlakte is {size}")
else:
    print("Not an option")
