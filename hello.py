def appl(environ, start):
    start('200 OK', [('Content-Type', 'text/plain')])
    for key, value in environ.items():
        if key == 'QUERY_STRING':
            body = value.split('&')
    return '\n'.join(body)


bind = '0.0.0.0.8080'
command = '/etc/init.d/gunicorn hello:appl'
workers = 5

CONFIG = {
  'mode': 'wsgi',
  'working_dir': '/home/box/web',
  'python': '/usr/bin/python3',
  'args': (
    '--bind=0.0.0.0:8080',
    '--workers=5',
    '--timeout=15',
    '--log-level=debug',
    'hello:appl'
  )
}
