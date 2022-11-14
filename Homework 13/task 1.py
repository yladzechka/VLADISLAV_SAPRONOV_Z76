'''
Необходимо создать таблицы 1 и 2 в вашей БД с помощью ORM Peewee. (Таблицы на диске)
'''
import peewee
from db_connection import db


class Table1(peewee.Model):
    Part = peewee.CharField(50)
    Cat = peewee.FloatField()

    class Meta:
        database = db
        db_table = "Table 1"


class Table2(peewee.Model):
    Catnumb = peewee.FloatField()
    Cat_name = peewee.CharField(50)
    Price = peewee.FloatField()

    class Meta:
        database = db
        db_table = "Table 2"


Table1.drop_table()
Table1.create_table()
Table2.drop_table()
Table2.create_table()
