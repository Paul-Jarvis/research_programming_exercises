import mpi4py
from mpi4py import MPI
import numpy
import time

def master_rank(comm):
    n_ranks = comm.Get_size()

    duration = []

    for i in range(1, n_ranks):
        start_time = time.clock()

        signal = numpy.array([1.0])
        comm.Send([signal, MPI.DOUBLE], dest = i, tag = 0)

        response = numpy.zeros([1])
        comm.Recv([response, MPI.DOUBLE], source = i, tag = 0)

        finish_time = time.clock()

        duration.append(finish_time - start_time)

    av_dur = sum(duration) / len(duration)
    print("Average time for ping-pong was {av} s.".format(av = av_dur))

def slave_rank(comm):
    signal = numpy.zeros([1])

    comm.Recv([signal, MPI.DOUBLE], source = 0, tag = 0)

    response = numpy.array([2.0])

    comm.Send([response, MPI.DOUBLE], dest = 0, tag = 0)


def ping_pong():
    comm = MPI.COMM_WORLD

    rank = comm.Get_rank()

    if rank == 0:
        master_rank(comm)
    else:
        slave_rank(comm)


ping_pong()
