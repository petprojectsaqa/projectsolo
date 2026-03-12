from faker import Faker


fake = Faker(locale='ru_RU')

for _ in range(5):
    print(fake.name())
    print(fake.first_name())
    print(fake.last_name())
    print(fake.company())
    print(fake.address())