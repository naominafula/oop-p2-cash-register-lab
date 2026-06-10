#!/usr/bin/env python3

class CashRegister:
  pass
#!/usr/bin/env python3

class CashRegister:
    """A simple cash register for adding items, applying discounts, and voiding transactions."""

    def __init__(self, discount=0):
        """Initialize the cash register.

        discount: optional percentage discount to apply later (0-100).
        total: running total cost of items.
        items: list of item names added to the register.
        previous_transactions: list of transaction records for voiding.
        """
        self._discount = 0
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        """Return the current discount percentage."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """Validate and set the discount percentage."""
        if not isinstance(value, int):
            print("Not valid discount")
            self._discount = 0
            return

        if value < 0 or value > 100:
            print("Not valid discount")
            self._discount = 0
            return

        self._discount = value

    def add_item(self, item, price, quantity=1):
        """Add an item to the register.

        item: item name string.
        price: price for one unit.
        quantity: number of the same item to add.
        """
        # update the total price for the amount of items added
        self.total += price * quantity

        # add item names into the `items` list for each quantity
        for _ in range(quantity):
            self.items.append(item)

        # store the transaction so it can be voided later
        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity,
        }
        self.previous_transactions.append(transaction)

    def apply_discount(self):
        """Apply the current discount to the total.

        If no valid discount is set or no transactions exist, print a message.
        """
        if self.discount == 0 or not self.previous_transactions:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total = round(self.total - discount_amount, 2)
        print(f"After the discount, the total comes to ${int(self.total) if self.total.is_integer() else self.total}.")

    def void_last_transaction(self):
        """Remove the most recent transaction and update total/items."""
        if not self.previous_transactions:
            return

        last_transaction = self.previous_transactions.pop()
        item = last_transaction["item"]
        price = last_transaction["price"]
        quantity = last_transaction["quantity"]

        # subtract the amount for the last transaction
        self.total -= price * quantity
        self.total = round(self.total, 2)

        # remove the last added item names for that transaction
        for _ in range(quantity):
            if item in self.items:
                self.items.remove(item)