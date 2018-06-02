"""Print utility functions."""

from src.common import data
from src.common.data import print_tpl_receipt_item, print_tpl_receipt_item_qty_label
from src.common.utils.money_utils import format_money


def format_bill_heading(id):
    return (
        data.print_tpl_heading.format(f' BILL {id} '),
        '-' * 35,
    )


def format_receipt(receipt, total_due, amount_received, change_total):
    formatted_receipt = (
        print_tpl_receipt_item.format(
            print_tpl_receipt_item_qty_label.format(n.quantity, n.label),
            format_money(n.unitprice),
        )
        for n in receipt
    )
    return (
        '=' * 35,
        *formatted_receipt,
        '-' * 35,
        print_tpl_receipt_item.format('total', format_money(total_due)),
        print_tpl_receipt_item.format('paid', format_money(amount_received)),
        print_tpl_receipt_item.format('change', format_money(change_total)),
        '=' * 35,
    )
