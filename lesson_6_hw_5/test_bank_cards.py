import pytest
from bank_cards import Card

@pytest.fixture
def card():
    card_instance = Card()
    yield card_instance
    card_instance.disconnect()

# def test_save_to_db_unique(card):
#     card.save_to_db('0000-0000-0000-0000', 101, '03/18', '03/22', 'new', 0)
#     with pytest.raises(Exception):
#         card.save_to_db('0000-0000-0000-0000', 101, '03/18', '03/22', 'new', 0)

def test_change_status(card):
    card.save_to_db('1111-1111-1111-1111', 111, '04/19', '04/24', 'new', -55)
    card.change_status()
    card.get_by_number('1111-1111-1111-1111')
    assert card.record[0][6] == 'block'


# def test_get_by_number(card):
#     card.save_to_db('5555-5555-5555-5555', 555, '03/18', '03/22', 'new', 60)
#     card.get_by_number('5555-5555-5555-5555')
#     assert len(card.record) == 1
#     assert card.record[0][1] == '5555-5555-5555-5555'

# def test_get_by_issue(card):
#     card.save_to_db('6666-6666-6666-6666', 666, '11/22', '11/28', 'new', 70)
#     card.get_by_issue('11/22')
#     assert len(card.record) == 1
#     assert card.record[0][3] == '11/22'

# def test_get_from_issue_to_expiration(card):
#     card.save_to_db('7777-7777-7777-7777', 777, '07/18', '01/24', 'new', 80)
#     card.save_to_db('8888-8888-8888-8888', 888, '07/18', '01/22', 'new', 90)
#     card.get_from_issue_to_expiration('07/18', '01/24')
#     assert len(card.record) == 1
#     assert card.record[0][3] == '07/18'
#     assert card.record[0][4] == '01/24'

def test_disconnect(card):
    assert card.connection is not None
