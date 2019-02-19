from django.contrib import admin
from . models import osys, render_engien_version, render_engien, plugin_version, plugin, softwareVersion, software
admin.site.register(osys)
admin.site.register(render_engien_version)
admin.site.register(render_engien)
admin.site.register(plugin_version)
admin.site.register(plugin)
admin.site.register(softwareVersion)
admin.site.register(software)