class Product:

 def __init__(self, Name_of_the_product, Description, Price, Category,Stock):
   self.Name_of_the_product = Name_of_the_product
   self.Description = Description 
   self.Price = Price
   self.Category = Category 
   self.Stock=Stock

 def showP(self):
   return f''' 
   Nombre de productos: {self.Name_of_the_product}
   Descripcion: {self.Description}
   Precio del producto: {self.Price}
   Categoria: {self.Category}
   Cantidad: {self.Stock}
   '''
