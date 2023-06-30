class Sale:

  def __init__(self,customer, purchased_products, payment_method, shipment_method, total_payment, date, pending_payment):
    self.customer = customer
    self.purchased_products = purchased_products
    self.payment_method = payment_method
    self.shipment_method = shipment_method
    self.total_payment = total_payment
    self.date = date
    self.pending_payment=pending_payment

  def showS(self):
    print(f'''
    Cliente: {self.customer}
    Productos comprados: {self.purchased_products}
    Metodo de pago: {self.payment_method}
    Metodo de envio: {self.shipment_method}
    total de pago: {self.total_payment}
    Fecha: {self.date}
    ''')
    