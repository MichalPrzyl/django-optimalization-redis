from main.models import Person, Profile, ProfileB, ProfileC
from faker import Faker


fake = Faker()

persons = Person.objects.all()
for person in persons:
    new_profile = Profile.objects.create(
        name=fake.unique.email(),
        column_a=fake.unique.email(),
        column_b=fake.unique.email(),
        column_c=fake.unique.email(),
        column_d=fake.unique.email(),
        column_e=fake.unique.email()
    )

    new_profile_b = ProfileB.objects.create(
        name=fake.unique.email(),
        column_a=fake.unique.email(),
        column_b=fake.unique.email(),
        column_c=fake.unique.email(),
        column_d=fake.unique.email(),
        column_e=fake.unique.email()
    )

    new_profile_c = ProfileC.objects.create(
        name=fake.unique.email(),
        column_a=fake.unique.email(),
        column_b=fake.unique.email(),
        column_c=fake.unique.email(),
        column_d=fake.unique.email(),
        column_e=fake.unique.email()
    )

    person.profile = new_profile
    person.profile_b = new_profile_b
    person.profile_c = new_profile_c
    person.save()
