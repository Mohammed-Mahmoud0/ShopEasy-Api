# ShopEasy-Api

A scalable, modern e-commerce backend API built with Django and Django REST Framework. Designed to power robust online shopping solutions with comprehensive product management, order processing, and customer relationship features.

## 🚀 Overview

ShopEasy-Api is a production-ready e-commerce backend that provides a complete REST API for managing:
- Product catalogs with images and promotions
- Shopping carts and order management
- Customer profiles and order history
- Collections and product categorization
- Advanced filtering, search, and pagination

## 🏗️ Architecture

The application follows a modular Django architecture with clear separation of concerns:

```
ShopEasy-Api/
├── config/                 # Project configuration & settings
│   ├── settings/          # Environment-specific settings
│   ├── urls.py            # Main URL routing
│   └── wsgi.py            # WSGI application
├── store/                 # Core e-commerce app
│   ├── models.py          # Product, Order, Cart models
│   ├── views.py           # ViewSets and API endpoints
│   ├── serializers.py     # Data serialization
│   ├── permissions.py     # Custom permission classes
│   ├── filters.py         # Advanced filtering logic
│   └── urls.py            # Store API routes
├── tags/                  # Product tagging system
├── likes/                 # User favorites/wishlist
├── core/                  # Core utilities & landing page
├── playground/            # Development & testing endpoints
└── manage.py              # Django management script
```

## 🎯 Key Features

### Product Management
- **Products**: Full CRUD operations with inventory tracking
- **Collections**: Organize products into categories
- **Product Images**: Multiple images per product with validation
- **Promotions**: Discount management and application
- **Reviews**: Customer product reviews and ratings

### Shopping & Orders
- **Shopping Carts**: Temporary cart management with UUID tracking
- **Orders**: Complete order lifecycle management
- **Order Items**: Track individual product quantities and pricing
- **Payment Status**: Monitor payment states (Pending, Complete, Failed)

### Customer Features
- **Customer Profiles**: Linked to Django User model with membership tiers
- **Membership Levels**: Bronze, Silver, and Gold tier support
- **Addresses**: Multiple address storage per customer
- **Order History**: Complete purchase history tracking

### Advanced Functionality
- **Filtering**: Product filtering by collection, price, and more
- **Search**: Full-text search across product titles and descriptions
- **Pagination**: Configurable pagination for large datasets
- **Permissions**: Role-based access control (Admin, Customer, Anonymous)
- **Authentication**: JWT-based authentication with SimpleJWT and Djoser

## 🛠️ Tech Stack

### Backend Framework
- **Django 6.0.1**: Web framework
- **Django REST Framework 3.16.1**: RESTful API building
- **Django Nested Routers**: Hierarchical URL routing

### Database & Caching
- **MySQL**: Primary database
- **Redis**: Caching layer
- **Celery 5.6.3**: Async task processing
- **Celery Beat**: Scheduled task execution

### Authentication & Security
- **SimpleJWT**: JSON Web Token authentication
- **Djoser**: User authentication endpoints
- **django-cors-headers**: CORS support
- **defusedxml**: XML security

### Development & Debugging
- **Django Debug Toolbar**: Development profiling
- **Silk**: Request/response profiling
- **pytest**: Testing framework
- **Locust**: Performance testing

### Utilities
- **Pillow**: Image processing
- **django-filter**: Advanced filtering
- **whitenoise**: Static file serving

## 📋 API Endpoints

### Store API (`/store/`)

#### Products
- `GET /store/products/` - List all products with filtering & search
- `POST /store/products/` - Create product (admin only)
- `GET /store/products/{id}/` - Product details
- `PUT/PATCH /store/products/{id}/` - Update product
- `DELETE /store/products/{id}/` - Delete product

#### Collections
- `GET /store/collections/` - List collections
- `POST /store/collections/` - Create collection (admin)
- `GET /store/collections/{id}/` - Collection details
- `PUT/PATCH /store/collections/{id}/` - Update collection
- `DELETE /store/collections/{id}/` - Delete collection

#### Product Images
- `GET /store/products/{product_id}/images/` - List product images
- `POST /store/products/{product_id}/images/` - Upload image
- `DELETE /store/products/{product_id}/images/{id}/` - Delete image

