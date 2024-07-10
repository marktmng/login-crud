from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


def sumNumbers(start_num, end_num):
    if start_num > end_num:
        start_num, end_num = end_num, start_num
    sum = 0
    for i in range(start_num, end_num + 1):
        sum += i
    return sum


@api_view(["POST"])
def sumNumbersView(request):
    data = request.data
    start_num = data["start_num"]
    end_num = data["end_num"]
    result = sumNumbers(start_num, end_num)
    return Response({"result": result})