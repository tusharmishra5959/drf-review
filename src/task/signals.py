from django.db.models.signals import post_save
from django.dispatch import receiver

from task.models import COMPLETE, NOT_COMPLETE, Task


@receiver(post_save, sender=Task)
def update_house_points(sender, instance, created, **kwargs):
    """."""

    house = instance.task_list.house
    if instance.status == COMPLETE:
        house.points += 10
    elif instance.status == NOT_COMPLETE:
        if house.points > 10:
            house.points -= 10
    house.save()


@receiver(post_save, sender=Task)
def update_tasklist_status(sender, instance, created, **kwargs):
    task_list = instance.task_list
    is_complete = True
    for task in task_list.tasks.all():
        if task.status != COMPLETE:
            is_complete = False
            break
    if is_complete:
        task_list.status = COMPLETE
    else:
        task_list.status = NOT_COMPLETE
    task_list.save()