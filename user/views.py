from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as logout_user,
)
from user.serializers import *
from user.models import *


class LoginView(APIView):
    """Class based view loggin in user and returning Auth Token."""

    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = request.data
        serializer_obj = LoginSerializer(data=data)

        if serializer_obj.is_valid():
            username = serializer_obj.data["username"]
            password = serializer_obj.data["password"]

            user = authenticate(username=username, password=password)

            if not user:
                return Response({"error": "Invalid Credentials"}, status=401)

            if not user.is_active:
                return Response(
                    {"error": "Your account is inactive. Please contact support!"},
                    status=401,
                )

            django_login(request, user)
            token, _ = Token.objects.get_or_create(user=user)

            response_data = UserAccountSerializer(
                user, context={"request": request}
            ).data
            response_data["key"] = token.key
            return Response(response_data, status=200)

        return Response(serializer_obj.errors, status=400)


class RegisterAPIView(CreateAPIView):
    queryset = UserAccount.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        django_login(request, user)

        response_data = UserAccountSerializer(user, context={"request": request}).data

        # get token for this user
        token_obj, _ = Token.objects.get_or_create(user=self.user)

        data = {**response_data, "key": token_obj.key}
        return Response(data, status=201)

    def perform_create(self, serializer):
        self.user = serializer.save()
        return self.user


class LogoutAPIView(APIView):

    def post(self, request):
        try:
            # on logout, make fcm_token empty, so that they don't receive notification
            request.user.fcm_token = None
            request.user.save()
            # now logout the user
            logout_user(request)
            return Response("Logged out successfully.")
        except Exception as e:
            self.log_error("Error in logout process", str(e))
            return Response("Couldn't log you out, please try again!", 500)


class UserInfo(APIView):
    """Check the userinfo of a user"""

    def get(self, request):
        user = request.user
        serializer = UserAccountSerializer(user, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = UserAccountSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()

            return Response({"data": data, "message": "Profile Updated Successfully"})


class PasswordChangeView(APIView):
    """Modify rest auth default password change view"""

    serializer_class = PasswordChangeSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Password updated successfully."})


class PasswordResetAPIView(APIView):
    """
    Calls Django Auth PasswordResetForm save method.

    Accepts the following POST parameters: email
    Returns the success/fail message.
    """

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # Create a serializer with request.data
        serializer = PasswordResetSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response({"detail": "Password reset e-mail has been sent."})


class PasswordResetConfirmAPIView(APIView):
    """
    Password reset e-mail link is confirmed, therefore
    this resets the user's password.

    Accepts the following POST parameters:
    token, uid, new_password1, new_password2
    Returns the success/fail message.
    """

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": "Password has been reset with the new password."}
        )
