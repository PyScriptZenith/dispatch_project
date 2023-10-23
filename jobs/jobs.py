from datetime import datetime, timedelta
from dateutil.parser import *
from django.core.mail import send_mail
from config import settings
from dispatch.models import Dispatch, Logs


def send_messages():

    current_time = datetime.now()
    for dispatch in Dispatch.objects.filter(status='создана'):
        is_dispatched = False
        emails = [dispatch.client.email]
        attempt_status = 'success'
        server_response = 'Email sent successfully'
        messages = dispatch.messages.all()

        start_time_str = dispatch.start_time.strftime("%Y-%m-%d %H:%M:%S")
        end_time_str = dispatch.end_time.strftime("%Y-%m-%d %H:%M:%S")



        if dispatch.frequency == 'раз в день' and \
                parse(start_time_str).timestamp() < current_time.timestamp() < parse(end_time_str).timestamp():
            dispatch.start_time = dispatch.start_time + timedelta(days=1)
            dispatch.end_time = dispatch.end_time + timedelta(days=1)
            is_dispatched = True
            print('Блок if отработал: отправлена 1 дневная рассылка')


        elif dispatch.frequency == 'раз в неделю' and \
                parse(start_time_str).timestamp() < current_time.timestamp() < parse(end_time_str).timestamp():
            dispatch.start_time = dispatch.start_time + timedelta(days=7)
            dispatch.end_time = dispatch.end_time + timedelta(days=7)
            is_dispatched = True
            print('Блок if отработал: отправлена 7 дневная рассылка')

        elif dispatch.frequency == 'раз в месяц' and \
                parse(start_time_str).timestamp() < current_time.timestamp() < parse(end_time_str).timestamp():
            dispatch.start_time = dispatch.start_time + timedelta(days=30)
            dispatch.end_time = dispatch.end_time + timedelta(days=30)
            is_dispatched = True
            print('Блок if отработал: отправлена 30 дневная рассылка')


        if is_dispatched:
            dispatch.save()
            for message in messages:
                try:
                    send_mail(
                        subject=message.title,
                        message=message.message,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=emails
                    )
                except Exception as e:

                    attempt_status = 'error'
                    server_response = str(e)

                finally:

                    Logs.objects.create(server_response=server_response,
                                        dispatch=dispatch,
                                        status=attempt_status,
                                        last_attempt=current_time)












































#
# def send_messages():
#
#     current_time = datetime.now()
#     for dispatch in Dispatch.objects.filter(status='создана'):
#         is_dispatched = False
#         emails = [client.email for client in dispatch.client.all()]
#         attempt_status = 'success'
#         server_response = 'Email sent successfully'
#         messages = dispatch.messages.all()
#
#         start_time_str = dispatch.start_time.strftime("%Y-%m-%d %H:%M:%S")
#         end_time_str = dispatch.end_time.strftime("%Y-%m-%d %H:%M:%S")
#
#
#         if dispatch.frequency == 'Раз в день':
#                 # and parse(start_time_str).timestamp() < current_time.timestamp() < parse(end_time_str).timestamp():
#             dispatch.start_time = dispatch.start_time + timedelta(days=1)
#             is_dispatched = True
#             print('Блок if отработал')

        # elif mailing.frequency == 'weekly' and day_start == current_datetime.day \
        #         and current_datetime.hour == hour_start and current_datetime.minute == minut_start:
        #     mailing.start_time = mailing.start_time + timedelta(days=7)
        #     is_mailing = True
        #
        # elif mailing.frequency == 'monthly' and month_start == current_datetime.month \
        #         and day_start == current_datetime.day \
        #         and current_datetime.hour == hour_start and current_datetime.minute == minut_start:
        #     mailing.start_time = mailing.start_time + timedelta(days=30)
        #     is_mailing = True

        # if is_dispatched:
        #     dispatch.save()
        #     for message in messages:
        #         try:
        #
        #             send_mail(
        #                 subject=message.title,
        #                 message=message.message,
        #                 from_email=settings.EMAIL_HOST_USER,
        #                 recipient_list=emails
        #             )
        #
        #         except Exception as e:
        #
        #             attempt_status = 'error'
        #             server_response = str(e)

                # finally:
                #
                #     Log.objects.create(message=message,
                #                        status=attempt_status,
                #                        response=server_response)


# current = datetime.datetime.now()
#         mes_start_time_str = mes_start_time.strftime("%Y-%m-%d %H:%M:%S")
#         mes_end_time_str = mes_end_time.strftime("%Y-%m-%d %H:%M:%S")
#         print(f'Время начала отправки рассылки {mes_start_time_str}')
#         print(f'Время окончания отправки рассылки {mes_end_time_str}')
#         print(current)
#
#         # if current.timestamp() > parse(mes_end_time_str).timestamp():
#         if parse(mes_start_time_str).timestamp() < current.timestamp() < parse(mes_end_time_str).timestamp():
#             send_mail(
#                 subject=message.title,
#                 message=message.message,
#                 from_email=settings.EMAIL_HOST_USER,
#                 recipient_list=['p3triv4nov91@yandex.ru'],
#             )