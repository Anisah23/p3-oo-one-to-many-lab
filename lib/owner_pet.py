class Owner:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise Exception("Owner name must be a non-empty string")
        self.name = name
        self._pets = []

    def pets(self):
        """Return all pets belonging to this owner"""
        return self._pets

    def add_pet(self, pet):
        """Add a pet to this owner after validation"""
        if not isinstance(pet, Pet):
            raise Exception("Must add a Pet instance")
        self._pets.append(pet)
        pet.owner = self

    def get_sorted_pets(self):
        """Return this owner's pets sorted by name"""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise Exception("Pet name must be a non-empty string")
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"pet_type must be one of {Pet.PET_TYPES}")

        self.name = name
        self.pet_type = pet_type
        self.owner = None

   
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("owner must be an Owner instance")
            self.owner = owner
            owner.add_pet(self)

        Pet.all.append(self)

    def __repr__(self):
        return f"<Pet {self.name} ({self.pet_type}) Owner: {self.owner.name if self.owner else 'None'}>"
