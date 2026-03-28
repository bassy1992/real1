from django.db.models.signals import pre_delete, post_delete, pre_save
from django.dispatch import receiver
from django.conf import settings
from .models import PropertyImage
import logging

logger = logging.getLogger(__name__)


@receiver(pre_save, sender=PropertyImage)
def delete_old_image_on_update(sender, instance, **kwargs):
    """
    Delete old image from DigitalOcean Spaces when a new image is uploaded.
    This prevents orphaned files in storage.
    """
    if not instance.pk:
        # New instance, no old image to delete
        return
    
    if not settings.USE_SPACES:
        return
    
    try:
        old_instance = PropertyImage.objects.get(pk=instance.pk)
        
        # Check if the image field has changed
        if old_instance.image and old_instance.image != instance.image:
            # Delete the old image file
            if old_instance.image.storage.exists(old_instance.image.name):
                old_instance.image.storage.delete(old_instance.image.name)
                logger.info(f"Deleted old image from Spaces: {old_instance.image.name}")
    except PropertyImage.DoesNotExist:
        pass
    except Exception as e:
        logger.error(f"Error deleting old image from Spaces. Error: {str(e)}")


@receiver(pre_delete, sender=PropertyImage)
def delete_image_from_spaces(sender, instance, **kwargs):
    """
    Delete image file from DigitalOcean Spaces when PropertyImage is deleted.
    This runs before the database record is deleted.
    """
    if instance.image and settings.USE_SPACES:
        try:
            # Delete the file from storage (DigitalOcean Spaces)
            if instance.image.storage.exists(instance.image.name):
                instance.image.storage.delete(instance.image.name)
                logger.info(f"Deleted image from Spaces: {instance.image.name}")
        except Exception as e:
            logger.error(f"Error deleting image from Spaces: {instance.image.name}. Error: {str(e)}")


@receiver(post_delete, sender=PropertyImage)
def log_image_deletion(sender, instance, **kwargs):
    """
    Log when an image is successfully deleted.
    """
    logger.info(f"PropertyImage deleted: {instance.property.title} - Image {instance.order}")
