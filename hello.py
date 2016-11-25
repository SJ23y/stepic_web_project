def appl(environ, start):
    start('200 OK', [('Content-Type', 'text/plain')])
    for key, value in environ.items():
        if key == 'QUERY_STRING':
            body = value.split('&')
    return '\n'.join(body)


bind = '0.0.0.0.8080'
command = '/etc/init.d/gunicorn hello:appl'

