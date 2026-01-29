# Library Admin System

A comprehensive Django-based library management system built to demonstrate Django models, database relationships, form handling, and security best practices.

## 🚀 Features

### Core Functionality
- **Book Lending**: Automated lending system with due date calculation (14 days)
- **Book Returns**: Smart return processing with overdue fine calculation
- **Fine Management**: Complete payment system with validation and balance tracking
- **Reader Management**: Member registration with automatic membership date
- **Inventory Tracking**: Real-time book availability management

### Advanced Features
- **Automatic Fine Calculation**: ₹0.50/day + ₹25.00 base fee for overdue books
- **Payment Validation**: Prevents overpayment and handles partial payments
- **ISBN Validation**: Supports both ISBN-10 and ISBN-13 formats
- **Data Integrity**: Comprehensive field validation and constraints
- **Security**: Environment-based configuration and input sanitization

## 🛠️ Technical Stack

- **Framework**: Django 4.2+
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Frontend**: Django Templates with responsive design
- **Security**: Environment variables, CSRF protection, input validation
- **Validation**: Custom validators for ISBN, monetary fields, and IDs

## 📊 Database Models

### Reader Model
- Name, email (unique), automatic membership date
- Decimal-based fine tracking with validation
- Prevents negative fine amounts

### Book Model
- Title, author, publication date
- ISBN validation (ISBN-10/ISBN-13)
- Availability status tracking
- Unique ISBN constraint

### Loan Model
- Foreign key relationships to Reader and Book
- Automatic loan and due date calculation
- Return date tracking
- Comprehensive loan lifecycle management

## 🔧 Quick Setup

### Option 1: Automated Setup
```bash
cd "library admin system/lib"
./setup.sh
```

### Option 2: Manual Setup
```bash
# 1. Install dependencies
pip3 install -r requirements.txt

# 2. Environment setup
cp .env.example .env
# Edit .env with your settings

# 3. Database setup
python3 manage.py makemigrations
python3 manage.py migrate

# 4. Create admin user (optional)
python3 manage.py createsuperuser

# 5. Run development server
python3 manage.py runserver
```

## 📁 Project Structure

```
lib/
├── library/                 # Main application
│   ├── models.py           # Database models with validation
│   ├── views.py            # Business logic and helper functions
│   ├── forms.py            # Form definitions with validation
│   ├── urls.py             # URL routing
│   ├── templates/lib/      # HTML templates
│   │   ├── lend.html       # Book lending interface
│   │   ├── return.html     # Book return interface
│   │   └── fine.html       # Fine payment interface
│   └── migrations/         # Database migrations
├── lib/                    # Project configuration
│   └── settings.py         # Secure Django settings
├── requirements.txt        # Python dependencies
├── .env.example           # Environment template
├── setup.sh               # Automated setup script
├── TROUBLESHOOTING.md     # Common issues and solutions
└── README.md              # This file
```

## 🔒 Security Features

- **Environment Configuration**: Sensitive settings via environment variables
- **Production Security**: SECRET_KEY validation, DEBUG control, ALLOWED_HOSTS
- **Input Validation**: Form-level and model-level validation
- **SQL Injection Protection**: Django ORM with parameterized queries
- **CSRF Protection**: Built-in Django CSRF middleware
- **Data Sanitization**: Proper escaping and validation

## 🐛 Troubleshooting

For common issues and solutions, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

**Quick Diagnostics:**
```bash
# Check Django installation
python3 -c "import django; print(django.get_version())"

# Verify database
python3 manage.py check

# Test migrations
python3 manage.py showmigrations
```

## 🔄 Recent Updates

### Latest Bug Fixes & Improvements
- ✅ **Complete Fine System**: Full payment processing with validation
- ✅ **ISBN Validation**: Proper ISBN-10/ISBN-13 format checking
- ✅ **Security Enhancements**: Production-ready configuration
- ✅ **Error Handling**: Comprehensive exception handling
- ✅ **Form Validation**: Prevents negative values and invalid inputs
- ✅ **Template Fixes**: Resolved URL routing issues
- ✅ **Model Improvements**: Automatic date handling and constraints
- ✅ **Code Quality**: Helper functions and maintainable structure

### Performance & Reliability
- ✅ **Database Optimization**: Proper field types and constraints
- ✅ **Memory Efficiency**: Decimal fields for monetary calculations
- ✅ **Error Recovery**: Graceful error handling and user feedback
- ✅ **Data Integrity**: Validation at multiple levels

## 🎯 Learning Objectives Achieved

- **Django Fundamentals**: Models, views, templates, forms
- **Database Design**: Relationships, constraints, migrations
- **Security Practices**: Environment config, validation, sanitization
- **Error Handling**: Exception management and user feedback
- **Code Organization**: Helper functions, constants, clean structure
- **Production Readiness**: Environment-based configuration
- **Testing Preparation**: Modular code structure for easy testing

## 🚀 Future Enhancements

- [ ] User authentication and authorization
- [ ] Advanced search and filtering
- [ ] Email notifications for due dates
- [ ] Reporting and analytics dashboard
- [ ] REST API for mobile integration
- [ ] Automated testing suite

## 📄 License

This project is for educational purposes. Feel free to use and modify for learning.

---

**Built with ❤️ using Django | Ready for production deployment**
