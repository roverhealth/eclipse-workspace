from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from PriceMyVet.views import *

admin.autodiscover()

urlpatterns = [
    #url(r'^PriceMyVet/$',search, name='search'),
    #url(r'^PriceMyVet/find_services/$', find_services, name='find_services'),
    #url(r'^PriceMyVet/about/$', about, name='about'),
    #url(r'^add_category/$', views.add_category, name='add_category'),
    #url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
    #url(r'^category/(?P<category_name_url>\w+)/add_page/$', views.add_page, name='add_page'),
    url(r'^PriceMyVet/register/$', register, name='register'),
    url(r'^PriceMyVet/login/$', user_login, name='login'),
    #url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^PriceMyVet/logout/$', user_logout, name ='logout'),
    url(r'^PriceMyVet/forgotpassword/$', forgotpassword, name ='forgotpassword'),
    url(r'^PriceMyVet/petparent/$',petparent, name='petparent'),
    #url(r'^PriceMyVet/vetpractice/$',vetpractice, name='vetpractice'),
    #url(r'^PriceMyVet/manage_pet/$',manage_pet, name='manage_pet'),
    #url(r'^PriceMyVet/manage_vet/$',manage_vet, name='manage_vet'),
     #to reset password 
    #url(r'^PriceMyVet/reset/$', 
    #    'django.contrib.auth.views.password_reset', 
    #    {'post_reset_redirect' : '/PriceMyVet/reset/done/'},
    #    name="password_reset"),
    (r'^PriceMyVet/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'^PriceMyVet/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/PriceMyVet/done/'}),
    (r'^PriceMyVet/done/$', 
        'django.contrib.auth.views.password_reset_complete'), 
#     url(r'^user/password/reset/$', 
#         'django.contrib.auth.views.password_reset', 
#         {'post_reset_redirect' : '/user/password/reset/done/'},
#         name="password_reset"),
#     (r'^user/password/reset/done/$',
#         'django.contrib.auth.views.password_reset_done'),
#     (r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
#         'django.contrib.auth.views.password_reset_confirm', 
#         {'post_reset_redirect' : '/user/password/done/'}),
#     (r'^user/password/done/$', 
#         'django.contrib.auth.views.password_reset_complete'),

    #end of password reset
    url(r'^admin/', include(admin.site.urls)),]
#if settings.DEBUG:
#    urlpatterns += [
#        'django.views.static',
#        (r'media/(?P<path>.*)',
#         'serve',
#         {'document_root':settings.MEDIA_ROOT}),]
    
#    url(r'^add/$', 'add_pet', name='add_pet'),
#    url(r'^update/(\d+)/$', 'update_pet', name='update_pet'),
