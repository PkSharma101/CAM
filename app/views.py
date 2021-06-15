from django.shortcuts import render
from django.http import HttpResponse
from .models import manufacturing_tracker,style_code,Product
from django.core import serializers
from django.http import JsonResponse
import json
from django.contrib import messages
import random
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
User= get_user_model()
def home(request):
    return render(request,"home.html")


def about(request):
    return render(request,"page-about-us.html")

def contact(request):
    return render(request,"page-contact-us.html")


def vote(request):
    val = Product.objects.filter(is_vote=True)
    val = serializers.serialize('json',list(val))
    if request.method =='POST' and request.POST['action']=='like':
        pid = request.POST.get('pid')
        val = Product.objects.filter(pk=pid).first()
        val.like_count = val.like_count +1
        count = val.like_count
        val.save()
        count = json.dumps(count)
        context = {'count':count}
        return JsonResponse(context)

    if request.method =='POST' and request.POST['action']=='dislike':
        pid = request.POST.get('pid')
        val = Product.objects.filter(pk=pid).first()
        val.dislike_count = val.dislike_count + 1
        count = val.dislike_count
        val.save()
        count = json.dumps(count)
        context = {'count':count}
        return JsonResponse(context)

    context={'products':val}
    return render(request,"vote.html",context)

def tracker(request):
    style_code_list=[]
    product_name=[]
    status=[]
    image=[]
    expected_delivery_date=[]
    track=[]
    if (request.method ) =='POST':
        track_id=request.POST.get('track_id')
        try:
            
            if(manufacturing_tracker.objects.filter(id=track_id)):
               tracker = manufacturing_tracker.objects.filter(id=track_id)
            
            else:
                 raise Exception('Invalid Tracker Id')
          
            st_code=style_code.objects.filter(prd_id=track_id)
            for i in st_code:
                style_code_list.append(i.style_code)
                product_name.append(i.product_name)
                status.append(i.status)
                image.append(i.image)
                expected_delivery_date.append(i.expected_delivery_date)
            style_code_list=json.dumps(style_code_list,indent=4, sort_keys=True, default=str)
            product_name=json.dumps(product_name,indent=4, sort_keys=True, default=str)
            status=json.dumps(status,indent=4, sort_keys=True, default=str)
            image=json.dumps(image,indent=4, sort_keys=True, default=str)
            expected_delivery_date=json.dumps(expected_delivery_date,indent=4, sort_keys=True, default=str)
            for i in tracker:
                track.append(i.id)
                track.append(i.order_placed_date)
                track.append(i.client_name)
            track=json.dumps(track,indent=4, sort_keys=True, default=str)
            flag=True
            flag=json.dumps(flag)
            return render(request,"track.html",{'flag':flag,'track':track,'style_code_list':style_code_list,'product_name':product_name,'status':status,'image':image,'expected_delivery_date':expected_delivery_date})
        except Exception as e:
            flag=False
            flag=json.dumps(flag)
            style_code_list=json.dumps(style_code_list,indent=4, sort_keys=True, default=str)
            product_name=json.dumps(product_name,indent=4, sort_keys=True, default=str)
            status=json.dumps(status,indent=4, sort_keys=True, default=str)
            image=json.dumps(image,indent=4, sort_keys=True, default=str)
            expected_delivery_date=json.dumps(expected_delivery_date,indent=4, sort_keys=True, default=str)
            track=json.dumps(track,indent=4, sort_keys=True, default=str)
            return render(request,"track.html",{'flag':flag,'track':track,'style_code_list':style_code_list,'product_name':product_name,'status':status,'image':image,'expected_delivery_date':expected_delivery_date})
    return render(request,"track.html")
