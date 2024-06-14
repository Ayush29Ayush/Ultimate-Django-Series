from django.contrib import admin
from store.models import Collection, Product, Customer, Order
from django.db.models.aggregates import Count

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "unit_price", "inventory", "invertory_status", "collection_title"]
    list_editable = ["unit_price"]
    list_per_page = 25
    list_select_related = ["collection"]

    def collection_title(self, Product):
        return Product.collection.title
    
    @admin.display(ordering="inventory")
    def invertory_status(self, Product):
        if Product.inventory < 10:
            return "LOW INVENTORY"
        return "IN STOCK"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "placed_at", "customer"]
    list_per_page = 25


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "products_count"]
    search_fields = ["title"]

    @admin.display(ordering="products_count")
    def products_count(self, Collection):
        return Collection.products_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count("product")
        )

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    list_per_page = 25
    ordering = ["first_name", "last_name"]
    search_fields = ["first_name__istartswith", "last_name__istartswith"]
    list_filter = ["membership"]
    actions = ["set_ayush"]

    @admin.action(description="Set first_name to Ayush")
    def set_ayush(self, request, queryset):
        queryset.update(first_name="Ayush")

# admin.site.register(Collection)
# admin.site.register(Customer)
