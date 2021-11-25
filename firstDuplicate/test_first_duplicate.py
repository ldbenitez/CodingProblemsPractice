from first_duplicate import solution

def test_one_or_more_duplicates():
    assert solution([3,4,5,4,7,8,7]) == 4

def test_one_duplicate():
    assert solution([3,3]) == 3

def test_no_duplicates():
    assert solution([1,2,4,6,7,9]) == -1