from db import db

class StoreModel(db.Model):
	""" Mapping between a row in a table to a Python class, therefore Python objects """
	# we want to use a table called stores for this class and all the objects of this class
	__tablename__ = "stores"

	# define the columns of this table
	id = db.Column(db.Integer, primary_key=True) #incrementing from 1
	name = db.Column(db.String(80), unique=True, nullable=False) #nullable means cannot create an item witouth name
	items = db.relationship("ItemModel", back_populates="store", lazy="dynamic")
	tags = db.relationship("TagModel", back_populates="store", lazy="dynamic")