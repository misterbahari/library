
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path('', include('members.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # path('', include('kotob.urls')),
    # path('admin/', admin.site.urls),
]
