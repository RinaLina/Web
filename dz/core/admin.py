from django.contrib import admin

from core.models import Book, User


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author', 'publisher')
    list_display = ('title', 'author', 'publisher')


admin.site.register(Book, BookAdmin)
admin.site.register(User)
