from django.contrib import admin
from django.urls import path
from ppk import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('new_dashboard/',views.dash,name='new_dashbord'),
    path('all_loans/',views.all_loans,name='all_loans'),
    
    # path('insur',views.insurances,name='insur'),
    # path('login/', views.user_login, name='login'),  # Updated to new function name
    # path('get_application_details',views.get_application_details,name='get_application_details'),
    # path('applications/',views. DSA_BUSI_applications, name='filtered_applications'),
    # path('applications/',views. DSA_GOLD_applications, name='filtered_applications'),

    # path('business-loans/dsaref/<str:dsaref_code>/',views. GetBusinessLoansByDsarefCode.as_view(), name='get_business_loans_by_dsaref'),

    # path('gold-applications/',views. DSA_GOLD_applications, name='gold_applications'),

    path('dsa_Refcount/',views. refcount, name='dsa_Refcount'),
    path('fra_Refcount/',views. fra_refcount, name='fra_Refcount'),
    path('sale_Refcount/',views. sale_refcount, name='sale_Refcount'),
    path('dsa_inscount/',views. dsainscount, name='dsa_inscount'),
    path('far_inscount/',views. farinscount, name='far_inscount'),
    path('sale_inscount/',views. saleinscount, name='sale_inscount'),
    path('login/check/', views.login_check, name='login_check'),  # Route for the login API call
    path('logout/', views.Logout, name='logout'),




]



