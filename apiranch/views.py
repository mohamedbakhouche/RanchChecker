from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from . models import osys, render_engine_version, render_engine, plugin_version, plugin, softwareVersion, software
from rest_framework.response import Response
from rest_framework import status
from . serializers import  osysSerializer, render_engine_versionSerializer, render_engineSerializer, plugin_versionSerializer, pluginSerializer, softwareVersionSerializer, softwareSerializer

class osysList(APIView):

    def get(self, request):
        _model = osys.objects.all()
        _serialize = osysSerializer(_model, many=True)
        return Response(_serialize.data)

class rendengversList(APIView):
    
    def get(self, request):
        _model = render_engine_version.objects.all()
        _serialize = render_engine_versionSerializer(_model, many=True)
        return Response(_serialize.data)

class render_engienList(APIView):
    
    def get(self, request):
        _model = render_engine.objects.all()
        _serialize = render_engineSerializer(_model, many=True)
        return Response(_serialize.data)

class plugin_versionList(APIView):
    
    def get(self, request):
        _model = plugin_version.objects.all()
        _serialize = plugin_versionSerializer(_model, many=True)
        return Response(_serialize.data)

class pluginList(APIView):
    
    def get(self, request):
        _model = plugin.objects.all()
        _serialize = pluginSerializer(_model, many=True)
        return Response(_serialize.data)

class softwareVersionList(APIView):
    
    def get(self, request):
        _model = softwareVersion.objects.all()
        _serialize = softwareVersionSerializer(_model, many=True)
        return Response(_serialize.data)

class softwareList(APIView):
    
    def get(self, request):
        _model = software.objects.all()
        _serialize = softwareSerializer(_model, many=True)
        return Response(_serialize.data)