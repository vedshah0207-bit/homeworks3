r = int(input("Give the radius of a circle. "))
pi = 3.14159265358979

def circumference(rad):
    circ = (2 * rad) * pi
    return circ

print("The circumference of the circle is:", circumference(r))