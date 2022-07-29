import pdb
import datetime
from models.pet import Pet
from models.owner import Owner
from models.vet import Vet


pet1 = Pet("Max", datetime.date(2015, 1, 1), "cat", "check up")
pet2 = Pet("Marcel", datetime.date(2010, 6, 15), "cat", "vaccinations")
pet3 = Pet("Penny", datetime.date(2012, 12, 30), "cocker spaniel", "de-worm")

owner1 = Owner("Bing", "Crosby")
owner2 = Owner("Frank", "Zappa")

vet1 = Vet("James", "Herriot")





