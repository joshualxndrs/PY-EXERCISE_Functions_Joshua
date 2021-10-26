def calc_weight_on_planet(w, g = 23.1):
    m = w/9.8
    print("The weight on the Planet is", m*g)

calc_weight_on_planet(eval(input("Enter Weight (w): ")), eval(input("Enter Gravity (g): ")))
calc_weight_on_planet(120)