import csv
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from django.db.models.options import Options


class Export_goods_mixin:
    def export_csv(self, request, queryset):
        meta = self.model._meta
        fields_name = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['content-Disposition'] = f'attachment; filename={meta} export_csv'

        csv_writer = csv.writer(response)

        csv_writer.writerow(fields_name)

        for row in queryset:
            csv_writer.writerow([getattr(row, field) for field in fields_name])

        return response
    
    export_csv.short_description = 'Выгрузка в csv файл'
