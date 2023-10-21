from django.contrib import admin
from .models import BotModel, BotModelSetting, BotStyle, BotMessageStyle, UserMessageStyle, boxChatStyle
# Register your models here.


for model in [BotModel, BotModelSetting, BotStyle, BotMessageStyle, UserMessageStyle, boxChatStyle]:
    admin.site.register(model)