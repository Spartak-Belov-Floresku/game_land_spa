"""
Tests for models.
"""
from unittest.mock import patch
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from base import models



def create_user(username='testUsename', password='testpass123'):
    """Create a return a new user."""
    return get_user_model().objects.create_user(username=username, password=password)

def create_product(name = 'Sample product name', price = 5.5, description = 'Sample product description.'):
    user = create_user()
    return models.Product.objects.create(
            user=user,
            name=name,
            price=price,
            description=description,
        )



class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_username_successful(self):
        """Test creating a user with an email is successful."""
        username = 'testUsername'
        password = 'testpass123'
        user = create_user(username, password,)
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


    def test_create_product(self):
        """Test creating a product is successful."""
        user = create_user()
        product = {
            'user':user,
            'name':'Sample product name',
            'price':Decimal('5.50'),
            'description':'Sample product description.',
        }
        models.Product.objects.create(
            user=product['user'],
            name=product['name'],
            price=product['price'],
            description=product['description'],
        )
        get_product = models.Product.objects.get(user=user)
        self.assertEqual(str(product['user']), str(get_product.user))
        self.assertEqual(product['name'], str(get_product.name))

    def test_create_reveiw(self):
        """Test creating a product review."""
        product = create_product()
        models.Review.objects.create(
            product=product,
            user=product.user,
            name = 'Test name reveiw',
            rating = 5
        )
        get_review = models.Review.objects.get(product=product)
        self.assertEqual(str(product), str(get_review.product))
        self.assertEqual(str(product.user), str(get_review.user))

    def test_create_order(self):
        """Test creating an order."""
        user = create_user()
        models.Order.objects.create(
            user=user,
            paymentMethod='PayPal',
        )
        get_order = models.Order.objects.get(user=user)
        self.assertFalse(get_order.isPaid)
        self.assertFalse(get_order.isDelivered)

    def test_create_order_items(self):
        """Test creating order items."""
        product = create_product()
        order = models.Order.objects.create(
            user=product.user,
            paymentMethod='PayPal',
        )
        models.OrderItem.objects.create(
            product=product,
            order=order,
        )
        get_orderItems = models.OrderItem.objects.get(product=product)
        self.assertEqual(str(product.user), str(get_orderItems.product.user))
        self.assertEqual(str(product.user), str(get_orderItems.order.user))

    
    def test_create_shipping_address(self):
        """Test creating order items."""
        user = create_user()
        order = models.Order.objects.create(
            user=user,
            paymentMethod='PayPal',
        )
        models.ShippingAddress.objects.create(
            order=order,
        )
        get_shippingAddress = models.ShippingAddress.objects.get(order=order)
        self.assertEqual(str(user), str(get_shippingAddress.order.user))