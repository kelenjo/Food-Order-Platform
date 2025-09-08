from functools import wraps
from flask import abort
from flask_login import current_user


def roles_required(*role_names):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Check if user is authenticated
            if not current_user.is_authenticated:
                abort(401)  # Unauthorized

            # Check if user has at least one required role
            if not any(current_user.has_role(role) for role in role_names):
                abort(403)  # Forbidden

            # If everything is fine, continue to the view
            return f(*args, **kwargs)
        return decorated_function
    return decorator
