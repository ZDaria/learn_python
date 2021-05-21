# 1


def hello_user():
    mark = 0
    while mark == 0:
        answer = input("Как дела? ")
        if answer == "Хорошо":
            mark = 1


hello_user()


# 2
actions_list = {"Как дела?": "Хорошо!",
                "Что делаешь?": "Программирую"}


def user_ask(question_dict: dict):
    print("Введите вопрос. Для остановки введите Пока")
    while True:
        user_question = input("Пользователь: ")
        prog_answer = question_dict.get(user_question)
        if user_question == "Пока":
            print("Программа: И тебе пока!")
            break
        elif prog_answer is not None:
            print(f"Программа: {prog_answer}")


user_ask(actions_list)
