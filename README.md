# 🛒 E-Commerce REST API

A full-featured e-commerce backend built with **Django REST Framework**.  
This project was built as a hands-on learning exercise and now includes user profiles, shopping carts, advanced filtering, object-level permissions, and interactive API documentation.

## 🚀 Project Overview

The API provides everything you need to run an online store backend:
- Product & category management
- User profiles (with public/private fields)
- Shopping cart per user, automatically created
- Fine-grained permissions (owner-only access for sensitive data)
- Powerful filtering, search, and ordering
- Swagger UI for live API exploration

## ✨ Features

- **Product Catalog** – CRUD operations for products and categories
- **Advanced Filtering** – Filter by category, price range, stock availability, and more
- **Sorting & Pagination** – Order results by any field, page-based navigation
- **User Profiles** – Extended user information (phone, address, avatar) with automatic creation
- **Shopping Cart** – One cart per user, with line items and computed totals
- **Permissions** – Custom `IsOwnerOrReadOnly`; public can only see non‑sensitive data
- **Dynamic Serializers** – Profile details change based on who is viewing (owner vs others)
- **Signals** – Profile and Cart are auto‑generated when a User is created
- **API Documentation** – Interactive Swagger UI (offline capable) via `drf-spectacular`
- **Image Upload** – Product and avatar images with full URL generation

## 🧱 Tech Stack

| Component          | Technology                          |
|--------------------|-------------------------------------|
| Framework          | Django 5.x + Django REST Framework  |
| Database           | PostgreSQL (configurable)           |
| Filtering          | `django-filter`                     |
| API Documentation  | `drf-spectacular` (Swagger/OpenAPI) |
| Authentication     | Basic Authentication (token ready)  |
| Permissions        | Custom `IsOwnerOrReadOnly`          |
| Image Handling     | Pillow                              |
| Signals            | Django signals for auto‑creation    |

## 📦 Models

### Category
- `name`, `description`, `created_at`
- Related to products via `ForeignKey`

### Product
- `name`, `description`, `price`, `stock`, `category`, `image`
- `is_active` (for soft delete), `created_at`, `updated_at`
- Computed property `in_stock` (stock > 0)

### Profile
- One-to-one extension of the built‑in `User` model
- Fields: `phone`, `address`, `city`, `postal_code`, `avatar`
- Automatic creation via signal

### Cart & CartItem
- **Cart**: one per user, linked via `OneToOneField`
- **CartItem**: product, quantity, unique together (`cart`, `product`)
- Computed properties: `total_price`, `total_items`, `line_total`
- Automatic cart creation via signal

## 🔌 API Endpoints

### Categories
| Method   | Endpoint                 | Description            |
|----------|--------------------------|------------------------|
| `GET`    | `/cats/`                 | List categories        |
| `POST`   | `/cats/`                 | Create category        |
| `GET`    | `/cats/{id}/`            | Retrieve category      |
| `PUT`    | `/cats/{id}/`            | Update category        |
| `PATCH`  | `/cats/{id}/`            | Partial update         |
| `DELETE` | `/cats/{id}/`            | Delete category        |

### Products
| Method   | Endpoint                 | Description            |
|----------|--------------------------|------------------------|
| `GET`    | `/prods/`                | List products (paginated) |
| `POST`   | `/prods/`                | Create product         |
| `GET`    | `/prods/{id}/`           | Retrieve product       |
| `PUT`    | `/prods/{id}/`           | Update product         |
| `PATCH`  | `/prods/{id}/`           | Partial update         |
| `DELETE` | `/prods/{id}/`           | Delete product         |

### Users / Profiles
| Method   | Endpoint                  | Description                |
|----------|---------------------------|----------------------------|
| `GET`    | `/user/{username}/`   | View profile (public/owner)|
| `PUT`    | `/user/{username}/`   | Update own profile only    |
| `PATCH`  | `/user/{username}/`   | Partial update own profile |

- **Public view**: `username` and `avatar` only
- **Owner view**: full details including phone, address, etc.
- Permission: `IsOwnerOrReadOnly`

### Cart
| Method   | Endpoint                  | Description                |
|----------|---------------------------|----------------------------|
| `GET`    | `user/cart/{username}/`       | View cart (owner only)     |
| `PUT`    | `user/cart/{username}/`       | Update cart (owner only)   |

- Access restricted to the cart owner
- Nested items shown with product details and line totals
- Endpoints for adding/removing items coming soon

### API Documentation
| Method   | Endpoint                 | Description                |
|----------|--------------------------|----------------------------|
| `GET`    | `/api/schema/`           | OpenAPI 3.0 schema (JSON)  |
| `GET`    | `/api/docs/`             | Swagger UI                 |

## 🔍 Product Filtering & Sorting

All product endpoints accept query parameters for advanced filtering.

| Parameter    | Type    | Description                | Example              |
|--------------|---------|----------------------------|----------------------|
| `category`   | integer | Filter by category ID      | `?category=2`        |
| `min_price`  | decimal | Minimum price              | `?min_price=100`     |
| `max_price`  | decimal | Maximum price              | `?max_price=500`     |
| `in_stock`   | boolean | Stock > 0 (`true`/`false`) | `?in_stock=true`     |
| `ordering`   | string  | Sort field (prefix `-` for desc) | `?ordering=-price` |
| `page`       | integer | Page number                | `?page=2`            |

**Ordering fields:** `price`, `name`, `created_at`

**Example:**
```bash
GET /prods/?category=2&min_price=100&max_price=500&in_stock=true&ordering=-price
