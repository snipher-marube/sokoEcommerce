from .models import Cart, CartItem

from .views import _cart_id

def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            if request.user.is_authenticated:
                item_count = 0
                cart_items = CartItem.objects.all().filter(user=request.user)
                for cart_item in cart_items:
                    item_count += cart_item.quantity
            else:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                cart_items = CartItem.objects.filter(cart=cart, is_active=True)
                for cart_item in cart_items:
                    item_count += cart_item.quantity
                    
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)