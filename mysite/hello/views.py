from django.http import HttpResponse

# Create your views here.

# https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpRequest.COOKIES
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/',
#     domain=None, secure=None, httponly=False, samesite=None)

#resp.set_cookie('dj4e_cookie', '282b2d93', max_age=1000)

def cookie(request):
    print(request.COOKIES)
    num_visits = sessfun(request)
    resp = HttpResponse('view count='+str(num_visits))
    resp.set_cookie('dj4e_cookie', '282b2d93', max_age=1000) # seconds until expire
    return resp


def sessfun(request) :
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    return num_visits



