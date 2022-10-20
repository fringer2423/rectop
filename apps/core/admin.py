from django.contrib import admin
from .models import User, Company, Schedule, Branch, Telebot, QRCode, Connect, Review, ReviewSettings, Answer, \
    WorkDay, Rate, RateInfo

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Schedule)
admin.site.register(Branch)
admin.site.register(Telebot)
admin.site.register(QRCode)
admin.site.register(Connect)
admin.site.register(Review)
admin.site.register(ReviewSettings)
admin.site.register(Answer)
admin.site.register(WorkDay)
admin.site.register(Rate)
admin.site.register(RateInfo)
