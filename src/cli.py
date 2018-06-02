"""Command line interface for Cash Register."""

import locale
import logging
from collections import Counter, defaultdict
from datetime import datetime

import click
import click_log

from src import data
from src.utils.cash_register_utils import build_receipt, calculate_change, calculate_total

logger = logging.getLogger(__name__)
click_log.basic_config(logger)

locale.setlocale(locale.LC_ALL, '')


@click.group()
@click.version_option(version='0.1.0')
def cli():
    pass


@cli.command()
@click_log.simple_verbosity_option(logger)
def bill(**kwargs):
    """Create a new bill."""

    bill_id = 1
    add_bill = True
    add_item = True
    quantities = defaultdict(int)

    while add_bill:
        click.echo('============= BILL {} ============='.format(bill_id))
        click.echo(datetime.utcnow())

        while add_item:
            # new item
            item_key = click.prompt('new item', type=click.Choice(data.inventory.keys()))

            # quantity
            quantity = click.prompt('quantity', type=int, default=1)

            quantities[item_key] += quantity
            if quantities[item_key] <= 0:
                del quantities[item_key]

            # another new item?
            add_item = click.confirm('add another new new item?', default=True)

        # build receipt
        receipt = build_receipt(quantities, data.inventory)

        # total
        total_due = calculate_total(receipt)
        click.echo('amount due is {}'.format(locale.currency(total_due / 100)))

        # amount received
        amount_received = int(click.prompt('amount received', type=float) * 100)

        # templates
        receipt_item_tpl = '{:<20} {}'
        receipt_item_qty_label_tpl = '{} x {}'

        # change
        change = calculate_change(total_due, amount_received, data.denominations)
        change_total = sum(change)
        change_denominations = (
            receipt_item_qty_label_tpl.format(n, locale.currency(denom / 100))
            for denom, n in Counter(change).items()
        )
        click.echo('change is {}'.format(locale.currency(change_total / 100)))
        click.echo('  \n'.join(change_denominations))

        # print receipt
        print_receipt = click.confirm('print receipt?', default=True)

        if print_receipt:
            click.echo('=' * 35)
            formatted_receipt = (
                receipt_item_tpl.format(
                    receipt_item_qty_label_tpl.format(n.quantity, n.label),
                    locale.currency(n.unitprice / 100),
                )
                for n in receipt
            )
            click.echo('\n'.join(formatted_receipt))
            click.echo('-' * 35)
            click.echo(receipt_item_tpl.format('total', locale.currency(total_due / 100)))
            click.echo(receipt_item_tpl.format('paid', locale.currency(amount_received / 100)))
            click.echo(receipt_item_tpl.format('change', locale.currency(change_total / 100)))
            click.echo('=' * 35)

        # another new bill?
        add_bill = click.confirm('create another new bill?', default=True)
        add_item = add_bill
        if add_bill:
            bill_id += 1


if __name__ == '__main__':
    cli()
