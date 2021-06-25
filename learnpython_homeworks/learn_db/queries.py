from model_salary import Salary


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


if __name__=='__main__':
    top_salary(10)
    salary_by_sity('Саратов')
    top_salary_by_domain("yandex.ru", 10)
