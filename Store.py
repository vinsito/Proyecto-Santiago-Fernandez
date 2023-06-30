from Product import Product
from Sale import Sale
from Shipment import Shipment
from Payment import Payment
from Customer import Customer 
from Bill import Bill 
from Order import Order 
from datetime import datetime
from datetime import timedelta
import pickle
class Store:
  
    def __init__(self, products, new_products, customers, sales, payments, shipments):
      self.products = products
      self.new_products = new_products
      self.customers = customers
      self.sales = sales
      self.payments = payments
      self.shipments = shipments

###################################################################

#Esta funcion es para ingresar la antigua lista de productos en una nueva
    def initial_products(self):
      if len(self.new_products)==0:
        for Dicc in self.products:
          Name_of_the_product = Dicc['name']
          Description = Dicc['description']
          Price = Dicc['price']
          Category = Dicc['category']
          Stock=Dicc['quantity']
          initial_product = Product(Name_of_the_product, Description, Price, Category,Stock)
          self.new_products.append(initial_product)   
#Esto para poder visualizar los objetos agregados en caso de necesitarlo
    def ShowSt(self):
     for products in range(len(self.new_products)):
        print(f'{products +1}.{self.new_products[products].showP()}')

#######################GESTION DE PRODUCTOS#######################

#Esto para añadir productos, se pide al usuario ingresar los respectivos atributos del producto para luego agregar el objeto a la lista de productos
    def add_products(self):
      Name_of_the_product = input('Ingrese el nombre del producto: ')
      while Name_of_the_product == '':
        Name_of_the_product = input('INGRESE un nombre para el producto: ')
      Name_of_the_product = Name_of_the_product.capitalize()
      Description = input('Ingrese la descripción del producto: ')
      while Description == '':
        Description = input('INGRESE una Descripcion para el producto: ')
      Price = input('Ingrese el precio del producto: ')
      while not Price.isnumeric() or Price=='0':
        Price = input('Error! ingrese un precio valido: ')
      Category = input('Ingrese la categoria del producto: ')
      while not Category.isalpha():
        Category = input('Error! las categorias no pueden llevar numeros, reingrese la categoria del producto: ')
      Category = Category.capitalize()
      Stock = input('Ingrese la cantidad del producto que desea añadir: ')
      while not Stock.isnumeric():
        Stock = input('Error! ingrese una cantidad valida: ')
      last_added_product = Product(Name_of_the_product, Description, int(Price), Category, int(Stock))
      self.new_products.append(last_added_product)
      print('''      
       EL PRODUCTO HA SIDO AÑADIDO CORRECTAMENTE
      --------------------------------------------
      ''')

################################################################

#Esta funcion espara buscar productos en base al nombre, se ingresa el nombre del producto que se desea buscar, para luego busccarlo en la lista de objetos en self.new_products, el found es para en caso de que no lo encuentre printee que el objeto no ha sido encontrado. Si el objeto es encontrado se usa el .show del modulo de Product  
    def search_products_name(self):

      Name_of_the_product = input('Ingrese el nombre del producto que desea buscar: ')
      Name_of_the_product = Name_of_the_product.split()
      for j in range(len(Name_of_the_product)):
        Name_of_the_product[j] = Name_of_the_product[j].capitalize()
      Name_of_the_product = ' '.join(Name_of_the_product)
      found=False
      for names in self.new_products:
        
        if names.Name_of_the_product==Name_of_the_product:
          print('''
          Su producto es:
          ---------------''')
          print(names.showP())
          found=True
      if found==False:
        print('''
        El producto no ha sido encontrado
        ---------------------------------
        ''')

#################################################################
  
#Este es exactamente el codigo anterior pero ahora busca por categoria 
    def search_products_category(self):
      Category_of_the_product = input('Ingrese la categoria del producto que desea buscar: ')
      Category_of_the_product = Category_of_the_product.split()
      for j in range(len(Category_of_the_product)):
        Category_of_the_product[j] = Category_of_the_product[j].capitalize()
      Category_of_the_product = ' '.join(Category_of_the_product)
      found=False
      for categories in self.new_products:
        
        if categories.Category==Category_of_the_product:
          print('''
          Su producto es:
          ---------------''')
          print(categories.showP())
          found=True
      if found==False:
        print('''
        El producto no ha sido encontrado
        ---------------------------------
        ''')

################################################################
  
#este es exactamente el mismo codigo de antes pero ahora busca por precio         
    def search_products_price(self):
      Price = input('Ingrese el precio del producto que desea buscar: ')
      while not Price.isnumeric():
        Price = input('Error! Ingrese un precio numerico: ')
      found=False
      for prices in self.new_products:
        if prices.Price==int(Price):
          print('''
          Su producto es:
          ---------------''')
          print(prices.showP())
          found=True
      if found==False:
        print('''
        El producto no ha sido encontrado
        ---------------------------------
        ''')

################################################################
  
#este es exactamente el mismo codigo de antes pero ahora busca por Cantidad en el stock          
    def search_products_quantity(self):
      quantity = input('Ingrese la cantidad en el inventario del producto que desea buscar: ')
      while not quantity.isnumeric():
        quantity = input('Error! Ingrese un precio numerico: ')
      found=False
      for quantities in self.new_products:
        if quantities.Stock==int(quantity):
          print('''
          Su producto es:
          ---------------''')
          print(quantities.showP())
          found=True
      if found==False:
        print('''
        El producto no ha sido encontrado
        ---------------------------------
        ''')

###############################################################
  
#esta funcion es para modificar un producto dentro de la lista, si no esta en la lista aparecera que el producto no ha sido encontrado
    def modify_products(self):
      Name_of_the_product = input('Ingrese el nombre del producto que desea modificar: ')
      Name_of_the_product = Name_of_the_product.split()
      for j in range(len(Name_of_the_product)):
        Name_of_the_product[j] = Name_of_the_product[j].capitalize()
      Name_of_the_product = ' '.join(Name_of_the_product)
      
      found=False
      for names in self.new_products:
        
        if names.Name_of_the_product==Name_of_the_product:
          names.Name_of_the_product = input('Ingrese un nuevo nombre para el producto: ')
          while names.Name_of_the_product == '':
            names.Name_of_the_product = input('INGRESE un nombre para el producto: ')
          names.Name_of_the_product = names.Name_of_the_product.capitalize()
          names.Description = input('Ingrese la descripción del producto: ')
          names.Price = input('Ingrese el precio del producto: ')
          while not names.Price.isnumeric():
            names.Price = input('Error! ingrese un precio valido: ')
          names.Category = input('Ingrese la categoria del producto: ')
          while not names.Category.isalpha():
            names.Category = input('Error! las categorias no pueden llevar numeros, reingrese la categoria del producto : ')
          names.Category = names.Category.capitalize()
          names.Stock = input('Ingrese la cantidad del producto: ')
          while not names.Stock.isnumeric():
            names.Stock = input('Error! ingrese una cantidad valida: ')
          print('''
        El producto ha sido modificado exitosamente
        ---------------------------------
        ''')
          print(names.showP())
          found=True
      if found==False:
        print('''
        El producto no ha sido encontrado
        ---------------------------------
        ''')

