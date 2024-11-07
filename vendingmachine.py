class VendingMachine:
    def __init__(self, num_items, items_price):
        
        self.num_items = num_items
        self.items_price = items_price
    
    def __str__(self):
        return f"VendingMachine with {self.num_items} items, each priced at {self.items_price}"


    def buy(self,req_items,money):
        items = {}
        if req_items >self.num_items:
            raise(ValueError("Not Enough items"))
        total_cost = req_items*self.items_price

        if money<total_cost:
            raise(ValueError("Not Enough money to buy items"))
        else:
            self.num_items -= req_items
            change = money - total_cost

        print(f"Purchase successful! Change returned: {change}")
        print(f"Items remaining in the machine: {self.num_items}")

machine = VendingMachine(num_items=5, items_price=2)
machine.buy(req_items=2, money=100)
print(machine)



        