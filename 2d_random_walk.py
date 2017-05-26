import numpy
import matplotlib
import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import pylab

def step_forward(person1, person2):
    person1 = move(person1)

    person2 = move(person2)
    

def rand_walk(p1x, p1y, p2x, p2y):

    fig = matplotlib.pyplot.figure()

    person1 = numpy.array([p1x, p1y])
    person2 = numpy.array([p2x, p2y])

    x_coord = numpy.array([p1x, p2x])
    y_coord = numpy.array([p1y, p2y])

    matplotlib.pyplot.xlim(1, 10)
    matplotlib.pyplot.ylim(1, 10)

#    matplotlib.pyplot.plot(x_coord, y_coord)
    pylab.plot(x_coord, y_coord)

    #ax = fig.add_subplot()
    #ax.grid()

    #ax.set_ylim[1:10]
    #ax.set_xlim[1:10]

    impact_cond = 0

    n_its = 0

    while impact_cond == 0:
        step_forward(person1, person2)

        n_its = n_its + 1
    
        if (person1 == person2).all():

            print("Collision occured after {its} steps.".format(its = n_its))

            impact_cond = 1

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

rand_walk(1, 1, 5, 5)
