from datetime import datetime, timedelta
from helpers import gravatar_for


entry_index = 0


def dummy_entries():
    return [
        new_entry({
            'name': 'Joe Esposito',
            'email': 'joe@joeyespo.com',
            'message': 'Hello',
        }),
        new_entry({
            'name': 'Jesse Legg',
            'email': 'jesse.legg@gmail.com',
            'message': 'Message 2',
        })
    ]


def new_entry(fields):
    global entry_index

    # TODO: validate
    entry_index += 1
    return {
        'id': entry_index,
        'timestamp': str(datetime.utcnow()),
        'name': fields['name'],
        'email': fields['email'],
        'photo': gravatar_for(fields['email']),
        'message': fields['message'],
    }
