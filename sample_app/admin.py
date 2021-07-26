from django.contrib import admin

from .models import Student, Subject


class SubjectInline(admin.TabularInline):
    model = Subject
    insert_after = 'name'


class StudentAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'department',
        'gender',

    )
    inlines = [
        SubjectInline,
    ]
    change_form_template = 'admin/custom/change_form.html'

    class Media:
        css = {
            'all': (
                'css/admin.css',
            )
        }


admin.site.register(Student, StudentAdmin)
