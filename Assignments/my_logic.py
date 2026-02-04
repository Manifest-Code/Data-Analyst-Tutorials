#Another way

from memory_profiler import profile



@profile

def create_list():

    a = [i for i in range(100000)]   # creates a big list

    b = [i * 2 for i in range(50000)]

    return a, b



create_list()