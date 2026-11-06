"""Code coverage suite: exercise each application statement at least once."""

import pytest

from bowling_alley import frame_score, lane_assignment, lane_cost


def test_weekday_booking_example():
    assert lane_cost("weekday", 2, 4, 2, False) == 900


def test_weekend_large_group_and_member_discount():
    assert lane_cost("weekend", 2, 5, 3, True) == 1240


@pytest.mark.parametrize("args", [
    ("holiday", 1, 2, 0, False),
    ("weekday", 0, 2, 0, False),
    ("weekday", 1, 0, 0, False),
    ("weekday", 1, 7, 0, False),
    ("weekday", 1, 2, 3, False),
])
def test_invalid_bookings(args):
    with pytest.raises(ValueError):
        lane_cost(*args)


def test_open_frame_and_spare():
    assert frame_score(3, 4, []) == 7
    assert frame_score(6, 4, [8]) == 18


def test_strike_frame():
    assert frame_score(10, 0, [7, 2]) == 19


@pytest.mark.parametrize("first,second", [(-1, 0), (11, 0), (2, -1)])
def test_invalid_roll(first, second):
    with pytest.raises(ValueError, match="invalid roll"):
        frame_score(first, second, [])


def test_invalid_frame_total():
    with pytest.raises(ValueError, match="invalid frame"):
        frame_score(8, 3, [])


def test_lane_assignment_options():
    assert lane_assignment(3, False, 0) == "wait"
    assert lane_assignment(3, True, 1) == "bumper lane"
    assert lane_assignment(8, False, 2) == "two lanes"
    assert lane_assignment(8, False, 1) == "wait"
    assert lane_assignment(4, False, 1) == "standard lane"
