"""Unit tests for Money utility functions."""

import locale

import pytest

from src.common.utils.money_utils import format_money


@pytest.mark.parametrize('locale_value,int_amount,expected_result', (
    ('en_US.UTF-8', 2000, '$20.00'),
    ('en_US.UTF-8', 3599, '$35.99'),
    ('en_ZA.UTF-8', 52001, 'R520.01'),
    ('en_GB.UTF-8', 97, '£0.97'),
))
def test_format_money_returns_format_int_as_expected_string(
    locale_value, int_amount, expected_result,
):
    """Should return format int as expected string."""
    # given ... locale is set to that provided
    locale.setlocale(locale.LC_ALL, locale_value)

    # when ... we format the provided integer
    # then ... should return string formatted as expected
    assert format_money(int_amount) == expected_result
