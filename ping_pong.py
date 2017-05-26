import mpi4py
from mpi4py import MPI
import numpy
import time

def ping_pong():
    comm = MPI.COMM_WORLD

    size = comm.Get_size()
    rank = comm.Get_rank()

    if rank == 0:
        duration = []

        for i in range(1, size):
            start_time = time.clock()

            signal = numpy.array([1.0])
            comm.Send([signal, MPI.DOUBLE], dest = i, tag = 10)

            response = numpy.zeros([1])
            comm.Recv([response, MPI.DOUBLE], source = i, tag = 11)

            finish_time = time.clock()

            duration.append(finish_time - start_time)

        av_dur = sum(duration) / len(duration)
        print("Average time for ping-pong was {av} s.".format(av = av_dur))

    else:
        signal = numpy.zeros([1])

        comm.Recv([signal, MPI.DOUBLE], source = 0, tag = 10)

        response = numpy.array([2.0])

        comm.Send([response, MPI.DOUBLE], dest = 0, tag = 11)


ping_pong()
