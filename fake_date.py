import json
from faker import Faker
from random import randrange
from db_init import abonent_collection
from datetime import datetime
from bson.json_util import dumps, loads

fake = Faker(['uk-UA', 'ru-RU', 'en-US'])


def create_fake_abonent():
    birthday = fake.date_between(start_date='-80y', end_date='-10y')
    return {
        "name": fake.name(),
        "birthday": datetime(birthday.year, birthday.month, birthday.day),
        "address": fake.address(),
        "emails": [fake.ascii_email() for _ in range(randrange(0, 4))],
        "phones": [fake.phone_number() for _ in range(randrange(0, 4))],
        "notes": [{'date': fake.date_time_between_dates(datetime_start=datetime(year=2016, month=1, day=1), datetime_end=datetime.today()).replace(microsecond=0), 'note': fake.sentence(
            nb_words=10, variable_nb_words=True)} for _ in range(randrange(0, 2))]
    }


def create_fake_abonents(num=10):
    return [create_fake_abonent() for _ in range(num)]


if __name__ == '__main__':
    data = create_fake_abonents()
    print(data)
    #result = abonent_collection.insert_many(data)
    #print(f"Result insertion mongo_db {result}")
