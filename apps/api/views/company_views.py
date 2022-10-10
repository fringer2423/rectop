from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist

from apps.core.models import Company

from ..serializers import CompanySerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createCompany(request):
    user = request.user

    try:

        company = Company.objects.create(
            owner=user,
            name=request.data['name']
        )

        serializer = CompanySerializer(company, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as er:
        message = f'Ошибка при создании {er}'
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCompany(request, pk):
    user = request.user

    try:
        company = Company.objects.get(pk=pk)

        if company.owner != user:
            return Response(data={'message': 'Это не ваша компания'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CompanySerializer(company, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой компании не найдено'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateCompany(request, pk):
    user = request.user

    try:
        company = Company.objects.get(pk=pk)

        if company.owner != user:
            return Response(data={'message': 'Это не ваша компания'}, status=status.HTTP_400_BAD_REQUEST)

        company.name = request.data['name']
        company.save()

        serializer = CompanySerializer(company, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой компании не найдено'}, status=status.HTTP_404_NOT_FOUND)

    except Exception:
        return Response(data={'message': 'Неверный запрос'}, status=status.HTTP_400_BAD_REQUEST)
