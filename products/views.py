from django.shortcuts import render
from django.http import HttpResponse
from openpyxl import Workbook
from .models import Product, Category, Size, Color

from openpyxl.drawing.image import Image as XLImage
from openpyxl.styles import Alignment
import os
from django.conf import settings


def export_products_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Products"

    # Заголовки
    headers = ["Code", "Name", "Description", "Price", "Image", "Categories", "Colors", "Sizes"]
    ws.append(headers)

    row_height = 200
    ws.row_dimensions[1].height = row_height  # заголовок

    row_num = 2
    for p in Product.objects.all():
        # ManyToMany поля
        categories = ", ".join([c.category for c in p.category.all()])
        colors = ", ".join([c.color for c in p.colors.all()])
        sizes = ", ".join([s.size for s in p.sizes.all()])

        # Додаємо текстові дані
        ws.cell(row=row_num, column=1, value=p.code)
        ws.cell(row=row_num, column=2, value=p.name)
        ws.cell(row=row_num, column=3, value=p.description)
        ws.cell(row=row_num, column=4, value=float(p.price))
        ws.cell(row=row_num, column=6, value=categories)
        ws.cell(row=row_num, column=7, value=colors)
        ws.cell(row=row_num, column=8, value=sizes)

        # Wrap text та вертикальне вирівнювання для всіх текстових колонок
        for col in ["A", "B", "C", "D", "F", "G", "H"]:
            ws[col + str(row_num)].alignment = Alignment(wrapText=True, vertical='center')

        # Додаємо фото у колонку E
        if p.image:
            image_path = os.path.join(settings.MEDIA_ROOT, p.image.name)
            if os.path.exists(image_path):
                img = XLImage(image_path)
                # Масштабування по висоті рядка з збереженням пропорцій
                aspect_ratio = img.width / img.height
                img.height = row_height
                img.width = int(row_height * aspect_ratio)
                ws.add_image(img, f"E{row_num}")

        # Встановлюємо висоту рядка
        ws.row_dimensions[row_num].height = row_height
        row_num += 1

    # Налаштування ширини колонок
    ws.column_dimensions["A"].width = 15
    ws.column_dimensions["B"].width = 25
    ws.column_dimensions["C"].width = 60  # опис
    ws.column_dimensions["D"].width = 12
    ws.column_dimensions["E"].width = 25  # картинка
    ws.column_dimensions["F"].width = 25
    ws.column_dimensions["G"].width = 25
    ws.column_dimensions["H"].width = 25

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response['Content-Disposition'] = 'attachment; filename="products.xlsx"'
    wb.save(response)
    return response

def product_list(request):
    # Отримуємо всі товари
    products = Product.objects.all().distinct()

    # Отримуємо списки для фільтрів
    categories = Category.objects.all()
    colors = Color.objects.all()
    sizes = Size.objects.all()

    # Перевіряємо GET-параметри для фільтру
    category_ids = request.GET.getlist('category')
    color_ids = request.GET.getlist('color')
    size_ids = request.GET.getlist('size')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Фільтруємо лише якщо користувач обрав параметри
    if category_ids:
        products = products.filter(category__id__in=category_ids)
    if color_ids:
        products = products.filter(colors__id__in=color_ids)
    if size_ids:
        products = products.filter(sizes__id__in=size_ids)
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Для ManyToMany потрібно distinct, щоб не втрачати товари
    products = products.distinct()

    context = {
        'products': products,
        'categories': categories,
        'colors': colors,
        'sizes': sizes,
    }

    return render(request, 'products/product_list.html', context)
# Create your views here.
