from pelican import signals
import khayyam
from datetime import datetime as dt

def jalali(content):
    content.date = khayyam.JalaliDatetime.from_datetime(content.date)
    content.date = dt.now()
    print content.date
    print '-------------------'

def register():
    signals.content_object_init.connect(jalali)
