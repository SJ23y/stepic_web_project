def appl(environ, start):
    start('200 OK', [('Content-Type', 'text/plain')])
    for key, value in environ.items():
        if key == 'QUERY_STRING':
            body = value.split('&')
    return '\n'.join(body)





