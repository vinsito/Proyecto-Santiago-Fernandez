class Payment:

  def __init__(self, Paid_By, Total_Sale, Payment_Currency, Type_of_Payment, Payment_Date):
    self.Paid_By = Paid_By
    self.Total_Sale = Total_Sale
    self.Payment_Currency = Payment_Currency
    self.Type_of_Payment = Type_of_Payment
    self.Payment_Date = Payment_Date

  def showPay(self):
    return f'''
    Cliente: {self.Paid_By}
    Total de pago: {self.Total_Sale}
    Moneda de pago: {self.Payment_Currency}
    Tipo de pago: {self.Type_of_Payment}
    Dia de pago: {self.Payment_Date}
    '''