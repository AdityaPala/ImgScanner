from django.shortcuts import render
from django.urls import reverse_lazy
from SkewCorrector.models import Post
from django.views.generic import ListView, CreateView
from django.conf import settings
from skewCorrector import Correction
import cv2
import os
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'home.html'


class PostCreateView(CreateView):
        model = Post
        fields = ['title', 'cover']
        print("in CreatePostView...")
        template_name = 'post_form.html'
        #success_url = reverse_lazy('home')

        def form_valid(self, form):
            self.object = form.save()
            print("form=", form)
            print ("self.model.title=", self.model.title)
            print("self.model.cover=", self.model.cover)
            print(form['cover'])
            A = Correction(self.object.cover.url)
            A.skewFix(self.object.cover.url)
            return HttpResponseRedirect(self.get_success_url())

# def img_post(request):
#     model = Post
#     return render(request, 'post.html')
