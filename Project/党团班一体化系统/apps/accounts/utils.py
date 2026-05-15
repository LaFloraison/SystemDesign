from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponseForbidden


def role_required(*allowed_roles):
    """Decorator: restrict view to specific roles."""
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("login")
            if request.user.role not in allowed_roles:
                messages.error(request, "权限不足")
                return redirect("home")
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


def class_member_required(view_func):
    """Decorator: user must belong to a class."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.class_name:
            messages.error(request, "请先完善班级信息")
            return redirect("profile_edit")
        return view_func(request, *args, **kwargs)
    return wrapper
