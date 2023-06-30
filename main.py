import requests
from Store import Store
import pickle
import os
Inventory = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json') 
Old_inventory=Inventory.json()
new_products = []
new_customers = []
sales = []
pagos = []
shipments = []
if os.stat('Customer.txt').st_size!=0:
  pick=open('Customer.txt','rb')
  new_customers=pickle.load(pick)
  pick.close()
if os.stat('Shipment.txt').st_size!=0:
  pick=open('Shipment.txt','rb')
  shipments=pickle.load(pick)
  pick.close()
if os.stat('Payment.txt').st_size!=0:
  pick=open('Payment.txt','rb')
  pagos=pickle.load(pick)
  pick.close()
if os.stat('Sale.txt').st_size!=0:
  pick=open('Sale.txt','rb')
  sales=pickle.load(pick)
  pick.close()
if os.stat('Product.txt').st_size!=0:
  pick=open('Product.txt','rb')
  new_products=pickle.load(pick)
  pick.close()
if os.stat('Product.txt').st_size == 0:
  pickl= open('Product.txt','wb')
  a=pickle.dumps(Old_inventory)
  pickl.write(a)
  pickl.close()

def main():
  print('''
  Bienvenido a La Tienda
  -----------------------
  ''')
  store = Store(Old_inventory, new_products, new_customers, sales, pagos,  shipments)
  store.initial_products()
  store.menu() 
main()
#se pudo