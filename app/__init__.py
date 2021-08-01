#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Simple flask app"""

from flask import Flask

app = Flask(__name__)       # __name__ is a dunder variable or "Magic Variable"


@app.route("/")
def about_me():             # view funtion " the functions dirtectly beneth the " '@' decorator"
    me = {
        "first_name": "Jorge",
        "last_name": "Guzman",
        "hobbies": "DIY stuff and dealing with Pooches",
        "test": True        # Boolean Variable
    }
    return me               # when it returns from a view functions, it converts into a JSON function.
