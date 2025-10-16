from django.contrib import admin
from django.urls import path, include

# from django.conf import settings
# from django.conf.urls.static import static
# from django.conf.urls import handler403, handler404
# from bolnogledachi_bg.core.views import \
#     custom_404, custom_403, custom_500


urlpatterns = [
    # path('admin/', admin.site.urls),
    
    path('', include('bolnogledachi_bg.core.urls'))
]

handler404 = 'bolnogledachi_bg.core.views.custom_404'
handler403 = 'bolnogledachi_bg.core.views.custom_403'
handler500 = 'bolnogledachi_bg.core.views.custom_500'

# # Serve media files during development (Make sure `MEDIA_URL` and `MEDIA_ROOT` are set correctly in settings.py)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     # urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]