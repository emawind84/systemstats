#!/usr/bin/env python

from systemstats import app

if __name__ == "__main__":
    app.run()

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["<h1 style='color:blue'>Hello There!</h1>"]
