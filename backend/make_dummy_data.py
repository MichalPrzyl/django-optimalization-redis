import random
from faker import Faker
from main.models import Person

fake = Faker()

persons = [
    Person(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.unique.email(),
    )
    for _ in range(100)
]

Person.objects.bulk_create(persons)

print("✅ Dodano 100 losowych rekordów!")
