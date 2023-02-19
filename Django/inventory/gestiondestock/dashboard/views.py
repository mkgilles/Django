from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Customer, Product, Sale, Cashier, Order


# Create your views here.

@login_required
def dashboard_home(request):
    return render(request, 'dashboard/home.html')


def staff(request):
    return render(request, 'dashboard/staff.html')


import pdb
from django.contrib.auth.models import User
from .models import Admin, Customer
from .models import Product, Sale, Cart
from .forms import CartForm, CashierForm


# logger = logging.getLogger(__name__)

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})


"""def product_list(request):
    products = Product.objects.all()
    return render(request, 'dashboard/products.html', {'products': products})
"""

"""
Mise en commentaire pour ces besoins futurs
"""

"""
Definition d'une nouvelle view pour recuperer les donnes produits en JSON
"""


def product_list(request):
    # Query the database to get all products
    products = Product.objects.all()

    # Serialize the data into a list of dictionaries
    data = []
    for product in products:
        product_data = {
            'reference': product.reference,
            'name': product.name,
            'category': product.category,
            'description': product.description,
            'price': float(product.price),
            'stock': product.stock,
            'volume': product.volume,
            'created_at': product.created_at,
            'updated_at': product.updated_at,
        }
        data.append(product_data)

    # Return the data in a JSON format
    # return JsonResponse(data, safe=False)
    return render(request, 'dashboard_product_list' {'product': data})


def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales.html', {'sales': sales})


# User registration


def cashier_list(request):
    cashiers = Cashier.objects.all()
    return render(request, 'cashiers.html', {'cashiers': cashiers})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})


def admin_list(request):
    admins = Admin.objects.all()
    return render(request, 'admins.html', {'admins': admins})


def create_customer(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        boarding_pass = request.POST['boarding_pass']
        email = request.POST['email']

        customer = Customer(first_name=first_name, last_name=last_name,
                            boarding_pass=boarding_pass, email=email)
        customer.save()
        return redirect('customer_list')
    return render(request, 'create_customer.html')


def create_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        stock = request.POST['stock']

        product = Product(name=name, description=description,
                          price=price, stock=stock)
        product.save()
        return redirect('product_list')
    return render(request, 'create_product.html')


def create_sale(request):
    if request.method == 'POST':
        customer = request.POST['customer']
        product = request.POST['product']
        quantity = request.POST['quantity']
        total_price = request.POST['total_price']

        sale = Sale(customer=customer, product=product, quantity=quantity,
                    total_price=total_price)
        sale.save()
        return redirect('sale_list')
    customers = Customer.objects.all()
    products = Product.objects.all()
    return render(request, 'create_sale.html', {'customers': customers, 'products': products})


def create_cashier(request):
    if request.method == 'POST':
        form = CashierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cashier_list')
    else:
        form = CashierForm()
    return render(request, 'cashier/create_cashier.html', {'form': form})





def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    if 'cart' not in request.session:
        request.session['cart'] = []
    cart = request.session['cart']
    cart.append({'product_id': product_id, 'name': product.name, 'price': product.price})
    request.session['cart'] = cart
    return redirect('view_cart')


def view_cart(request):
    cart = request.session.get('cart', [])
    total = sum(item['price'] for item in cart)
    return render(request, 'cashier/cart.html', {'cart': cart, 'total': total})


def checkout(request):
    if request.method == 'POST':
        customer = Customer.objects.get(id=request.POST['customer_id'])
        cart = request.session.get('cart', [])
        for item in cart:
            product = Product.objects.get(id=item['product_id'])
            sale = Sale(customer=customer, product=product, quantity=1, total_price=product.price)
            sale.save()
            product.stock -= 1
            product.save()
        request.session['cart'] = []
        return redirect('sale_list')
    customers = Customer.objects.all()
    return render(request, 'checkout.html', {'customers': customers})


def view_cart(request):
    cart = Cart.objects.first()
    form = CartForm(instance=cart)
    if request.method == 'POST':
        form = CartForm(request.POST, instance=cart)
        if form.is_valid():
            form.save()
            return redirect('checkout')
    context = {
        'form': form,
        'cart': cart,
    }
    return render(request, 'cashier/cart.html', context)


def success(request):
    return render(request, 'success.html')


from .models import Customer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


@login_required(login_url='/login/')
def checkout(request):
    if request.method == 'POST':
        # Get product and quantity from form
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        # Get the product from the database
        product = Product.objects.get(id=product_id)

        # Calculate the total price
        total_price = product.price * int(quantity)

        # If customer is not logged in, create a new customer account
        if not request.user.is_authenticated:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')

            # Hash the password
            password_hash = make_password(password)

            # Create a new customer account
            customer = Customer(first_name=first_name, last_name=last_name, email=email)
            customer.save()

            # Create a new user account
            user = User(username=email, password=password_hash)
            user.save()

            # Associate the user with the customer account
            customer.user = user
            customer.save()

            # Log in the new user
            login(request, user)

        # Add the product to the cart
        cart_item = Cart(product=product, quantity=quantity, price=total_price)
        cart_item.save()

        # Create a sale transaction
        sale = Sale(customer=request.user.customer, product=product, quantity=quantity, total_price=total_price)
        sale.save()

        # Redirect to the cart page
        return redirect('view_cart')

    # If the request method is GET, render the checkout page
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'checkout.html', context)


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.first()
    cart_item = cart.cart_items.filter(product=product).first()
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item = cart.cart_items.create(product=product, quantity=1)
    return redirect('cart')