###############################################################

#Esta funcion es para eliminar productos de la lista           
    def delete_products(self):
      Name_of_the_product = input('Ingrese el nombre del producto que desea eliminar: ')
      Name_of_the_product = Name_of_the_product.split()
      for j in range(len(Name_of_the_product)):
        Name_of_the_product[j] = Name_of_the_product[j].capitalize()
      Name_of_the_product = ' '.join(Name_of_the_product)
      found=False
      for names in range(len(self.new_products)):
        
        if self.new_products[names].Name_of_the_product==Name_of_the_product:
          print(f''' 
          El producto:
          {self.new_products[names].showP()}
          HA sido eliminado
          -----------------
          ''')
          self.new_products.pop(names)
          found=True
      if found==False:
        print('El producto no se ha encontrado')

########################GESTION DE CLIENTES####################

 #esta funcion es para registrar clientes en caso de que el cliente ya haya sido registrado volvera al menu , se verifica por rif por que por nombre , hay gente que se puede llamar igual 
    def register_customer(self):
      options_customer=['Rif', 'cedula']
      for index_ops_customer in range(len(options_customer)):
       print(f'''{index_ops_customer+1}.{options_customer[index_ops_customer]}''')
      option_customer = input('Ingrese la opción deseada: ')
      while not option_customer.isnumeric() or not int(option_customer)-1 in range(len(options_customer)):
          option_customer=input('Error! Ingrese un numero dentro de las opciones ')
      if option_customer=='1':
        
       rif=input('Ingrese el RIF : ')
       while not (rif[1:].isnumeric() and (rif[0]=='v' or rif[0]=='e' or rif[0]=='j' or rif[0]=='g' or rif[0]=='p')) or len(rif)!=10:
        rif=input('Ingrese un RIF valido recuerde la primera letra minuscula y luego 9 numeros, tome de ejmplo el siguient: v123456789 : ')
      elif option_customer=='2':
        rif=input('Ingrese su cedula: ')
        while not rif.isnumeric():
          rif=input('INGRESE una cedula valida: ')
      for names in self.customers:
        if names.RIF==rif:
          print('''
          El cliente ya ha sido previamente registrado
          ''')
      else:      
          Name_of_the_customer = input('Ingrese el nombre completo del cliente o razon social : ')
          while Name_of_the_customer == '':
            Name_of_the_customer = input('INGRESE el nombre completo del cliente o razon social : ')
          Name_of_the_customer = Name_of_the_customer.split()
          for j in range(len(Name_of_the_customer)):
            Name_of_the_customer[j] = Name_of_the_customer[j].capitalize()
          Name_of_the_customer = ' '.join(Name_of_the_customer)
          type_of_the_customer_juridico=True
          ops=input('Si el cliente es juridico presione 1, si el cliente es natural presione 2: ')
          while not (ops=='1' or  ops=='2'):
            ops=input('Ingrese una opcion valida: ')
          if ops=='2':
            type_of_the_customer_juridico=False
          gmail=input('Ingrese su gmail: ')
          while not ('@gmail.com' in gmail) or len(gmail)<11:
            gmail=input('Ingrese su gmail, recuerde que debe tener @gmail.com en su correo: ')
          shippment_adress=input('Ingrese su direccion: ')
          phone=input('Ingrese el numero de telefono: ')
          while not phone.isnumeric() or not len(phone)==11:
            phone=input('Ingrese un numero valido recuerde debe tener 11 digitos , como en el siguiente ejemplo 04126216153: ')
          new_costumer=Customer(Name_of_the_customer, type_of_the_customer_juridico, rif, gmail, shippment_adress, phone)
          self.customers.append(new_costumer)
          print('''
          El cliente se ha registrado exitosamente
          ''')

###############################################################
  
#Esta funcion es para modificar los clientes ya registrados en caso de no haber clientes  te dice que no hay nada que registrar y busca en base al nombre  
    def modify_customer(self):
      if len(self.customers)==0:
        print('No hay ningun cliente para modificar')
      else:  
        Name_of_the_customer = input('Ingrese el nombre del cliente que desea modificar: ')
        Name_of_the_customer = Name_of_the_customer.split()
        for j in range(len(Name_of_the_customer)):
          Name_of_the_customer[j] = Name_of_the_customer[j].capitalize()
        Name_of_the_customer = ' '.join(Name_of_the_customer)
        found=False
        for names in self.customers:
          if names.Name_of_the_customer==Name_of_the_customer:
            print('''
          El cliente se ha encontrado por favor reescriba los datos 
          ''')
            names.Name_of_the_customer = input('Ingrese el nombre completo del cliente o razon social : ')
            while names.Name_of_the_customer == '':
              names.Name_of_the_customer = input('INGRESE el nombre completo del cliente o razon social : ')
            Name_of_the_customer = Name_of_the_customer.split()
            for j in range(len(Name_of_the_customer)):
              Name_of_the_customer[j] = Name_of_the_customer[j].capitalize()
            Name_of_the_customer = ' '.join(Name_of_the_customer)
            names.type_of_the_customer_juridico=True
            ops=input('Si el cliente es juridico presione 1, si el cliente es natural presione 2: ')
            while not (ops=='1' or  ops=='2'):
              ops=input('Ingrese una opcion valida ')
            if ops=='2':
              names.type_of_the_customer_juridico=False
            options_customer=['Rif', 'cedula']
            for index_ops_customer in range(len(options_customer)):
              print(f'''{index_ops_customer+1}.{options_customer[index_ops_customer]}''')
            option_customer = input('Ingrese la opción deseada: ')
            while not option_customer.isnumeric() or not int(option_customer)-1 in range(len(options_customer)):
              option_customer =input('Error! Ingrese un numero dentro de las opciones ')
            if option_customer=='1':
            
              names.RIF=input('Ingrese el RIF: ')
              while not (names.RIF[1:].isnumeric() and (names.RIF[0]=='v' or names.RIF[0]=='e' or names.RIF[0]=='j' or names.RIF[0]=='g' or names.RIF[0]=='p')) or len(names.RIF)!=10:
                names.RIF=input('Ingrese un RIF valido recuerde la primera letra minuscula y luego 9 numeros, tome de ejmplo el siguient: v123456789 : ')
            elif option_customer=='2':
              names.RIF=input('Ingrese la cedula: ')
              while not names.RIF.isnumeric():
                names.RIF=input('INGRESE una cedula valida: ')
            names.Gmail=input('Ingrese su gmail: ')
            while not '@gmail.com' in names.Gmail or len(names.Gmail)<11:
              names.Gmail=input('Ingrese su gmail, recuerde que debe tener @gmail.com en su correo: ')
            names.shipment_adress=input('Ingrese su direccion: ')
            names.phone_number=input('Ingrese el numero de telefono: ')
            while not names.phone_number.isnumeric() or not len(names.phone_number)==11:
              names.phone_number= input('Ingrese un numero valido recuerde debe tener 11 digitos , como en el siguiente ejemplo 04126216153: ')
            found=True
            print('''
          El cliente se ha modificado exitosamente
          ------------------------------------------
          ''')
            return {names.showC()}
          if found==False:
            print('''
         EL PRODUCTO QUE SE DESEA MODIFICAR NO HA SIDO ENCONTRADO
         -----------------------------''') 

