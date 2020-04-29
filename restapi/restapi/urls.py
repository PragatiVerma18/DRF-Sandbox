from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from updates.views import(
    update_model_detail_view,
    JsonCBV,
    JsonCBV2,
    SerializedListView,
    SerializedDetailView
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/updates/', include('updates.api.urls')),
    url(r'^api/status/', include('status.api.urls')),
    # url(r'^json/cbv/$', JsonCBV.as_view()),
    # url(r'^json/cbv2/$', JsonCBV2.as_view()),
    # url(r'^json/example/$', update_model_detail_view),
    # url(r'^json/serialized/list/$', SerializedListView.as_view()),
    # url(r'^json/serialized/details/$', SerializedDetailView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

