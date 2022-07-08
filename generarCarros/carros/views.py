import imp
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import carros

# Create your views here.

@api_view(["POST","GET"])
def getCarros(request,*args,**kwargs):

    if request.method == "POST":

        marca = request.data.get("marca")
        modelo = request.data.get("modelo")
        color = request.data.get("color")
        potencia = request.data.get("potencia")
        año = request.data.get("año")
        placa = request.data.get("placa")

        carro = carros(marca=marca, modelo=modelo, color=color, potencia=potencia, año=año, placa=placa)
        carro.save()

        return Response({
            "data": {
                "marca": carro.marca,
                "modelo": carro.modelo,
                "color": carro.color,
                "caballos de fuerza": carro.potencia,
                "año": carro.año,
                "placa": carro.placa
            }
        })

    if request.method == "GET":
        _carros = carros.objects.all()
        return Response({
            "data": [{
                "marca": carro.marca,
                "modelo": carro.modelo,
                "color": carro.color,
                "caballos de fuerza": carro.potencia,
                "año": carro.año,
                "placa": carro.placa
            } for carro in _carros]
        })