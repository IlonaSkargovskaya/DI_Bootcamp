from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render # this line is added automatically
# from django.http import HttpResponse # pass view information into the browser
from datetime import date
from .models import Post, Person, Email, Category
from .forms import CategoryForm, PostForm, SearchForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView #шаблон для функций с формами
from django.urls import reverse_lazy #
from django.views.generic import ListView #альтернатива для posts
from django.db.models import Q #дя поиска по всем полям

#чтобы в форме сделать значение по умолчанию выводим его в глобальную
current_user = Person.objects.get(first_name = 'Ben')

def add_post_view(request):

    if request.method == 'POST':
        data = request.POST
        filled_form = PostForm(data)
        # сохраняем в БД
        filled_form.save()

    #GET
    post_form = PostForm(initial = {'title' : 'post!',
                                    'content' : 'whatever',
                                    'author' : current_user})
    context = {'form' : post_form}

    return render(request, 'posts/add_post.html', context)


#alternative class add_post_view
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/add_post.html'
    #редирект на add_post (имя из urls)
    success_url = reverse_lazy('add_post')

    #утсанавливаем данные по умолчанию для полей
    def get_initial(self):
        return {'title' : 'post!',
                'content' : 'whatever',
                'author' : current_user
                }

    #контроль как форма будет submitted
    def form_valid(self, form):
        #cleaned_data. - берет данные из формы и трансформирует в понятные python
        #получаем поле из формы name
        title = form.cleaned_data.get('title')
        
        if title =='Fantasy':
            form.instance.name = 'FANTASY 1000' #form.instance - объект который мы редактируем
        return super().form_valid(form) # super() - ссылка на родительский класс(CreateView)










def add_category_view(request):

    if request.method == 'POST':
        data = request.POST
        filled_form = CategoryForm(data)
        # сохраняем в БД
        filled_form.save()

    #GET
    category_form = CategoryForm()
    context = {'form' : category_form}

    return render(request, 'posts/add_category.html', context)


#alternative generic view
class AddCategoryView(CreateView):
    model = Category
    #можно добавлять сразу fields из model
    # fields = ['name']
    # можно добавлять просто форму
    form_class = CategoryForm
    template_name = 'posts/add_category.html'
    #редирект на add_category (имя из urls)
    success_url = reverse_lazy('add_category')


    #контроль как форма будет submitted
    def form_valid(self, form):
        #cleaned_data. - берет данные из формы и трансформирует в понятные python
        #получаем поле из формы name
        name = form.cleaned_data.get('name')
        
        if name =='Fantasy':
            form.instance.name = 'FANTASY 1000' #form.instance - объект который мы редактируем
        return super().form_valid(form) # super() - ссылка на родительский класс(CreateView)



def posts(request):

    # поиск
    query = request.GET.get('query', None)
    if query:
        posts_all = Post.objects.filter(title__icontains = query)
    else:
        posts_all = Post.objects.all()

    search_form = SearchForm()
    posts_all = Post.objects.all()
    context = {'post_list': posts_all, 'search' : search_form}
    
    return render(request, 'posts/posts.html', context)


#альтернатива для posts view
class PostList(ListView):
    model = Post
    template_name = 'posts/posts.html'
    #говорим что хотим чтобы ключ в context был 'post_list'
    context_object_name = 'post_list'

    #отслеживаем запрос в строке который отправил пользователь
    def get_queryset(self):

        query = self.request.GET.get('query', None) #
        if query:
            posts_all = Post.objects.filter(Q(title__icontains = query) | Q(author__first_name__icontains = query))
        else:
            posts_all = Post.objects.all()

        return posts_all #что будет использовано как post_list

    #добавляем search и изменяем context чтобы добавить второй ключ search
    def get_context_data(self, **kwargs: Any):
        #получаем текущий контекст
        context = super().get_context_data(**kwargs)
        search_form = SearchForm()
        #обновляем контекст и добавляем search
        context['search'] = search_form

        return context






def profile(request):
    username = 'John'
    age = 15
    hobbies = ['Tennis', 'Music', 'Computer games']

    context = {
        'name' : username,
        'age' : age,
        'hobbies_list' : hobbies,
        'gendre': 'F'

    }

    return render(request, 'posts/profile_user.html', context)


# def about(request):
#     return HttpResponse("<h1>Welcome Users</h1>")

def profile_user(request):

    
    addresses = Person.objects.get(location = 'Petah Tikva')
    user_email = current_user.email

    context = {'user': current_user, 'email': user_email, 'location': addresses}

    return render(request, 'posts/profile.html', context)