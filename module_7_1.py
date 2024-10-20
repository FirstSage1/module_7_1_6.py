# Модуль 7_1 Режимы открытия файлов.
# =======================================
class Shop:
    def __init__(self):
        self.__file_name =  'products.txt'

    def get_products(self):# возвращает строку со всеми товарами из файла __file_name
        file1 = open(self.__file_name, 'r')
        product = file1.read()
        file1.close()
        return product

    def add(self, *products): # Добавляет в файл __file_name каждый продукт
        # из products, если его ещё нет в файле (по названию).
        file = open(self.__file_name, 'r+')
        for i in products:
            if str(i) in self.get_products(): # Если такой продукт уже есть,
                                             # то не добавляет и выводит строку
                                         # 'Продукт <название> уже есть в магазине'
                print(f"Продукт {str(i)} уже есть в магазине")
            else:
                file.write(str(i) + '\n')
        file.close()


class Product:
    def __init__(self, name, weight, category):
        self.name = name            # название продукта (строка).
        self.weight = weight        # общий вес товара (дробное число)
        self.category = category    # категория товара (строка)

    def __str__(self): # возвращает строку в формате '<название>, <вес>, <категория>
        return f'{self.name}, {self.weight}, {self.category}'


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
#
print(p2)  # __str__
#
s1.add(p1, p2, p3)
#
print(s1.get_products())
