from yandex_testing_lesson import is_palindrome

def test_polindrome():
    # Список тестов
    # Каждый тест — это пара (входное значение, ожидаемое выходное значение)
    test_data = (
        (42, False),
        (['a', 'b', 'c'], False),
        ('', True),
        ('aba', True),
        ('a', True),
        ('abc', False),
        ("123454321", True)
    )

    for input_s, correct_output_s in test_data:
        try:
            output_s = is_palindrome(input_s)
        except TypeError as E:
            if correct_output_s is None:
                # это исключение и ожидалось, продолжаем тестирование
                continue
            if type(input_s) == str:
                # вход корректный, но выброшено исключение TypeError — это ошибка
                #print(f'Ошибка! Не удалось выполнить is_polindrome("{input_s}"). Ошибка: {E}')
                print('NO')
                return False
            #print(input_s, "<===============")
        except Exception as E:
            # Выброшено неожиданное исключение — это ошибка
            #print(f'Ошибка! Не удалось выполнить is_polindrome("{input_s}"). Ошибка: {E}')
            print('NO')
            return False
        else:
            if output_s != correct_output_s:
                # если ответ не совпал с ожидаемым, завершаем тестирование и возвращаем False
                #print(f'Ошибка! is_polindrome({input_s}) равно {output_s} вместо "{correct_output_s}"')
                print('NO')
                return False
    # тестирование успешно пройдено
    print('YES')
    return True

test_polindrome()