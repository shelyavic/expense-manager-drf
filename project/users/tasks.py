import datetime
from main.celery import app
from users.models import CustomUser
from users.serializers import UserStatisticsSerializer


def compose_email_body(data):
    return f"""Total expenses: {data['total_expenses']}
Total income: {data['total_income']}
Total expenses for the last 7 days: {data['last_week_expenses']}
Total income for the last 7 days: {data['last_week_income']}"""


@app.task
def send_statistics_by_email(user_id):
    user = CustomUser.objects.get(pk=user_id)
    message = compose_email_body(UserStatisticsSerializer(user).data)
    date_time_str = datetime.datetime.now().strftime("%d.%m.%y %H:%M")

    user.email_user(
        subject=f"Your statistics for {date_time_str}",
        message=message,
    )
    return f"Sent email to {user.email}"


@app.task
def distribute_email_tasks():
    users = CustomUser.objects.all()
    for user in users:
        send_statistics_by_email.delay(user.id)
    return "Email scheduling"
