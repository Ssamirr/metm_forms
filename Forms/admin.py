from django.contrib import admin
from Forms.models import Forms, Fields, Value, Option, Emails, Response

# Register your models here.

# admin.site.register(Fields)
@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ('field','value',)
    search_fields = ('field','value',)
    list_filter = ('field','value',)
    save_on_top = True
    fieldsets = (
        ('Information', {
            'description': 'Əsas Sahə',
            'classes': ('collapse',),
            'fields': ('field','value',)
        }),
    )

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('field','option',)
    search_fields = ('field','option',)
    list_filter = ('field','option',)
    save_on_top = True
    fieldsets = (
        ('Information', {
            'description': 'Əsas Sahə',
            'classes': ('collapse',),
            'fields': ('field','option',)
        }),
    )


@admin.register(Emails)
class EmailsAdmin(admin.ModelAdmin):
    list_display = ('form','email',)
    search_fields = ('form','email',)
    list_filter = ('form','email',)
    save_on_top = True
    fieldsets = (
        ('Information', {
            'description': 'Əsas Sahə',
            'classes': ('collapse',),
            'fields': ('form','email',)
        }),
    )

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('form','field','value',)
    search_fields = ('form','field','value',)
    list_filter = ('form','field','value',)
    readonly_fields=('form','field','value')
    save_on_top = True
    fieldsets = (
        ('Information', {
            'description': 'Əsas Sahə',
            'classes': ('collapse',),
            'fields': ('form','field','value',)
        }),
    )


class FieldsInline(admin.TabularInline):
    model = Fields
    extra = 0

class OptionsInline(admin.TabularInline):
    model = Option
    extra = 0

class EmailInline(admin.TabularInline):
    model = Emails
    extra = 0

class ResponsenInline(admin.TabularInline):
    model = Response
    extra = 0

@admin.register(Forms)
class FormsAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','updated_at','is_published') 
    search_fields = ('name','created_at','is_published')
    list_filter = ('name','created_at','is_published')
    save_on_top = True
    fieldsets = (
        ('Information', {
            'description': 'Əsas Sahə',
            'classes': ('collapse',),
            'fields': ('name','is_published',)
        }),
        # ('relations', {
        #     'description': 'relations desc',
        #     'classes': ('collapse',),
        #     'fields': ('category', 'author', 'tags',)
        # }),
    )
    inlines = [FieldsInline,EmailInline,ResponsenInline]

@admin.register(Fields)
class FieldsAdmin(admin.ModelAdmin):
    list_display = ('form','label','field_type','validation','requirement','is_published',) 
    search_fields = ('form','label','field_type','validation','requirement','is_published',)
    list_filter = ('form','label','field_type','validation','requirement','is_published',)
    save_on_top = True
    fieldsets = (
        ('Information', {
            'description': 'Əsas Sahə',
            'classes': ('collapse',),
            'fields': ('form','label','field_type','validation','requirement','is_published',)
        }),
    )
    inlines = [OptionsInline]



# @admin.register(Response)
# class ResponseAdmin(admin.ModelAdmin):
#     inlines = [ResponsenInline,]
