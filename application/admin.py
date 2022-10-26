from django.contrib import admin
from application.models import Application_Form


class Application_FormAdmin(admin.ModelAdmin):
    list_display = ('child_full_name', 'cell_numbers', 'email_address', 'grade_applied_for', 'emergency_numbers', 'date_applied')
    list_display_links = ('child_full_name', 'cell_numbers', 'email_address', 'grade_applied_for',)
    search_fields = ('child_full_name', 'grade_applied_for', 'email_address', 'cell_numbers' )
    list_filter = ('grade_applied_for', 'date_applied' )
    list_per_page = 20

admin.site.register(Application_Form, Application_FormAdmin)




 