from django.contrib import admin
from .models import Notice,Course,Contact,Feedback_Rating,Employee,Student,Event,Consultancy,Student_Feedback_Rating
#admin panel customization
class Course_Admin(admin.ModelAdmin):
    list_display = ('course_name','course_fees','course_duration')
    list_filter = ['course_fees','course_duration']
    search_fields = ('course_name',)

class Employee_Admin(admin.ModelAdmin):
    list_display = ('name','email','phone','designation')
    list_filter = ['designation']




# Register your models here.
admin.site.register(Notice)
admin.site.register(Course,Course_Admin)
admin.site.register(Contact)
admin.site.register(Feedback_Rating)
admin.site.register(Employee,Employee_Admin)
admin.site.register(Student)
admin.site.register(Event)
admin.site.register(Consultancy)
admin.site.register(Student_Feedback_Rating)








admin.site.site_header = "CollegePortalAdministration"
admin.site.site_title = "CollegeAdminDashBoard"
admin.site.index_title = "CollegeAdmin"