import os.path
import sys
from pathlib import Path
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import CartoonForm
from .models import CartoonModel
from django.views.generic import DetailView
from subprocess import run, PIPE


# class EmpImageDisplay(DetailView):
#     model = CartoonModel
#     template_name = 'emp_image_display.html'
#     context_object_name = 'emp'
#
#
# class EmployeeImage(TemplateView):
#     form = CartoonForm
#     template_name = 'create_cartoon/upload.html'
#
#     def post(self, request, *args, **kwargs):
#         form = CartoonForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return render(request, form)
#         context = self.get_context_data(form=form)
#         return self.render_to_response(context)
#
#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)

# print(Path(__file__).resolve().parent.parent)
# BASE_DIR = Path(__file__).resolve().parent.parent
# path = os.path.join(BASE_DIR, 'media\images')
# print(path)

def home_view(request):
    context = {}
    if request.method == "POST":
        form = CartoonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data['img']
            BASE_DIR = Path(__file__).resolve().parent.parent
            path = os.path.join(BASE_DIR, 'media', str(subject))
            out = run([sys.executable, 'C:\\cpp\\js\\django\\cartoon\\cartoonize.py', path, str(subject)], shell=False, stdout=PIPE)
            # print(subject)
            extension = os.path.splitext(path)[1]
            string = "cartoonified_Image" + extension
            return render(request, 'create_cartoon/result.html', {'data1': string})
    else:
        form = CartoonForm()
    context['form'] = form
    return render(request, "create_cartoon/index.html", context)