###############################################################

#Esta funcion es para eliminar clientes de la lista , supongo que una tienda lo hace para no guardar tanto espacio en la memoria o porque vetaron el cliente, busca por rif porque por nombre dos personas se pueden llamar igual
    def delete_customer(self):
      if len(self.customers)==0:
        print('''
        No hay ningun cliente para eliminar
        ''')
      else:
        options_customer=['Rif', 'cedula']
        for index_ops_customer in range(len(options_customer)):
         print(f'''{index_ops_customer+1}.{options_customer[index_ops_customer]}''')
        option_customer = input('Ingrese la opción que desea para poder eliminar el cliente: ')
        while not option_customer.isnumeric() or not int(option_customer)-1 in range(len(options_customer)):
            option_customer=input('Error! Ingrese un numero dentro de las opciones ')
        if option_customer=='1':
        
          rif=input('Ingrese el RIF a buscar: ')
          while not (rif[1:].isnumeric() and (rif[0]=='v' or rif[0]=='e' or rif[0]=='j' or rif[0]=='g' or rif[0]=='p')) or len(rif)!=10:
            rif=input('Ingrese un RIF valido recuerde la primera letra minuscula y luego 9 numeros, tome de ejmplo el siguient: v123456789 : ')
        elif option_customer=='2':
          rif=input('Ingrese su cedula a buscar: ')
          while not rif.isnumeric():
            rif=input('INGRESE una cedula valida: ')   
        found=False
        for names in range(len(self.customers)):
          if self.customers[names].RIF==rif:
            self.customers.pop(names)
            print('''
          Cliente eliminado exitosamente
          ---------------------------------
          ''')
            found=True
        if found==False:
          print('''
        No se puede eliminar el cliente debido a que no se encontro
        ''')

###############################################################

#Esta funcion es para buscar clientes por rif es el mismo codigo de buscar productos 
    def search_customers_rif(self):
      options_customer=['Rif', 'cedula']
      for index_ops_customer in range(len(options_customer)):
        print(f'''{index_ops_customer+1}.{options_customer[index_ops_customer]}''')
      option_customer = input('Ingrese la opción que desea buscar: ')
      while not option_customer.isnumeric() or not int(option_customer)-1 in range(len(options_customer)):
          option_customer=input('Error! Ingrese un numero dentro de las opciones ')
      if option_customer=='1':
        
       rif=input('Ingrese el RIF : ')
       while not (rif[1:].isnumeric() and (rif[0]=='v' or rif[0]=='e' or rif[0]=='j' or rif[0]=='g' or rif[0]=='p')) or len(rif)!=10:
        rif=input('Ingrese un RIF valido recuerde la primera letra minuscula y luego 9 numeros, tome de ejmplo el siguient: v123456789 : ')
      elif option_customer=='2':
        rif=input('Ingrese su cedula: ')
        while not rif.isnumeric():
          rif=input('INGRESE una cedula valida: ')
      found=False
      for names in self.customers:
        if names.RIF==rif:
          found=True
          print('''
          El cliente ha sido encontrado
          ''')
          return names.showC()
      if found==False:
        print('''
        No se ha encontrado el cliente
        --------------------------------''')

###############################################################

#Esta funcion es para buscar clientes por rif es el mismo codigo de buscar productos   
    def search_customers_gmail(self):
      Gmail = input('Ingrese el correo del cliente que desea buscar: ')
      while not '@gmail.com' in Gmail or len(Gmail)<10:
        Gmail = input('Error! Ingrese un gmail para la busqueda, recuerde que debe incluir @gmail.com: ')
      found=False
      for gmails in self.customers:
        if gmails.Gmail==Gmail:
          print('''
          El cliente ha sido encontrado
          ''')
          return gmails.showC()
          found=True
      if found==False:
        print('''
        No se ha encontrado el cliente
        --------------------------------''')

####################GESTION DE VENTAS##########################

