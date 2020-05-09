from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

database = SqliteDatabase(r'.\data_set\douban_comment_data.db')


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Comment(BaseModel):
    add_time = TextField(column_name='ADD_TIME')
    content = TextField(column_name='CONTENT')
    creator = TextField(column_name='CREATOR')
    id = AutoField(column_name='ID', null=True)
    movieid = TextField(column_name='MOVIEID')
    rating = IntegerField(column_name='RATING')
    time = TextField(column_name='TIME')

    class Meta:
        table_name = 'comment'


class Movie(BaseModel):
    add_time = TextField(column_name='ADD_TIME')
    id = TextField(column_name='ID', primary_key=True)
    name = TextField(column_name='NAME')

    class Meta:
        table_name = 'movie'


class MovieChinese(BaseModel):
    add_time = TextField(column_name='ADD_TIME')
    id = TextField(column_name='ID', primary_key=True)
    name = TextField(column_name='NAME')

    class Meta:
        table_name = 'movie_chinese'


class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = 'sqlite_sequence'
        primary_key = False


print(database.get_tables())

movie = Movie.get(Movie.name == '低俗小说')
print(movie.id)

movie2 = Movie.get_or_none(Movie.name == 'lalalalalalal')
print(movie2)

movie_id = movie.id
comments = Comment.select().where(Comment.movieid == movie_id, Comment.rating > 4)
for comment in comments:
    print(comment.content)

comments = Comment.select().where(Comment.movieid == movie_id).order_by(Comment.rating.desc())
for comment in comments:
    print(comment.content)

comments = Comment.select().where(Comment.movieid == movie_id).limit(50)
for comment in comments:
    print(model_to_dict(comment))
