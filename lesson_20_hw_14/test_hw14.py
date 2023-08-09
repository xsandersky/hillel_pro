from hw_14 import valid_passport_number, valid_inn, valid_car_number

def test_valid_passport_numbe():
    #given
    pass_1 = 'ВО135548'
    pass_2 = 'О135548'
    pass_3 = '135548'
    pass_4 = 'ВО13554'
    pass_5 = 'ВО1355488'
    pass_6 = 'SY135548'

    expected_result_1 = True
    expected_result_2 = False
    expected_result_3 = False
    expected_result_4 = False
    expected_result_5 = False
    expected_result_6 = False

    #when
    result_1 = valid_passport_number(pass_1)
    result_2 = valid_passport_number(pass_2)
    result_3 = valid_passport_number(pass_3)
    result_4 = valid_passport_number(pass_4)
    result_5 = valid_passport_number(pass_5)
    result_6 = valid_passport_number(pass_6)

    #then
    print('asdasdasd')
    assert result_1 == expected_result_1
    assert result_2 == expected_result_2
    assert result_3 == expected_result_3
    assert result_4 == expected_result_4
    assert result_5 == expected_result_5
    assert result_6 == expected_result_6


def test_valid_inn():
    #given
    inn_1 = '5130057915'
    inn_2 = '10348910484'
    inn_3 = '0125648034'
    expected_result_1 = True
    expected_result_2 = False
    expected_result_3 = False

    #when
    result_1 = valid_inn(inn_1)
    result_2 = valid_inn(inn_2)
    result_3 = valid_inn(inn_3)

    #then
    assert result_1 == expected_result_1
    assert result_2 == expected_result_2
    assert result_3 == expected_result_3


def test_valid_car_number():
    #given
    car_1 = 'ХХ0483АЄ'
    car_2 = 'АЯ1944НН'
    car_3 = 'Х0483АЄ'
    car_4 = 'ХХ0483Є'
    car_5 = '0483АЄ'
    car_6 = 'ХХ0483'
    car_7 = 'ХХ043АЄ'
    expected_result_1 = True
    expected_result_2 = False
    expected_result_3 = False
    expected_result_4 = False
    expected_result_5 = False
    expected_result_6 = False
    expected_result_7 = False

    #when
    result_1 = valid_car_number(car_1)
    result_2 = valid_car_number(car_2)
    result_3 = valid_car_number(car_3)
    result_4 = valid_car_number(car_4)
    result_5 = valid_car_number(car_5)
    result_6 = valid_car_number(car_6)
    result_7 = valid_car_number(car_7)


    #then
    assert result_1 == expected_result_1
    assert result_2 == expected_result_2
    assert result_3 == expected_result_3
    assert result_4 == expected_result_4
    assert result_5 == expected_result_5
    assert result_6 == expected_result_6
    assert result_7 == expected_result_7


if __name__=='__main__':
    test_valid_car_number()