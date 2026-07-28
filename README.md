# FastAPI E-Commerce Project Structure

This document explains the purpose of every folder and file in the project.

---

# Project Structure

```
ecommerce/
│
├── app/
├── uploads/
├── scripts/
├── .env
├── .env.example
├── alembic.ini
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# app/

Contains the complete application source code.

---

# app/main.py

Application entry point.

Responsibilities:

- Create FastAPI instance
- Register routers
- Add middleware
- Configure startup/shutdown events
- Start the application

---

# app/core/

Contains global configurations and application-wide functionality.

## config.py

Application settings.

Examples:

- Database URL
- JWT Secret
- Environment Variables
- API Version
- SMTP Settings
- Redis URL

Usually implemented using Pydantic Settings.

---

## security.py

Authentication and security utilities.

Examples:

- Password Hashing
- JWT Token Creation
- JWT Verification
- OAuth2
- Refresh Tokens

---

## dependencies.py

Common FastAPI dependencies.

Examples:

- Current User
- Current Seller
- Current Buyer
- Database Session
- Authentication Dependency

---

## constants.py

Application constants.

Examples:

- User Roles
- Status Codes
- Product Status
- Order Status
- Payment Status

---

## exceptions.py

Custom exception classes.

Examples:

- UserNotFound
- ProductNotFound
- UnauthorizedAccess
- InvalidToken

---

## logging.py

Application logging configuration.

Examples:

- File Logger
- Console Logger
- Error Logger

---

## middleware.py

Application middleware.

Examples:

- Request Logging
- Execution Time
- CORS
- Rate Limiting
- Request ID

---

# app/database/

Database configuration.

---

## session.py

Creates SQLAlchemy database session.

Responsibilities:

- Engine Creation
- Session Factory
- Dependency for Database Session

---

## base.py

Contains SQLAlchemy Base class.

All models inherit from this Base.

---

## migrations/

Alembic migration files.

Responsibilities:

- Create Tables
- Update Tables
- Rollback Database

---

## seed.py

Initial database data.

Examples:

- Default Admin
- Roles
- Categories

---

# app/modules/

Contains all business modules.

Each module follows the same architecture.

```
module/
│
├── router.py
├── service.py
├── repository.py
├── models.py
├── schemas.py
└── extra files...
```

---

# router.py

API endpoints only.

Responsibilities:

- Receive Request
- Validate Input
- Call Service
- Return Response

Should never contain business logic.

---

# service.py

Business logic layer.

Responsibilities:

- Validate Business Rules
- Call Repository
- Handle Transactions
- Process Data

This is the heart of the application.

---

# repository.py

Database layer.

Responsibilities:

- CRUD Operations
- SQLAlchemy Queries
- Database Transactions

Should never contain business rules.

---

# models.py

Database models.

Responsibilities:

- SQLAlchemy ORM Classes
- Table Definitions
- Relationships

---

# schemas.py

Pydantic models.

Responsibilities:

- Request Validation
- Response Serialization
- API Documentation

Examples:

- ProductCreate
- ProductUpdate
- ProductResponse

---

# auth/

Authentication module.

Responsibilities:

- Login
- Register
- Logout
- JWT Authentication
- Refresh Token
- Password Reset

Extra Files

### dependencies.py

Authentication dependencies.

Examples:

- get_current_user()
- get_current_seller()
- get_current_admin()

### utils.py

Authentication helper functions.

Examples:

- OTP
- Token Utilities
- Password Helpers

---

# users/

User management.

Responsibilities:

- User CRUD
- Profile
- User Information

---

# seller/

Seller functionality.

Responsibilities:

- Seller Dashboard
- Seller Profile
- Product Management
- Inventory
- Seller Orders

Extra File

## permissions.py

Seller authorization.

Examples:

- Is Seller
- Own Product Check
- Product Ownership

---

# buyer/

Buyer functionality.

Responsibilities:

- Browse Products
- Place Orders
- Wishlist
- Cart
- Profile

---

# products/

Product management.

Responsibilities:

- CRUD Products
- Product Search
- Inventory
- Images
- Product Details

Extra Files

## filters.py

Product filtering.

Examples:

- Category Filter
- Price Filter
- Rating Filter
- Search

## utils.py

Product helper functions.

Examples:

- SKU Generator
- Slug Generator
- Image Processing

---

# categories/

Category management.

Responsibilities:

- Create Categories
- Update Categories
- Delete Categories
- Category Tree

---

# cart/

Shopping cart.

Responsibilities:

- Add Product
- Remove Product
- Update Quantity
- View Cart

---

# orders/

Order management.

Responsibilities:

- Place Order
- Cancel Order
- Track Order
- Order History

---

# payments/

Payment processing.

Responsibilities:

- Payment Gateway
- Payment Verification
- Refund
- Transaction History

---

# reviews/

Product reviews.

Responsibilities:

- Add Review
- Update Review
- Delete Review
- Product Ratings

---

# wishlist/

Wishlist management.

Responsibilities:

- Add Wishlist
- Remove Wishlist
- View Wishlist

---

# notifications/

Notification services.

## service.py

Business logic for notifications.

Examples:

- Send Email
- Send SMS
- Push Notifications

## email.py

Email templates and email sending.

---

# app/shared/

Reusable components.

---

## enums.py

Application enums.

Examples:

- UserRole
- PaymentMethod
- OrderStatus

---

## responses.py

Standard API responses.

Examples:

- Success Response
- Error Response
- Pagination Response

---

## pagination.py

Pagination utilities.

Examples:

- Offset Pagination
- Cursor Pagination

---

## validators.py

Reusable validators.

Examples:

- Password Validator
- Email Validator
- Phone Validator

---

## utils.py

General helper functions.

Examples:

- Date Utilities
- String Utilities
- File Utilities

---

# app/tests/

Application tests.

Recommended structure:

```
tests/
│
├── auth/
├── seller/
├── buyer/
├── products/
└── orders/
```

Each folder contains:

- Unit Tests
- Integration Tests
- API Tests

---

# uploads/

Stores uploaded files.

Examples:

- Product Images
- Profile Pictures
- Documents

---

# scripts/

Automation scripts.

Examples:

- Database Seeder
- Backup
- Data Import
- Data Export

---

# .env

Environment variables.

Never commit this file.

Examples:

- Database URL
- JWT Secret
- SMTP Password
- API Keys

---

# .env.example

Template for .env.

Contains placeholders instead of real secrets.

---

# alembic.ini

Alembic configuration.

---

# requirements.txt

Python package dependencies.

---

# Dockerfile

Instructions for building Docker image.

---

# docker-compose.yml

Runs multiple services.

Examples:

- FastAPI
- PostgreSQL
- Redis
- Nginx

---

# README.md

Project documentation.

Should include:

- Project Overview
- Installation
- Environment Setup
- Running the Project
- API Documentation
- Folder Structure
- Deployment

---

# Request Flow

```
Client
    │
    ▼
