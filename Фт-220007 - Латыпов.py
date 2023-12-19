import logging
# Настройка логгирования
logging.basicConfig(filename="Lab_13.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

logging.info("Начало работы")
# Запись имени файла в переменную
filename = 'test.txt'

try:
    # Открытия и считывание файла
    with open(filename, encoding='utf-8') as file:
        logging.info("Успешное открытие файла")
        amount_of_question = int(file.readline().strip())
        amount_of_correct_answers = 0
        answers = []
        nums_of_answers = []
        for a in range(amount_of_question):
            question = file.readline().strip()
            amount_of_answers = int(file.readline().strip())
            answer = int(file.readline().strip())
            for b in range(amount_of_answers):
                nums_of_answers.append(b + 1)
                answers.append(file.readline().strip())
            # Вывод вопросов
            print(question)
            logging.info(f"Вопрос {a + 1} - {question}")
            for c in range(amount_of_answers):
                print(f'{c + 1}. {answers[c]}')
            # Запрос ответов с обработкой ошибок
            while True:
                try:
                    user_answer = int(input('Ваш ответ - '))
                    while user_answer not in nums_of_answers:
                        print('Числовая ошибка!!! Введите номер ответа')
                        logging.error(f"Числовая ошибка. Пользователь ввел {user_answer}")
                        user_answer = int(input('Ваш ответ - '))
                    if user_answer == answer:
                        print('Правильно')
                        amount_of_correct_answers += 1
                        logging.info(f"Ответ пользователя - {user_answer}. Он правильный")
                    else:
                        print(f'Неправильно. Правильный ответ - {answer}')
                        logging.info(f"Ответ пользователя - {user_answer}. Он неправильный")
                    break
                except ValueError:
                    print('Буквенная ошибка!!! Введите номер ответа')
                    logging.error(f"Буквенная ошибка.")
            answers.clear()
            nums_of_answers.clear()
            print()
    # Расчет кол-ва правильных ответов из общего кол-ва и вывод
    percentage = (amount_of_correct_answers / amount_of_question) * 100
    print(f'Количество правильных ответов {amount_of_correct_answers} из {amount_of_question} ({round(percentage, 2)}%)')
    logging.info(f"Количество правильных ответов - {amount_of_correct_answers} ({round(percentage, 2)}%)")
except Exception:
    print('Ошибка открытия файла')
    logging.error("Ошибка открытия файла")
logging.info("")