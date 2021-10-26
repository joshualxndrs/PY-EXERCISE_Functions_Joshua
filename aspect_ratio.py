def calc_correct_height():
    width = eval(input("Enter the initial width: "))
    height = eval(input("Enter the initial height: "))
    width_2 = eval(input("Enter the desired width: "))

    while width_2 > width:
        width_2 = eval(input("Desired width must be smaller than current width: "))
        continue
    
    if width_2 < width:
        height_2 = (width_2*height) / width
        print ("The correct height for the ratio is: ", float(height_2))


calc_correct_height()