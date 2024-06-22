
# Create your views here.
# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Farmer


def farmer_form(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        pincode = request.POST.get('pincode')
        gender = request.POST.get('gender')
        aadhar_number = request.POST.get('aadhar_number')
        contact_number = request.POST.get('contact_number')
        area_ploughed = request.POST.get('area_ploughed')
        season = request.POST.get('season')
        crops_grown = request.POST.get('crops_grown')
        seeds_used = request.POST.get('seeds_used')
        date_of_seed_sown = request.POST.get('date_of_seed_sown')
        transplanting = request.POST.get('transplanting')
        irrigation_method = request.POST.get('irrigation_method')
        fertilisers_used = request.POST.get('fertilisers_used')
        date_of_harvesting = request.POST.get('date_of_harvesting')
        yield_in_kg = request.POST.get('yield')
        financial_need = request.POST.get('financial_need')

        # Save data to the database
        farmer = Farmer(
            name=name,
            pincode=pincode,
            gender=gender,
            aadhar_number=aadhar_number,
            contact_number=contact_number,
            area_ploughed=area_ploughed,
            season=season,
            crops_grown=crops_grown,
            seeds_used=seeds_used,
            date_of_seed_sown=date_of_seed_sown,
            transplanting=transplanting,
            irrigation_method=irrigation_method,
            fertilisers_used=fertilisers_used,
            date_of_harvesting=date_of_harvesting,
            yield_in_kg=yield_in_kg,
            financial_need=financial_need
        )
        farmer.save()

        return HttpResponse("Form submitted successfully!")
    return render(request, 'farmer_form.html')
