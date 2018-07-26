# Creates the configuration code whcih sets up the envirinment and also links to the various database


import sys #manipualtes the python run time environment
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base= declarative_base()   # instance of the declarative_base() class 

######################### 

#mapper 
class Restaurant(Base):
	__tablename__ = 'restaurant'
	name = Column(String(80), nullable = False) # 80 is the max length of the string and if nullable is declared as false means You cannot leave it blank.
	id = Column(Integer, primary_key = True)  # means this is the primary key


class MenuItem(Base):
	__tablename__ = 'menu_item'
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	course = Column(String(250))
	description = Column(String(250))
	price =	Column(String(8))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id')) # setting up the foreign key to resturant id

	restaurant = relationship(Restaurant) # this class has a relationship with Restaurant class

################


#at the end

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)

	
################