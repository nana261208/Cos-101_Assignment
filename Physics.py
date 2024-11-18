def area_of_circle():
    radius = float(input('Enter radius'))
    area = 2 * 22/7 * radius
    print(area)

#area_of_circle()

def calculate_velocity():
    distance = float(input('Enter your distance: '))
    time = int(input('Enter your time: '))
    velocity = distance/time
    print(velocity)
#calculate_velocity()

print ('Welcome to physics 101')
topic = input('We have the special way of answering question under the topic: Dimension of Physical Quantity')


print ('we provide simple answer on whatever equation writen on the topic Physical Quantity')
print ('We have formulae on the topic Physical Quantities')
print('(a) calculate Density')
print('(b) calculate ohms law')
print('(c) calculate frequency')
print('(d) calculate Pressure')
print('(e) calculate latent heat')


def a():
    mass = float(input('Enter your mass'))
    volume = int(input('Enter your volume'))
    a = mass/volume
    print(a)


def b():
    current = float(input('Enter your current'))
    resistance = int(input('Enter your resistance'))
    b = current / resistance
    print(b)


def c():
    velocity = float(input('Enter your velocity'))
    wavelength = int(input('Enter your wavelength'))
    c = velocity / wavelength
    print(c)


def d():
    force = float(input('Enter your force'))
    area = int(input('Enter your area'))
    d = force / area
    print(d)


def e():
    quantity_of_heat = float(input('Enter your quantity of heat'))
    mass = int(input('Enter your mass'))
    e = quantity_of_heat / mass
    print(e)

def main():
    choice = input("Choose option")

    if choice == "a":
        a()

    if choice == "b":
        b()

    if choice == "c":
        c()

    if choice == "d":
        d()

    if choice == "e":
        e()


if __name__ == '__main__':
    main()




