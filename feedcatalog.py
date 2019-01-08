from flask import url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, CatalogItem

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy user
user1 = User(name="Patricio Villar", email="patricior.villar@"
             "gmail.com", picture="https://cdn2.iconfinder.com/data/icons/"
             "happy-users/100/users09-512.png")
session.add(user1)
session.commit()

# Create category #1 and add items to the category
category1 = Category(name="European Mountains", user_id=1)
session.add(category1)
session.commit()

item1 = CatalogItem(user_id=1, name="Rysy",
                    description="The Rysy peak is located in the Tatras "
                    "mountains. Source: Wikipedia.com",
                    category=category1,
                    difficulty="2")
item2 = CatalogItem(user_id=1, name="Jahnaci",
                    description="The Jahanaci peak is located in the Tatras "
                    "mountains. Source: Wikipedia.com",
                    category=category1,
                    difficulty="3")
item3 = CatalogItem(user_id=1, name="Mount Elbrus",
                    description="The Mount Elbrus peak is located in the "
                    "Russia with 5642 msnm. Source: Wikipedia.com",
                    category=category1,
                    difficulty="5")
session.add(item1)
session.add(item2)
session.add(item3)
session.commit()
# Create category #2 and add items to the category
category2 = Category(name="American Mountains", user_id=1)
session.add(category2)
session.commit()

item1 = CatalogItem(user_id=1, name="Yosemite",
                    description="The Yosemite peak is located in the Rocky "
                    "mountains. Source: Wikipedia.com",
                    category=category2,
                    difficulty="5")
item2 = CatalogItem(user_id=1, name="Aconcagua",
                    description="The Aconcagua peak is located in the Andes "
                    "mountains. Source: Wikipedia.com",
                    category=category2,
                    difficulty="5")
item3 = CatalogItem(user_id=1, name="Cerro Bayo",
                    description="The Cerro Bayo peak is located in the Andes "
                    "Mountains. Source: Wikipedia.com",
                    category=category2,
                    difficulty="3")
session.add(item1)
session.add(item2)
session.add(item3)
session.commit()
# Create category #3 and add items to the category
category3 = Category(name="Asian Mountains", user_id=1)
session.add(category3)
session.commit()

item1 = CatalogItem(user_id=1, name="Hkakabo Razi",
                    description="The Hkakabo Razi peak is located in the "
                    "Myanmar mountains. Source: Wikipedia.com",
                    category=category3,
                    difficulty="5")
item2 = CatalogItem(user_id=1, name="Gamlang Razi",
                    description="The Gamlang Razi peak is located in the "
                    "Myanmar mountains. Source: Wikipedia.com",
                    category=category3,
                    difficulty="5")
item3 = CatalogItem(user_id=1, name="Peak 5710",
                    description="The Peak 5710 peak is located in the "
                    "Myanmar with 5710 msnm. Source: Wikipedia.com",
                    category=category3,
                    difficulty="5")
session.add(item1)
session.add(item2)
session.add(item3)
session.commit()
