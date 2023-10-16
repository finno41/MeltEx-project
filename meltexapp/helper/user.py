from meltexapp.models import User
from meltexapp.data.user import get_users_by_company

def get_company_users(user):
    user_company = user.company
    company_users = get_users_by_company(user_company)
    return list(company_users)
