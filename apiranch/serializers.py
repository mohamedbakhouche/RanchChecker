from rest_framework import serializers
from . models import osys, render_engine_version, render_engine, plugin_version, plugin, softwareVersion, software

class osysSerializer(serializers.ModelSerializer):
    class Meta:
        model = osys
        #fiels = ('os_name', 'os_version', 'os_bit')
        fields = '__all__'

class render_engine_versionSerializer(serializers.ModelSerializer):
    class Meta:
        model = render_engine_version
        #fiels = ('renEngVer_name')
        fields = '__all__'

class render_engineSerializer(serializers.ModelSerializer):
    class Meta:
        model = render_engine
        #fiels = ('render_engien_name', 'render_engien_version')
        fields = '__all__'

class plugin_versionSerializer(serializers.ModelSerializer):
    class Meta:
        model = plugin_version
        #fiels = ('plugin_version_name')
        fields = '__all__'

class pluginSerializer(serializers.ModelSerializer):
    class Meta:
        model = plugin
        #fiels = ('plugin_name', 'plugin_version')
        fields = '__all__'

class softwareVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = softwareVersion
        #fiels = ('software_version', 'plugin', 'render_engien')
        fields = '__all__'

class softwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = software
        #fiels = ('software_name', 'software_bit', 'software_os', 'software_version')
        fields = '__all__'