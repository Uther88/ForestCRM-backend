# Utilities
from .models import Message


# Message sender
def message_sender(sender, recipient, title, text, *args, **kwargs):
    message = Message.objects.create(
        title=title, text=text,
        sender=sender
    )
    message.recipient.add(recipient)