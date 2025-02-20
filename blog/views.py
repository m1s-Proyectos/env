from django.shortcuts import render, redirect
from django.views import View
from .forms import PostCreateForm
from .models import Post


class BlogListView(View):



    def get(self, request, *args, **kwargs):  # 🔹 Método GET para listar los posts
        posts = Post.objects.all()  # Obtiene todos los posts de la base de datos
        context = {'posts': posts}  # 🔹 Se corrigió la indentación
        return render(request, 'blog_list.html', context)



class BlogCreateView(View):
    def get(self, request, *args, **kwargs):  # 🔹 Método GET para mostrar el formulario de creación
        form = PostCreateForm()
        context = {
            'form': form  # Pasa el formulario al contexto
        }
        return render(request, 'blog_create.html', context)

    def post(self, request, *args, **kwargs):  # 🔹 Método POST para procesar la creación de un nuevo post
        if request.method == "POST":  # 🔹 Comprobación de si el método es POST
            form = PostCreateForm(request.POST)  # Inicializamos el formulario con los datos de la solicitud POST
            if form.is_valid():  # Si el formulario es válido
                title = form.cleaned_data.get('title')  # Extraemos el título
                content = form.cleaned_data.get('content')  # Extraemos el contenido

                post, created = Post.objects.get_or_create(title=title, content=content)  # 🔹 Crea el post si no existe
                post.save()  # Guardamos el post

                return redirect('blog:home')  # Redirige a la página de inicio del blog después de guardar

        else:
            form = PostCreateForm()  # 🔹 Si no es POST, inicializa un formulario vacío

        context = {'form': form}  # 🔹 Incluye el formulario en el contexto para mostrar errores en la plantilla
        return render(request, 'blog_create.html', context)


class blogDetailView(View):

 #   def get(self, request, *args, **kwargs):  # 🔹 Método GET para listar los posts
      #  posts = get_object_or_404(Post, pk=pk)  # Obtiene todos los posts de la base de datos
      #  context = {'posts': posts}  # 🔹 Se corrigió la indentación
      #  return render(request, 'blog_detail.html', context)


 def get(self, request, id, *args, **kwargs):
        post = Post.objects.get(id=id)  # Obtiene el post por su ID
        context = {'post': post}
        return render(request, 'blog_detail.html', context)