from collections import UserDict
from django.shortcuts import get_object_or_404, render,redirect
from .models import Product,Category,CartItem,Order
from .forms import ProductForm,CustomUserForm

from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction

from django.db.models import Q


# Create your views here.
# def home(request):
#     product = Product.objects.all()
#     return render(request,'index.html',{"product":product})

# def home(request):
#     products = Product.objects.filter(quantity__gt=0)
#     return render(request, 'index.html', {'products': products})

# def home(request):
#     products = Product.objects.all()
#     return render(request, 'index.html', {'product': products})

# def home(request):
#     products = Product.objects.all()
#     return render(request, 'index.html', {'products': products})


def umma_view(request):
    return render(request, 'about.html')


# def home(request):
#     products = Product.objects.all()
#     categories = Category.objects.all()
#     return render(request, 'index.html', {'products': products, 'categories': categories})


# def search(request):
#     query = request.GET.get('q')

#     if query:
#         results = Product.objects.filter(name__icontains=query)
#     else:
#         results = []

#     return render(request, 'search_results.html', {'results': results, 'query': query})




# def home(request):
#     # Get the search query from the URL parameters
#     query = request.GET.get('q')

#     # Filter products based on the search query
#     if query:
#         products = Product.objects.filter(
#             Q(name__icontains=query) |               # Search by product name (case-insensitive)
#             Q(description__icontains=query) |        # Search by description (case-insensitive)
#             Q(isbn__icontains=query) |               # Search by ISBN (case-insensitive)
#             Q(binding__icontains=query) |            # Search by binding (case-insensitive)
#             Q(language__icontains=query) |           # Search by language (case-insensitive)
#             Q(category__name__icontains=query)       # Search by category name (case-insensitive)
#         )
#     else:
#         # If no search query is provided, retrieve all products
#         products = Product.objects.all()

#     categories = Category.objects.all()
#     context = {'products': products, 'categories': categories, 'query': query}
#     return render(request, 'index.html', context)




def home(request):
    # Get the search query from the URL parameters
    query = request.GET.get('q')

    # Filter products based on the search query
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            # Q(description__icontains=query) |
            Q(isbn__icontains=query) |
            Q(binding__icontains=query) |
            Q(language__icontains=query) |
            Q(category__name__icontains=query)
        )
    else:
        # If no search query is provided, retrieve all products
        products = Product.objects.all()

    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'query': query,
        'no_results': not bool(products) if query else False  # Check if there are no results
    }
    
    return render(request, 'index.html', context)






def hom(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'admin.html', {'products': products, 'categories': categories})


def my_view(request):
    return render(request, 'ind.html')


def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    # Add logic to get products related to this category if needed
    return render(request, 'category_detail.html', {'category': category})




def view(request):
    products = Product.objects.all()
    return render(request,'view.html',{"products":products})



def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = ProductForm()
    return render(request, 'addproduct.html', {'form': form})

