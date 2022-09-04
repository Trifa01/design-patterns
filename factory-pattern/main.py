# Abstract class of Product 
from abc import ABC, abstractmethod
from argparse import ArgumentParser

class Product(ABC):
    @abstractmethod
    def do_something(self)->str:
        pass

# 2 types for Products 
class ProductOne(Product):
    def do_something(self):
        return 'Am Product One'

# Creator function that returns a Product type 
def create_product()->Product:
    # parser = ArgumentParser()
    # parser.add_argument("-productNumber")
    # args = parser.parse_args()
    products_dict = {"one": ProductOne()}
    return products_dict["one"]
def main():
    product = create_product()
    msg = product.do_something()
    print(msg)

if __name__ == "__main__":
    main()