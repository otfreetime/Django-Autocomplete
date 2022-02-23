
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import ListOfUsers
        
def email_autocomplete(request):
    if request.GET.get('q'):
        q = request.GET['q']
        data = ListOfUsers.objects.using('legacy').filter(email__startswith=q).values_list('email',flat=True)
        json = list(data)
        return JsonResponse(json, safe=False)
    else:
        HttpResponse("No cookies")



# from django.shortcuts import render


# from django.http import HttpResponse


def page(request):
     return render(request,'inputpage/page.html')
# # # # Create your views here.
# # class EmailAutocomplete(autocomplete.Select2ListView):
# #     def get_list(self):
# #         qs = ListOfUsers.objects.using('legacy')

# #         if self.q:
# #             qs = qs.filter(email__icontains=self.q).values_list('email', flat=True)

# #         return qs