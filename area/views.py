from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

# show_area
from area.models import AreaInfo


# show_area
def show_area(request):
    '''显示地区详情'''
    area = AreaInfo.objects.get(atitle='广州市')

    # child_area = AreaInfo.objects.get(aparent=area) #使用get方法返回的是多个对象，在模板文件中无法遍历，所以会报MultipleObjectsReturned错误

    child_area = AreaInfo.objects.filter(aparent__exact=area)
    return render(request, 'area/show_area.html', {'area': area, 'child_area': child_area})


# /show_select_area
def show_select_area(request):
    '''显示省市县选择页面'''
    return render(request, 'area/select_area.html')


# /get_prov
def get_prov(request):
    '''获取省级数据'''
    # aparent为空，表示省
    provs = AreaInfo.objects.filter(aparent__isnull=True)

    if provs:
        prov_list = list()
        for prov in provs:
            tuple = (prov.id, prov.atitle)
            prov_list.append(tuple)

    return JsonResponse({'prov_list': prov_list})


# /get_city
def get_city(request):
    '''获取市级数据'''

    param_dict = request.GET
    prov_id = param_dict.get("prov_id");

    citys = AreaInfo.objects.filter(aparent_id__exact=prov_id)

    if citys:
        city_list = list()
        for city in citys:
            tuple = (city.id, city.atitle)
            city_list.append(tuple)
    print(city_list)
    return JsonResponse({'city_list': city_list})
