from django.contrib import admin

import book


class BookStoreAdminSite(admin.AdminSite):
    site_header = "Book store app"
    site_title = "Book Store"
    index_title = "Book Store admin interface"
