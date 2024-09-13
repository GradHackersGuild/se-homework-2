import hw2_debugging as OP

def test_mergesort1():
    arr = [10, 12, 2, 4, 1, 14, 10, 15, 16, 7, 9, 10]
    assert OP.mergeSort(arr) == [1, 2, 4, 7, 9, 10, 10, 10, 12, 14, 15, 16]

def test_mergesort2():
    arr = [8, 12, 2, 1, 4, 10, 14, 15, 20, 7, 9, 4]
    assert OP.mergeSort(arr) == [1, 2, 4, 4, 7, 8, 9, 10, 12, 14, 15, 20]

def test_mergesort3():
    arr = [12, 14, 10, 20, 17, 7, 13, 8, 9, 8, 10, 10, 6, 3, 7, 5, 15, 6, 18, 6]
    assert OP.mergeSort(arr) == [3, 5, 6, 6, 6, 7, 7, 8, 8, 9, 10, 10, 10, 12, 13, 14, 15, 17, 18, 20]