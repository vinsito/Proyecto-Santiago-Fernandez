
class Order:

  def __init__(self, Customer_Name, Shipment_Date, Products_Taken):
    self.Customer_Name = Customer_Name
    self.Shipment_Date = Shipment_Date
    self.Product_Taken = Products_Taken


  def showO(self):
    return f'''
    RIF del cliente: {self.Customer_Name}
    Dia del envio: {self.Shipment_Date}
    Productos comprados: {self.Product_Taken}
    '''