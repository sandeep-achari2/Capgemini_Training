
# Order Items Class
class Order_items:
    def __init__(self, order_id, product_id, quantity, price_list, discount):  # Fixed '__init__'
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price_list = price_list
        self.discount = discount

    def get_total(self):
        return self.quantity * self.price_list * (1 - self.discount / 100)
