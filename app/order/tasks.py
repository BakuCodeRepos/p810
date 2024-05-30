from celery import shared_task


@shared_task
def send_sms_when_status_changed():
    print('Sms is sending...')
