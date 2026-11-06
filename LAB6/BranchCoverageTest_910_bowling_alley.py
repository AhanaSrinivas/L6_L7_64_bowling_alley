"""Branch coverage suite: cover both outcomes of every decision branch."""

import pytest

from bowling_alley import frame_score, lane_assignment, lane_cost


@pytest.mark.parametrize("day_type", ["weekday", "weekend"])
def test_lane_rate_choices(day_type):
    assert lane_cost(day_type, 1, 1, 0, False) in (400, 600)


@pytest.mark.parametrize("games,players", [(1, 1), (0, 1), (1, 0), (1, 7)])
def test_booking_limits(games, players):
    if games < 1 or players < 1 or players > 6:
        with pytest.raises(ValueError, match="invalid booking"):
            lane_cost("weekday", games, players, 0, False)
    else:
        assert lane_cost("weekday", games, players, 0, False) == 400


def test_shoe_rentals_limit_and_member_discount():
    with pytest.raises(ValueError, match="unknown day type"):
        lane_cost("holiday", 1, 2, 0, False)
    with pytest.raises(ValueError, match="too many shoe rentals"):
        lane_cost("weekday", 1, 2, 3, False)
    assert lane_cost("weekday", 1, 2, 1, False) == 450
    assert lane_cost("weekday", 1, 2, 1, True) == 360


def test_group_surcharge_boundary():
    assert lane_cost("weekday", 1, 4, 0, False) == 400
    assert lane_cost("weekday", 1, 5, 0, False) == 500


def test_frame_validation_and_scoring_branches():
    for first, second in [(-1, 0), (11, 0), (0, -1)]:
        with pytest.raises(ValueError, match="invalid roll"):
            frame_score(first, second, [])
    assert frame_score(10, 0, [5, 4]) == 19
    with pytest.raises(ValueError, match="invalid frame"):
        frame_score(8, 3, [])
    assert frame_score(6, 4, [8]) == 18
    assert frame_score(3, 4, []) == 7


def test_lane_assignment_decisions():
    assert lane_assignment(2, False, 0) == "wait"
    assert lane_assignment(2, True, 1) == "bumper lane"
    assert lane_assignment(7, False, 2) == "two lanes"
    assert lane_assignment(7, False, 1) == "wait"
    assert lane_assignment(6, False, 1) == "standard lane"
