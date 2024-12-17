from .services.excel_export_service import ExcelExportService
from django.http import  HttpResponse, HttpResponseServerError
from django.views import View

class ExportRobotsView(View):
    def get(self, request):
        try:
            output = ExcelExportService.generate_robots_report()
            response = HttpResponse(output,
                                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="all_robots.xlsx"'
            return response
        except Exception as e:
            return HttpResponseServerError("An error occurred while generating the Excel file.")
