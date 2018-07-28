from flask import Flask,render_template,request,redirect, url_for
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db',connect_args={'check_same_thread':False}) # Note: I have written connect_args because i was getting this error thread. It was saying the thread was created here and using somewhere else.
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def display():
	restaurant = session.query(Restaurant).first()
	menus = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
	

@app.route('/restaurants/<int:restaurant_id>/', methods =['POST', 'GET'])
def restaurantMenu(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()   # Note: Writing one is crucial to signify you want only one restaurant
	menus = session.query(MenuItem).filter_by (restaurant_id = restaurant_id)
	return render_template('menu.html', restaurant = restaurant, menus = menus)


# Task 1: Create route for newMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/new', methods =['POST', 'GET'])
def newMenuItem(restaurant_id):
	if request.method == "POST":
		newitem = MenuItem(name = request.form['name'], restaurant_id = restaurant_id)
		session.add(newitem)
		session.commit()
		return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
	else:
		return render_template('newmenuitem.html', restaurant_id=restaurant_id)
# Task 2: Create route for editMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit', methods =['POST', 'GET'])
def editMenuItem(restaurant_id, menu_id):
	editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
	if request.method == 'POST':
		if request.form['name']:
			editedItem.name = request.form['name']
		session.add(editedItem)
		session.commit()
		return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
	else:
		# USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU
        # SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
		return render_template(
			'editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem)

# Task 3: Create a route for deleteMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"



if __name__ == '__main__':
	app.debug = True
	app.run('localhost', 8080)
 


