from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/menu')
def menu():
	conn = sqlite3.connect('restaurant.db')
	c = conn.cursor()
	c.execute('SELECT ID, NAME, PRICE FROM menu')
	items = c.fetchall()
	return render_template('menu.html', items=items)

@app.route('/order', methods=['GET', 'POST'])
def order():
	if request.method == 'POST':
		ID = request.form['ID']
		NAME = request.form['NAME']
		PRICE = request.form['PRICE']

		conn = sqlite3.connect('orders2.db')
		c = conn.cursor()
		c.execute('''INSERT INTO customerorders (ID, NAME, PRICE) VALUES (?, ?, ?)''', (ID, NAME, PRICE))
		conn.commit()
		return 'Order Successful'
		conn.close()
	else:
		return render_template('order.html')
		conn.close()

@app.route('/orders')
def orders():
	conn = sqlite3.connect('orders2.db')
	c = conn.cursor()
	c.execute('SELECT * FROM customerorders')
	customerorders = c.fetchall()
	conn.close()
	return render_template('orders.html', customerorders=customerorders)


if __name__ == '__main__':
	app.run(debug=True)
