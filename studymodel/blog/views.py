from django.shortcuts import render,redirect
from .models import Blog
from .forms import BlogForms

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})

def new(request):
    if request.method == 'POST':
        forms = BlogForms(request.POST)

        if forms.is_valid:
            #내가 폼 안에 입력한 데이터가 올바른가(유효성 검사를 통과하면 다 저장해라)
            #저장한 내용은 blog라는 model의 객체(새 글)로 저장됨 
            forms.save()
            return redirect('home')
            # return render(request,'home.html')
    forms = BlogForms()
    return render(request,'new.html',{'forms':forms})