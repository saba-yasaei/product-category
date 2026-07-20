from django.test import TestCase
from django.urls import reverse

from .models import Category, Product, Tag


class ProductModelTests(TestCase):
    def test_string_representations(self):
        category = Category.objects.create(name="Electronics")
        tag = Tag.objects.create(name="Featured")
        product = Product.objects.create(
            name="Phone",
            description="A compact smartphone",
            category=category,
        )

        self.assertEqual(str(category), "Electronics")
        self.assertEqual(str(tag), "Featured")
        self.assertEqual(str(product), "Phone")


class ProductListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.electronics = Category.objects.create(name="Electronics")
        cls.books = Category.objects.create(name="Books")
        cls.featured = Tag.objects.create(name="Featured")
        cls.sale = Tag.objects.create(name="Sale")

        cls.phone = Product.objects.create(
            name="Phone",
            description="A compact smartphone",
            category=cls.electronics,
        )
        cls.phone.tags.add(cls.featured, cls.sale)

        cls.novel = Product.objects.create(
            name="Novel",
            description="A historical story",
            category=cls.books,
        )
        cls.novel.tags.add(cls.featured)

    def setUp(self):
        self.url = reverse("product_list")

    def test_lists_all_products(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(
            response.context["products"],
            [self.phone, self.novel],
            ordered=False,
        )
        self.assertEqual(len(response.context["products"]), 2)
        self.assertContains(response, "products found.")

    def test_searches_descriptions_case_insensitively(self):
        response = self.client.get(self.url, {"search": "SMARTPHONE"})

        self.assertQuerySetEqual(response.context["products"], [self.phone])
        self.assertEqual(response.context["search_query"], "SMARTPHONE")

    def test_filters_by_category_and_retains_selection(self):
        selected_category = str(self.books.pk)

        response = self.client.get(
            self.url,
            {"category": selected_category},
        )

        self.assertQuerySetEqual(response.context["products"], [self.novel])
        self.assertEqual(
            response.context["selected_category"],
            selected_category,
        )

    def test_filters_by_any_selected_tag_and_retains_selections(self):
        selected_tags = [str(self.sale.pk), str(self.featured.pk)]

        response = self.client.get(self.url, {"tags": selected_tags})

        self.assertQuerySetEqual(
            response.context["products"],
            [self.phone, self.novel],
            ordered=False,
        )
        self.assertEqual(response.context["selected_tags"], selected_tags)

    def test_combines_search_category_and_tag_filters(self):
        response = self.client.get(
            self.url,
            {
                "search": "compact",
                "category": str(self.electronics.pk),
                "tags": str(self.sale.pk),
            },
        )

        self.assertQuerySetEqual(response.context["products"], [self.phone])

    def test_displays_empty_state(self):
        response = self.client.get(self.url, {"search": "missing"})

        self.assertQuerySetEqual(response.context["products"], [])
        self.assertEqual(len(response.context["products"]), 0)
        self.assertContains(response, "products found.")
        self.assertContains(response, "No products found.")