#Esta Funciones para registrar ventas en caso de no haber clientes te envia a registrar , te pide los productos comprados , en caso de que ingrese un producto no existente te manda a volver a copiarlo, si el cliente es natural lo manda directo a pago si es juridico le da la opcion de pagar ahora o despues
    def register_sales(self):
      if len(self.customers)==0:
        print('No hay clientes registrados por favor registrelos ')
        self.register_customer()
      else:
        options_customer=['Rif', 'cedula']
        for index_ops_customer in range(len(options_customer)):
          print(f'''{index_ops_customer+1}.{options_customer[index_ops_customer]}''')
        option_customer = input('Ingrese el rif o cedula del comprador para registrar los productos: ')
        while not option_customer.isnumeric() or not int(option_customer)-1 in range(len(options_customer)):
          option_customer=input('Error! Ingrese un numero dentro de las opciones ')
        if option_customer=='1':
          rif=input('Ingrese el RIF : ')
          while not (rif[1:].isnumeric() and (rif[0]=='v' or rif[0]=='e' or rif[0]=='j' or rif[0]=='g' or rif[0]=='p')) or len(rif)!=10:
            rif=input('Ingrese un RIF valido recuerde la primera letra minuscula y luego 9 numeros, tome de ejmplo el siguient: v123456789 : ')
        elif option_customer=='2':
          rif=input('Ingrese su cedula: ')
          while not rif.isnumeric():
            rif=input('INGRESE una cedula valida: ')  
        found=False
        for rifs in self.customers:
          if rifs.RIF==(rif):
            found=True
            costumer_bought = rifs.RIF
            juridic = rifs.customer_type
        if found==False:
          print('''
          El cliente no esta registrado por favor registrelo
          ''')
          self.register_customer()
          costumer_bought = rifs.Name_of_the_customer
          juridic = rifs.customer_type
        products_bought = []
        Price_1 = 0 
        sub_total=0
        optionss=0
        self.ShowSt()
        while not optionss=='1':
          product_bought={}
          optionss = input('Ingrese el nombre del producto comprado o coloque 1 para no colocar mas: ')
          if optionss=='1':
            break
          while not optionss != '':
            optionss = input('INGRESE el nombre del producto comprado: ') 
          optionss = optionss.split()
          for j in range(len(optionss)):
            optionss[j] = optionss[j].capitalize()
          optionss = ' '.join(optionss)
          found=False
          while not found==True:
            for products in self.new_products:
              if products.Name_of_the_product == optionss:
                found=True
                break
            if found==False:
              optionss=input('Ingrese un producto valido: ')
              optionss = optionss.split()
              for j in range(len(optionss)):
                optionss[j] = optionss[j].capitalize()
              optionss = ' '.join(optionss)
          opptions = input('Ingrese la cantidad comprada de cada producto: ')
          while not (opptions.isnumeric()) or opptions == '':
              opptions = input('INGRESE la cantidad comprada de cada producto: ') 
          for products in range(len(self.new_products)):
            if self.new_products[products].Name_of_the_product==optionss:
              self.new_products[products].Stock=self.new_products[products].Stock - int(opptions)
              Price_1=self.new_products[products].Price
              product_bought[optionss]=opptions
              products_bought.append(product_bought)
        sub_total += (Price_1*(int(opptions)))
        print('''
      Como desea pagar
      ''')
        options_1_1_1=['Bs','USD']
        for index_ops_1_1_1 in range(len(options_1_1_1)):
          print(f'''{index_ops_1_1_1+1}.{options_1_1_1[index_ops_1_1_1]}''')
        option_1_1_1=input('Ingrese la opción de pago: ')
        while not option_1_1_1.isnumeric() or not int(option_1_1_1)-1 in range(len(options_1_1_1)):
          option_1_1_1=input('Error! Ingrese un numero dentro de las opciones ')
        date = datetime.now()
        date_beautiful =datetime.strftime(date,'%d/%m/%Y')
        Type_of_payment=options_1_1_1[int(option_1_1_1)-1]

        print('''
      Que tipo de delivery desea?
      ''')
        options_1_1_2=['Zoom','Delivery','MRW','No deseo']
        for index_ops_1_1_2 in range(len(options_1_1_2)):
           print(f'''{index_ops_1_1_2+1}.{options_1_1_2[index_ops_1_1_2]}''')
        option_1_1_2=input('Ingrese la opción de delivery: ')
        while not option_1_1_2.isnumeric() or not int(option_1_1_2)-1 in range(len(options_1_1_2)):
          option_1_1_2=input('Error! Ingrese un numero dentro de las opciones ')
        Type_of_shipment = options_1_1_2[int(option_1_1_2)-1]  
        if Type_of_shipment=='No deseo':
          Type_of_shipment==False
        total_payment = sub_total
        discount=0
        IGTF=0
        if juridic==True:
          discount=total_payment*(5/100)
        IVA=total_payment*(16/100)
        if option_1_1_1=='2':
          IGTF=total_payment*(3/100)
        total_payment=total_payment-discount+IVA+IGTF
        Pending_payment=False
        bill = Bill(sub_total, discount, IVA, IGTF, total_payment)
        print('''
      Desea generar factura?
      ''')
        options_1_3=['Si','NO']
        for index_ops_1_3 in range(len(options_1_3)):
          print(f'''{index_ops_1_3+1}.{options_1_3[index_ops_1_3]}''')
        option_1_3=input('Ingrese la opción deseada: ')
        while not option_1_3.isnumeric() or not int(option_1_3)-1 in range(len(options_1_3)):
          option_1_3=input('Error! Ingrese un numero dentro de las opciones ')
        if option_1_3=='1':
          print(bill.showB())
        if juridic==True:
            print('''
          Puede pagar dentro de 15 a 30 dias, desea pagar ahora?
          ''') 
            options_1_3=['Si','NO']
            for index_ops_1_3 in range(len(options_1_3)):
              print(f'''{index_ops_1_3+1}.{options_1_3[index_ops_1_3]}''')
            option_1_3=input('Ingrese la opción deseada: ')
            while not option_1_3.isnumeric() or not int(option_1_3)-1 in range(len(options_1_3)):
              option_1_3=input('Error! Ingrese un numero dentro de las opciones ')
            if option_1_3=='2':
              Pending_payment=True
        sales=Sale(costumer_bought, products_bought, Type_of_payment,Type_of_shipment,total_payment,date_beautiful,Pending_payment)
        self.sales.append(sales)
        if Pending_payment==False:
          self.register_payment()

###############################################################

#Igual que anteriores codigos de busqueda es el mismo codigo si no que con mas validaciones debido a que la fecha es un poco mas dificil de inputear  
    def search_sale_date(self):
      if len(self.sales)==0:
        print('''
        No hay ninguna venta registrada
        ''')
      else:
        Date_1 = input('Ingrese la fecha de la venta que desea buscar, tome como ejemplo esta fecha 27/06/2023: ')
        while  Date_1 == '' or not '/' in Date_1 or not len(Date_1)==10 or int(Date_1[3])>1 or int(Date_1[0])>3:
        
          Date_1 = input('Error! Ingrese una fecha valida: ')
        found = False
        for dates in self.sales:
          if dates.date == Date_1:
            print( dates.showS())
            found = True
        if found == False:
          print('La fecha no esta registrada en el sistema o no existe')

###############################################################

#Igual funcion de busqueda a partir de los rifs
    def search_sale_customer(self):
      if len(self.sales)==0:
        print('''
        No hay ninguna venta registrada
        ''')
      else:
        print('''
      Ingrese RIF o cedula para buscar la venta
      ''')
        options_customer=['Rif', 'cedula']
        for index_ops_customer in range(len(options_customer)):
          print(f'''{index_ops_customer+1}.{options_customer[index_ops_customer]}''')
        option_customer = input('Ingrese la opción deseada: ')
        while not option_customer.isnumeric() or not int(option_customer)-1 in range(len(options_customer)):
          option_customer=input('Error! Ingrese un numero dentro de las opciones ')
        if option_customer=='1':
        
          rif=input('Ingrese el RIF : ')
          while not (rif[1:].isnumeric() and (rif[0]=='v' or rif[0]=='e' or rif[0]=='j' or rif[0]=='g' or rif[0]=='p')) or len(rif)!=10:
            rif=input('Ingrese un RIF valido recuerde la primera letra minuscula y luego 9 numeros, tome de ejmplo el siguient: v123456789 : ')
        elif option_customer=='2':
          rif=input('Ingrese su cedula: ')
          while not rif.isnumeric():
            rif=input('INGRESE una cedula valida: ')
        found = False
        for Rifz in self.sales:
          if Rifz.customer == rif:
            print( Rifz.showS())
            found = True
        if found == False:
          print('No se ha encontrado la venta')

