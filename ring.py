import mpi4py
from mpi4py import MPI
import numpy
import time
import sys

def Pass_the_parcel(start_rank):
    '''Function to pass a signal around processors in a ring. The first signal is an 
       integer with value "1". At the n'th processor the signal is multiplied by the 
       n'th prime

       start_rank = Rank at which signal starts
    '''

    comm = MPI.COMM_WORLD

    n_ranks = comm.Get_size()

    primes = numpy.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    if n_ranks > primes.size:
        print("Number of processors must be less than or equal to 10")
        sys.exit()

    for i in range(n_ranks):
        rank = comm.Get_rank()

Pass_the_parcel(0)
