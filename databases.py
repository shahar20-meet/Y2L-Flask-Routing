from model import Base, Product, Cart


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def createThread():
	engine = create_engine('sqlite:///database.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session

def add_product(session,name,price,picture_link,description):
	product=Product(name=name,price=price,picture_link=picture_link,description=description)
	session.add(product)
	session.commit()

def edit_by_id(session,product_id,name,price,picture_link,description):
	 p = session.query(Product).filter_by(id=product_id).first()
	 p.name = name
	 p.price = price
	 p.picture_link = link
	 p.description = description
	 session.commit()


def delete_by_id(session,product_id):
	session.query(product_id).filter_by(id=product_id).delete()
	session.commit()


def return_all(session):
	Products = session.query(Product).all()
	return Products

	
def return_by_id(session):
	Product = session.query(Product).filter_by(id=product_id)
	return Product

def Add_To_Cart(session,product_id):
	cart=Cart(product_id)
	session.add(Cart)
	session.commit()

# add_product("A STAR","$29,999.79","star.jpg","This is a star loai gave me")