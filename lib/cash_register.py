#!/usr/bin/env python3

class CashRegister:
    
    def __init__(self, discount = 0):  # when adding a default, it says that param is optional
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_tranactions = []

    def add_item(self, title, price, qty = 1):
        self.total += price * qty
        # self.items.append((title, price, qty))
        for _ in range(qty):
            self.items.append(title)
        self.previous_tranactions.append(
            {'title': title, 'price': price, 'qty': qty}
        )

    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * ((100 - self.discount) / 100))
            print(f"After the discount, the total comes to ${self.total}.")  #learn morea about :.2f/ formatters
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.previous_tranactions:
            return "There are no transactions to void."
        self.total -= (
            self.previous_tranactions[-1]["price"]
            * self.previous_tranactions[-1]["qty"]
        )
        for _ in range(self.previous_tranactions[-1]["qty"]):
            self.items.pop()
        self.previous_tranactions.pop()

cash_register_with_discount = CashRegister(20)
cash_register_with_discount.add_item("book", 5.00, 3)
cash_register_with_discount.add_item("Lucky Charms", 4.5)
print(cash_register_with_discount)
