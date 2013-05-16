from pelican import signals
import sjdatetime


def jalali(article_generator):
    for article in article_generator.dates:
        article.locale_date = sjdatetime.datetime.fromgregorian(force_persian_output=True, datetime=article.date).strftime(article.date_format)
        article.date = sjdatetime.datetime.fromgregorian(force_persian_output=False, datetime=article.date)


def register():
    signals.article_generator_finalized.connect(jalali)
