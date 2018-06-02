"""Command line interface for Cash Register."""

import logging

import click
import click_log

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


@click.group()
@click.version_option(version='0.1.0')
def cli():
    pass


if __name__ == '__main__':
    cli()
