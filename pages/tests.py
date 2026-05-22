# pages/tests.py
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView  # اضافه کردن AboutPageView

class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')  # گرفتن URL مربوط به name='home'
        self.response = self.client.get(url)  # ارسال درخواست GET به آن URL

    def test_homepage_status_code(self):
        # بررسی می‌کند که صفحه کد وضعیت 200 (OK) برگردانده باشد
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        # بررسی می‌کند که از قالب 'home.html' استفاده شده باشد
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        # بررسی می‌کند که صفحه حاوی کلمه 'Homepage' باشد
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        # بررسی می‌کند که صفحه حاوی متن مشخص شده نباشد
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.'
        )

    def test_homepage_url_resolves_homepageview(self):
        # بررسی می‌کند که URL '/' به درستی به View مورد نظر متصل شده باشد
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')  # گرفتن URL مربوط به name='about'
        self.response = self.client.get(url)  # ارسال درخواست GET به آن URL

    def test_aboutpage_status_code(self):
        # بررسی می‌کند که صفحه کد وضعیت 200 (OK) برگردانده باشد
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        # بررسی می‌کند که از قالب 'about.html' استفاده شده باشد
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        # بررسی می‌کند که صفحه حاوی 'About Page' باشد
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        # بررسی می‌کند که صفحه حاوی متن مشخص شده نباشد
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.'
        )

    def test_aboutpage_url_resolves_aboutpageview(self):
        # بررسی می‌کند که URL '/about/' به درستی به View مورد نظر متصل شده باشد
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )