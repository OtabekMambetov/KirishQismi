from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from serializers import UserSerializer
from .models import User
# from .serializers import UserSerializer

class UserListCreateView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def register_user(request):
    phone_number = request.data.get('phone_number')
    country_code = request.data.get('country_code')

    if not phone_number or not country_code:
        return Response({'error': 'Telefon raqami va mamlakat kodi talab qilinadi'}, status=400)

    # Foydalanuvchini saqlash
    user, created = User.objects.get_or_create(
        phone_number=phone_number,
        country_code=country_code
    )
    if created:
        return Response({'message': 'Ro‘yxatdan muvaffaqiyatli o‘tdingiz'})
    else:
        return Response({'message': 'Foydalanuvchi allaqachon ro‘yxatdan o‘tgan'}, status=200)
