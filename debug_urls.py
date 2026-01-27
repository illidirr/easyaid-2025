import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EasyAid.settings')
django.setup()

from django.urls import get_resolver

resolver = get_resolver()
print("=== ВСЕ URL МАРШРУТЫ ===")
for pattern in resolver.url_patterns:
    print(f"URL: {pattern.pattern} -> {pattern.name if hasattr(pattern, 'name') else 'No name'}")