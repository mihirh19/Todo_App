# for database

install flask-sqlalchemy

	
	pip install flask-sqlalchemy
	

# TO configure sqlalchemy

	app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///form.db"
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 


#To set a database to app

to set database with app you need to create a sqllite database

	
	python
	from app import db
	db.create_all()
	exit()
	

# to show database contant

upload your database to this website
[view database](https://inloop.github.io/sqlite-viewer/)
	