###############################################################

#Igual funcion de busqueda a partir del total de pago
    def search_sale_total_amount(self):
      if len(self.sales)==0:
        print('''
        No hay ninguna venta registrada
        ''')
      else:
        Total_Sale = input('Ingrese el monto total(el numero entero sin decimales) de la venta que desea buscar: ')
        while Total_Sale == '' or not Total_Sale.isnumeric():
          Total_Sale = int(input('Error! Ingrese un monto numerico valido: '))
        found = False
        for Totalz in self.sales:
          if int(Totalz.total_payment) == int(Total_Sale):
            print( Totalz.showS())
            found = True
        if found == False:
          print('No se encontro la venta')

##################GESTION DE PAGOS##############################

#Esta Funcion es para registrar los pagos, pido cedula o rif de nuevo debido a que el cliente puede ser juridico y esta pagando luego de una fecha
    def register_payment(self):
      if len(self.sales) == 0:
        print('No hay ventas registradas por favor registrelas ')
      else:
        print('''
        Se empezara el proceso de pago
        -------------------------------
        ''')
        print('''
      Indique la cedula o rif del cliente que desea pagar
      ''')
        options_customer=['Rif', 'cedula']
        for index_ops_customer in range(len(options_customer)):
          print(f'''{index_ops_customer+1}.{options_customer[index_ops_customer]}''')
        option_customer = input('Ingrese la opción deseada: ')
        while not option_customer.isnumeric() or not int(option_customer)-1 in range(len(options_customer)):
          option_customer=input('Error! Ingrese un numero dentro de las opciones ')
        if option_customer=='1':
        
          rif=input('Ingrese el RIF : ')
          while not (rif[1:].isnumeric() and (rif[0]=='v' or rif[0]=='e' or rif[0]=='j' or rif[0]=='g' or rif[0]=='p')) or len(rif)!=10:
            rif=input('Ingrese un RIF valido recuerde la primera letra minuscula y luego 9 numeros, tome de ejmplo el siguient: v123456789 : ')
        elif option_customer=='2':
          rif=input('Ingrese su cedula: ')
          while not rif.isnumeric():
            rif=input('INGRESE una cedula valida: ')
      
        found=False
        for rifs in self.sales:
          if rifs.customer==rif:
            Total_Sale=rifs.total_payment
            print('''
      Como desea pagar
      ''')
            options_1_1_1=['PdV','Cash','PM','Zelle']
            for index_ops_1_1_1 in range(len(options_1_1_1)):
              print(f'''{index_ops_1_1_1+1}.{options_1_1_1[index_ops_1_1_1]}''')
            option_1_1_1=input('Ingrese la opción de pago: ')
            while not option_1_1_1.isnumeric() or not int(option_1_1_1)-1 in range(len(options_1_1_1)):
              option_1_1_1=input('Error! Ingrese un numero dentro de las opciones ')
            Type_of_payment_1=options_1_1_1[int(option_1_1_1)-1]
            
            Payment_Currency=rifs.payment_method
            date = datetime.now()
            Payment_Date= datetime.strftime(date,'%d/%m/%Y')
            rifs.pending_payment=False
            found = True
            Payments = Payment(rif, Total_Sale, Payment_Currency, Type_of_payment_1, Payment_Date)
            self.payments.append(Payments)
            print('''
      El pago se ha registrado exitosamente
      ''')
          
        if found==False:
          print('''
        No se ha encontrado ningun cliente con pago pendiente
        ''')
      
###############################################################
  
#Igual a las otras funciones de busqueda   
    def search_payment_customer(self):
      if len(self.payments)==0:
        print('''
        No hay ninguna venta registrada
        ''')
      else:
        options_customer=['Rif', 'cedula']
        for index_ops_customer in range(len(options_customer)):
          print(f'''{index_ops_customer+1}.{options_customer[index_ops_customer]}''')
        option_customer = input('Ingrese la opción deseada: ')
        while not option_customer.isnumeric() or not int(option_customer)-1 in range(len(options_customer)):
          option_customer=input('Error! Ingrese un numero dentro de las opciones ')
        if option_customer=='1':
        
          rif=input('Ingrese el RIF : ')
          while not (rif[1:].isnumeric() and (rif[0]=='v' or rif[0]=='e' or rif[0]=='j' or rif[0]=='g' or rif[0]=='p')) or len(rif)!=10:
            rif=input('Ingrese un RIF valido recuerde la primera letra minuscula y luego 9 numeros, tome de ejmplo el siguient: v123456789 : ')
        elif option_customer=='2':
          rif=input('Ingrese su cedula: ')
          while not rif.isnumeric():
            rif=input('INGRESE una cedula valida: ')
        found = False
        for Rifx in self.payments:
          if Rifx.Paid_By == rif:
            print(Rifx.showPay())
            found = True
        if found == False:
          print('''
        No se ha encontrado ningun pago
        ''')

###############################################################

#Igual a la funcion de busqueda por fecha
    def search_payment_date(self):
      if len(self.payments)==0:
        print('''
        No hay ninguna venta registrada
        ''')
      else:
        Date_1 = input('Ingrese la fecha de la venta que desea buscar, tome como ejemplo esta fecha 27/06/2023: ')
        while  Date_1 == '' or not '/' in Date_1 or not len(Date_1)==10 or int(Date_1[3])>1 or int(Date_1[0])>3:
          Date_1 = input('Error! Ingrese una fecha valida: ')
        found = False
        for dates in self.payments:
          if dates.Payment_Date == Date_1:
            return dates.showPay()
            found = True
        if found == False:
          print('La fecha no esta registrada en el sistema o no existe')

###############################################################

#Igual a las demas funciones de busqueda
    def search_payment_type_of_payment(self):
      if len(self.payments)==0:
        print('''
        No hay ninguna venta registrada
        ''')
      else:
        Type_of_Payment_3 = input('Ingrese la forma de pago en la que se realizo el pago que busca: ')
        while not (Type_of_Payment_3 != '' or Type_of_Payment_3.isalpha()):
          Type_of_Payment_3 = input('INGRESE la forma de pago en la que se realizo el pago que busca: ')
        Type_of_Payment_3=Type_of_Payment_3.capitalize()
        found = False
        for Tpayment in self.payments:
          if Tpayment.Type_of_Payment == Type_of_Payment_3:
            print(Tpayment.showPay())
            found = True
          if found == False:
            print('''
          No se ha encontrado ningun pago
          ''')

###############################################################

