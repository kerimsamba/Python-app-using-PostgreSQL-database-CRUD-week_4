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



owner1 = Owner("Bing", "Crosby", "6437777", "bing@crosby.com")
owner2 = Owner("Frank", "Zappa", "7652222", "frank@zappa.com")
owner3 = Owner("Bryan", "Adams", "9878888", "bryan@adams.com")

vet1 = Vet("James", "Herriot")
vet2 = Vet("Steve", "Irwin")

owner_repository.save(owner1)
owner_repository.save(owner2)
owner_repository.save(owner3)
vet_repository.save(vet1)
vet_repository.save(vet2)

pet1 = Pet("Max", datetime.date(2015, 1, 1), "cat", "check up", vet1.id, owner1.id)
pet2 = Pet("Marcel", datetime.date(2010, 6, 15), "cat", "vaccinations", vet1.id, owner1.id)
pet3 = Pet("Penny", datetime.date(2012, 12, 30), "cocker spaniel", "de-worm", vet2.id, owner2.id)
pet4 = Pet("Hammy", datetime.date(2020,2,3), "hamster", "trim claws", vet2.id, owner3.id)

pet_repository.save(pet1)
pet_repository.save(pet2)
pet_repository.save(pet3)
pet_repository.save(pet4)


# pet_repository.select(pet1)









