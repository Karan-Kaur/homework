class CashRegister:
    def __init__(self):
        self.total_items = dict()
        self.total_price = 0
        self.discount = 0

    def add_item(self, item, price):
        self.total_items[item] = price

    def remove_item(self, item):
        del self.total_items[item]

    def apply_discount(self):
        discount = int(input('Percentage discount to be applied: 10, 20, 25, 50, 75: '))
        if discount == 10:
            self.discount= self.total_price * 0.10
            print('Discount applied: {}'.format(self.discount))
        elif discount == 20:
            self.discount= self.total_price * 0.20
            print('Discount applied: {}'.format(self.discount))
        elif discount == 25:
            self.discount= self.total_price * 0.25
            print('Discount applied: {}'.format(self.discount))
        elif discount == 50:
            self.discount= self.total_price * 0.50
            print('Discount applied: {}'.format(self.discount))
        elif discount == 75:
            self.discount= self.total_price * 0.75
            print('Discount applied: {}'.format(self.discount))
        else:
            pass

    def get_total(self):
        self.total_price = sum(self.total_items.values()) - self.discount
        print('Total price is: ', format(self.total_price, '.2f'))

    def show_items(self):
        print(self.total_items)

    def reset_register(self):
        deleted_dict= self.total_items.clear()
        print(deleted_dict) # double checking
        self.total_price = 0
        self.discount = 0

    def give_change(self):
        amount_given = float(input('Amount given by customer: '))
        if amount_given < self.total_price:
            print('Full amount has not been paid')
        else:
            change = amount_given - self.total_price
            print('Change to be given: ', (format(change, '.2f')))

#experimenting
shopping = CashRegister()
shopping.add_item('icecream', 2.60)
shopping.add_item('doughnuts', 1.50)
shopping.show_items()
shopping.reset_register() #None
shopping.add_item('banana', 0.60)
shopping.add_item('yoghurt', 1.20)
shopping.show_items()
shopping.remove_item('banana')
shopping.show_items()
shopping.add_item('strawberry', 1.20)
shopping.get_total()
shopping.apply_discount() #e.g. 50
shopping.get_total()
shopping.give_change()