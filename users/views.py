from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import UserValidateSerializer
from django.core.mail import send_mail
from rest_framework.generics import GenericAPIView, CreateAPIView


class RegisterAPIView(GenericAPIView):
    def post(self, request):
        serializer = UserValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        User.objects.create_user(**serializer.validated_data, is_active=False)
        user_id = User.objects.get(username=serializer.validated_data['username']).id
        send_mail(
            subject='Activate Your Account Now',
            message='You’re just one click away from getting started with our service.\n'
                    'All you need to do is verify your email address to activate your account.\n'
                    f'CLICK LINK: http://127.0.0.1:8000/api/v1/activate/{user_id}/\n'
                    'You’re receiving this email because you recently created a new user. '
                    'If this wasn’t you, please ignore this email.',
            from_email='pyback12@gmail.com',
            recipient_list=[f'{serializer.validated_data["email"]}'],
            fail_silently=False,
        )
        return Response(data={'User created!'}, status=status.HTTP_201_CREATED)


class LoginAPIView(GenericAPIView):
    def post(self, request):
        user = authenticate(**request.data)
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'token': token.key})
        return Response(data={'User does not exist!'}, status=status.HTTP_404_NOT_FOUND)


class ActivateAPIView(GenericAPIView):
    def activate(request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(data={'User not found!'}, status=status.HTTP_404_NOT_FOUND)
        user.is_active = True
        user.save()
        return Response(data={'User activated successfully!'})


class SomeNewClass:
    print('New class for branch test')

# @api_view(['POST'])
# def register(request):
#     if request.method == 'POST':
#         serializer = UserValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={'errors': serializer.errors},
#                             status=status.HTTP_406_NOT_ACCEPTABLE)
#         User.objects.create_user(**serializer.validated_data, is_active=False)
#         user_id = User.objects.get(username=serializer.validated_data['username']).id
#         send_mail(
#             subject='Activate Your Account Now',
#             message='You’re just one click away from getting started with our service.\n'
#                     'All you need to do is verify your email address to activate your account.\n'
#                     f'CLICK LINK: http://127.0.0.1:8000/api/v1/activate/{user_id}/\n'
#                     'You’re receiving this email because you recently created a new user. '
#                     'If this wasn’t you, please ignore this email.',
#             from_email='pyback12@gmail.com',
#             recipient_list=[f'{serializer.validated_data["email"]}'],
#             fail_silently=False,
#         )
#         return Response(data={'User created!'}, status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# def login(request):
#     if request.method == 'POST':
#         user = authenticate(**request.data)
#         if user:
#             try:
#                 token = Token.objects.get(user=user)
#             except Token.DoesNotExist:
#                 token = Token.objects.create(user=user)
#             return Response(data={'token': token.key})
#         return Response(data={'User does not exist!'}, status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['GET'])
# def activate(request, id):
#     try:
#         user = User.objects.get(id=id)
#     except User.DoesNotExist:
#         return Response(data={'User not found!'}, status=status.HTTP_404_NOT_FOUND)
#     user.is_active = True
#     user.save()
#     return Response(data={'User activated successfully!'})
