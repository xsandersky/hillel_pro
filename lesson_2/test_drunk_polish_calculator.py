from drunk_polish_calculator import op_plus, op_minus, op_multiply, op_divide, main
from io import StringIO
import sys


def test_op_plus():
    #given
    x = 3
    y = 3
    expected_result = 6

    #when
    result = op_plus(x, y)

    #then
    assert result == expected_result


def test_op_minus():
    #given
    x = 10
    y = 20
    expected_result = 10

    #when
    result = op_minus(x, y)

    #then
    assert result == expected_result


def test_op_multiply():
    #given
    x = 2
    y = 3
    expected_result = 6

    #when
    result = op_multiply(x, y)

    #then
    assert result == expected_result


def test_op_divide():
    #given
    x = 8
    y = 4
    expected_result = 2

    #when
    result = op_divide(x, y)

    #then
    assert result == expected_result


def test_main_addition(capsys):
    # Входное выражение для тестирования сложения
    user_input = "5 2 +"

    # Изменяем стандартный ввод, чтобы считать вход пользователя
    sys.stdin = StringIO(user_input)

    # Вызываем главную функцию
    main()

    # Захватываем вывод
    captured = capsys.readouterr()

    # Проверяем, что результат сложения равен 7
    assert captured.out.strip() == "Expression with space delimiter:7.0"

def test_main_subtraction(capsys):
    # Входное выражение для тестирования вычитания
    user_input = "10 4 -"

    # Изменяем стандартный ввод, чтобы считать вход пользователя
    sys.stdin = StringIO(user_input)

    # Вызываем главную функцию
    main()

    # Захватываем вывод
    captured = capsys.readouterr()

    # Проверяем, что результат вычитания равен 6
    assert captured.out.strip() == "Expression with space delimiter:6.0"

def test_main_multiplication(capsys):
    # Входное выражение для тестирования умножения
    user_input = "3 5 *"

    # Изменяем стандартный ввод, чтобы считать вход пользователя
    sys.stdin = StringIO(user_input)

    # Вызываем главную функцию
    main()

    # Захватываем вывод
    captured = capsys.readouterr()

    # Проверяем, что результат умножения равен 15
    assert captured.out.strip() == "Expression with space delimiter:15.0"

def test_main_division(capsys):
    # Входное выражение для тестирования деления
    user_input = "8 4 /"

    # Изменяем стандартный ввод, чтобы считать вход пользователя
    sys.stdin = StringIO(user_input)

    # Вызываем главную функцию
    main()

    # Захватываем вывод
    captured = capsys.readouterr()

    # Проверяем, что результат деления равен 5
    assert captured.out.strip() == "Expression with space delimiter:0.5"
