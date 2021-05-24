# 1
for i in range(10):
    print(i+1)

# 2
input_string = input("Введите строку ")
for symbol in input_string:
    print(symbol)

# 3


def get_mid_mark(school_marks):
    middle_mark_school = 0
    class_middle_marks = []
    for school_class_scores in school_marks:
        class_mid_mark = sum(school_class_scores['scores'])/len(school_class_scores['scores'])
        class_middle_marks.append({"name": school_class_scores["name"], "mid_mark": class_mid_mark})
        middle_mark_school += class_mid_mark
    return class_middle_marks, middle_mark_school/len(school_marks)


school_scores = [{'name': '4a', 'scores': [1, 1, 2, 5, 3]},
                 {'name': '4б', 'scores': [5, 3, 5, 2, 5]},
                 {'name': '4в', 'scores': [5, 4, 5, 5, 2, 2, 5]},
                 ]

classes_mid_marks, mid_mark_school = get_mid_mark(school_scores)

print(classes_mid_marks)
print(mid_mark_school)
