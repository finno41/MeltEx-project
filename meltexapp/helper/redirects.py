from django.urls import reverse


def login_redirect_url(variables: dict):
    login_params = (
        f"?{'&'.join([f'{key}={value}' for key, value in variables.items()])}"
    )
    login_url = reverse("login") + login_params
    return login_url
