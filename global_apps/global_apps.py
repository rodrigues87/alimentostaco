from allauth.socialaccount.models import SocialAccount


def global_apps(request):
    context = {}
    if request.user.is_authenticated:
        solicalAccount = SocialAccount.objects.get(user=request.user).extra_data
        picture = solicalAccount.get('picture')
        given_name = solicalAccount.get('given_name')

        return {'picture': picture,'given_name':given_name}
    return context