from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError

# from db import items
from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

""" A Blueprint in flask smorests is used to divide an API into multiple segments """

# blp = Blueprint("Items", __name__, description="Operations on items")
blp = Blueprint("Items", "items", description="Operations on items")

# connect flask smorest to flask methods
@blp.route("/item/<int:item_id>")
class Item(MethodView):
	""" When we send a get/delete request to /store we want to receive get/delete defined below. Different request will go to different Methodviews because is a different endpoint/ endroute"""
	# main success response
	@jwt_required() # cannot call this endpoint unless with correct jwt
	@blp.response(200, ItemSchema)
	def get(self, item_id):
		item = ItemModel.query.get_or_404(item_id)
		return item

	@jwt_required() # cannot call this endpoint unless with correct jwt
	def delete(self, item_id):
		jwt = get_jwt()
		if not jwt.get("is_admin"):
			abort(401, message="Admin priviledge required.")

		item = ItemModel.query.get_or_404(item_id)
		db.session.delete(item)
		db.session.commit()
		# raise NotImplementedError("deleting is not implemented")
		return {"message": "item deleted."}
    

	# ORDER OF DECORATORS MATTERS!, response decorator goes deeper than rest
	@blp.arguments(ItemUpdateSchema) 
	@blp.response(200, ItemSchema)
	def put(self, item_data, item_id): # argument decorators go in front of root arguments
		item = ItemModel.query.get(item_id)
		
		if item:
			item.price = item_data["price"]
			item.name = item_data["name"]
		else:
			item = ItemModel(id=item_id, **item_data)

		db.session.add(item)
		db.session.commit()

		return item

@blp.route("/item")
class ItemList(MethodView):
	""" The JSON the client sends get validated through the ItemSchema"""
	@jwt_required() # cannot call this endpoint unless with correct jwt
	@blp.response(200, ItemSchema(many=True))
	def get(self):
	# return {"items": list(items.values())}
		# return items.values() # this will return a list, not an object!
		return ItemModel.query.all()

	
	# @jwt_required() # cannot call this endpoint unless with correct jwt
	@jwt_required(fresh=True) # cannot call this endpoint unless with correct jwt
	@blp.arguments(ItemSchema) # validating requested data
	@blp.response(201, ItemSchema)
	def post(self, item_data): # receive item_data
		# double * will turn the dict into keyword args
		item = ItemModel(**item_data)

		try: 
			db.session.add(item)
			db.session.commit() # write to db
		except SQLAlchemyError:
			abort(500, message="An error occured when importing the item")

		return item 