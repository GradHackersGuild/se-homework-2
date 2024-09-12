import random

def random_array(arr)-> list[int]:
    shuffled_num = None
    for i in range(len(arr)):
        arr[i] = random.randint(1,20)
    return arr
