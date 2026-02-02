"""
import time
import multiprocessing


if __name__ == "__main__":  # Use if __name__ == "__main__" (Required on Windows) Even in Jupyter, multiprocessing should be protected:

    start = time.perf_counter()

def test_func():
    print("do something")
    print("sleep for 1 sec")
    time.sleep(1)
    print("done with sleeping")
test_func()
test_func()
end = time.perf_counter()

print(f"The program finished in {round(end-start, 2)} seconds")



import multiprocessing

import time


def test_func():
    print("do something")
    print("sleep for 1 sec")
    time.sleep(1)
    print("done with sleeping")

if __name__ == "__main__":        # <---- MOST IMPORTANT - ANY line that creates Process or Pool MUST be inside if __name__ == "__main__":

    start = time.perf_counter()

    p1 = multiprocessing.Process(target = test_func)
    p2 = multiprocessing.Process(target = test_func)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
        

    end = time.perf_counter()

    print(f"The program finished in {round(end-start, 2)} seconds")



import multiprocessing

import time


def test_func():
    print("do something")
    print("sleep for 1 sec")
    time.sleep(1)
    print("done with sleeping")


if __name__ == "__main__":        # <---- MOST IMPORTANT - ANY line that creates Process or Pool MUST be inside if __name__ == "__main__":

    start = time.perf_counter()

    processes = []
    for i in range(10):
        p = multiprocessing.Process(target = test_func)
        p.start()
        processes.append(p)
        
    for process in processes:
        process.join()

        

    end = time.perf_counter()

    print(f"The program finished in {round(end-start, 2)} seconds")




#multiprocessing>> should be used in case of computation
#use case 1:


import multiprocessing
import time


def square(index, value):
    value[index] = value[index] ** 2


if __name__ == "__main__":
    
    start = time.perf_counter()
    arr = multiprocessing.Array('i', [1, 2, 5, 3, 40000000000])


    processes = []
    for i in range(5): #in array 5 nos, therefore loop will be in range(5)
        p4 = multiprocessing.Process(target = square, args = (i, arr))
        p4.start()
        processes.append(p4)
        
    for process in processes:
        process.join()

    print(list(arr))

        

    end = time.perf_counter()

    print(f"The program finished in {round(end-start, 2)} seconds")



#using multiprocessing.pool

import multiprocessing
import time

def square1(no):
    result = no*no
    print(f"The square of {no} is {result}  .")

if __name__ == "__main__":

    start = time.perf_counter()

    numbers = [1, 2, 3, 4, 6000]

    with multiprocessing.Pool() as pool:
        pool.map(square1, numbers)
        
    end = time.perf_counter()

    print(f"The program finished in {round(end-start, 2)} seconds")



# no order in the results shows multiple core/processors being used and result returned not sequentially>>parallel execution of the code


#use case 2:
#say you want to get admission is a school
#you will make a enrollment request in a queue
#these requests will be processed from the queue and registration will be done

#These enrollment and registration tasks can run in parallel
#this means while one process is busy putting the requests into the queue, the other process
#can be busy processing those request


import multiprocessing

def enroll_students(student_queue):
    for student in ["Rahul", "Rohit", "Aman", "Ajay"]:
        student_queue.put(f"enroll request for {student}")
        
def register_students(student_queue):
    while True:
        enrollment_req = student_queue.get()
        if enrollment_req is None:
            break
        print(f"Register the enrollment request: {enrollment_req}")
        
if __name__ == "__main__":

    student_queue = multiprocessing.Queue() #multiprocessing has data structure queue
    enrollment_process = multiprocessing.Process(target = enroll_students, args = (student_queue,))
    reg_process = multiprocessing.Process(target = register_students, args = (student_queue,))
    
    enrollment_process.start()
    reg_process.start()
    
    enrollment_process.join()
    reg_process.join()


"""

#using concurrent.futures process pool
import concurrent.futures

import time
start = time.perf_counter()

def test_func(i):
    print("do something")
    print("sleep for 1 sec")
    time.sleep(1)
    print("done with sleeping")

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(test_func, range(10))

    

end = time.perf_counter()

print(f"The program finished in {round(end-start, 2)} seconds")








