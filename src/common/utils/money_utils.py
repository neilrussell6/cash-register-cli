"""Money utility functions."""

import locale


def format_money(int_amount):
    """Format provided integer as currency using locale."""
    return locale.currency(int_amount / 100)
