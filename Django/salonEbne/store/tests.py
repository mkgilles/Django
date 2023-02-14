from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.utils import timezone
from decimal import Decimal
from .models import Customer, Product, Sale, Cashier, Order, Admin, Cart


class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Customer.objects.create(first_name='John', last_name='Doe', boarding_pass='ABC123', email='johndoe@example.com')

    def test_first_name_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_last_name_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_boarding_pass_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('boarding_pass').verbose_name
        self.assertEqual(field_label, 'boarding pass')

    def test_email_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_first_name_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 50)

    def test_last_name_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 50)

    def test_boarding_pass_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('boarding_pass').max_length
        self.assertEqual(max_length, 50)

    def test_email_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('email').max_length
        self.assertEqual(max_length, 254)

    def test_created_at_auto_now_add(self):
        customer = Customer.objects.get(id=1)
        created_at = customer.created_at
        self.assertLessEqual(timezone.now() - created_at, timezone.timedelta(seconds=1))

    def test_updated_at_auto_now(self):
        customer = Customer.objects.get(id=1)
        updated_at = customer.updated_at
        self.assertLessEqual(timezone.now() - updated_at, timezone.timedelta(seconds=1))


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(name='Product 1', description='This is product 1', price=Decimal('10.00'), stock=100)

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_stock_label(self):
        product = Product.objects.get(id=1)
        field_label = product
