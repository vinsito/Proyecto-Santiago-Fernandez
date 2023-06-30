from Order import Order
class Shipment:

  def __init__(self, Moto_data, Shipment_Service, Shipment_Price,Order_bought,Order_pending,Order_date):
    self.Moto_data = Moto_data 
    self.Shipment_Service = Shipment_Service
    self.Shipment_Price = Shipment_Price
    self.Order_bought=Order_bought
    self.Order_pending=Order_pending
    self.Order_date=Order_date
  def showShip(self):
    return f'''
    Orden de compra: {self.Order_bought.showO()}
    Datos del motorizado: {self.Moto_data}
    Servicio de delivery: {self.Shipment_Service}
    Precio del servicio: {self.Shipment_Price}
    Envio pendiente:{self.Order_pending}
    Estado de pedido pendiente: {self.Order_pending}
    Dia del registro del envio: {self.Order_date}'''