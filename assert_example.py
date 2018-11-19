products = {'Apple': 10, 'Orange': 20}


def make_discount(product, discount):
    products[product] = products[product] - discount
    assert 0 <= products[product]


print(products)
make_discount('Apple', 2)
make_discount('Apple', 20)
print(products)

counter = 10
assert (counter == 9, 'Error')  # dont write tuple in assert, its always True


