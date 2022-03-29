from django import forms
from django.contrib import admin


from .models import * #импортирование всех моделей


from ckeditor_uploader.widgets import CKEditorUploadingWidget #импортирование виджета редактора


class PostAdminForm(forms.ModelForm): #форма редактора
    post = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Posts
        fields = '__all__'


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'url', 'date') #оглавление в постах
    list_filter = ('category', ) #фильтры по категории
    search_fields = ('title', 'category__name') #поиск по названию и категории
    form = PostAdminForm
    fieldsets = (
        (None, {
            'fields': (('title', 'author', 'date'),)
        }),
        (None, {
            'fields': ('post', 'category')
        }),
        (None, {
            'fields': ('url', 'image')
        })
    )
#порядок вывода полей

#регистрация моделей в админке
admin.site.register(Category)
admin.site.register(Reviews)
admin.site.register(ReviewContact)
