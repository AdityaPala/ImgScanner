from django.shortcuts import render
from django.urls import reverse_lazy
from SkewCorrector.models import Post
from django.views.generic import ListView, CreateView
from django.conf import settings
from skewCorrector import Correction
import cv2
import os
from django.http import HttpResponse

# Create your views here.
def home(request):
    path = 'media/media/aetna_rotated.png'
    img = cv2.imread(path)
    A = Correction(img)
    data = A.skewFix(img)
    cont = {
        'object_info': data
    }
    return render(request, 'corrected.html', cont)


class PostListView(ListView):
    model = Post
    template_name = 'home.html'


class PostCreateView(CreateView):
        model = Post
        fields = ['title', 'cover']
        print("in CreatePostView...")
        template_name = 'post_form.html'
        success_url = reverse_lazy('home')

# def img_post(request):
#     model = Post
#     return render(request, 'post.html')
