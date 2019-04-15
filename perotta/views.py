from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from .forms import SellBookForm


# Create your views here.
class IndexView(generic.ListView):

    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created_at')


def add(request):
    # 送信内容を基にフォームを作る。POSTじゃなければ、空のフォーム
    form = SellBookForm(request.POST or None)

    # method=POST、送信時に入力に誤りなければ

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('perotta:index')

    # 通常時のアクセスや、入力に誤りがあればページを表示

    context = {
    'form':form

    }
    return render(request, 'perotta/post_form.html', context)

# landing_pageを見せる。
class TemplateView(generic.TemplateView):

    template_name = 'perotta/landing_page.html'
