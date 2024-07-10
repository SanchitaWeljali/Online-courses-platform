from tastypie.resources import ModelResource
from shop.models import Category, Course
from .authentication import CustomApiKeyAuthentication
from tastypie.authorization import Authorization

#api/categories respond with array of all categories
#api/course/1/ for specific course

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']
        
class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get','delete','post']
        authentication = CustomApiKeyAuthentication()
        authorization = Authorization()
        
    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle
    
    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return bundle
    
    def dehydrate_title(self, bundle):
        return bundle.data['title'].upper()