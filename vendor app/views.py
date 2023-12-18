from django.shortcuts import render
from rest_framework import status  # Add this import
# Create your views here.
from django.shortcuts import render

# Create your views here.
# vendor_management_project/vendor_app/views.py
from django.db import connection
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer

@api_view(['POST'])
def create_vendor(request):
    serializer = VendorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Vendor created successfully'}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def list_vendors(request):
    vendors = Vendor.objects.all().order_by('id')
    serializer = VendorSerializer(vendors, many=True)
    return Response({'vendors': serializer.data})

@api_view(['GET'])
def get_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    serializer = VendorSerializer(vendor)
    return Response(serializer.data)

@api_view(['PUT'])
def update_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    serializer = VendorSerializer(instance=vendor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Vendor updated successfully'})
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    vendor.delete()
    return Response({'message': 'Vendor deleted successfully'})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PurchaseOrder, Vendor
from .serializers import PurchaseOrderSerializer, VendorSerializer

@api_view(['POST'])
def create_purchase_order(request):
    purchase_order_data = request.data

    # Extract vendor data from purchase order data
    vendor_data = purchase_order_data.pop('vendor', None)

    # Create or get the Vendor instance
    if vendor_data:
        vendor_serializer = VendorSerializer(data=vendor_data)
        if vendor_serializer.is_valid():
            vendor_instance = vendor_serializer.save()
        else:
            return Response({'vendor': vendor_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'detail': 'Vendor data is required'}, status=status.HTTP_400_BAD_REQUEST)

    # Add the Vendor instance's pk to the purchase order data
    purchase_order_data['vendor'] = vendor_instance.pk

    # Serialize and save the PurchaseOrder
    serializer = PurchaseOrderSerializer(data=purchase_order_data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Purchase order created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_purchase_orders(request):
    purchase_orders = PurchaseOrder.objects.all()
    serializer = PurchaseOrderSerializer(purchase_orders, many=True)
    return Response({'purchase_orders': serializer.data})

@api_view(['GET'])
def get_purchase_order(request, po_id):
    po = get_object_or_404(PurchaseOrder, pk=po_id)
    serializer = PurchaseOrderSerializer(po)
    return Response(serializer.data)

@api_view(['PUT'])
def update_purchase_order(request, po_id):
    po = get_object_or_404(PurchaseOrder, pk=po_id)
    serializer = PurchaseOrderSerializer(instance=po, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Purchase order updated successfully'})
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_purchase_order(request, po_id):
    po = get_object_or_404(PurchaseOrder, pk=po_id)
    po.delete()
    return Response({'message': 'Purchase order deleted successfully'})


@api_view(['GET'])
def get_vendor_performance(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)

    on_time_delivery_rate = vendor.calculate_on_time_delivery_rate()
    quality_rating_avg = vendor.calculate_quality_rating_avg()
    average_response_time = vendor.calculate_average_response_time()
    fulfillment_rate = vendor.calculate_fulfillment_rate()

    performance_data = {
        'on_time_delivery_rate': on_time_delivery_rate,
        'quality_rating_avg': quality_rating_avg,
        'average_response_time': average_response_time,
        'fulfillment_rate': fulfillment_rate,
    }

    return Response(performance_data)
    

def acknowledge_purchase_order(request, po_id):
    po = get_object_or_404(PurchaseOrder, pk=po_id)

    # Update acknowledgment_date
    po.acknowledgment_date = timezone.now()
    po.save()

    # Recalculate average_response_time for the vendor
    vendor = po.vendor
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed').exclude(acknowledgment_date=None)
    response_times = [(po.acknowledgment_date - po.issue_date).total_seconds() for po in completed_pos]
    vendor.average_response_time = sum(response_times) / len(response_times) if len(response_times) > 0 else 0
    vendor.save()

    return Response({'message': 'Purchase order acknowledged successfully'})



def vendor_list(request):
    vendors = Vendor.objects.all()
   
    return render(request, 'vendor_list.html', {'vendors': vendors})

def vendor_form(request, vendor_id=None):
    if vendor_id:
        vendor = get_object_or_404(Vendor, pk=vendor_id)
    else:
        vendor = None
    
    return render(request, 'vendor_form.html', {'vendor': vendor})

def vendor_detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    return render(request, 'vendor_detail.html', {'vendor': vendor})

