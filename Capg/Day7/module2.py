

# Order Details Class
class Order_details:
    def __init__(self, order_id, cust_id, order_status, order_date, store_id):
        self.order_id = order_id
        self.cust_id = cust_id
        self.order_status = order_status
        self.order_date = order_date
        self.store_id = store_id
        self.list_items = []  # Fixed list initialization

    def add_items(self, item):
        self.list_items.append(item)  # Fixed attribute name

    def total_item_prices(self):
        return sum(item.get_total() for item in self.list_items)  # Fixed loop variable
