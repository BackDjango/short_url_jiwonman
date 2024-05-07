from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    # 기본 DRF 예외 처리기 호출
    response = exception_handler(exc, context)

    if response is not None:
        # 예외가 발생한 경우
        custom_response_data = {
            "error": response.data.get("detail", "An error occurred"),
        }
        response.data = custom_response_data

    return response
