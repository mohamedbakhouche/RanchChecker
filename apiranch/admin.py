from django.contrib import admin
from . models import osys, render_engine_version, render_engine, plugin_version, plugin, softwareVersion, software
admin.site.register(osys)
admin.site.register(render_engine_version)
admin.site.register(render_engine)
admin.site.register(plugin_version)
admin.site.register(plugin)
admin.site.register(softwareVersion)
admin.site.register(software)