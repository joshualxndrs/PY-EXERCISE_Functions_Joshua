def conv_temps():
    degree_sign = u"\N{DEGREE SIGN}"
    
    fahr = eval(input("Please enter a temperature in Fahrenheit (F): "))
    print("Temperature in Fahrenheit is equivalent to: ", fahr, degree_sign,"F")
    
    cel = Celcius (fahr)
    kel = Kelvin (cel)

    print("Temperature in Celcius is equivalent to", cel, degree_sign,"C")
    print("Temperature in Kelvin is equivalent to: ", kel, "K")

def Celcius(fahr):
    cel = (5/9)*(fahr-32)
    return cel

def Kelvin(cel):
    kel = (cel + 273.15)
    return kel

conv_temps()