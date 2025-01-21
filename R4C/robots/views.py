from .services.excel_export_service import ExcelExportService
from django.http import  HttpResponse, HttpResponseServerError
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from .RobotForm import RobotForm

@method_decorator(csrf_exempt, name='dispatch')
class CreateRobotAPIView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            form = RobotForm(data)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Робот успешно создан!'}, status=201)
            else:
                return JsonResponse({'errors': form.errors}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Некорректные данные JSON'}, status=400)

class ExportRobotsView(View):
    def get(self, request):
        try:
            output = ExcelExportService.generate_robots_report()
            response = HttpResponse(output,
                                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="all_robots.xlsx"'
            return response
        except Exception as e:
            return HttpResponseServerError("Произошла ошибка при генерации файла Excel")
            data = json.loads(request.body)
            form = RobotForm(data)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Робот успешно создан!'}, status=201)
            else:
                return JsonResponse({'errors': form.errors}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Некорректные данные JSON'}, status=400)
