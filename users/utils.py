from .models import Profile, Skill
from django.db.models import Q


def searchProfiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    print('SEARCH QUERY', search_query)
    
    skills = Skill.objects.filter(name__iexact = search_query)

    # If we use filter like this, then when we search for profiles, the name,
    # and short_intro, both needs to contain the same search query,
    # but we want to filter either by name or short_intro.
    # profiles = Profile.objects.filter(name__icontains = search_query,
    #                                   short_intro__icontains = search_query)

    # so we gonna use Q lookups to prevent what's happening above.
    profiles = Profile.objects.distinct().filter(Q(name__icontains = search_query) |
                                      Q(short_intro__icontains = search_query) |
                                      Q(skill__in = skills)
                                      )
    return profiles, search_query
    