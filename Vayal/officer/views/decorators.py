from django.contrib.auth.decorators import user_passes_test


def officer_login_required(function):
    actual_decorator = user_passes_test(lambda u: u.is_staff)
    return actual_decorator(function)
