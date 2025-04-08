from Maps import Map
from faker import Faker

if __name__ == "__main__":
    fake = Faker()
    hash = Map()

    for i in range(100):
        hash.add(i, [fake.name(), fake.phone_number()])


    print(hash.valueOf(76))