#Igual a las demas funciones de busqueda
    def search_payment_currency_type(self):
      if len(self.payments)==0:
        print('''
        No hay ninguna venta registrada
        ''')
      else:
        Payment_Currency_3 = input('Ingrese la moneda en la que se realizo el pago que busca: ')
        while not (Payment_Currency_3 != '' or Payment_Currency_3.isalpha()):
          Payment_Currency_3 = input('INGRESE la moneda en la que se realizo el pago que busca: ')
        Payment_Currency_3=Payment_Currency_3.capitalize()
        found = False
        for paymentC in self.pagos:
          if paymentC.Payment_Currency == Payment_Currency_3:
            print(paymentC.showPay())
            found = True
        if found == False:
          print('''
          No se ha encontrado ningun pago
          ''')

####################GESTION DE ENVIOS##########################

#Funcion para registrar los envios revisa si el cliente tiene un envio en sales si el cliente previamente no deseo delivery ps no se puede registrar 
    def register_shipment(self):
      if len(self.sales) == 0:
        print('No hay ventas registradas por favor registrelas ')
      else:
        options_customer=['Rif', 'cedula']
        for index_ops_customer in range(len(options_customer)):
          print(f'''{index_ops_customer+1}.{options_customer[index_ops_customer]}''')
        option_customer = input('Ingrese la opción deseada: ')
        while not option_customer.isnumeric() or not int(option_customer)-1 in range(len(options_customer)):
          option_customer=input('Error! Ingrese un numero dentro de las opciones ')
        if option_customer=='1':
        
          rif=input('Ingrese el RIF : ')
          while not (rif[1:].isnumeric() and (rif[0]=='v' or rif[0]=='e' or rif[0]=='j' or rif[0]=='g' or rif[0]=='p')) or len(rif)!=10:
            rif=input('Ingrese un RIF valido recuerde la primera letra minuscula y luego 9 numeros, tome de ejmplo el siguient: v123456789 : ')
        elif option_customer=='2':
          rif=input('Ingrese su cedula: ')
          while not rif.isnumeric():
            rif=input('INGRESE una cedula valida: ')
      
        found=False
        for rifs in self.sales:
          if rifs.customer==rif or rifs.shipment_method != 'No deseo':
            Shipment_Service=rifs.shipment_method
            Date_1 = input('Ingrese la fecha de envio que desea, tome como ejemplo esta fecha 27/06/2023: ')
            while  Date_1 == '' or not '/' in Date_1 or not len(Date_1)==10 or int(Date_1[3])>1 or int(Date_1[0])>3:
        
              Date_1 = input('Error! Ingrese una fecha valida: ')
            order_bought=Order(rifs.customer,Date_1,rifs.purchased_products)
            if rifs.shipment_method == 'Zoom':
              Shipment_Price = 11
            elif rifs.shipment_method == 'Delivery':
              Shipment_Price= 13
            elif rifs.shipment_method == 'MRW':
              Shipment_Price=15
            date_today=datetime.now()
            date_beautiful =datetime.strftime(date_today,'%d/%m/%Y')
            Order_pending=True
            if Date_1==date_beautiful:
              Order_pending=False
            moto_data=input('Ingrese los datos del motorizado')
            shipping = Shipment(moto_data, Shipment_Service, Shipment_Price,order_bought,Order_pending,date_beautiful)
            self.shipments.append(shipping)
            found = True
            print('''
        El envio se ha registrado exitosamente
        ''')
        if found == False:
          print('''
          No se ha encontrado al cliente que se desea enviar
          ''')
          
###############################################################

# Igual a las demas funciones de busqueda
    def search_shipment_customer(self):
      if len(self.payments)==0:
        print('''
        No hay ninguna venta registrada
        ''')
      else:
        options_customer=['Rif', 'cedula']
        for index_ops_customer in range(len(options_customer)):
          print(f'''{index_ops_customer+1}.{options_customer[index_ops_customer]}''')
        option_customer = input('Ingrese la opción deseada: ')
        while not option_customer.isnumeric() or not int(option_customer)-1 in range(len(options_customer)):
          option_customer=input('Error! Ingrese un numero dentro de las opciones ')
        if option_customer=='1':
        
          rif=input('Ingrese el RIF : ')
          while not (rif[1:].isnumeric() and (rif[0]=='v' or rif[0]=='e' or rif[0]=='j' or rif[0]=='g' or rif[0]=='p')) or len(rif)!=10:
            rif=input('Ingrese un RIF valido recuerde la primera letra minuscula y luego 9 numeros, tome de ejmplo el siguient: v123456789 : ')
        elif option_customer=='2':
          rif=input('Ingrese su cedula: ')
          while not rif.isnumeric():
            rif=input('INGRESE una cedula valida: ')
        found = False
        for Rifw in self.shipments:
          if Rifw.Order_bought.Customer_Name == rif:
            print(Rifw.showShip())
            found = True
        if found == False:
          print('No hay ningun envio con el cliente')

###############################################################

#Igual a las demas funciones de busqueda
    def search_shipment_date(self):
      if len(self.sales)==0:
        print('''
        No hay ninguna venta registrada
        ''')
      else:
        Date_1 = input('Ingrese la fecha del envio que desea buscar, tome como ejemplo esta fecha 27/06/2023: ')
        while  Date_1 == '' or not '/' in Date_1 or not len(Date_1)==10 or int(Date_1[3])>1 or int(Date_1[0])>3:
          Date_1 = input('Error! Ingrese una fecha valida: ')
        found = False
        for dates in self.shipments:
          if dates.Order_bought.Shipment_Date == Date_1:
            print(dates.showShip())
            found = True  
        if found == False:
          print('La fecha no esta registrada en el sistema o no existe')

###################ESTADISTICAS###############################

#Esta funcion genera reportes de ventas esto en funcion de la fechas  use datetime para guiarme semanalmente,mensualmente y anualmente y revisa los productos mas comprados mediante diccionarios
    def generate_reports_sales(self):
      date = datetime.now()
      sale_Date= datetime.strftime(date,'%d/%m/%Y')
      sale_m=datetime.strftime(date,'%m')
      sale_y=datetime.strftime(date,'%Y')
      sales_today=0
      sales_week=0
      sales_month=0
      sales_year=0
      dic={}
      for sales in self.sales:
        sale_d=datetime.strptime(sales.date, '%d/%m/%Y')
        sale_m_real=datetime.strftime(sale_d,'%m')
        sale_y_real=datetime.strftime(sale_d,'%Y')
        if sales.date == sale_Date:
          sales_today+=1
        if date>=sale_d>=(date-timedelta(days=7)):
          sales_week+=1
        if sale_m==sale_m_real:
          sales_month+=1
        if sale_y==sale_y_real:
          sales_year+=1
      print('''
      Las cedulas o rif de los clientes frecuentes son
      ''')
      for customers in self.sales:
        if customers.customer in dic:
          dic[customers.customer]+=1
        else:
          dic[customers.customer]=1
      for x in dic:
        if dic[x]>3:
          print(f'''
          {x}
          ''')
      doc={}
      print('''
      Los productos mas comprados son:
      ''')
      for x in self.sales:
        for dic in x.purchased_products:
          for key,keyvalue in dic.items():
            if key in doc:
              doc[key]+=int(keyvalue)
            else:
              doc[key]=int(keyvalue)
      for x in doc:
        if doc[x]>7:
          print(f'''
          {x}
          ''')
          
      print(f'''
      Las ventas de hoy son: {sales_today}
      las ventas en la semana son: {sales_week}
      las ventas en lo que lleva el mes son: {sales_month}
      las ventas en lo que lleva el año son: {sales_year}
      ''')
  
