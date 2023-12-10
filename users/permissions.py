from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
            
class IsCustomAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """
    
    def has_permission(self, request, view):
        access_token = request.COOKIES.get('access_token')
        refresh_token = request.COOKIES.get('refresh_token')
        return self.are_tokens_valid(access_token, refresh_token) \
                    or bool(request.user and request.user.is_authenticated)
    
    def are_tokens_valid(self, access_token, refresh_token):
        if not access_token or not refresh_token:
            return False
        try:
            AccessToken(access_token).verify()
            RefreshToken(refresh_token).verify()
            return True
        except Exception as e:
            print("Error with token:", e)