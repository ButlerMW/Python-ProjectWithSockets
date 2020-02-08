from django.shortcuts import render, HttpResponse
# from django.utils.safestring import mark_safe
# import json

# def index(request):
#     return HttpResponse("good to go!")

# def user_list(request):
#     return render(request, 'project_app/user_list.html')

def index(request):
    return render(request, 'project_app/login.html')

# def room(request, room_name):
#     return render(request, 'project_app/user_list.html', {
#         'room_name_json': mark_safe(json.dumps(room_name))
#     })

# def register(request)
    