##############################################################

#Esta funcion genera reportes de los pagos igualmente que la anterior en funcion de las fechas y te muestra si hay pagos pendientes
    def generate_reports_payments(self):
      date = datetime.now()
      pay_Date= datetime.strftime(date,'%d/%m/%Y')
      pay_m=datetime.strftime(date,'%m')
      pay_y=datetime.strftime(date,'%Y')
      pays_today=0
      pays_week=0
      pays_month=0
      pays_year=0
      for pays in self.payments:
        pay_d=datetime.strptime(pays.Payment_Date, '%d/%m/%Y')
        pay_m_real=datetime.strftime(pay_d,'%m')
        pay_y_real=datetime.strftime(pay_d,'%Y')
        if pays.Payment_Date == pay_Date:
          pays_today+=1
        if date>=pay_d>=(date-timedelta(days=7)):
          pays_week+=1
        if pay_m==pay_m_real:
          pays_month+=1
        if pay_y==pay_y_real:
          pays_year+=1
      print(f'''
      los pagos de hoy son: {pays_today}
      los pagos en la semana son: {pays_week}
      los pagos en lo que lleva el mes son: {pays_month}
      los pagos en lo que lleva el año son: {pays_year}''')
      print('''
      Los rif/cedulas de clientes con pagos pendientes son:
      -----------------------------------------------------
      ''')
      for sales in self.sales:
        if sales.pending_payment==True:
          print(f'''
          {sales.customer}''')

#############################################################

#Esta funcion genera reportes de los envios funciona igual que el anterior pero ve los productos mas enviados
    def generate_reports_shipments(self):
      date = datetime.now()
      ship_Date= datetime.strftime(date,'%d/%m/%Y')
      ship_m=datetime.strftime(date,'%m')
      ship_y=datetime.strftime(date,'%Y')
      ships_today=0
      ships_week=0
      ships_month=0
      ships_year=0
      
      for ships in self.shipments:
        ship_d=datetime.strptime(ships.Order_bought.Shipment_Date, '%d/%m/%Y')
        ship_m_real=datetime.strftime(ship_d,'%m')
        ship_y_real=datetime.strftime(ship_d,'%Y')
        if ships.Order_bought.Shipment_Date == ship_Date:
          ships_today+=1
        if date>=ship_d>=(date-timedelta(days=7)):
          ships_week+=1
        if ship_m==ship_m_real:
          ships_month+=1
        if ship_y==ship_y_real:
          ships_year+=1
      print(f'''
      los envios de hoy son: {ships_today}
      los envios en la semana son: {ships_week}
      los envios en lo que lleva el mes son: {ships_month}
      los envios en lo que lleva el año son: {ships_year}''')
      print('''
      Los rif/cedualas de clientes con envios pendientes son:
      -------------------------------------------------------''')
      for ships in self.shipments:
        if ships.Order_pending==True:
          print(ships.Order_bought.Customer)
      doc={}
      print('''
      Los productos mas enviados son:
      ''')
      for x in self.sales:
        for dic in x.purchased_products:
          for key,keyvalue in dic.items():
            if key in doc:
              doc[key]+=int(keyvalue)
            else:
              doc[key]=int(keyvalue)
      for x in doc:
        if doc[x]>7:
          print(f'''
          {x}
          ''')
        
########################MENU###################################
  
