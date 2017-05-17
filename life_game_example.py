import numpy

def create_test_array(ind, size):
    test_array = [ind - 1, ind, ind + 1]

    max_grid_pos = size - 1

    if test_array[0] < 0:
        test_array[0] = max_grid_pos

    if test_array[2] > max_grid_pos:
        test_array[2] = 0

    return test_array


x_size = 5
y_size = 5

grid = numpy.random.randint(2, size = (x_size, y_size))

print(grid)

for i in range(x_size):
    for j in range(y_size):
        horiz_test_var = create_test_array(i, x_size)
        vert_test_var = create_test_array(j, y_size)

        count = 0
        for k in horiz_test_var:
            for l in vert_test_var:
                if k != 1 and l != 1:
                    count = count + grid[k, l]

        print(i, j, count)



