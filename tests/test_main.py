import pytest
from main import Product, Category


def test_product_creation():
    product = Product("Test Product", "Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_creation():
    product1 = Product("Test Product 1", "Description 1", 50.0, 5)
    product2 = Product("Test Product 2", "Description 2", 75.0, 8)
    category = Category("Test Category", "Test Description", [product1, product2])

    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert len(category.products) == 2


def test_category_counts():
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Product 1", "Description 1", 10.0, 2)
    product2 = Product("Product 2", "Description 2", 15.0, 3)
    category1 = Category("Category 1", "Description", [product1, product2])

    product3 = Product("Product 3", "Description 3", 20.0, 4)
    category2 = Category("Category 2", "Description", [product3])

    assert Category.category_count == 2
    assert Category.product_count == 3  # 2 в первой категории + 1 во второй
