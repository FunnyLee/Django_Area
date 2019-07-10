from django.shortcuts import render

# Create your views here.

# show_area
from area.models import AreaInfo


def show_area(request):
    '''显示地区详情'''
    area = AreaInfo.objects.get(atitle='广州市')

    # child_area = AreaInfo.objects.get(aparent=area) #使用get方法返回的是多个对象，在模板文件中无法遍历，所以会报MultipleObjectsReturned错误

    child_area = AreaInfo.objects.filter(aparent__exact=area)
    return render(request, 'area/show_area.html', {'area': area, 'child_area': child_area})
