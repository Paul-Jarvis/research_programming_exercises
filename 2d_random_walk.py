import numpy

def rand_walk(p1x, p1y, p2x, p2y):
    person1 = numpy.array([p1x, p1y])
    person2 = numpy.array([p2x, p2y])

    person1 = move(person1)

    person2 = move(person2)
    
    print(person1)

    return "Collision occured"

def move(person):

    which_dim = numpy.random.choice(["horiz", "vert"])

    if (which_dim == "horiz"):
        which_way = numpy.random.choice(["left", "right"])

        if (which_way == "left"):
            person[0] = person[0] - 1;

        else:
            person[0] = person[0] + 1;

    else:
        which_way = numpy.random.choice(["up", "down"])

        if (which_way == "up"):
            person[1] = person[1] + 1;

        else:
            person[1] = person[1] - 1;

    for i in [0,1]:
        if (person[i] < 1):
            person[i] = 10
        elif (person[i] > 10):
            person[i] = 1

    return person

rand_walk(1, 1, 10, 10)
