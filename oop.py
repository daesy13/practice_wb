
class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print("My name is {}".format(self.name))


class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print("... and I am {}".format(self.hero_name))

# Instances:
daesy =  Person("Daesy")
daesy.reveal_identity()

# gia = SuperHero("Gia Power", "Wonder Woman")
# gia.reveal_identity()