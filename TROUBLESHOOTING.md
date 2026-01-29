# Troubleshooting Guide

## Common Issues and Solutions

### 1. Django Not Installed Error
**Error**: `ModuleNotFoundError: No module named 'django'`

**Solution**:
```bash
pip3 install Django
# or
python3 -m pip install Django
```

### 2. Migration Issues
**Error**: Migration-related errors

**Solution**:
```bash
# Delete existing migrations (except __init__.py)
rm library/migrations/000*.py

# Create fresh migrations
python3 manage.py makemigrations library

# Apply migrations
python3 manage.py migrate
```

### 3. Template Not Found Error
**Error**: `TemplateDoesNotExist`

**Solution**: Make sure templates exist in `library/templates/lib/`
- lend.html
- return.html  
- fine.html

### 4. URL Configuration Error
**Error**: `NoReverseMatch` or URL not found

**Solution**: Check that URLs are properly configured:
- Main urls.py includes library.urls
- Library urls.py has correct patterns

### 5. Form Import Error
**Error**: Import errors for forms

**Solution**: Check imports in views.py match form class names in forms.py

### Quick Setup Commands:
```bash
# 1. Install Django
pip3 install Django

# 2. Make migrations
python3 manage.py makemigrations

# 3. Apply migrations  
python3 manage.py migrate

# 4. Create superuser (optional)
python3 manage.py createsuperuser

# 5. Run server
python3 manage.py runserver
```

### If you're still getting errors:
1. Share the exact error message
2. Check which command/action triggers the error
3. Verify Django installation: `python3 -c "import django; print(django.get_version())"`