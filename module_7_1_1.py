class Product:

    def __init__(self, name, weight, category):

        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:

    __file_name = 'products.txt'

    def get_products(self):

        file = open(self.__file_name, 'r' )
        get_prod = file.read()
        file.close()

        return get_prod

    def add(self, *products):

        product_shop = self.get_products()
        file = open(self.__file_name, 'a')
        m = 0

        for _ in products:

            str_products = str(products[m])
            list_products = str_products.split(', ')
            name = list_products[0]

            if name in product_shop:
                print(f'Продукт {name} уже есть в магазине')

            else:
                file.write(str_products + '\n')

            m += 1

        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
