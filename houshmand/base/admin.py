from django.contrib import admin
from .models import Articles,roadmaps,films

# Register your models here.
from .models import Room,Topic,Messages
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Messages)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    # def category_to_str(self, obj):
    #     return "، ".join([category.title for category in obj.category.all()])
    # category_to_str.short_description = "دسته بندی"
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(roadmaps)
admin.site.register(films)