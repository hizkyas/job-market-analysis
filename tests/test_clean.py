# tests/test_clean.py
from scripts.clean_data import (
    parse_salary,
)  # We’ll make parse_salary function importable


def test_parse_salary():
    assert parse_salary("$120,000") == 120000
    assert parse_salary("100000") == 100000
    assert parse_salary(None) is None
