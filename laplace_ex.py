import numpy
import unittest

def Laplacian(indata, result, d):

    for i in range(d, indata.shape[0] - d):
        for j in range(d, indata.shape[1] - d):
            for k in range(d, indata.shape[2] - d):
                result[i, j, k] = (indata[i - 1, j, k] + indata[i + 1, j, k] + \
                                   indata[i, j - 1, k] + indata[i, j + 1, k] + \
                                   indata[i, j, k - 1] + indata[i, j, k + 1] - \
                                   6.0 * indata[i, j, k]) / (d * d)


    return 0

class TestFunctions(unittest.TestCase):
    def testLaplacian(self):
        xsize = 10
        ysize = 10
        zsize = 10

        step_size = 1

        data = numpy.zeros((xsize, ysize, zsize))

        for i in range(xsize):
            for j in range(ysize):
                for k in range(zsize):
                    data[i, j, k] = (i * i + j * j + k * k) / 6.0

        laplace = numpy.zeros((xsize, ysize, zsize))

        Laplacian(data, laplace, step_size)

        corr_ans = numpy.zeros((xsize, ysize, zsize))
        for i in range(step_size, xsize - step_size):
            for j in range(step_size, ysize - step_size):
                for k in range(step_size, zsize - step_size):
                    corr_ans[i, j, k] = 1

        self.assertTrue(((laplace - corr_ans) < 1E-10).all())


if __name__ == '__main__':
    unittest.main()

xsize = 10
ysize = 10
zsize = 10

max_data_value = 10.0

step_size = 1

# data = max_data_value * numpy.random.rand(xsize, ysize, zsize)

data = numpy.zeros((xsize, ysize, zsize))

for i in range(xsize):
    for j in range(ysize):
        for k in range(zsize):
            data[i, j, k] = (i * i + j * j + k * k) / 6.0

laplace = numpy.zeros((xsize, ysize, zsize))

Laplacian(data, laplace, step_size)

print(laplace)



