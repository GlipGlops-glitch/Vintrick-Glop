# python fix_imports.py

import os

for subdir in ['api', 'models']:
    path = f'vintrace_client/swagger_client/{subdir}/__init__.py'
    if os.path.exists(path):
        with open(path, 'r', encoding='utf8') as f:
            content = f.read()
        # Replace .api.xxx with .xxx
        new_content = content.replace('from .api.', 'from .')
        if new_content != content:
            with open(path, 'w', encoding='utf8') as f:
                f.write(new_content)