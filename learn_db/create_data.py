import csv
import random

from faker import Faker

fake = Faker('ru_RU')

def fake_companies(num_rows = 10):
    companies = []