Router
    │
    ▼
Service
    │
    ▼
Repository
    │
    ▼
Database
```

### Router

Receives HTTP requests.

↓

### Service

Processes business logic.

↓

### Repository

Interacts with the database.

↓

### Database

Stores and retrieves data.

---

# Architecture Principles

- Keep routers thin.
- Put all business logic in services.
- Keep database queries in repositories.
- Validate requests with Pydantic schemas.
- Use dependency injection.
- Keep reusable code in shared.
- Store configuration in core.
- Write tests for every module.
- Never expose database models directly to clients.
- Follow separation of concerns for maintainability.




ecommerce/
│
├── app/
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   ├── dependencies.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── logging.py
│   │   └── middleware.py
│   │
│   ├── database/
│   │   ├── session.py
│   │   ├── base.py
│   │   ├── migrations/
│   │   └── seed.py
│   │
│   ├── modules/
│   │
│   │   ├── auth/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── repository.py
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   ├── dependencies.py
│   │   │   └── utils.py
│   │   │
│   │   ├── users/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── repository.py
│   │   │   ├── models.py
│   │   │   └── schemas.py
│   │   │
│   │   ├── seller/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── repository.py
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   └── permissions.py
│   │   │
│   │   ├── buyer/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── repository.py
│   │   │   ├── models.py
│   │   │   └── schemas.py
│   │   │
│   │   ├── products/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── repository.py
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   ├── filters.py
│   │   │   └── utils.py
│   │   │
│   │   ├── categories/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── repository.py
│   │   │   ├── models.py
│   │   │   └── schemas.py
│   │   │
│   │   ├── cart/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── repository.py
│   │   │   ├── models.py
│   │   │   └── schemas.py
│   │   │
│   │   ├── orders/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── repository.py
│   │   │   ├── models.py
│   │   │   └── schemas.py
│   │   │
│   │   ├── payments/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── repository.py
│   │   │   ├── models.py
│   │   │   └── schemas.py
│   │   │
│   │   ├── reviews/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── repository.py
│   │   │   ├── models.py
│   │   │   └── schemas.py
│   │   │
│   │   ├── wishlist/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── repository.py
│   │   │   ├── models.py
│   │   │   └── schemas.py
│   │   │
│   │   └── notifications/
│   │       ├── service.py
│   │       └── email.py
│   │
│   ├── shared/
│   │   ├── enums.py
│   │   ├── responses.py
│   │   ├── pagination.py
│   │   ├── validators.py
│   │   └── utils.py
│   │
│   ├── tests/
│   │   ├── auth/
│   │   ├── seller/
│   │   ├── buyer/
│   │   ├── products/
│   │   └── orders/
│   │
│   └── main.py
│
├── uploads/
│
├── scripts/
│
├── .env 
├── requirements.txt
└── README.md