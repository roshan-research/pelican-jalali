from pelican import signals
import khayyam


def jalali(article_generator):
    # content.locale_date = khayyam.JalaliDatetime.from_datetime(content.date).strftime(content.date_format)
    for article in article_generator.dates:
        article.locale_date = khayyam.JalaliDatetime.from_datetime(article.date).strftime(article.date_format)


def register():
    signals.article_generator_finalized.connect(jalali)
