from src.common.models import InventoryItem

inventory = {
    'americano': InventoryItem('Americano', 2500),
    'cappuccino': InventoryItem('Cappuccino', 3790),
    'blacktea': InventoryItem('Black Tea', 1580),
    'greentea': InventoryItem('Green Tea', 1255),
}

denominations = [2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print_tpl_heading = '{:=^35}'
print_tpl_subheading = '{: ^35}'
print_tpl_receipt_item = '{:<20} {}'
print_tpl_receipt_item_qty_label = '{} x {}'
