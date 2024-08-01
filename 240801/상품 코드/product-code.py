class Product():
    def __init__(self, name="", code=0):
        self.name = name
        self.code = code
    
    def print_info(self):
        print("product", self.code, "is", self.name)

product1 = Product("codetree", 50)
product2 = Product()
product2_name, product2_code = input().split()
product2.name = product2_name
product2.code = int(product2_code)

product1.print_info()
product2.print_info()