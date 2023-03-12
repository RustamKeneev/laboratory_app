from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Analyze(models.Model):
    class Meta:
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализы'

    title = models.CharField('Название', max_length=256)
    description = models.TextField('Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    parent_subcategory = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='child_subcategories')
    preparationForAnalysis = models.TextField('Подготовка к анализу')
    requirements = models.TextField('Требования')
    interpretationOfResults = models.TextField('Интерпретация результатов')
    laboratoryTest = models.CharField('Лабораторные тесты', max_length=500)
    biomaterial = models.TextField('Биоматериал')
    deadlineDateOfIssueOfResults = models.CharField('срок выполнения день, выдачи результатов', max_length=300)

    def __str__(self):
        return self.title


class Lab(models.Model):
    class Meta:
        verbose_name = 'Лаборатория'
        verbose_name_plural = 'Лаборатории'

    name = models.CharField(max_length=50)
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='laboratory/images')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон номер')
    address = models.CharField(max_length=200, verbose_name='Адрес аптеки')
    website = models.URLField(null=True, blank=True, verbose_name='Веб сайт (url)')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class PriceAnalyzeToLaboratory(models.Model):
    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    analyze = models.ForeignKey(Analyze, on_delete=models.CASCADE, related_name="lab_prices", blank=True)
    laboratory = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name="prices_lab", blank=True)
    price = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return f'{self.price}'
