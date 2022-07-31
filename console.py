import pdb
import datetime

from models.pet import Pet
from models.owner import Owner
from models.vet import Vet

import repositories.pet_repository as pet_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository

pet_repository.delete_all()
owner_repository.delete_all()
vet_repository.delete_all()

pet1 = Pet("Max", datetime.date(2015, 1, 1), "cat", "check up")
pet2 = Pet("Marcel", datetime.date(2010, 6, 15), "cat", "vaccinations")
pet3 = Pet("Penny", datetime.date(2012, 12, 30), "cocker spaniel", "de-worm")

owner1 = Owner("Bing", "Crosby")
owner2 = Owner("Frank", "Zappa")

vet1 = Vet("James", "Herriot")

owner_repository.save(owner1)
vet_repository.save(vet1)
pet_repository.save(pet1, vet1.id, owner1.id)
pet_repository.save(pet2, vet1.id, owner1.id)


# pet_repository.select(pet1)









