from views import CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DestroyMixin
# from registration import User
import json

# class Cars(CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DestroyMixin, User):
    
#     def save(self):
#         with open('data1.json', 'w') as file:
#             json.dump(self.objects, file)
#         return {'msg': 'saved'}
    
#     def __init__(self, brand, model, year, engine, color, body, mileage, price):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.engine = engine
#         self.color = color
#         self.body = body
#         self.mileage = mileage
#         self.price = price




# log = User()
# print(log.register('JohnSnowNothing4567', 'qwerty1234', 'qwerty1234'))
# print(log.login('JohnSnowNothing4567', 'qwerty1234'))













class Cars(CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DestroyMixin):
    def save(self):
        with open('data1.json', 'w') as file:
            json.dump(self.objects, file)
        return {'msg': 'saved'}

class Order:
    discount = 5
    def __init__(self) -> None:
        self.orders = []
        self.product = Cars()
        self.product.post(title = 'Iphone 14 Pro Max', description = 'The best new phone!', qty = 5, price = 1300)
        self.product.post(title = 'Samsung S22 Ultra', description = 'The best new phone by Samsung', qty = 10, price = 900)

    def create_order(self, objects):
        ls = []
        for item in objects:
            for product in self.product.objects:
                if item['id'] == product['id']:
                    self.subtract_qty(item, product)
                    ls.append({'title': product['title'], 'qty': item['qty'], 'price': product['price']})
        self.orders.append(ls)
        money = self.total_count(ls)
        return {'Order': ls, 'Total sum': money}

    def total_count(self, objects):
        total_count = 0
        for product in objects:
            price = product['price']
            qty = product['qty']
            total_count += self.make_discount(price, self.discount) * qty
        return total_count

    def subtract_qty(self, item, product):
        result = product['qty'] - item['qty']
        if result < 0:
            raise Exception('Too many qty or product!')
        product['qty'] = result

    def make_discount(self, price, percent):
        return price - (price / 100 * percent)

orders = Order()
print('Before: ', orders.product.objects)
products = [{'id': 1, 'qty': 3}, {'id': 2, 'qty': 2}]
print(orders.create_order(products))
print('After: ', orders.product.objects)

# cars = Cars()
# print(cars.post(title = 'Iphone 14 Pro Max', description = 'The best new phone!', qty = 5, price = 1300))
# print(cars.post(title = 'Redmi Note 10', description = 'The best phone for own price!', qty = 10, price = 300))
# print(cars.get())
# print(cars.patch(2, title = 'Redmi Note 100'))
# print(cars.get_detail(2))
# print(cars.delete(2))
# print(cars.get())
# print(cars.post(title = 'Samsung S22 Ultra', description = 'The best new phone by Samsung', qty = 10, price = 900))
# print(cars.save())