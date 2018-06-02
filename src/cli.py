"""Command line interface for Cash Register."""

import locale
import logging

import click
import click_log

from src.bill.main import new_bill

logger = logging.getLogger(__name__)
click_log.basic_config(logger)

locale.setlocale(locale.LC_ALL, '')


@click.group()
@click.version_option(version='0.1.0')
def cli():
    """Cash Register CLI."""
    pass


@cli.command()
@click_log.simple_verbosity_option(logger)
def bill():
    """Bill command.

    Allows creating of an itemized bills.
    Calculates total and change in available denominations.
    """
    new_bill()


if __name__ == '__main__':
    cli()
