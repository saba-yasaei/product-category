# # Django Product Search and Filter

A Django application for managing and browsing toy building products. Products belong to categories and can have multiple tags. Users can search product descriptions and filter products by category and tags.

## Features

* Manage products, categories, and tags through Django Admin
* Search products by description
* Filter products by category
* Filter products by one or more tags
* Combine search, category, and tag filters
* Display product names, descriptions, categories, and tags

## Technologies Used

* Python 3
* Django
* SQLite
* HTML
* Django Templates
* Pipenv

## Data Models

### Category

Represents the shape of a product, such as Sphere, Cylinder, or Cube.

Each category can contain multiple products.

### Tag

Represents a product color, such as Red, Blue, or Green.

A tag can belong to multiple products, and a product can have multiple tags.

### Product

Each product contains:

* Name
* Description
* One category
* Zero or more tags

## Project Setup

### 1. Install the dependencies

```bash
pipenv install
```

### 2. Activate the virtual environment

```bash
pipenv shell
```

### 3. Apply database migrations

```bash
python manage.py migrate
```

### 4. Create an administrator account (Optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to create a username and password.

**Note:** The repository includes a pre-populated SQLite database containing the required sample data (5 categories, 10 tags, and 20 products). Creating a new superuser is only necessary if you want to access the Django Admin with your own credentials.

### 5. Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

The Django Admin interface is available at:

```text
http://127.0.0.1:8000/admin/
```

## Search and Filtering

The product page supports the following query parameters:

* `search` searches product descriptions.
* `category` filters products by category ID.
* `tags` filters products by one or more tag IDs.

The filters can be used individually or combined.

When multiple tags are selected, the application returns products containing any of the selected tags.

## Sample Data

The database contains sample data created through the Django Admin interface:

* 5 categories
* 10 tags
* 20 products

## Assumptions

* Each product belongs to exactly one category.
* A product may have multiple tags.
* Tags are optional.
* Tag filtering uses “match any selected tag” behavior.
* Styling is intentionally minimal and the focus is on Django models, querysets, views, and functionality.

## AI Usage

Codex was used to generate tests in products/tests.py and the tests were reviewed and verified by me. 
Codex auto code generation was used for HTML template. 
