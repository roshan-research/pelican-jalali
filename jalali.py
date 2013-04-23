from pelican import signals
import khayyam


def jalali(content):
    content.locale_date = khayyam.JalaliDatetime.from_datetime(content.date).strftime(content.date_format)


def register():
    signals.content_object_init.connect(jalali)
