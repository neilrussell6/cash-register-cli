"""Money utility functions."""

import locale


def format_money(int_amount):
    return locale.currency(int_amount / 100)
