from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os

# @csrf_exempt
# def endpoint(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         # Save data to a JSON file
#         with open('received_data.json', 'a') as f:
#             f.write(json.dumps(data) + '\n')
#         # Save data to a TXT file
#         with open('received_data.txt', 'a') as f:
#             f.write(json.dumps(data) + '\n')
#         return JsonResponse({"message": "Data received", "received_data": data}, status=200)
#     return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def endpoint(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('user', 'unknown')
        filename = f'{username}_data.json'

        with open(filename, 'a') as f:
            f.write(json.dumps(data) + '\n')

        return JsonResponse({"message": "Data received", "received_data": data}, status=200)
    return JsonResponse({"error": "Invalid method"}, status=405)


 

def display_data(request):
    data_list = []
    for filename in os.listdir():
        if filename.endswith('.json'):
            with open(filename, 'r') as f:
                file_data = [json.loads(line) for line in f]
                data_list.append((filename, file_data))

    # Debugging: Print the data to ensure it's in the correct format
    print(data_list)
    return render(request, 'index.html', {'data': data_list})

def home(request):
    return render(request, 'home.html')


# def display_data(request):
#     data_list = []
#     for filename in os.listdir():
#         if filename.endswith('.json'):
#             with open(filename, 'r') as f:
#                 data_list.extend([json.loads(line) for line in f])
#     return render(request, 'index.html', {'data': data_list})

# Create your views here.
