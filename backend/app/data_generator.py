from faker import Faker
import random

fake = Faker()

def generate_fake_data():
    return {
        "company": fake.company(),
        "revenue": random.randint(10000, 100000),
        "users": random.randint(100, 5000)
    }