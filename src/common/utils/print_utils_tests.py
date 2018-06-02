"""Unit tests for Print utility functions."""
import locale

from src.common.models import ReceiptItem
from src.common.utils.print_utils import format_bill_heading, format_receipt


def test_format_bill_heading_returns_heading_formatted_as_expected():
    """Should return heading formatted as expected."""
    assert format_bill_heading(123) == (
        '============ BILL 123 =============',
        '-----------------------------------',
    )


def test_format_receipt_return_receipt_formatted_as_expected():
    """Should return receipt formatted as expected."""
    # given ... locale is set to that EN ZA
    locale.setlocale(locale.LC_ALL, 'en_ZA.UTF-8')

    # when ... we format the following receipt
    receipt = (
        ReceiptItem(3, 'Black Coffee', 7500),
        ReceiptItem(2, 'Fancy Tea', 3500),
    )
    total_due = 2500
    amount_received = 3000
    change_total = 500
    result = format_receipt(receipt, total_due, amount_received, change_total)

    # then ... should format as expected
    assert result == (
        '===================================',
        '3 x Black Coffee     R75.00',
        '2 x Fancy Tea        R35.00',
        '-----------------------------------',
        'total                R25.00',
        'paid                 R30.00',
        'change               R5.00',
        '===================================',
    )
