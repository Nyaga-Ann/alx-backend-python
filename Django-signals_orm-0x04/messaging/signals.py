from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.id is not None:
        try:
            old_message = Message.objects.get(id=instance.id)
            if old_message.content != instance.content:
                # Save the old content to the history
                MessageHistory.objects.create(
                    message=old_message,
                    old_content=old_message.content
                )
                # Mark message as edited
                instance.edited = True
        except Message.DoesNotExist:
            pass