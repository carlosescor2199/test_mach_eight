import pytest
from pairs import get_pairs

@pytest.mark.parametrize(
    "arr, num_sum, expected",
    [
        ([1, 9, 5, 0, 20, -4, 12, 16, 7], 12, [(0, 12), (-4, 16), (5, 7)]),
        ([10, 5, -7, 3, -5, 4, -2, 9, 1], 5, [(10, -5), (4, 1)]),
        ([15, 2, 10, -5, 5, 40, -20, -2], 20, [(15, 5), (40, -20)]),
        ([-1, 9, 5, -19, 20, -9, 12, 16, -15], -10, [(9, -19), (-1, -9), (5, -15)]),
        ([5, 10, 7, 20, -5, 12, -10, 14], 0, [(5, -5), (10, -10)]),
    ]
)
def test_get_pairs_multi(arr, num_sum, expected):
    assert get_pairs(arr, num_sum) == expected
