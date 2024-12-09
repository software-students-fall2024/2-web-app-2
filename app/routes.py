from flask import render_template, request, redirect, url_for
from app import app, mongo
from bson.objectid import ObjectId

@app.route('/')
def home():
    data = mongo.db.items.find()
    return render_template('home.html', items=data)

@app.route('/add', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'description': request.form['description']
        }
        mongo.db.items.insert_one(data)
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_data(id):
    item = mongo.db.items.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        updated_data = {
            'name': request.form['name'],
            'description': request.form['description']
        }
        mongo.db.items.update_one({'_id': ObjectId(id)}, {'$set': updated_data})
        return redirect(url_for('home'))
    return render_template('edit.html', item=item)

@app.route('/delete/<id>')
def delete_data(id):
    mongo.db.items.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('home'))

@app.route('/search', methods=['GET', 'POST'])
def search_data():
    query = request.form.get('query', '')
    results = mongo.db.items.find({'name': {'$regex': query, '$options': 'i'}})
    return render_template('search.html', items=results, query=query)
