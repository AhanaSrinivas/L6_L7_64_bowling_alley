"""Hypothesis properties for the three bowling alley input functions."""

from hypothesis import given, strategies as st

from processor import format_player_name, parse_frame, parse_scoreboard


@given(st.one_of(st.text(), st.none(), st.integers(), st.lists(st.text())))
def test_format_player_name_never_crashes(value):
    try:
        result = format_player_name(value)
    except Exception as exc:
        assert False, f"format_player_name crashed for {value!r}: {exc}"
    assert isinstance(result, str)
    assert len(result) <= 10


@given(st.one_of(st.text(), st.none(), st.integers(), st.lists(st.integers())))
def test_parse_frame_never_crashes(value):
    try:
        result = parse_frame(value)
    except Exception as exc:
        assert False, f"parse_frame crashed for {value!r}: {exc}"
    assert isinstance(result, tuple) and len(result) == 2
    first, second = result
    assert isinstance(first, int) and isinstance(second, int)
    assert 0 <= first <= 10 and 0 <= second <= 10
    assert first + second <= 10


@given(st.one_of(st.text(), st.none(), st.integers(), st.dictionaries(st.text(), st.integers())))
def test_parse_scoreboard_never_crashes(value):
    try:
        result = parse_scoreboard(value)
    except Exception as exc:
        assert False, f"parse_scoreboard crashed for {value!r}: {exc}"
    assert isinstance(result, dict)
    assert all(isinstance(name, str) and isinstance(score, int) for name, score in result.items())


def test_valid_examples_keep_expected_results():
    assert format_player_name("  aSHA pATEL  ") == "Asha Patel"
    assert parse_frame("X") == (10, 0)
    assert parse_frame("7/") == (7, 3)
    assert parse_frame("45") == (4, 5)
    assert parse_scoreboard("Asha:150,Ravi:132") == {"Asha": 150, "Ravi": 132}
