from django.urls import path
from mobileapp import views

urlpatterns=[
    path("mobile/add",views.mobile_create,name="addmobiles"),
    path("home",views.home,name="home"),
    path("brand/create",views.createbrands,name="brand"),
    path("brand/list",views.listbrands,name="listbrand"),
    path("brand/view/<int:id>",views.viewbrands,name="display"),
    path("brand/delete/<int:id>",views.remove,name="delete"),
    path("brand/update/<int:id>",views.update,name="update"),
    path("mobiles",views.mobile_list,name="listmobile"),
    path("mobile/update/<int:id>",views.update_mobile,name="updatemobiles"),
    path("mobiles/view/<int:id>",views.viewmobile,name="displaymobile"),
    path("mobile/delete/<int:id>",views.removemobile,name="deletemobile")
]