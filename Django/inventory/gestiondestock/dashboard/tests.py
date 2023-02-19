from django.test import TestCase
from django.contrib.auth.models import User
from .models import Customer, Product, Sale, Cashier, Order, Admin, Cart, OrderItem


class TestModels(TestCase):
    def setUp(self):
        # Create some test users
        self.user1 = User.objects.create_user(username='user1', password='salonEb1n')
        self.user2 = User.objects.create_user(username='user2', password='salonEb1n')

        # Create some test customers
        self.customer1 = Customer.objects.create(
            user=self.user1,
            first_name='John',
            last_name='Doe',
            boarding_pass='ABC123',
            email='john.doe@example.com'
        )
        self.customer2 = Customer.objects.create(
            user=self.user2,
            first_name='Jane',
            last_name='Doe',
            boarding_pass='XYZ789',
            email='jane.doe@example.com'
        )

        # Create some test products
        self.product1 = Product.objects.create(
            name='Product 1',
            category='Ustensile',
            description='Description of product 1',
            price=9.99,
            stock=10,
            volume=1
        )
        self.product2 = Product.objects.create(
            name='Product 2',
            category='Boisson',
            description='Description of product 2',
            price=4.99,
            stock=20,
            volume=0
        )

        # Create some test sales
        self.sale1 = Sale.objects.create(
            customer=self.customer1,
            product=self.product1,
            quantity=2,
            total_price=19.98
        )
        self.sale2 = Sale.objects.create(
            customer=self.customer2,
            product=self.product2,
            quantity=3,
            total_price=14.97
        )

        # Create some test cashiers
        self.cashier1 = Cashier.objects.create(
            user=self.user1,
            first_name='John',
            last_name='Smith'
        )
        self.cashier2 = Cashier.objects.create(
            user=self.user2,
            first_name='Jane',
            last_name='Doe'
        )

        # Create some test orders
        self.order1 = Order.objects.create(
            customer_name='John Doe',
            customer_email='john.doe@example.com',
            order_total=29.97,
            order_status='Pending'
        )
        self.order2 = Order.objects.create(
            customer_name='Jane Doe',
            customer_email='jane.doe@example.com',
            order_total=9.99,
            order_status='Completed'
        )

        # Create some test admins
        self.admin1 = Admin.objects.create(
            first_name='Admin',
            last_name='User',
            username='adminuser',
            password='salonEb1n'
        )
        self.admin2 = Admin.objects.create(
            first_name='Super',
            last_name='User',
            username='superuser',
            password='salonEb1n'
        )

        # Create some test carts
        self.cart1 = Cart.objects.create(
            product=self.product1,
            quantity=2,
            price=19.98
        )
        self.cart2 = Cart.objects.create(
            product=self.product2,
            quantity=3,
            price=14.97
        )

        # Create some test order items
        self.order_item1 = OrderItem.objects.create(
            product=self.product1,
            user=self.user1,
            quantity=2
        )

# in yourapp/tests/test_models.py
def test_customer_count(setup_test_data):
    assert Customer.objects.count() == 2

def test_product_count(setup_test_data):
    assert Product.objects.count() == 2

def test_sale_count(setup_test_data):
    assert Sale.objects.count() == 2

# in yourapp/tests/test_data.py


import pytest


@pytest.fixture
def test_data():
    # Create some customers
    customer1 = Customer.objects.create(first_name='John', last_name='Doe', boarding_pass='AB123', email='johndoe@example.com')
    customer2 = Customer.objects.create(first_name='Jane', last_name='Doe', boarding_pass='CD456', email='janedoe@example.com')

    # Create some products
    product1 = Product.objects.create(name='Product 1', description='This is product 1', price=10.00, stock=100)
    product2 = Product.objects.create(name='Product 2', description='This is product 2', price=20.00, stock=50)

    # Create some sales
    Sale.objects.create(customer=customer1, product=product1, quantity=1, total_price=10.00)
    Sale.objects.create(customer=customer2, product=product2, quantity=2, total_price=40.00)

    yield
    # Clean up the database after the tests
    Customer.objects.all().delete()
    Product.objects.all().delete()
    Sale.objects.all().delete()
