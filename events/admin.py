from django.contrib import admin

from .models import Question


# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                {'fields': ['question_text']}),
        ('Date informatioin', {'fields': ['pub_date'], 'classes': ['collapse']}),
        (None,                {'fields': ['number']}),
        (None,                {'fields': ['difficulty']}),
        (None,                {'fields': ['method']}),
        (None,                {'fields': ['note']})
    ]

    list_display = ('question_text', 'number', 'difficulty', 'pub_date', 'was_published_recently', )
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
