from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('-created_date')
    
    # Initialize an empty list to store reviews
    reviews = []

    # Get reviews for each product and append them to the list
    for product in products:
        product_reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
        reviews.extend(product_reviews)

    context = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'pages/home.html', context)
