from DatabaseServices import *
from Product import *

productService = ProductSevice()

products = productService.getAllProduct()

for product in products:
    print(product.name)