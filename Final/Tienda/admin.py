from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Producto,Seccion,Order


# Register your models here.
admin.site.site_header = "Panel Administrativo"
admin.site.site_title = "Jaguarete KAA"
admin.site.index_title = "Control de ventas"

class ProductoAdmin(admin.ModelAdmin):
	def change_category_to_default(self,request,queryset):
		queryset.update(seccion="default")

	change_category_to_default.short_description = 'Categoria predeterminada'
	list_display = ('nombre','precio','seccion')
	search_fields = ('nombre',)
	actions = ('change_category_to_default',)

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Seccion)
admin.site.register(Order)
