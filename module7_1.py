class Product():
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self, __file_name = 'products.txt'):
        self.__file_name = __file_name

    def read_file(self):
        file = open(self.__file_name, 'r')
        content = file.read()
        file.close()
        return content

    def get_products(self):
        return self.read_file()


    def add(self, *products):
        existing_products = self.read_file()
        file = open(self.__file_name, 'a')
        for product in products:
            product_str = str(product) + '\n'
            if product.name in existing_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(product_str)
                existing_products += str(product)
        file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

