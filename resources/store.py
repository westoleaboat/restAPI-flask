import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
# from db import stores


from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import StoreModel
from schemas import StoreSchema

""" A Blueprint in flask smorests is used to divide an API into multiple segments """

blp = Blueprint("stores", __name__, description="Operations on stores")

# connect flask smorest to flask methods
@blp.route("/store/<int:store_id>")
class Store(MethodView):
	""" When we send a get/delete request to /store we want to receive get/delete defined below. Different request will go to different Methodviews because is a different endpoint/ endroute"""
	@blp.response(200, StoreSchema)
	def get(self, store_id):
		store = StoreModel.query.get_or_404(store_id)
		return store
    

	def delete(self, store_id):
		store = StoreModel.query.get_or_404(store_id)
		db.session.delete(store)
		db.session.commit()
		# raise NotImplementedError("deleting is not implemented")
		return {"message": "Store deleted"}


@blp.route("/store")
class StoreList(MethodView):
	@blp.response(200, StoreSchema(many=True))
	def get(self):
	# return {"stores": list(stores.values())}
		# return stores.values()
		return StoreModel.query.all()

	@blp.arguments(StoreSchema)
	@blp.response(200, StoreSchema)
	def post(self, store_data):
		store = StoreModel(**store_data)
		try:
			db.session.add(store)
			db.session.commit()
		except IntegrityError:
			abort(
				400,
				message="A store with that name already exists.",
			)
		except SQLAlchemyError:
			abort(500, message="An error occurred.")


		return store