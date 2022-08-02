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



owner1 = Owner("Bing", "Crosby", "6437777", "bing@crosby.com", "active")
owner2 = Owner("Frank", "Zappa", "7652222", "frank@zappa.com", "active")
owner3 = Owner("Bryan", "Adams", "9878888", "bryan@adams.com", "active")
owner4 = Owner("Bruce", "Hornsby", "8888888", "bruce@hornsby.com", "active")
owner5 = Owner("Taylor", "Swift", "7776666", "taylor@swift.com", "active")
owner6 = Owner("Trent", "Reznor", "4449999", "trent@reznor.com", "active")
owner7 = Owner("Billy", "Butcher", "3334444", "billy@butcher.com", "active")
owner8 = Owner("P.T.", "Barnum", "0000000", "unknown", "inactive")

vet1 = Vet("James", "Herriot")
vet2 = Vet("Steve", "Irwin")
vet3 = Vet("Doctor", "Dolittle")

owner_repository.save(owner1)
owner_repository.save(owner2)
owner_repository.save(owner3)
owner_repository.save(owner4)
owner_repository.save(owner5)
owner_repository.save(owner6)
owner_repository.save(owner7)
owner_repository.save(owner8)

vet_repository.save(vet1)
vet_repository.save(vet2)
vet_repository.save(vet3)

pet1 = Pet("Max", datetime.date(2015, 1, 1), "cat", "check up", vet1.id, owner1.id)
pet2 = Pet("Marcel", datetime.date(2010, 6, 15), "cat", "vaccinations", vet1.id, owner1.id)
pet3 = Pet("Penny", datetime.date(2012, 12, 30), "cocker spaniel", "de-worm", vet1.id, owner3.id)
pet4 = Pet("Hammy", datetime.date(2012,2,3), "hamster", "trim claws", vet1.id, owner4.id)
pet5 = Pet("Donald", datetime.date(2003,4,23), "duck", "neutered", vet1.id, owner5.id)
pet6 = Pet("Mickey", datetime.date(2014,6,12), "labrador", "stomach ulcer", vet2.id, owner6.id)
pet7 = Pet("Pluto", datetime.date(2015,8,6), "rottweiler", "tooth decay", vet2.id, owner7.id)
pet8 = Pet("Blue", datetime.date(2018,12,6), "velociraptor", "claw removal", vet2.id, owner2.id)
pet9 = Pet("Willy", datetime.date(2010,1,9), "whale", "fin re-alignment", vet2.id, owner3.id)
pet10 = Pet("Lawrence", datetime.date(2001,9,24), "llama", "broken leg", vet2.id, owner4.id)
pet11 = Pet("Mufasa", datetime.date(2005,6,3), "lion", "abandonement distress", vet3.id, owner5.id)
pet12 = Pet("Scar", datetime.date(2009,3,13), "lion", "fighting injuries", vet3.id, owner6.id)
pet13 = Pet("Nemo", datetime.date(2019,2,20), "fish", "shark bite", vet3.id, owner7.id)
pet14 = Pet("Jaws", datetime.date(2001,9,11), "shark", "fish trapped in teeth", vet3.id, owner3.id)
pet15 = Pet("ShadowFax", datetime.date(1066,1,14), "horse", "re-shoe", vet3.id, owner4.id)

pet_repository.save(pet1)
pet_repository.save(pet2)
pet_repository.save(pet3)
pet_repository.save(pet4)
pet_repository.save(pet5)
pet_repository.save(pet6)
pet_repository.save(pet7)
pet_repository.save(pet8)
pet_repository.save(pet9)
pet_repository.save(pet10)
pet_repository.save(pet11)
pet_repository.save(pet12)
pet_repository.save(pet13)
pet_repository.save(pet14)
pet_repository.save(pet15)

pet1.name = "Fluffy"
pet_repository.change(pet1)
found = pet_repository.select(pet1.id)

print(found.__dict__)








