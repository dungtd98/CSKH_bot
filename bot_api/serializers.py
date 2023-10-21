from .models import (BotModel, 
                     BotModelSetting, 
                     BotStyle, 
                     BotMessageStyle, 
                     UserMessageStyle, 
                     boxChatStyle,
                     BotDatatrain)
from rest_framework import serializers
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
# BOT STYLE SERIALIZER
class UserMessageStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessageStyle
        exclude = ['style']

class BotMessageStyleSerialzier(serializers.ModelSerializer):
    class Meta:
        model = BotMessageStyle
        exclude = ['style']

class BoxChatStyleSerialzier(serializers.ModelSerializer):
    class Meta:
        model = boxChatStyle
        exclude = ['style']

class BotStyleSerializer(serializers.ModelSerializer):
    userMessage = UserMessageStyleSerializer()
    botMessage = BotMessageStyleSerialzier()
    boxChat = BoxChatStyleSerialzier()
    class Meta:
        model = BotStyle
        exclude = ['bot']
    
# BOT SETTING SERIALIZER   
class BotSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotModelSetting
        exclude = ['bot']

# BOT SERIALIZER
class BotSerializer(serializers.ModelSerializer):
    settings = BotSettingSerializer(required = False)
    styles = BotStyleSerializer(required = False)
    class Meta:
        model = BotModel
        fields = '__all__'
        
    def to_internal_value(self, data):
        # Đọc file đầu vào nếu là file upload .txt
        datatrain_input = data.get('datatrain')
        if isinstance(datatrain_input, (InMemoryUploadedFile, TemporaryUploadedFile)):
            if datatrain_input.content_type == 'text/plain':
                data['datatrain'] =datatrain_input.read().decode('utf-8')
        return super().to_internal_value(data)
    

    def create(self, validated_data):
        settings_input = validated_data.pop('settings',{})
        styles_input = validated_data.pop('styles',{})
        datatrain_input = validated_data.pop('datatrain',{})
        bot = BotModel.objects.create(**validated_data)
        # Handle setting create
        BotModelSetting.objects.create(bot=bot, **settings_input)
        # Handle style create
        style = BotStyle.objects.create(bot=bot)
        
        userMessageStyle_data = styles_input.pop('userMessage',{})
        UserMessageStyle.objects.create(style = style, **userMessageStyle_data)

        botMessageStyle_data = styles_input.pop('botMessage',{})
        BotMessageStyle.objects.create(style = style, **botMessageStyle_data)

        boxChatStyle_data = styles_input.pop('boxChat',{})
        boxChatStyle.objects.create(style=style, **boxChatStyle_data)
        # Handle create datatrain
        if datatrain_input!={}:
            BotDatatrain.objects.create(bot=bot, **datatrain_input)
        return bot 

    def update(self, instance, validated_data):
        setting_data = validated_data.pop('settings',{})
        styles_data = validated_data.pop('styles',{})
        datatrain_data = validated_data.pop('datatrain',{})
        setting_instance = instance.settings
        styles_instance = instance.styles
        if datatrain_data != {}:
            BotDatatrain.objects.create(bot=instance, **datatrain_data)
        # Update BOT instance
        instance.bot_name = validated_data.get('bot_name', instance.bot_name)
        instance.system_message = validated_data.get('system_message', instance.system_message)
        instance.save()
        # Update BOT setting
        setting_instance.is_public = setting_data.get('is_public', setting_instance.is_public)
        setting_instance.languageCode = setting_data.get('languageCode', setting_instance.languageCode)
        setting_instance.isMessage = setting_data.get('isMessage', setting_instance.isMessage)
        setting_instance.save()
        # Update BOT style
        # userMessage Style
        userMessageStyle_instance = styles_instance.userMessage
        userMessageStyle_data = styles_data.get('userMessage', {})
        userMessageStyle_instance.backgroundColor = userMessageStyle_data.get('backgroundColor',userMessageStyle_instance.backgroundColor)
        userMessageStyle_instance.color = userMessageStyle_data.get('color',userMessageStyle_instance.color)
        userMessageStyle_instance.save()
        # botMessage Style
        botMessageStyle_instance = styles_instance.botMessage
        botMessageStyle_data = styles_data.get('botMessage',{})
        botMessageStyle_instance.backgroundColor = botMessageStyle_data.get('backgroundColor',botMessageStyle_instance.backgroundColor)
        botMessageStyle_instance.color = botMessageStyle_data.get('color',botMessageStyle_instance.color)
        botMessageStyle_instance.save()
        # boxChat Style
        boxChatStyle_instance = styles_instance.boxChat
        boxChatStyle_data = styles_data.get('boxChat',{})
        boxChatStyle_instance.backgroundColor = boxChatStyle_data.get('backgroundColor',boxChatStyle_instance.backgroundColor)
        boxChatStyle_instance.title = boxChatStyle_data.get('title',boxChatStyle_instance.title)
        boxChatStyle_instance.subTitle = boxChatStyle_data.get('subTitle',boxChatStyle_instance.subTitle)
        boxChatStyle_instance.colorWidgetBg = boxChatStyle_data.get('colorWidgetBg',boxChatStyle_instance.colorWidgetBg)
        boxChatStyle_instance.save()
        return instance