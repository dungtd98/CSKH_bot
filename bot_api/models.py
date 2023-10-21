from django.db import models
import uuid
from django.contrib.auth import get_user_model
# Create your models here.
UserModel = get_user_model()
class BotModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bot_name = models.CharField(max_length=255, unique=True, blank=False, null=False, verbose_name="Tên bot")
    created_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='bots', verbose_name='Người tạo bot')
    created_at = models.DateTimeField(auto_now_add=True)
    system_message = models.TextField(blank=True)
    # Bot settings
    def __str__(self) -> str:
        return self.bot_name
# BOT SETTING
class BotModelSetting(models.Model):
    bot = models.OneToOneField(BotModel, on_delete=models.CASCADE, related_name='settings',primary_key=True)
    is_public = models.BooleanField(default=False, help_text='False: Privatebot, True: Publicbot')
    languageCode = models.CharField(max_length=10, verbose_name='Ngôn ngữ')
    isMessage = models.TextField(blank=True)
    def __str__(self) -> str:
        return f'{self.bot.bot_name}_SETTING'

# BOT STYLE  
class BotStyle(models.Model):
    bot = models.OneToOneField(BotModel, on_delete=models.CASCADE, related_name='styles',primary_key=True)
    def __str__(self) -> str:
        return f'{self.bot.bot_name}_STYLE'
    
class UserMessageStyle(models.Model):
    style = models.OneToOneField(BotStyle, on_delete=models.CASCADE, related_name='userMessage', primary_key=True)
    backgroundColor = models.CharField(max_length=10, default='')
    color = models.CharField(max_length=10, default='')
    def __str__(self) -> str:
        return f'{self.style.bot}_USER_MESSAGE'
    
class BotMessageStyle(models.Model):
    style = models.OneToOneField(BotStyle, on_delete=models.CASCADE, related_name='botMessage', primary_key=True)
    backgroundColor = models.CharField(max_length=10, default='')
    color = models.CharField(max_length=10, default='')
    def __str__(self) -> str:
        return f'{self.style.bot}_BOT_MESSAGE'
    
class boxChatStyle(models.Model):
    style = models.OneToOneField(BotStyle, on_delete=models.CASCADE, related_name='boxChat', primary_key=True)
    backgroundColor = models.CharField(max_length=10, default='')
    title = models.CharField(max_length=255, blank=False)
    subTitle = models.TextField(blank=True)
    colorWidgetBg = models.CharField(max_length=10, default='')
    def __str__(self) -> str:
        return f'{self.style.bot}_BOX_CHAT'

# Bot dataset
class BotDatatrain(models.Model):
    bot = models.ForeignKey(BotModel, on_delete=models.CASCADE, related_name='datatrains')
    datatrain = models.TextField(blank=True)
    def __str__(self) -> str:
        return f'{self.bot.bot_name}_DATATRAIN'

