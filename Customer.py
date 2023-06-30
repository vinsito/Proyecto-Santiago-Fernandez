class Customer:

  def __init__(self, Name_of_the_customer, customer_type, RIF, Gmail, shipment_address, phone_number):
    self.Name_of_the_customer = Name_of_the_customer
    self.customer_type = customer_type
    self.RIF = RIF
    self.Gmail = Gmail
    self.shipment_address = shipment_address
    self.phone_number = phone_number

  def showC(self):
    print(f'''
    Nombre completo o razón social: {self.Name_of_the_customer}
    El cliente es juridico: {self.customer_type}
    RIF: {self.RIF}
    Gmail: {self.Gmail}
    Direccion de envio: {self.shipment_address}
    Numero de telefono: {self.phone_number}
    ''')