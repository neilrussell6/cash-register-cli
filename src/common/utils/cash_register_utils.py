"""Cash Register utility functions."""

from src.common.models import ReceiptItem


def build_receipt(quantities, inventory):
    """Build a sequence of receipt items using provided quantities and inventory."""
    return tuple(
        ReceiptItem(v, inventory[k].label, inventory[k].unitprice * v)
        for k, v in quantities.items()
    )


def calculate_receipt_total(receipt):
    """Calculate total of all items in provided receipt."""
    return sum([n.unitprice for n in receipt])


def _calculate_denoms(n, denoms):
    """Split the provided n amount into a sequence denominations."""
    if n == 0 or len(denoms) == 0:
        return []
    x = denoms[0]
    if n < x:
        return _calculate_denoms(n, denoms[1:])
    return [x, *_calculate_denoms(n - x, denoms)]


def calculate_change(total, received, denoms):
    """Calculate change in the form of a sequence of denominations."""
    change = received - total
    return _calculate_denoms(change, denoms)
