from address import Address
from  mailing import Mailing
to_address = Address("442200", "Пенза", "Леснова", "77", "239")
from_address = Address("142412", 'Ногинск','Аэроклубная', '12','398')
mail = Mailing(123432, from_address,to_address,460)
print (mail)