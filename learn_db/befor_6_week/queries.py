from model_salary import Salary
from sqlalchemy.sql import func
from db import db_session
from sqlalchemy import desc


def top_salary(num_rows):
    top_salary = Salary.query.order_by(Salary.salary.desc()).limit(num_rows)

    for s in top_salary:
        print(f"Зп {s.salary}")


def salary_by_sity(city_name):
    top_salary = Salary.query.filter(Salary.city == city_name).\
        order_by(Salary.salary.desc())

    print(f"Город {city_name}")
    for s in top_salary:
        print(f"Зп {s.salary}")


def top_salary_by_domain(domain_name, num_rows):
    top_salary = Salary.query.filter(Salary.email.like(f'%{domain_name}')).\
        order_by(Salary.salary.desc()).limit(num_rows)

    print(f"Домен {domain_name}")
    for s in top_salary:
        print(f"Зп {s.salary}")


def average_salary():
    avg_salary = db_session.query(func.avg(Salary.salary)).scalar()
    print(f"Средняя зп {avg_salary:.2f}")


def count_distinct_cities():
    count_cites = db_session.query(Salary.city).group_by(Salary.city).count()
    print(f'Количество городов {count_cites}')


def top_avg_salary_by_city(num_rows):
    top_salary = db_session.query(
        Salary.city,
        func.avg(Salary.salary).label('avg_salary')).group_by(Salary.city).\
        order_by(desc('avg_salary')).limit(num_rows)

    for city, salary in top_salary:
        print(f"Город {city} зп {salary:.2f}")


if __name__=='__main__':
    top_salary(10)
    salary_by_sity('Саратов')
    top_salary_by_domain("yandex.ru", 10)
    average_salary()
    count_distinct_cities()
    top_avg_salary_by_city(5)
