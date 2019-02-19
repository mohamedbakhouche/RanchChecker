from __future__ import unicode_literals

from django.db import models

class osys(models.Model):
    os_name = models.CharField(max_length=50)
    os_version = models.CharField(max_length=50)
    os_bit = models.CharField(max_length=50)
    def __str__(self):
        return self.os_name

class render_engien_version(models.Model):
    renEngVer_name = models.CharField(max_length=50)
    def __str__(self):
        return self.renEngVer_name

class render_engien(models.Model):
    render_engien_name = models.CharField(max_length=50)
    render_engien_version = models.ManyToManyField(render_engien_version)
    def __str__(self):
        return self.render_engien_name

class plugin_version(models.Model):
    plugin_version_name = models.CharField(max_length=50)
    def __str__(self):
        return self.plugin_version_name

class plugin(models.Model):
    plugin_name = models.CharField(max_length=50)
    plugin_version = models.ManyToManyField(plugin_version)
    def __str__(self):
        return self.plugin_name

class softwareVersion(models.Model):
    software_version = models.CharField(max_length=50)
    plugin = models.ManyToManyField(plugin, blank=True)
    render_engien = models.ManyToManyField(render_engien, blank=True)
    def __str__(self):
        return self.software_version

class software(models.Model):
    software_name = models.CharField(max_length=50)
    software_bit = models.CharField(max_length=50)
    software_os = models.ManyToManyField(osys)
    software_version = models.ManyToManyField(softwareVersion)
    
    def __str__(self):
        return self.software_name