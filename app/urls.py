from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.loginView,name="login"),
    path("insert/",views.InsertData,name="insert"),
    path("home",views.homeView,name="home"),
    path("lost",views.lostView,name="lost"),
    path("found",views.foundView,name="found"),
    path("profile/",views.profileView,name="profile"),
    path("logoutRequest",views.logoutRequestView,name="logoutRequest"),
    path("show",views.showPage,name="show"),
    path("editpage/<int:pk>",views.EditPage,name="editpage"),
    path("update/<int:pk>",views.UpdateData,name="update"),
    path("delete/<int:pk>",views.DeleteData,name="delete"),
    path("register",views.registerView,name='register'),
    path("register1",views.UserRegister,name='register1'),
    path("loginuser",views.LoginUser,name="loginuser"),
    path("founddata",views.FoundView,name="founddata"),
    path("foundshow",views.foundshowPage,name="foundshow"),
    path("lostprofile",views.lostProfileView,name="lostProfile"),
    path("foundProfile",views.foundProfileView,name="foundProfile"),
    path("updatefound/<int:pk>",views.UpdateFoundData,name="updatefound"),
    path("deletefound/<int:pk>",views.DeleteFoundData,name="deletefound"),
    path("editfound/<int:pk>",views.editFoundpage,name="editfound"),
    path("editprofilepage/<int:pk>",views.editprofilepage,name="editprofilepage"),
    path("editprofileview/<int:pk>",views.editprofileview,name="editprofileview"),
]