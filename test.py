from django.test import TestCase
from microservice.models import Article
from microservice.sorting_service import sort
from datetime import datetime

class ArticlesTestCase(TestCase):
    # def setUp(self):
    #     for book in Article.objects().all():
    #         book.delete()
    #     Article(title="A menina que roubava livros",
    #         author="Markus Zusak",
    #         edition_year=2005,
    #         created_at=datetime.now()).save()
    #     Article(title="O Senhor dos Anéis - As duas torres",
    #         author="J. R. R. Tolkien",
    #         edition_year=1949,
    #         created_at=datetime.now()).save()
    #     Article(title="O Senhor dos Anéis - A sociedade do anel",
    #         author="J. R. R. Tolkien",
    #         edition_year=1949,
    #         created_at=datetime.now()).save()
    #     Article(title="O Senhor dos Anéis - O retorno do Rei",
    #         author="J. R. R. Tolkien",
    #         edition_year=1949,
    #         created_at=datetime.now()).save()
    #
    # def test_sorting_by_title(self):
    #     sorted = sort("title")
    #     self.assertEqual(sorted[0].title, 'A menina que roubava livros')
    #     self.assertEqual(sorted[-1].title, 'O Senhor dos Anéis - O retorno do Rei')
    #
    # def test_sorting_by_author(self):
    #     sorted = sort("author")
    #     self.assertEqual(sorted[0].author, 'J. R. R. Tolkien')
    #     self.assertEqual(sorted[-1].author, 'Markus Zusak')
    #
    # def test_sorting_by_edition_year(self):
    #     sorted = sort("edition_year")
    #     self.assertEqual(sorted[0].edition_year, 1949)
    #     self.assertEqual(sorted[-1].edition_year, 2005)
    #
    # def test_creating_book(self):
    #     new_book = Article(title="As Crônicas de Nárnia",
    #         author="Clive Staples Lewis",
    #         edition_year=2000,
    #         created_at=datetime.now()).save()
    #     self.assertEqual(new_book, Article.objects(title = "As Crônicas de Nárnia").first())
