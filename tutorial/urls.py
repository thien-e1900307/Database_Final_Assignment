"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'auth_group', views.AuthGroupViewSet)
router.register(r'auth_group_permissions', views.AuthGroupPermissionsViewSet)
router.register(r'auth_permission', views.AuthPermissionViewSet)
router.register(r'auth_user', views.AuthUserViewSet)
router.register(r'auth_user_groups', views.AuthUserGroupsViewSet)
router.register(r'auth_user_user_permissions', views.AuthUserUserPermissionsViewSet)
router.register(r'customers', views.CustomersViewSet)
router.register(r'django_admin_log', views.DjangoAdminLogViewSet)
router.register(r'django_content_type', views.DjangoContentTypeViewSet)
router.register(r'django_migrations', views.DjangoMigrationsViewSet)
router.register(r'django_session', views.DjangoSessionViewSet)
router.register(r'employee_privileges', views.EmployeePrivilegesViewSet)
router.register(r'employees', views.EmployeesViewSet)
router.register(r'inventory_transaction_types', views.InventoryTransactionTypesViewSet)
router.register(r'inventory_transactions', views.InventoryTransactionsViewSet)
router.register(r'invoices', views.InvoicesViewSet)
router.register(r'order_details', views.OrderDetailsViewSet)
router.register(r'order_details_status', views.OrderDetailsStatusViewSet)
router.register(r'orders', views.OrdersViewSet)
router.register(r'orders_status', views.OrdersStatusViewSet)
router.register(r'orders_tax_status', views.OrdersTaxStatusViewSet)
router.register(r'privileges', views.PrivilegesViewSet)
router.register(r'products', views.ProductsViewSet)
router.register(r'purchase_order_details', views.PurchaseOrderDetailsViewSet)
router.register(r'purchase_order_status', views.PurchaseOrderStatusViewSet)
router.register(r'purchase_orders', views.PurchaseOrdersViewSet)
router.register(r'sales_reports', views.SalesReportsViewSet)
router.register(r'shippers', views.ShippersViewSet)
router.register(r'strings', views.StringsViewSet)
router.register(r'suppliers', views.ShippersViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
