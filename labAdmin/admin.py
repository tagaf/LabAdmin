from django.contrib import admin
from labAdmin.models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'nfcId','firstSignup', 'lastSignup', 'subscription',)
    ordering = ('name',) # The negative sign indicate descendent order

    def subscription(self, obj):
        return obj.endSubcription if obj.needSubcription else "lifetime membership"

admin.site.register(User, UserAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'role_kind', 'time_slots','valid')
    ordering = ('name',)

admin.site.register(Role, RoleAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'roles')
    ordering = ('name',)

admin.site.register(Group, GroupAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name')
    ordering = ('name',)

admin.site.register(Category, CategoryAdmin)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'hourlyCost', 'category', 'mac')
    ordering = ('name',)

admin.site.register(Device, DeviceAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('date', 'value', 'user')
    ordering = ('-date','user',)

admin.site.register(Payment, PaymentAdmin)


class LogAccessAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'user', 'opened')
    ordering = ('-datetime','user',)

admin.site.register(LogAccess,LogAccessAdmin)


class LogDeviceAdmin(admin.ModelAdmin):
    list_display = ('user', 'device', 'bootDevice', 'shutdownDevice', 'startWork', 'finishWork', 'inWorking', 'priceWork')
    ordering = ('-bootDevice','-startWork',)

admin.site.register(LogDevice, LogDeviceAdmin)

class LogErrorAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'description', 'code')
    ordering = ('-bootDevice','-startWork',)

admin.site.register(LogError, LogErrorAdmin)


class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('name', 'weekday_start', 'weekday_end', 'hour_start', 'hour_end')
    ordering = ('name',)

admin.site.register(TimeSlot, TimeSlotAdmin)
