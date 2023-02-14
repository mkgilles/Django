import pdb

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Customer, Product, Sale, Cashier, Order, Admin
from django.shortcuts import render, redirect
from .models import Product, Sale, Cart
from .forms import CartForm


# logger = logging.getLogger(__name__)

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales.html', {'sales': sales})


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
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']


from .models import Customer, Product, Sale, Cashier, Order


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
    return render(request, 'view_cart.html', {'cart': cart, 'total': total})


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


def index(request):
    return render(request, "store/index.html")


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
    return render(request, 'view_cart.html', context)


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
        return redirect('cart')

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
    return redirect('view_cart')


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
    logger.info("Rendering home.html template with context data")
    return render(request, 'cashier/home.html', context)


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
                return redirect('cashier_home')
            else:
                error_message = 'Incorrect username or password. Please try again.'
                return render(request, 'cashier_login.html', {'form': form, 'error': error_message})
    else:
        form = CashierLoginForm()
    return render(request, 'cashier_login.html', {'form': form})
