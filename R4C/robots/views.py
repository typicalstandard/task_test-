from django.http import JsonResponse,HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import openpyxl

from .models import Robot
from .RobotForm import RobotForm


@method_decorator(csrf_exempt, name='dispatch')
class CreateRobotAPIView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            form = RobotForm(data)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Robot created successfully!'}, status=201)
            else:
                return JsonResponse({'errors': form.errors}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)


class ExportRobotsView(View):
    def get(self, request, *args, **kwargs):
        # Создаем новый Excel файл
        workbook = openpyxl.Workbook()
        for model in Robot.objects.values_list('model', flat=True).distinct():
            # Создаем новый лист для каждой модели
            worksheet = workbook.create_sheet(title=model)
            worksheet.append(['Version', 'Count'])

            # Получаем данные по версиям этой модели
            versions = Robot.objects.filter(model=model).values('version').annotate(count=models.Count('version'))
            for version in versions:
                worksheet.append([version['version'], version['count']])

        # Удаляем стандартный пустой лист
        if 'Sheet' in workbook.sheetnames:
            del workbook['Sheet']

        # Создаем HTTP response с заголовками для скачивания файла
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=robots_summary.xlsx'
        workbook.save(response)
        return response
