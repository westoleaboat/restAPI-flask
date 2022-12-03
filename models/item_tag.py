from db import db

class ItemTags(db.Model):
    __tablename__ = "items_tag"
    """ Many-to-many relationship. """


    # own ID
    id = db.Column(db.Integer, primary_key=True)
    # two columns which are foreing keys, one of each side of relationship
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))