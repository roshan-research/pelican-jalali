from pelican import signals
import jdatetime


def jalali(article_generator):
	for article in article_generator.dates:
		article.locale_date = jdatetime.datetime.fromgregorian(force_persian_output=True, datetime=article.date).strftime(article.date_format)


def register():
	signals.article_generator_finalized.connect(jalali)