def remove_from_cart(request, cart_item_id):
    cart_item = Cart.objects.first().cart_items.get(id=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')


import logging
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)


# Cashier home
@login_required
def cashier_home(request):
    logger.info("Executing cashier_home view function")
    # Retrieve sales, customers, cart, and orders data
    sales = Sale.objects.all()
    customers = Customer.objects.all()
    cart = Cart.objects.filter(cashier=request.user)
    orders = Order.objects.filter(cashier=request.user)

    context = {
        'sales': sales,
        'customers': customers,
        'cart': cart,
        'orders': orders,
    }
    logger.info("Rendering index.html template with context data")
    return render(request, 'cashier/index.html', context)


# Cashier login

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CashierLoginForm


def cashier_login(request):
    if request.method == 'POST':
        form = CashierLoginForm(request, request.POST)
        if form.is_valid():
            logger.info('Cashier login form is valid.')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            logger.info('User object: {}'.format(user))
            if user is not None:
                login(request, user)
                pdb.set_trace()
                return redirect('cashier_home', permanent=True)
            else:
                error_message = 'Incorrect username or password. Please try again.'
                return render(request, 'cashier_login.html', {'form': form, 'error': error_message})
    else:
        form = CashierLoginForm()
    return render(request, 'cashier_login.html', {'form': form})


# User account profile

@login_required
def profile(request):
    # Logic to retrieve the user's profile data and render the profile template
    return render(request, 'dashboard/profile.html')


# Cashiers dashboard

@login_required
def cashier_dashboard(request):
    # Logic to retrieve data for the cashier dashboard and render the template
    return render(request, 'cashier/cashier_dashboard.html')


# Update views to enhance functonalies
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Sale, Customer, OrderItem


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'partial/index.html', context)


@login_required
def cart(request):
    customer = Customer.objects.get(user=request.user)
    cart_items = customer.cart_set.all()
    context = {'cart_items': cart_items}
    return render(request, 'cashier/cart.html', context)


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    customer = Customer.objects.get(user=request.user)
    cart_item, created = customer.cart_set.get_or_create(product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required
def checkout(request):
    customer = Customer.objects.get(user=request.user)
    cart_items = customer.cart_set.all()
    total = sum([item.price for item in cart_items])
    context = {'cart_items': cart_items, 'total': total}
    return render(request, 'checkout.html', context)


@login_required
def place_order(request):
    if request.method == 'POST':
        customer = Customer.objects.get(user=request.user)
        cart_items = customer.cart_set.all()
        order_total = sum([item.price for item in cart_items])
        order = Order.objects.create(
            customer_name=customer.first_name + ' ' + customer.last_name,
            customer_email=customer.email,
            order_total=order_total,
            order_status='Pending'
        )

        for item in cart_items:
            Sale.objects.create(
                customer=customer,
                product=item.product,
                quantity=item.quantity,
                total_price=item.price
            )
            item.delete()

        return redirect('order_confirmation')


@login_required
def order_confirmation(request):
    return render(request, 'order_confirmation.html')


@login_required
def order_history(request):
    customer = Customer.objects.get(user=request.user)
    sales = Sale.objects.filter(customer=customer)
    context = {'sales': sales}
    return render(request, 'order_history.html', context)


@login_required
def order_item(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    context = {'order_item': order_item}
    return render(request, 'order_item.html', context)


@login_required
def add_to_order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order_item, created = OrderItem.objects.get_or_create(
        product=product,
        user=request.user,
        quantity=1
    )

    if not created:
        order_item.quantity += 1
        order_item.save()

    return redirect('cart')


from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.db.models import Sum
from .models import Product


# returns the sales data for products in a JSON format

@require_GET
def product_sales_data(request):
    products = []
    sales = []

    # Query the database to get the sales data
    sales_data = Product.objects.values('name').annotate(total_sales=Sum('order_items__quantity'))

    # Add the product names and sales to the respective lists
    for item in sales_data:
        products.append(item['name'])
        sales.append(item['total_sales'])

    # Return the data in a JSON format
    data = {
        'products': products,
        'sales': sales,
    }
    return JsonResponse(data)


"""
A query is executed using the Django ORM to get the sales data for each product.
 This query uses the values() method to group the results by the name field of the Product model and
  the annotate() method to calculate the total sales for each product based on the related OrderItem model.
"""
