#object oriented programming

class partyAnimal:
  def __init__(self):
    self.x = 0 
  def party(self):
    self.x = self.x + 1
    print('So far',self.x)
    

rigby = partyAnimal()
rigby.party()
rigby.party()
rigby.party()
