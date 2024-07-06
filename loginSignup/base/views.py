from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product, Order

@login_required
def home(request):
    return render(request, "registration/home.html",{})



@login_required    
def product_list(request):
    products = Product.objects.all()
    return render(request, 'registration/product_list.html', {'products': products})

@login_required
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'registration/product_detail.html', {'products': product})


@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', {})

    if str(product.id) in cart:
        cart[str(product.id)] += 1
    else:
        cart[str(product.id)] = 1

    request.session['cart'] = cart
    return redirect('cart_detail')


@login_required
def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        total_price += product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': product.price * quantity
        })

    return render(request, 'registration/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})


@login_required
def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    product_id = str(pk)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart
    return redirect('cart_detail')

@login_required
def order_placement(request):
    # Implement order placement logic, form handling, and calculation of total price
    if request.method == 'POST':
        # Process order form submission
        pass  # Replace with actual logic
    else:
        # Display order form
        pass  # Replace with actual logic
    return render(request, 'registration/order_placement.html', {})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('register')
    return render(request, 'registration/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')    
