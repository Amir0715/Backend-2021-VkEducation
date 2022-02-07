from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from ui.models import City, Line, Station


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "count_of_lines"
    ]

    search_fields = ["name"]
    # ordering = ["lines__count", ]

    def count_of_lines(self, obj):
        return obj.lines.count()


@admin.register(Line)
class LineAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "city_url",
        # "count_of_stations",
    ]

    search_fields = ["name", "city__name"]

    list_filter = [
        "name",
        "city__name",
    ]

    ordering = [
        "name",
        "city__name",
        # "count_of_stations",
    ]

    def city_url(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:ui_city_change", args=(obj.city.pk, )),
            obj.city.name
        ))

    # def count_of_stations(self, obj):
    #     return obj.stations.count()


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "order",
        "latitude",
        "longitude",
    ]

    list_filter = [
        "line__name",
    ]
    
    search_fields = ["name", "line__name"]

    ordering = [
        "name",
        "order",
    ]
