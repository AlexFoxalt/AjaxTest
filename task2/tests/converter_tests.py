import pytest

from task2.converter import converter


@pytest.mark.parametrize('dd, expected', [(-180, "180^0W"),
                                          (-180.0, "180^0W"),
                                          (-13.912, "13^54.72W"),
                                          (0, "0^0E"),
                                          (180.0, "180^0E"),
                                          (180, "180^0E"),
                                          (170.0323, "170^1.938E")])
def test_converter(dd, expected):
    response = converter(dd)
    assert response == expected, f"Response does not equal to expected one!\n" \
                                 f"Response\t\t{response}\n" \
                                 f"Expected\t\t{expected}"
