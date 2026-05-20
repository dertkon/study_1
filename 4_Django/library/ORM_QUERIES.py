from datetime import datetime

from django.db.models import Count, Avg, F, Q
from .models import Author, Book, Review


# 1. Найди всех авторов с именем «John»
authors_named_john = Author.objects.filter(first_name='John')
print(authors_named_john)

# 2. Найди всех авторов, кроме тех, у кого фамилия «Doe»
authors_not_doe = Author.objects.exclude(last_name='Doe')
print(authors_not_doe)

# 3. Найди все книги, цена которых меньше 500
price_lt_fivehund = Book.objects.filter(price__lt=500)
print(price_lt_fivehund)

# 4. Найди все книги с ценой не более 300
price_lte_threehund = Book.objects.filter(price__lte=300)
print(price_lte_threehund)

# 5. Найди все книги дороже 1000
price_gt_onek = Book.objects.filter(price__gt=1000)
print(price_gt_onek)

# 6. Найди все книги с ценой от 750 и выше
price_gte_sevenfift = Book.objects.filter(price__gte=750)
print(price_gte_sevenfift)

# 7. Найди все книги, содержащие слово «django» в названии
django_name = Book.objects.filter(title__contains='django')
print(django_name)

# 8. Найди книги, в названии которых есть «python» (без учёта регистра)
python_name = Book.objects.filter(title__icontains='python')
print(python_name)

# 9. Найди книги, название которых начинается со слова «Advanced»
advanced_name = Book.objects.filter(title__startswith='Advanced')
print(advanced_name)

# 10. Найди книги, название которых начинается с «pro» (игнорируя регистр)
pro_name = Book.objects.filter(title__istartswith='Pro')
print(pro_name)

# 11. Найди книги, название которых заканчивается на слово «Guide»
guide_name = Book.objects.filter(title__endswith='Guide')
print(guide_name)

# 12. Найди книги, название которых заканчивается на «tutorial» (без учёта регистра)
tutorial_name = Book.objects.filter(title__iendswith='Tutorial')
print(tutorial_name)

# 13. Найди все отзывы без комментариев
has_no_comments = Review.objects.filter(Q(comment__isnull=True) |
                                        Q(comment=''))
print(has_no_comments)

# 14. Найди все отзывы, у которых есть комментарий
has_comments = Review.objects.exclude(Q(comment__isnull=True) |
                                     Q(comment=''))
print(has_comments)

# 15. Найди авторов с идентификаторами 1, 3 и 5
find_author = Author.objects.filter(id__in=[1, 3, 5])
print(find_author)

# 16. Найди книги, опубликованные с 1 января по 31 декабря 2023 года
find_book = Book.objects.filter(
    published_date__range=(datetime(2023, 1, 1),
                         datetime(2023, 12, 31))
)
print(find_book)

# 17. Найди книги, название которых начинается со слова «Python».
python_name = Book.objects.filter(title__startswith='Python')
print(python_name)

# 18. Найди авторов, чья фамилия начинается на «Mc» (игнорируя регистр).
mc_name = Author.objects.filter(last_name__istartswith='Mc')
print(mc_name)

# 19. Найди книги, опубликованные в 2024 году
find_twootwofour = Book.objects.filter(published_date__year=2024)
print(find_twootwofour)

# 20. Найди книги, опубликованные в июне
find_june = Book.objects.filter(published_date__month=6)
print(find_june)

# 21. Найди отзывы, оставленные 11-го числа любого месяца
review_eleven = Review.objects.filter(created_at__day=11)
print(review_eleven)

# 22. Найди книги, опубликованные на 23-й неделе года
book_week = Book.objects.filter(published_date__week=23)
print(book_week)

# 23. Найди отзывы, оставленные во вторник
tuesday_review = Review.objects.filter(created_at__week_day=3)
print(tuesday_review)

# 24. Найди книги, опубликованные во втором квартале года
second_quarter_book = Book.objects.filter(published_date__quarter=2)
print(second_quarter_book)

# 25. Найди отзывы, сделанные в определённую дату (например взял 2026-05-19)
review_date = Review.objects.filter(created_at__date='2026-05-19')
print(review_date)

# 26. Найди отзывы, сделанные ровно в 15:30
review_time = Review.objects.filter(created_at__hour=15, created_at__minute=30)
print(review_time)

# 27. Найди отзывы, сделанные в 15 часов
review_hour = Review.objects.filter(created_at__hour=15)
print(review_hour)

# 28. Найди отзывы, сделанные в 30 минут любого часа
review_minutes = Review.objects.filter(created_at__minute=30)
print(review_minutes)

# 29. Найди отзывы, созданные в момент, когда секунды были равны 0
review_secs = Review.objects.filter(created_at__second=0)
print(review_secs)

# 30. Найди книги, написанные автором с почтой «author@example.com»
book_mail = Book.objects.filter(author__email='author@example.com')
print(book_mail)
# ИЛИ БЕЗ N+1
book_mail_select = Book.objects.select_related('author').filter(
    author__email='author@example.com')
print(book_mail_select)

# 31. Найди книги авторов, чья фамилия содержит «smith» (без учёта регистра)
book_author_smith = Book.objects.filter(author__last_name__icontains='Smith')
print(book_author_smith)
# ИЛИ БЕЗ N+1
book_author_smith_select = Book.objects.select_related('author').filter(
    author__last_name__icontains='Smith')
print(book_author_smith_select)

# 32. Найди авторов, написавших более пяти книг
five_books_author = Author.objects.annotate(book_count=Count('books')).filter(
    book_count__gt=5)
print(five_books_author)

# 33. Найди книги, у которых значение ключа «genre» равно «fiction»
json_genre_fiction = Book.objects.filter(metadata__genre='fiction')
print(json_genre_fiction)

# 34. Найди книги, где значение ключа «tags» содержит слово «bestseller» (игнорируя регистр)
json_tags_bestseller = Book.objects.filter(metadata__tags__icontains='bestseller')
print(json_tags_bestseller)

# 35. Найди книги, у которых цена равна скидке
price_eq_disc = Book.objects.filter(price=F('discount'))
print(price_eq_disc)

# 36. Найди книги, у которых цена больше скидки
price_gt_disc = Book.objects.filter(price__gt=F('discount'))
print(price_gt_disc)

# 37. Найди авторов с именем «Alice» или с фамилией, не равной «Brown»
books_alice = Author.objects.filter(Q(first_name='Alice') | ~Q(last_name='Brown'))
print(books_alice)

# 38. Подсчитай количество книг каждого автора
book_counter = Author.objects.annotate(book_count=Count('books'))
for author in book_counter:
    print(author.first_name, author.last_name, author.book_count)

# 39. Подсчитай средний рейтинг каждой книги
avg_rating = Book.objects.annotate(avg=Avg('reviews__rating'))
for book in avg_rating:
    print(book.title, book.avg)

# 40. Посчитай окончательную цену книги (цена минус скидка)
price_minus_disc = Book.objects.annotate(final_price=F('price') - F('price') * F('discount') / 100)
for book in price_minus_disc:
    print(book.title, book.final_price)

# 41. Получи список книг и авторов так, чтобы выполнить всего один SQL-запрос
book_list = Book.objects.select_related('author').all()
for book in book_list:
    print(book.title, book.author)

# 42. Получи список авторов и всех их книг так, чтобы было выполнено ровно два SQL-запроса.
author_list = Author.objects.prefetch_related('books')
for author in author_list:
    print(author.first_name, author.last_name)
    for book in author.books.all():
        print(book.title)
