from .models import User
def current_user(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            return {'current_user': user}  # ✅ matches what you're using in templates
        except User.DoesNotExist:
            return {'current_user': None}
    return {'current_user': None}