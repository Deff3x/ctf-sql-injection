from flask import Flask, request, render_template, redirect
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

if os.path.exists('database.db'):
	os.remove('database.db')

con = sqlite3.connect('database.db', check_same_thread=False)

with sqlite3.connect('database.db', check_same_thread=False) as con:
	cur = con.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, title TEXT, content TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')
	cur.execute('CREATE TABLE IF NOT EXISTS flags (id INTEGER PRIMARY KEY, name TEXT, flag TEXT)')
	cur.execute('INSERT INTO flags (name, flag) VALUES (?, ?)', ("flag", open("flag.txt").read()))
	cur.execute('INSERT INTO notes (title, content) VALUES (?, ?)', ("Welcome", "Welcome to the notes app!"))


def default_route(filter=None):
	cursor = con.cursor()
	if filter is not None:
		cursor.execute('SELECT * FROM notes WHERE title LIKE ? ORDER BY id DESC', (f'"%{filter}%"',))
	else:
		cursor.execute('SELECT * FROM notes ORDER BY id DESC')
	notes = cursor.fetchall()
	return render_template("index.html", notes=notes)


@app.route('/', methods=['GET'])
def index():
	filter = request.args.get('filter')
	return default_route(filter)


@app.route('/remove', methods=['POST'])
def remove_note():
	note_id = request.form['note_id']
	if note_id:
		cursor = con.cursor()
		cursor.execute('DELETE FROM notes WHERE id = %s' % (note_id,))
		return redirect('/')
	return redirect('/')


@app.route('/create', methods=['POST', 'GET'])
def create_note():
	if request.method == 'POST':
		title = request.form['title']
		content = request.form['content']
		print("Title, Content: ", title, content)
		if title and content:
			cursor = con.cursor()
			cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
			return redirect('/')
		return "Title or content is missing"
	return render_template('create.html')


@app.errorhandler(404)
def page_not_found(e):
	return default_route(None), 404

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=9374)
	