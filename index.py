import bottle
from bottle import Bottle, route, run, Response, template
import json
import image

import cProfile, pstats, io
from pstats import SortKey

pr = cProfile.Profile()
pr.enable()

app = Bottle()

def call_service():
    directoryName = 'photos'
    image.process(directoryName)

@app.route('/')
def index():
    """Home page"""
    title = "Image Processor App"
    call_service()
    return template('index.tpl',data="Request completed!", title=title)

if __name__ == '__main__':
	run(app, host='0.0.0.0', port=8000, debug=False, reloader=True)
	
serverApp = bottle.default_app()

pr.disable()
s = io.StringIO()
sortby = SortKey.TIME
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
