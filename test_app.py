from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EasyAid.settings')
application = get_wsgi_application()

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8080, application)
    print("Server started on http://0.0.0.0:8080")
    server.serve_forever()