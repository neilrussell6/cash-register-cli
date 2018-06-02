from collections import namedtuple

ReceiptItem = namedtuple('ReceiptItem', ('quantity', 'label', 'unitprice'))
InventoryItem = namedtuple('Receipt', ('label', 'unitprice'))
