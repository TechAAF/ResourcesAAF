from django.contrib import admin
from contests.models import Contest, Category, Submission

class Contest_Admin(admin.ModelAdmin):
    filter_horizontal = ('category',)


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'contest')
    readonly_fields = ('user_id', 'contest', 'caption', 'likes', 'image', 'image_id','date')
    
admin.site.register(Contest, Contest_Admin)
admin.site.register(Category)
admin.site.register(Submission, SubmissionAdmin)

