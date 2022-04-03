from django.contrib import admin

from .models import Lead, Agent, User, UserProfile, Category


class LeadAdmin(admin.ModelAdmin):

    list_display = ["first_name", "last_name", "age"]
    list_display_links = ["first_name"]
    list_editable = ["last_name"]
    list_filter = ["category"]
    search_fields = ["first_name", "last_name"]


admin.site.register(User)
admin.site.register(Lead, LeadAdmin)
admin.site.register(Agent)
admin.site.register(UserProfile)
admin.site.register(Category)
# admin.site.register(FollowUp)
