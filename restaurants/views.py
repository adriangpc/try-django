from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view
# def home(request):
#     html_var = 'nestle strings'
#     html_ = f"""<!DOCTYPE html>
#     <head>
#     </head>
#     <body>
#     <h1>Hello World!</h1>
#     <p>This is {html_var} coming through!</p>
#     </body>
#     </html>
#     """
#     return HttpResponse(html_)

def home(request):
    return render(request, "base.html", {"html_var": "Insert text here"})