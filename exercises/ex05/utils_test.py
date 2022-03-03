"""Ex05 utils_test.py"""

__author__ = "730411898"

def test_only_evens_edge() -> None:
    assert only_evens([]) == []

def test_only_evens_use1() -> None:
    assert only_evens([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8]

def test_only_evens_use2() -> None:
    assert only_evens([100, 101, 102, 103, 104]) == [100, 102, 104]

def test_sub_edge() -> None:
    assert sub([], 1, 3) == []

def test_sub_use1() -> None:
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]

def test_sub_use2() -> None:
    assert sub([1, 2, 3, 4], 1, 3) == [2, 3]

def test_concat_edge() -> None:
    assert concat([], []) == []

def test_concat_use1() -> None:
    assert concat([1,2], [3,4]) == [1,2,3,4]

def test_concat_use2() -> None:
    assert concat([100, 200], [300, 400]) == [100, 200,300,400]





