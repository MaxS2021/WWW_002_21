def test_reverse():
    # Список тестов
    # Каждый тест — это пара (входное значение, ожидаемое выходное значение)
    test_data = (
        # неправильный тип входного аргумента, ни с чем не будем сравнивать
        (42, None),
        # тоже неправильный входной аргумент, но он "похож" на строку
        # (можно итерироваться и брать срезы)
        (['a', 'b', 'c'], None),
        # "граничный" случай — пустая строка
        ('', ''),
        # "особый" случай — строка, которая не меняется при разворачивании
        ('aba', 'aba'),
        # ещё один "особый" и почти "граничный" случай
        ('a', 'a'),
        # "обычный" случай
        ('abc', 'cba'),
    )

    for input_s, correct_output_s in test_data:
        try:
            # Вычисляем результат на входных данных
            # Есть вариант, что наша функция выбросит исключение,
            # поэтому делаем это в блоке try
            output_s = reverse(input_s)
        except TypeError as E:
            if correct_output_s is None:
                # это исключение и ожидалось, продолжаем тестирование
                continue
            if type(input_s) == str:
                # вход корректный, но выброшено исключение TypeError — это ошибка
                print(f'Ошибка! Не удалось вычислить reverse("{input_s}"). Ошибка: {E}')
                return False
        except Exception as E:
            # Выброшено неожиданное исключение — это ошибка
            print(f'Ошибка! Не удалось вычислить reverse("{input_s}"). Ошибка: {E}')
            return False
        else:
            if output_s != correct_output_s:
                # если ответ не совпал с ожидаемым, завершаем тестирование и возвращаем False
                print(f'Ошибка! reverse({input_s}) равно {output_s} вместо "{correct_output_s}"')
                return False
    # тестирование успешно пройдено
    print('Все тесты пройдены успешно')
    return True

def reverse(s):
    if type(s) != str:
        raise TypeError()
    return s[::-1]

test_reverse()