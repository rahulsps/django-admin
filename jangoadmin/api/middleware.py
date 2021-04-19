from django.utils.deprecation import MiddlewareMixin 
class DisableCsrf(MiddlewareMixin):
    def process_request(self,request):
        setattr(request,"_dont_enforce_csrf_check",True)
class DisableCors(MiddlewareMixin):
    def process_response(self,request,response):
        response['Access-Control-Allow-Origin']="*"
        response['Access-Control-Allow-Headers']="*"
        return response  