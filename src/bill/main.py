"""Bill command main process."""

from collections import Counter, defaultdict

import click

from src.common import data
from src.common.data import print_tpl_receipt_item_qty_label
from src.common.utils.cash_register_utils import build_receipt, calculate_change, calculate_total
from src.common.utils.money_utils import format_money
from src.common.utils.print_utils import format_bill_heading, format_receipt


def new_bill(bill_id=None):
    """New bill process."""

    if not bill_id:
        bill_id = 1

    # heading
    click.echo('\n'.join(format_bill_heading(bill_id)))

    # quantities
    quantities = new_bill_item()

    # build receipt
    receipt = build_receipt(quantities, data.inventory)

    # total
    total_due = calculate_total(receipt)
    click.echo('amount due is {}'.format(format_money(total_due)))

    # amount received
    amount_received = int(click.prompt('amount received', type=float) * 100)

    # change
    change = calculate_change(total_due, amount_received, data.denominations)
    change_total = sum(change)
    change_denominations = (
        print_tpl_receipt_item_qty_label.format(n, format_money(denom))
        for denom, n in Counter(change).items()
    )
    click.echo('change is {}'.format(format_money(change_total)))
    click.echo('  \n'.join(change_denominations))

    # print receipt
    if click.confirm('print receipt?', default=True):
        click.echo('\n'.join(format_receipt(receipt, total_due, amount_received, change_total)))

    # another new bill?
    if not click.confirm('create another new bill?', default=True):
        return

    return new_bill(bill_id + 1)


def new_bill_item(quantities=None):
    """New bill item process."""

    if not quantities:
        quantities = defaultdict(int)

    # new item
    item_key = click.prompt('new item', type=click.Choice(data.inventory.keys()))

    # quantity
    quantity = click.prompt('quantity', type=int, default=1)
    quantities[item_key] += quantity
    if quantities[item_key] <= 0:
        del quantities[item_key]

    # another new item?
    if not click.confirm('add another new new item?', default=True):
        return quantities

    return new_bill_item(quantities)
