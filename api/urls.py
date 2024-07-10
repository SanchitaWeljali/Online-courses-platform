from api.models import CourseResource, CategoryResource
from tastypie.api import Api
from django.urls import path, include

api = Api(api_name='v1')
api.register(CategoryResource())
api.register(CourseResource())

# /api/v1/courses/          GET, POST       All Courses
# /api/v1/cayegories/       GET             All Categories
# /api/v1/courses/3/        GET, DELETE     Single Course
# /api/v1/categories/2/     GET             Single Category

#For DELETE, POST requests enable authorization headers in postman 
#authentication Example: ApiKey admin:admin123
#created in django administration -> Api keys



urlpatterns = [
    path('', include(api.urls))
]