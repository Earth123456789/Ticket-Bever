# organizers/url.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from organizers.views import OrganizerRegisterView, DashBoardView


urlpatterns = [
    # Auth Path
    path("register/", OrganizerRegisterView.as_view(), name="organizer-register"),
    path("dashboard/<int:company_id>/", DashBoardView.as_view(), name="dashboard"),
] 

# ตั้งค่าเพื่อให้ใช้ รูปที่มาจาก media (imagefiled) ได้
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)