def product_update(request, product_id):
    product = Product.objects.get(id = product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the admin page or any other appropriate URL
    else:
        form = ProductForm(instance=product)

    return render(request, 'product_update.html', {'form': form, 'product': product})


# def product_delete(request, product_id):
#     product = Product.objects.get(id = product_id)

#     product.delete()
#     return redirect('home') 

def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Set the quantity to zero instead of deleting the product
    product.quantity = 0
    product.save()

    return redirect('home')


def register(request):
    form = CustomUserForm
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration success. Login now!!!")
            return redirect('/login')
    return render(request,"register.html",{"form":form})


# def loginpage(request):
#     if request.method == 'POST':
#         name = request.POST.get('username')
#         pwd = request.POST.get('password')
#         user = authenticate(request, username=name, password=pwd)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Logged in successfully")
#             return redirect("/")
#         else:
#             messages.error(request, "Invalid Username or password")
#             return redirect('login')
#     return render(request, "login.html")




def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user is an admin
        admin_user = authenticate(request, username=username, password=password)

        if admin_user and admin_user.is_superuser:
            auth_login(request, admin_user)
            return redirect('view')  # Replace 'adminbookview' with the actual URL for the admin view

        # Check if the user is a regular user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("/")
        else:
            messages.error(request, "Invalid Username or password")
            return redirect('login')

    return render(request, "login.html")



def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')

@login_required
def user_status(request):
    # This function is just used to check the user's login status
    pass


# def cart(request):
#     cart_items = CartItem.objects.all()

#     # Calculate the total quantity
#     total_quantity = sum(item.quantity for item in cart_items)

#     # Calculate subtotals for each cart item
#     for item in cart_items:
#         item.subtotal = item.product.price * item.quantity

#     total_cart_price = sum(item.subtotal for item in cart_items)

#     return render(request, 'cart.html', {'cart_items': cart_items, 'total_cart_price': total_cart_price, 'total_quantity': total_quantity})


# def add_to_cart(request, product_id):
#     product = Product.objects.get(id=product_id)

#     if request.method == 'POST':
#         size = request.POST.get('size')

#         # Add size information to the session or cart item as needed
#         # For simplicity, let's assume you have a CartItem model with a size field
#         # Modify this according to your actual data structure
#         cart_item, created = CartItem.objects.get_or_create(product=product)

#         if not created:
#             cart_item.quantity += 1
#             cart_item.save()
#             product.quantity -= 1  # Reduce the product quantity
#             product.save()

#         return redirect('cart')
    
#     # Handle GET request (redirect to home or display an error message)
#     messages.error(request, "Invalid request.")
#     return redirect('home')



# def cart(request):
#     cart_items = CartItem.objects.all()

#     # Calculate the total quantity
#     total_quantity = sum(item.quantity for item in cart_items)

#     # Calculate subtotals for each cart item
#     for item in cart_items:
#         item.subtotal = item.product.price * item.quantity

#     total_cart_price = sum(item.subtotal for item in cart_items)

#     return render(request, 'cart.html', {'cart_items': cart_items, 'total_cart_price': total_cart_price, 'total_quantity': total_quantity})



@login_required(login_url='login')
def cart(request):
    # Retrieve cart items for the current user
    cart_items = CartItem.objects.filter(user=request.user)

    # Calculate the total quantity
    total_quantity = sum(item.quantity for item in cart_items)

    # Calculate subtotals for each cart item
    for item in cart_items:
        item.subtotal = item.product.price * item.quantity

    total_cart_price = sum(item.subtotal for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_cart_price': total_cart_price, 'total_quantity': total_quantity})





# @login_required(login_url='login')
# def add_to_cart(request, product_id):
#     product = Product.objects.get(id=product_id)

#     if request.method == 'POST':
#         size = request.POST.get('size')

#         # Add size information to the session or cart item as needed
#         # For simplicity, let's assume you have a CartItem model with a size field
#         # Modify this according to your actual data structure
#         cart_item, created = CartItem.objects.get_or_create(product=product)

#         if not created:
#             cart_item.quantity += 1
#             cart_item.save()
#             product.quantity -= 1  # Reduce the product quantity
#             product.save()

#         return redirect('cart')
    
#     # Handle GET request (redirect to home or display an error message)
#     messages.error(request, "Invalid request.")
#     return redirect('home')


@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        size = request.POST.get('size')

        # Get the current user
        user = request.user

        # Add size information to the session or cart item as needed
        # For simplicity, let's assume you have a CartItem model with a size field
        # Modify this according to your actual data structure
        cart_item, created = CartItem.objects.get_or_create(user=user, product=product)

        if not created:
            cart_item.quantity += 1
            cart_item.save()
            product.quantity -= 1  # Reduce the product quantity
            product.save()

        return redirect('cart')
    
    # Handle GET request (redirect to home or display an error message)
    messages.error(request, "Invalid request.")
    return redirect('home')






def remove_from_cart(request, product_id):
    try:
        cart_item = CartItem.objects.get(product__id=product_id)

        # Increase the product quantity
        cart_item.product.quantity += cart_item.quantity
        cart_item.product.save()

        # Delete the cart item
        cart_item.delete()

        messages.success(request, "Product removed from cart.")
    except CartItem.DoesNotExist:
        messages.error(request, "Product not found in cart.")

    return redirect('cart')

# def increase_quantity(request, product_id):
#     cart_item = get_object_or_404(CartItem, product__id=product_id)

#     # Check if there is enough quantity in the product
#     if cart_item.product.quantity > cart_item.quantity:
#         cart_item.quantity += 1
#         cart_item.save()

#         # Update the product quantity
#         cart_item.product.quantity -= 1
#         cart_item.product.save()

#         messages.success(request, "Quantity increased.")
#     else:
#         messages.error(request, "Not enough quantity available.")

#     return redirect('cart')

# def decrease_quantity(request, product_id):
#     cart_item = get_object_or_404(CartItem, product__id=product_id)

#     if cart_item.quantity > 1:
#         cart_item.quantity -= 1
#         cart_item.save()

#         # Update the product quantity
#         cart_item.product.quantity += 1
#         cart_item.product.save()

#         messages.success(request, "Quantity decreased.")
#     else:
#         messages.error(request, "Minimum quantity reached.")

#     return redirect('cart')




def increase_quantity(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)

    # Check if the product quantity is greater than 0 before increasing it
    if cart_item.product.quantity > 0:
        cart_item.quantity += 1
        cart_item.save()
        cart_item.product.quantity -= 1  # Reduce the product quantity
        cart_item.product.save()

    return redirect('cart')


def decrease_quantity(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)

    # Check if the cart item's quantity is greater than 1 before decreasing it
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        cart_item.product.quantity += 1  # Increase the product quantity
        cart_item.product.save()

    return redirect('cart')


@login_required
def checkout(request):
    cart_items = CartItem.objects.all()

    # Calculate the total quantity and total price
    total_quantity = sum(item.quantity for item in cart_items)
    total_cart_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        # Get billing address from the form data
        billing_address = request.POST.get('billing_address')

        # Use a database transaction to ensure atomicity
        with transaction.atomic():
            # Create an order
            order = Order.objects.create(
                user=request.user,
                total_quantity=total_quantity,
                total_price=total_cart_price,
                billing_address=billing_address,
            )

            # Associate cart items with the order
            order.items.set(cart_items)

            # Clear the cart after checkout
            CartItem.objects.all().delete()

            return render(request, 'billing.html', {'order': order})

    return render(request, 'checkout.html', {'total_quantity': total_quantity, 'total_cart_price': total_cart_price})




@login_required(login_url='login')
def user_orders(request):
    # Fetch orders for the current user
    orders = Order.objects.filter(user=request.user)
    
    return render(request, 'user_orders.html', {'orders': orders})



from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Order

def users_with_orders(request):
    # Fetch users who have placed orders along with order details
    users_with_orders = User.objects.filter(order__isnull=False).distinct()

    return render(request, 'users_with_orders.html', {'users_with_orders': users_with_orders})
