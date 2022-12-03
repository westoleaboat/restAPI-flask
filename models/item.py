from db import db

class ItemModel(db.Model):
	""" Mapping between a row in a table to a Python class, therefore Python objects """
	# we want to use a table called items for this class and all the objects of this class
	__tablename__ = "items"

	# define the columns of this table
	id = db.Column(db.Integer, primary_key=True) #incrementing from 1
	name = db.Column(db.String(80), unique=True,nullable=False) #nullable means cannot create an item witouth name
	description = db.Column(db.String)
	price = db.Column(db.Float(precision=2), unique=False, nullable=False)
	# foreingKey is one-to-many relationship from store_id of item db to store db
	store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)
	
	store = db.relationship("StoreModel", back_populates="items")
	tags = db.relationship("TagModel", back_populates="items", secondary="items_tag")