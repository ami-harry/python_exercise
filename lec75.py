# function caching
# function caching means that some function is taking some time to execute,
# if we want to use that function again between the processing time for another use ,
# we need to store it in some cache variable and make it use again if it is already running

from time import sleep
from functools import lru_cache


@lru_cache(maxsize=2)  # when the function runs, it will take as much time, but if we run again it will be very faster
def some_work(n):
    # some task taking n seconds
    sleep(n)
    print(f"some work function is running for {n} seconds parameter")
    return n


if __name__ == '__main__':
    print("now running some work")
    some_work(5)
    print("some work done...calling again")
    some_work(5)
    print("some work done...calling again")
    some_work(1)
    print("some work done...calling again")
    some_work(4)
    print("done again")
