# 1
for i in range(10):
    print(i+1)

# 2
input_string = input("Введите строку ")
for symbol in input_string:
    print(symbol)

# 3


def get_mid_mark_class(school_class):
    mid_mark = 0
    for score in school_class['scores']:
        mid_mark += score
    mid_mark = mid_mark / len(school_class['scores'])
    return mid_mark


def get_mid_mark(school_marks):
    middle_mark_school = 0
    middle_mark_class = []
    for school_class_scores in school_marks:
        class_mid_mark = get_mid_mark_class(school_class_scores)
        middle_mark_school += class_mid_mark
        middle_mark_class.append({'name': school_class_scores['name'], 'mid_mark': class_mid_mark})
    middle_mark_school = middle_mark_school / len(school_marks)
    return middle_mark_school, middle_mark_class


school_scores = [{'name': '4a', 'scores': [5, 5, 2, 5, 3]},
                 {'name': '4б', 'scores': [5, 3, 5, 2, 5]},
                 {'name': '4в', 'scores': [5, 4, 5, 5, 2, 2, 5]},
                 ]

mid_mark_school, mid_mark_class = get_mid_mark(school_scores)

print(mid_mark_school)
print(mid_mark_class)
