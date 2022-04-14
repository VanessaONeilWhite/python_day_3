def calculate_area():
    length_house = int(input("What is the length of your house? "))
    width_house = int(input("What is the width of your house? "))
    area = length_house * width_house
    print("The area of your house is " + str(area))


calculate_area()


def calculate_circumference():
    from math import pi
    radius_of_circle = int(input("What is the radius of your circle?"))
    print("the circumference of your circle is 6" + str(2*radius_of_circle*pi))

calculate_circumference()