from peewee import SqliteDatabase
from peewee import Model
from peewee import CharField, DateField, ForeignKeyField
from datetime import date

db = SqliteDatabase('people.db')


class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db


# 创建表
# db.connect()
# db.create_tables([Person, Pet])

# 增加
# uncle_bob = Person(name='Bob', birthday=date(1960, 1, 12))
# uncle_bob.save()
# sam = Person.create(name='Sam', birthday=date(1970, 4, 5))

# 查找或增加
user1, created1 = Person.get_or_create(name='Sam')
user2, created2 = Person.get_or_create(name='Kate', birthday=date(1988, 3, 31))

# 查找后修改
kate = Person.get(name='Kate')
kate.birthday = date(1988, 12, 6)
kate.save()

# 更新
query = Person.update(name='Mr.' + Person.name)
query.execute()

# 删除
kate = Person.get(Person.name.endswith('Kate'))
kate.delete_instance()

# 删除语句
q = Person.delete().where(Person.name.endswith('Bob'))
print(q.sql())
q.execute()
