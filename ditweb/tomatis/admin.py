from django.contrib import admin, messages

from .models import Device, Log

admin.site.site_header = "AGOS Management by Amar"

class DeviceA(admin.ModelAdmin):
	list_display = ('ip_address', 'hostname','vendor')
	list_filter = ('vendor',)


class LogA(admin.ModelAdmin):
	list_display = ('target', 'action','status','time','messages',)
	list_filter = ('action','status','time',)
		

class StateAdmin(admin.ModelAdmin): 
    list_display = ('name', 'active', 'created_on') 
  
    def active(self, obj): 
        return obj.is_active == 1
  
    active.boolean = True
  
    def make_active(modeladmin, request, queryset): 
        queryset.update(is_active = 1) 
        messages.success(request, "Selected Record(s) Marked as Active Successfully !!") 
  
    def make_inactive(modeladmin, request, queryset): 
        queryset.update(is_active = 0) 
        messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!") 
  
    admin.site.add_action(make_active, "Make Active") 
    admin.site.add_action(make_inactive, "Make Inactive") 
  
# Register your models here.

admin.site.register(Device, DeviceA)
admin.site.register(Log, LogA)