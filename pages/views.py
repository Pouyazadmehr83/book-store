# pages/views.py
from django.views.generic import TemplateView
from books.models import Book  # اضافه کن برای نمایش کتاب‌ها


class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular_books'] = Book.objects.all()[:6]  # 6 کتاب اول
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'