class Bill:

  def __init__(self, sub_total, discount, IVA, IGTF, total_payment):
    self.sub_total = sub_total
    self.discount = discount 
    self.IVA = IVA
    self.IGTF = IGTF 
    self.total_payment = total_payment

  def showB(self):
    return f'''
    Sub Total: {self.sub_total}
    Discuont: {self.discount} 
    IVA: {self.IVA}
    IGTF: {self.IGTF}
    Total Payment: {self.total_payment}
    '''
