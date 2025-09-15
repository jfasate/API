'''
This file is usually added in urls but to seperate out viewset routing we have added this file.
'''

from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet

router = DefaultRouter()
router.register('products-jayeshfasate', ProductViewSet, basename='products')
print(router.urls)
urlpatterns = router.urls