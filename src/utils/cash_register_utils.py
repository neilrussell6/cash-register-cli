"""Cash Reigister utility functions."""

from src.models import ReceiptItem


def build_receipt(quantities, inventory):
    return tuple(
        ReceiptItem(v, inventory[k].label, inventory[k].unitprice)
        for k, v in quantities.items()
    )


def calculate_total(receipt):
    return sum([n.unitprice for n in receipt])


def _calculate_denoms(n, denoms):
    if n == 0 or len(denoms) == 0:
        return []
    x = denoms[0]
    if n < x:
        return _calculate_denoms(n, denoms[1:])
    return [x, *_calculate_denoms(n - x, denoms)]


def calculate_change(total, received, denoms):
    change = received - total
    return _calculate_denoms(change, denoms)