#Esta funcion es un menu para poder ingresar a las funciones de la tienda
    def menu(self):
      while True:
     
        options=['Gestionar Productos','Gestionar ventas','Gestionar Clientes','Gestionar Pagos','Gestionar envios','Ver Estadísticas','Salir']
        for index_ops in range(len(options)):
          print(f'''{index_ops+1}.{options[index_ops]}''')
        option=input('Ingrese la opción deseada: ')
        while not option.isnumeric() or not int(option)-1 in range(len(options)):
          option=input('Error! Ingrese un numero dentro de las opciones ')

        if option=='1':
          options_1=['Agregar Productos','Buscar Productos','Modificar Productos','Eliminar Productos','Atras']
          for index_ops_1 in range(len(options_1)):
            print(f'''{index_ops_1+1}.{options_1[index_ops_1]}''')
          option_1=input('Ingrese la opción deseada: ')
          while not option_1.isnumeric() or not int(option_1)-1 in range(len(options_1)):
            option_1=input('Error! Ingrese un numero dentro de las opciones ')
          if option_1=='1':
            self.add_products()

          elif option_1=='2':
            options_1_1=['Buscar por nombre','Buscar por categoria','Buscar por precio','Buscar por disponibilidad','Atras']
            for index_ops_1_1 in range(len(options_1_1)):
              print(f'''{index_ops_1_1+1}.{options_1_1[index_ops_1_1]}''')
            option_1_1=input('Ingrese la opción deseada: ')
            while not option_1_1.isnumeric() or not int(option_1_1)-1 in range(len(options_1_1)):
              option_1_1=input('Error! Ingrese un numero dentro de las opciones ')
            if option_1_1=='1':
              self.search_products_name()
            elif option_1_1=='2':
              self.search_products_category()
            elif option_1_1=='3':
              self.search_products_price()
            elif option_1_1=='4':
               self.search_products_quantity()
          elif option_1=='3':
            self.modify_products()

          elif option_1=='4':
            self.delete_products()

        elif option == '2':
          options_2 = ['Registrar ventas','Buscar Venta','Atras']
          for index_ops_2 in range(len(options_2)):
            print(f'''{index_ops_2+1}.{options_2[index_ops_2]}''')
          option_2 = input('Ingrese la opción deseada: ')
          while not option_2.isnumeric() or not int(option_2)-1 in range(len(options_2)):
            option_2=input('Error! Ingrese un numero dentro de las opciones ')
          if option_2 == '1':
            self.register_sales()

          elif option_2 == '2':
            options_4 = ['Buscar por fecha','Buscar por cliente','Buscar por monto total de la venta', 'Atras']
            for index_ops_4 in range(len(options_4)):
              print(f'''{index_ops_4+1}.{options_4[index_ops_4]}''')
            option_4 = input('Ingrese la opción deseada: ')
            while not option_4.isnumeric() or not int(option_4)-1 in range(len(options_4)):
              option_4 = input('Error! Ingrese un numero dentro de las opciones ')
            if option_4 == '1':
              self.search_sale_date()

            elif option_4 == '2':
              self.search_sale_customer()

            elif option_4 == '3':
              self.search_sale_total_amount()

        elif option=='3':
          options_3=['Resgistrar Clientes','Modificar Informacion de clientes','Eliminar clientes','Buscar clientes','Atras']
          for index_ops_3 in range(len(options_3)):
            print(f'''{index_ops_3+1}.{options_3[index_ops_3]}''')
          option_3=input('Ingrese la opción deseada: ')
          while not option_3.isnumeric() or not int(option_3)-1 in range(len(options_3)):
            option_3=input('Error! Ingrese un numero dentro de las opciones ')
          if option_3=='1':
            self.register_customer()

          elif option_3=='2':
            self.modify_customer()

          elif option_3=='3':
            self.delete_customer()

          elif option_3=='4':
            options_3_1=['Buscar por Rif','Buscar por gmail','Salir']
            for index_ops_3_1 in range(len(options_3_1)):
              print(f'''{index_ops_3_1+1}.{options_3_1[index_ops_3_1]}''')
            option_3_1=input('Ingrese la opción deseada: ')
            while not option_3_1.isnumeric() or not int(option_3_1)-1 in range(len(options_3_1)):
              option_3_1=input('Error! Ingrese un numero dentro de las opciones ')
            if option_3_1=='1':
              self.search_customers_rif()
            elif option_3_1=='2':
              self.search_customers_gmail()
       
        elif option=='4':
          options_4=['Registrar pagos','Buscar pagos','Atras']
          for index_ops_4 in range(len(options_4)):
            print(f'''{index_ops_4+1}.{options_4[index_ops_4]}''')
          option_4=input('Ingrese la opción deseada: ')
          while not option_4.isnumeric() or not int(option_4)-1 in range(len(options_4)):
            option_4=input('Error! Ingrese un numero dentro de las opciones ')
          if option_4=='1':
            self.register_payment()

          elif option_4 == '2':
            options_9 = ['Buscar por clientes','Buscar por fechas','Buscar por tipo de pago', 'Buscar por moneda de pago', 'Atras']
            for index_ops_9 in range(len(options_9)):
              print(f'''{index_ops_9+1}.{options_9[index_ops_9]}''')
            option_9 = input('Ingrese la opción deseada: ')
            while not option_9.isnumeric() or not int(option_9)-1 in range(len(options_9)):
              option_9 = input('Error! Ingrese un numero dentro de las opciones ')
            if option_9 == '1':
              self.search_payment_customer()
            elif option_9 == '2':
              self.search_payment_date()
            elif option_9 == '3':
              self.search_payment_type_of_payment()
            elif option_9 == '4':
              self.search_payment_currency_type()

        elif option=='5':
          options_5=['Registrar envios','Buscar envios','Atras']
          for index_ops_5 in range(len(options_5)):
            print(f'''{index_ops_5+1}.{options_5[index_ops_5]}''')
          option_5=input('Ingrese la opción deseada: ')
          while not option_5.isnumeric() or not int(option_5)-1 in range(len(options_5)):
            option_5=input('Error! Ingrese un numero dentro de las opciones ')
          if option_5=='1':
            self.register_shipment()

          elif option_5=='2':
            options_5=['Buscar por cliente','Buscar por fecha','Atras']
            for index_ops_5 in range(len(options_5)):
              print(f'''{index_ops_5+1}.{options_5[index_ops_5]}''')
            option_5=input('Ingrese la opción deseada: ')
            while not option_5.isnumeric() or not int(option_5)-1 in range(len(options_5)):
              option_5=input('Error! Ingrese un numero dentro de las opciones ')
            if option_5=='1':
              self.search_shipment_customer()
            elif option_5=='2':
              self.search_shipment_date()
       
        elif option=='6':
          options_6=['Generar Informes de Ventas','Generar Informes de Pagos','Generar Informes de Envios','Salir']
          for index_ops_6 in range(len(options_6)):
            print(f'''{index_ops_6+1}.{options_6[index_ops_6]}''')
          option_6=input('Ingrese la opción deseada: ')
          while not option_6.isnumeric() or not int(option_6)-1 in range(len(options_6)):
            option_6=input('Error! Ingrese un numero dentro de las opciones ')
          if option_6=='1':
            self.generate_reports_sales()

          elif option_6=='2':
            self.generate_reports_payments()

          elif option_6=='3':
            self.generate_reports_shipments()

        else:
          pic= open('Product.txt','wb')
          rw=pickle.dumps(self.new_products)
          pic.write(rw)
          pic.close()
          pic= open('Sale.txt','wb')
          rw=pickle.dumps(self.sales)
          pic.write(rw)
          pic.close()
          pic= open('Customer.txt','wb')
          rw=pickle.dumps(self.customers)
          pic.write(rw)
          pic.close()
          pic= open('Shipment.txt','wb')
          rw=pickle.dumps(self.shipments)
          pic.write(rw)
          pic.close()
          pic= open('Payment.txt','wb')
          rw=pickle.dumps(self.payments)
          pic.write(rw)
          pic.close()
          print(''' 
          Desea volver a los datos iniciales del viejo inventario
          ''')
          options_3_1=['Si','No']
          for index_ops_3_1 in range(len(options_3_1)):
            print(f'''{index_ops_3_1+1}.{options_3_1[index_ops_3_1]}''')
          option_3_1=input('Ingrese la opción deseada: ')
          while not option_3_1.isnumeric() or not int(option_3_1)-1 in range(len(options_3_1)):
            option_3_1=input('Error! Ingrese un numero dentro de las opciones ')
          if option_3_1=='1':
            txt='Product.txt'
            try:
              with open(txt,'+r') as f:
                f.truncate()
            except IOError:
              print('Error')
            txt='Sale.txt'
            try:
              with open(txt,'+r') as f:
                f.truncate()
            except IOError:
              print('Error')
            txt='Payment.txt'
            try:
              with open(txt,'+r') as f:
                f.truncate()
            except IOError:
              print('Error')
            txt='Shipment.txt'
            try:
              with open(txt,'+r') as f:
                f.truncate()
            except IOError:
              print('Error')
            txt='Customer.txt'
            try:
              with open(txt,'+r') as f:
                f.truncate()
            except IOError:
              print('Error')
          break   
#ya txt listo , luego de 50 fallos, en tal caso remoto, espero que no pase de que suelte un error por favor eliminar el contenido de los txt