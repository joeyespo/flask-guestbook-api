from __future__ import print_function

from flask import Flask, request, jsonify
from data import dummy_entries, new_entry


# Flask application
app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.config.from_pyfile('settings_local.py', silent=True)


# In-memory entries
entry_collection = dummy_entries()


# Views
@app.route('/')
def index():
    return jsonify({'message': 'TODO: Implement root response.'})


@app.route('/entries', methods=['GET', 'POST'])
def entries():
    if (request.method == 'POST'):
        entry_collection.append(new_entry(request.form))
        return jsonify({})

    print(entry_collection)
    return jsonify({
        'entries': entry_collection,
    })


@app.route('/entry/<entry_id>')
def entry(entry_id):
    # TODO: PATCH to update individual fields of the entry
    # TODO: PUT to replace the entry entirely

    # TODO: Look up entries by ID and return the entry
    return jsonify(entry_collection[0])



# Run development server
if __name__ == '__main__':
    app.run(app.config['HOST'], app.config['PORT'], app.debug)
