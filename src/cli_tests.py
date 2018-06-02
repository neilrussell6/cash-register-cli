"""End to end tests for Cash Register CLI."""

from click.testing import CliRunner

from src import data
from src.cli import bill
from src.models import InventoryItem


def test_bill_command_runs(monkeypatch):
    """Should successfully run."""
    # given ... item with key 'coffee' is available in the inventory
    mock_inventory = {
        'coffee': InventoryItem('Coffee', 2500),
    }
    monkeypatch.setattr(data, 'inventory', mock_inventory)

    # when ... we run command with a valid series of inputs
    runner = CliRunner()
    inputs = (
        'coffee',  # item
        '2',  # quantity
        'n',  # no more items
        '30',  # amount received
        'n',  # don't print receipt
        'n',  # no more bills
    )
    result = runner.invoke(bill, input='\n'.join(inputs))

    # then ... should successfully run
    assert result.exit_code == 0
