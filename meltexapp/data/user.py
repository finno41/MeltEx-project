from meltexapp.models import User


def get_users_by_ids(user_ids):
    return User.objects.filter(id__in=user_ids)


def get_users_by_company(company):
    return User.objects.filter(company=company)
