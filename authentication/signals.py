from django.db.models.signals import post_save, pre_save
from .models import Account, Profile
from django.dispatch import receiver
from django.core.files.storage import default_storage
import os


# https://stackoverflow.com/questions/62633525/
# how-to-delete-old-profile-picture-when-upload-a-new-one-django

# https://pythonguides.com/python-get-filename-from-the-path/

@receiver(pre_save, sender=Profile)
def delete_old_profile_file(sender, instance, **kwargs):
    # on creation, signal callback won't be triggered
    if instance._state.adding and not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).image.url
        # old_file_name, old_file_ext = os.path.splitext(old_file)
        # print(old_file_name, old_file_ext)
    except sender.DoesNotExist:
        return False

    # comparing the new file with the old one
    file = instance.image.url

    # determining base directory where file is present
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if not old_file == file and not old_file == '/media/default.png':
        # print("building path to old file from", base_dir)
        full_old_file_path = os.path.join(base_dir, old_file[1:])
        # print("old file detected at", old_file)
        # print("Is the old file found:", os.path.isfile(full_old_file_path))
        # print("old file found at", full_old_file_path)
        # print("deleting old file...")
        if os.path.isfile(full_old_file_path):
            os.remove(full_old_file_path)
            # print("old file successfully deleted.")


@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(account=instance)


@receiver(post_save, sender=Account)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
