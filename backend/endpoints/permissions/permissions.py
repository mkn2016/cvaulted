from functools import wraps

from flask import request
from flask.json import jsonify
from flask_praetorian import current_user_id, current_user


def is_owner(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user().is_valid():
            if request.view_args.get("id") == current_user_id():
                return func(args, kwargs)
            else:
                return jsonify(
                    {
                        "message": "Access forbidden."
                    },
                    403
                )
    return wrapper


def is_not_owner(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user().is_valid():
            if request.view_args.get("id") != current_user_id():
                return func(args, kwargs)
            else:
                return jsonify(
                    {
                        "message": "Access forbidden"
                    },
                    403
                )
    return wrapper
