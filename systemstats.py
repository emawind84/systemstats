import psutil

from flask import Flask, url_for, render_template
from flask import Blueprint

app = Flask(__name__)
app.config['DEBUG'] = True
#app.config['APPLICATION_ROOT'] = '/abc/123'
#app.debug = True # Uncomment to debug

bp = Blueprint('sysinfo', __name__, static_folder='static')


def home():
    return 'System Stats! {}'.format(url_for('memory'))

@app.route('/givemeurl')
@bp.route('/givemeurl')
def givemeurl():
    return "The URL for this page is {}".format(url_for('.givemeurl'))

@bp.route('/cpu')
@app.route('/cpu')
def cpu():
    return str(psutil.cpu_percent()) + '%'

@bp.route('/memory')
@app.route('/memory')
def memory():
    memory = psutil.virtual_memory()
    # Divide from Bytes -> KB -> MB
    available = round(memory.available/1024.0/1024.0,1)
    total = round(memory.total/1024.0/1024.0,1)
    return str(available) + 'MB free / ' + str(total) + 'MB total ( ' + str(memory.percent) + '% )'

@bp.route('/disk')
@app.route('/disk')
def disk():
    disk = psutil.disk_usage('/')
    # Divide from Bytes -> KB -> MB -> GB
    free = round(disk.free/1024.0/1024.0/1024.0,1)
    total = round(disk.total/1024.0/1024.0/1024.0,1)
    return str(free) + 'GB free / ' + str(total) + 'GB total ( ' + str(disk.percent) + '% )'

@bp.route('/')
@app.route('/')
@app.route('/routes')
def routes():
  routes = []
  for rule in app.url_map.iter_rules():
    # To show how to do it, we are going to filter what type of
    # request are we going to show, for example here we are only 
    # going to use GET requests
    if "GET" in rule.methods:
      url = rule.rule
      routes.append(url)
  return render_template('routes.html', routes=routes)

@bp.route('/test')
def testImg():
  return render_template('test.html')

app.register_blueprint(bp, url_prefix = '/sysinfo')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
