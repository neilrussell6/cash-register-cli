"""Unit tests for Cash Register utility functions."""
import pytest

from src.models import InventoryItem, ReceiptItem
from src.utils.cash_register_utils import (
    _calculate_denoms,
    build_receipt,
    calculate_change,
    calculate_total,
)


def test_build_receipt_builds_as_expected():
    """Should build expected receipt for provided quantities and inventory."""

    # when
    # ... we build a receipt consisting of 3 coffees and 2 teas
    # ... and both are available in our inventory
    inventory = {
        'coffee': InventoryItem('Black Coffee', 2500),
        'tea': InventoryItem('Fancy Tea', 1750),
    }
    quantities = {'coffee': 3, 'tea': 2}
    result = build_receipt(quantities, inventory)

    # then ... should build expected receipt
    assert result == (
        ReceiptItem(3, 'Black Coffee', 2500),
        ReceiptItem(2, 'Fancy Tea', 1750),
    )


@pytest.mark.parametrize('receipt,expected', (
    # 1. 1 coffee
    (
        (
            ReceiptItem(1, 'Black Coffee', 7500),
        ),
        7500,
    ),
    # 2. 3 coffees & 2 teas
    (
        (
            ReceiptItem(3, 'Black Coffee', 7500),
            ReceiptItem(2, 'Fancy Tea', 3500),
        ),
        11000,
    ),
))
def test_calculate_total_returns_expected_result(receipt, expected):
    """Should calculate total as expected for provided receipt."""

    # when ... we calculate total with the provided receipt
    result = calculate_total(receipt)

    # then ... should calculate expected total
    assert result == expected


@pytest.mark.parametrize('change_amount,possible_denoms,expected', (
    # 1. 20 change, only 10s, 5s & 2s available, should return two 10s
    (20, (10, 5, 2), [10, 10]),
    # 2. 27 change, only 20s, 5s & 2s available, should return one 20, three 5s & one 2
    (37, (20, 5, 2), [20, 5, 5, 5, 2]),
    # # 3. 8 change, only 10s, 5s, 2s & 1s available, should return one 5, one 2 & one 1
    (8, (10, 5, 2, 1), [5, 2, 1]),
))
def test_calculate_denoms_returns_expected_value(change_amount, possible_denoms, expected):
    """Should calculate expected change denoms for provided change amount and possible denoms."""

    # when ... we calculate denoms for provided change amount and possible denoms
    result = _calculate_denoms(change_amount, possible_denoms)

    # then ... should calculate expected change denoms
    assert result == expected


# TODO: calculate_denoms: test case where sufficient denoms are not available to provide correct change  # noqa

def test_calculate_change_returns_expected_value():
    """Should return expected value."""

    # when
    # ... we calculate change for 110.00, having received 200.00 as payment
    # ... and we have 20s, 10s, 5s, 2s & 1s available
    denoms = (20, 10, 5, 2, 1)
    total = 110
    received = 200
    result = calculate_change(total, received, denoms)

    # then ... should return correct change split into correct denoms
    assert result == [20, 20, 20, 20, 10]

# TODO: calculate_denoms: test case where sufficient denoms are not available to provide correct change  # noqa

# TODO: calculate_denoms: test case where insufficient amount is received  # noqa
