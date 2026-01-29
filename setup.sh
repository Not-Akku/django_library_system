#!/bin/bash

echo "Setting up Library Admin System..."

# Install Django
echo "Installing Django..."
pip3 install Django

# Check if installation was successful
if python3 -c "import django" 2>/dev/null; then
    echo "Django installed successfully!"
    
    # Make migrations
    echo "Creating migrations..."
    python3 manage.py makemigrations
    
    # Apply migrations
    echo "Applying migrations..."
    python3 manage.py migrate
    
    echo "Setup complete! You can now run:"
    echo "python3 manage.py runserver"
else
    echo "Django installation failed. Please install manually:"
    echo "pip3 install Django"
fi