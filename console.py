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
pet4 = Pet("Hammy", datetime.date(2020,2,3), "hamster", "trim claws")

owner1 = Owner("Bing", "Crosby")
owner2 = Owner("Frank", "Zappa")
owner3 = Owner("Bryan", "Adams")

vet1 = Vet("James", "Herriot")
vet2 = Vet("Steve", "Irwin")

owner_repository.save(owner1)
owner_repository.save(owner2)
owner_repository.save(owner3)
vet_repository.save(vet1)
vet_repository.save(vet2)
pet_repository.save(pet1, vet1.id, owner1.id)
pet_repository.save(pet2, vet1.id, owner1.id)
pet_repository.save(pet3, vet2.id, owner2.id)
pet_repository.save(pet4, vet2.id, owner3.id)


# pet_repository.select(pet1)