#### Reviews
- `GET /store/products/{product_id}/reviews/` - List reviews
- `POST /store/products/{product_id}/reviews/` - Add review

#### Carts
- `POST /store/carts/` - Create cart
- `GET /store/carts/{id}/` - Retrieve cart
- `DELETE /store/carts/{id}/` - Delete cart

#### Cart Items
- `GET /store/carts/{cart_id}/items/` - List cart items
- `POST /store/carts/{cart_id}/items/` - Add to cart
- `PATCH /store/carts/{cart_id}/items/{id}/` - Update quantity
- `DELETE /store/carts/{cart_id}/items/{id}/` - Remove from cart

#### Orders
- `GET /store/orders/` - List orders (user's or all for staff)
- `POST /store/orders/` - Create order
- `GET /store/orders/{id}/` - Order details
- `PATCH /store/orders/{id}/` - Update order status (admin)

#### Customers
- `GET /store/customers/` - List customers (admin)
- `GET /store/customers/me/` - Current customer profile
- `PUT /store/customers/me/` - Update profile
- `GET /store/customers/{id}/history/` - Customer order history

#### Authentication (`/auth/`)
- `POST /auth/users/` - Register
- `POST /auth/jwt/create/` - Login
- `POST /auth/jwt/refresh/` - Refresh token
- `POST /auth/jwt/verify/` - Verify token

## 🔐 Security & Permissions

### Permission Classes
- **IsAdminOrReadOnly**: Admin write access, public read access
- **ViewCustomerHistoryPermission**: Custom history viewing permissions
- **IsAuthenticated**: Requires login
- **IsAdminUser**: Admin-only endpoints

### Authentication
- JWT-based authentication for secure API access
- Social authentication support (OAuth2)
- CORS configured for frontend communication

## 📊 Database Schema

### Core Models
- **Product**: Title, slug, description, price, inventory, collection, promotions
- **Collection**: Title, featured product
- **Promotion**: Description, discount percentage
- **Cart**: UUID-based temporary carts
- **Order**: Customer, payment status, order date
- **Customer**: User profile with membership level and contact info
- **Address**: Shipping/billing addresses per customer
- **Review**: Product reviews with ratings

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- MySQL database
- Redis server (for caching & Celery)

### Installation

1. Clone the repository
```bash
git clone https://github.com/Mohammed-Mahmoud0/ShopEasy-Api.git
cd ShopEasy-Api
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
```bash
cp .env.example .env
# Edit .env with your database and Redis credentials
```

5. Run migrations
```bash
python manage.py migrate
```

6. Create superuser
```bash
python manage.py createsuperuser
```

7. Load dummy data (optional)
```bash
python manage.py loaddata DB_Script_Dummy_Data/
```

8. Run development server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

### Running Celery (Background Tasks)
```bash
celery -A config worker -l info
```

### Running Celery Beat (Scheduled Tasks)
```bash
celery -A config beat -l info
```

## 🧪 Testing

Run the test suite with pytest:
```bash
pytest
```

### Performance Testing with Locust
```bash
locust -f locustfiles/yourfile.py
```

## 📈 Performance Features

- **Caching**: Redis-based caching for frequently accessed data
- **Database Optimization**: Query optimization with select_related and prefetch_related
- **Pagination**: Efficient data pagination for large datasets
- **Async Tasks**: Celery for background processing
- **Query Profiling**: Silk integration for monitoring database queries

## 🔧 Configuration

### Environment Variables
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=mysql://user:password@localhost/shopdb
REDIS_URL=redis://localhost:6379
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

### Settings Structure
- `config/settings/common.py`: Shared configuration
- `config/settings/development.py`: Development-specific settings
- `config/settings/production.py`: Production-specific settings

## 📝 API Documentation

The API follows REST conventions with:
- **Standard HTTP Methods**: GET, POST, PUT, PATCH, DELETE
- **Status Codes**: Appropriate HTTP status codes for all operations
- **Error Handling**: Detailed error messages and validation
- **Pagination**: Default pagination with configurable page size

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests for bug fixes, features, or documentation improvements.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Support

For issues, questions, or feedback, please open an GitHub issue in the repository.

---

**Built with ❤️ for scalable e-commerce solutions**
