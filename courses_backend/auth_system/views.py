import json
from django.contrib.auth.models import User
from django.http import JsonResponse


def UserRegistration(request):

    json_response = {
        "status":"no_status",
        "errors":"no_errors",
    }

    json_data = request.POST.get('json_data', default=None)

    if json_data == None:
        json_response["status"] = "failed"
        json_response["errors"] = "Not found data"
        return JsonResponse(json_response)

    data = json.loads(json_data)

    #Проверка сушествования пользователя
    mail_exist = User.objects.filter(email=data["email"]).exists()

    if mail_exist:
        json_response["status"] = "failed"
        json_response["errors"] = "User with this mail is exist"
    else:
        user = User.objects.create_user(data["email"], data["email"], data["password"])

        user.first_name = data["firstname"]
        user.last_name = data["lastname"]
        user.save()
        json_response["status"] = "succesfully"

    return JsonResponse(json_response)