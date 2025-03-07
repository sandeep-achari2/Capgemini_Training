
# Transaction Class
class Transaction:
    def __init__(self, transaction_id, customer, order):
        self.transaction_id = transaction_id
        self.customer = customer
        self.order = order

    def get_transaction_details(self):
        return {
            "Transaction ID": self.transaction_id,
            "Customer Name": self.customer.name,
            "Order ID": self.order.order_id,
            "Total Amount": self.order.total_item_prices(),
            "Order Details": [
                {
                    "Product ID": item.product_id,
                    "Quantity": item.quantity,
                    "Price": item.get_total()
                } for item in self.order.list_items
            ]
        }