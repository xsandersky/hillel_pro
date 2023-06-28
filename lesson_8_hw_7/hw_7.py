import uuid
import os

import psycopg2
from psycopg2.pool import SimpleConnectionPool
from datetime import datetime


class Card:
    def __init__(self):
        self.connection = psycopg2.connect(
            host = '127.0.0.1',
            port = '5432',
            dbname = 'bank_cards',
            user = 'vitalii',
            password = os.environ.get('DB_PASSWORD', '1325')
        )
        self.cursor = self.connection.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS cards(
            id TEXT NOT NULL,
            number TEXT NOT NULL UNIQUE,
            cvv SMALLINT NOT NULL,
            issue TEXT,
            expiration TEXT NOT NULL,
            balance INT,
            status TEXT NOT NULL)""")
        self.connection.commit()


    def save_to_db(self, number:str, cvv:int, issue:str, expiration:str, status:str, balance=None):
        self.cursor.execute("SELECT * FROM cards WHERE number = %s", (number,))
        self.existing_data = self.cursor.fetchone()

        if self.existing_data is None:
            self.id = str(uuid.uuid4())
            self.cursor.execute("""INSERT INTO cards 
                (id, number, cvv, issue, expiration, balance, status) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                (self.id, number, cvv, issue, expiration, balance, status))
            self.connection.commit()
            print('Добавлена новая запись')
        else:
            print('Такие данные уже существуют')


    def get_by_issue(self, issue:str):
        self.cursor.execute("SELECT * FROM cards WHERE issue = %s", (issue,))

        self.record = self.cursor.fetchall()
        for row in self.record:
            print(f'id: {row[0]} | number: {row[1]} | cvv: {row[2]} | issue: {row[3]} | expiration: {row[4]} | status: {row[5]}')


    def get_from_issue_to_expiration(self, issue, expiration):
        self.cursor.execute("SELECT * FROM cards WHERE issue = %s and expiration = %s", (issue, expiration))

        self.record = self.cursor.fetchall()
        for row in self.record:
            print(f'id: {row[0]} | number: {row[1]} | cvv: {row[2]} | issue: {row[3]} | expiration: {row[4]} | status: {row[5]}')


    def get_by_balance(self, balance):
        self.cursor.execute("SELECT * FROM cards WHERE balance > %s", (balance,))
        self.record = self.cursor.fetchall()
        for row in self.record:
            print(f'id: {row[0]} | number: {row[1]} | cvv: {row[2]} | issue: {row[3]} | expiration: {row[4]} | status: {row[5]}')
    
    def get_by_number(self, number):
        self.cursor.execute("SELECT * FROM cards WHERE number = %s", (number,))
        self.record = self.cursor.fetchall()
        # for row in self.record:
        #     print(f'id: {row[0]} | number: {row[1]} | cvv: {row[2]} | issue: {row[3]} | expiration: {row[4]} | status: {row[5]}')
        return self.record
        


    def change_status(self):
        self.time_now = datetime.now()
        self.current_month = self.time_now.month
        self.current_year = self.time_now.year % 100

        self.status_new = 'new'
        self.status_active = 'active'
        self.status_block = 'block'

        self.query = self.cursor.execute("SELECT id, expiration, balance, status FROM cards")
        self.record = self.cursor.fetchall()

        for row in self.record:
            self.check_id = row[0]
            self.balance = int(row[2])
            self.status = row[3]

            if  self.balance == 0 and self.current_year <= int(row[1][3:]):
                if self.current_year == int(row[1][3:]):
                    if self.current_month < int(row[1][:2]):
                        if self.status == 'new':
                            continue
                        self.cursor.execute("UPDATE cards SET status = %s WHERE id = %s", (self.status_new, self.check_id))
                        print(f'Запись ID: {self.check_id} успешно обновлена. Статус изменен на: {self.status_new}')
                        self.connection.commit()

                else:
                    self.cursor.execute("UPDATE cards SET status = %s WHERE id = %s", (self.status_new, self.check_id))
                    print(f'Запись ID: {self.check_id} успешно обновлена. Статус изменен на: {self.status_new}')
                    self.connection.commit()


            elif self.balance > 0 and self.current_year <= int(row[1][3:]):
                if self.current_year == int(row[1][3:]):
                    if self.current_month < int(row[1][:2]):
                        if self.status == 'active':
                            continue
                        self.cursor.execute("UPDATE cards SET status = %s WHERE id = %s", (self.status_active, self.check_id))
                        print(f'Запись ID: {self.check_id} успешно обновлена. Статус изменен на: {self.status_active}')
                        self.connection.commit()

                else:
                    self.cursor.execute("UPDATE cards SET status = %s WHERE id = %s", (self.status_active, self.check_id))
                    print(f'Запись ID: {self.check_id} успешно обновлена. Статус изменен на: {self.status_active}')
                    self.connection.commit()

            else:
                if self.status == 'block':
                    continue
                self.cursor.execute("UPDATE cards SET status = %s WHERE id = %s", (self.status_block, self.check_id))
                print(f'Запись ID: {self.check_id} успешно обновлена. Статус изменен на: {self.status_block}')
                self.connection.commit()


    def disconnect(self):
        if self.connection:
            self.connection.close()

card, card, card, card = Card(), Card(), Card(), Card()
card, card, card, card = Card(), Card(), Card(), Card()

#Добавить юзера в таблицу
# card.save_to_db('0000-0000-0000-0000', 101, '03/18', '03/22', 'new', 0)
# card.save_to_db('1111-1111-1111-1111', 111, '04/19', '04/24', 'new', -55)
# card.save_to_db('2222-2222-2222-2222', 222, '03/19', '03/22', 'new', 30)
# card.save_to_db('3333-3333-3333-3333', 333, '03/18', '01/22', 'new', 40)
# card.save_to_db('4444-4444-4444-4444', 444, '04/19', '04/25', 'new', 50)
# card.save_to_db('5555-5555-5555-5555', 555, '03/18', '03/22', 'new', 60)
# card.save_to_db('6666-6666-6666-6666', 666, '11/22', '11/28', 'new', 70)
# card.save_to_db('8888-8888-8888-8888', 888, '06/23', '06/29', 'new', 80)

#Получить данные из таблицы
#card.get_by_issue('03/18')
#card.get_from_issue_to_expiration('03/18', '02/22')
#card.get_by_balance(20)
#card.get_by_number('0000-0000-0000-0000')


#CHANGE STATUS
#card.change_status()
