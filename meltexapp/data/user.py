from meltexapp.models import User

def get_users_by_company(company):
    return User.objects.filter(company=company)
