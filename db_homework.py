# -*- coding: utf-8 -*-
# @Author: ander
# @Date:   2020-03-16 17:58:09
# @Last Modified by:   ander
# @Last Modified time: 2020-03-16 18:49:31
from db_models import Movie, Comment
from peewee import SqliteDatabase
from peewee import Model
from peewee import CharField, IntegerField, FloatField

db = SqliteDatabase('movie_comment_rating.db')


class CommentRating(Model):
	name = CharField()
	movie_id = IntegerField()
	rating = FloatField()
	count = IntegerField()

	class Meta:
		database = db


ratings = {}

# 对全部评论循环一遍
for comment in Comment.select():
	# 只有打分类型为int的数据才处理
	if isinstance(comment.rating, int):
		# 如果是第一次遇到这部电影，做一些初始化操作
		if comment.movieid not in ratings:
			try:
				movie_name = Movie.get(Movie.id == comment.movieid).name
				ratings[comment.movieid] = {
					'name': movie_name,
					'rating': int(comment.rating),
					'count': 1
				}
			except Exception as e:
				# 如果出现问题可以打印出来或者做其他异常处理
				# print('该评论对应的电影ID未找到')
				# print(e)
				pass
		else:
			rating = ratings[comment.movieid]['rating']
			count = ratings[comment.movieid]['count']
			ratings[comment.movieid]['rating'] = (rating * count + int(comment.rating)) / (count + 1)
			ratings[comment.movieid]['count'] += 1

db.connect()
db.create_tables([CommentRating])

for movie_id in ratings:
	CommentRating.create(
		name=ratings[movie_id]['name'],
		movie_id=movie_id,
		rating=ratings[movie_id]['rating'],
		count=ratings[movie_id]['count']
	)
