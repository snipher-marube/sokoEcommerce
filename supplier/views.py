# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CommodityForm, SupplyRequestForm
from .models import Commodity, SupplyRequest

def supplier_dashboard(request):
    supply_requests = SupplyRequest.objects.filter(supplier=request.user)
    supplies_count = supply_requests.count()
    approved_supplies_count = supply_requests.filter(status='approved').count()
    rejected_supplies_count = supply_requests.filter(status='rejected').count()
    pending_supplies_count = supplies_count - (approved_supplies_count + rejected_supplies_count)
    context = {
        'supplies_count': supplies_count,
        'approved_supplies_count': approved_supplies_count,
        'rejected_supplies_count': rejected_supplies_count,
        'pending_supplies_count': pending_supplies_count
    }
    return render(request, 'supplier/dashboard.html', context)

@login_required
def create_commodity(request):
    if request.method == 'POST':
        form = CommodityForm(request.POST)
        if form.is_valid():
            commodity = form.save()
            messages.success(request, 'Commodity created successfully')
            return redirect('supplier_dashboard')
    else:
        form = CommodityForm()
    return render(request, 'supplier/create_commodity.html', {'form': form})

@login_required
def request_supply_tender(request):
    if request.method == 'POST':
        form = SupplyRequestForm(request.POST)
        if form.is_valid():
            supply_request = form.save(commit=False)
            supply_request.supplier = request.user  # Assign logged-in user as the supplier
            supply_request.save()
            form.save_m2m()  # Save the many-to-many relationship with commodities
            messages.success(request, 'Supply tender requested successfully')
            return redirect('supplier_dashboard')
    else:
        form = SupplyRequestForm()
    return render(request, 'supplier/request_supply_tender.html', {'form': form})

@login_required
def supply_requests(request):
    supply_requests = SupplyRequest.objects.filter(supplier=request.user)
    context = {
        'supply_requests': supply_requests
    }
    return render(request, 'supplier/supply_request.html', context)


@login_required
def rejected_supply_requests(request):
    supply_requests = SupplyRequest.objects.filter(supplier=request.user, status='rejected')
    context = {
        'supply_requests': supply_requests
    }
    return render(request, 'supplier/rejected_supply_requests.html', context)

@login_required
def approved_supply_requests(request):
    supply_requests = SupplyRequest.objects.filter(supplier=request.user, status='approved')
    context = {
        'supply_requests': supply_requests
    }
    return render(request, 'supplier/approved_supply_requests.html', context)

@login_required
def pending_supply_requests(request):
    supply_requests = SupplyRequest.objects.filter(supplier=request.user, status='pending')
    context = {
        'supply_requests': supply_requests
    }
    return render(request, 'supplier/pending_supply_requests.html', context)

def request_detail(request, request_id):
    supply_request = get_object_or_404(SupplyRequest, id=request_id)
    
    total_price = 0
    for commodity in supply_request.commodities.all():
        total_price += commodity.price * commodity.available_amount

    context = {
        'supply_request': supply_request,
        'total_price': total_price,
    }
    return render(request, 'supplier/request_detail.html', context)
