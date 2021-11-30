from random import randint, choice
from datacenter.models import (
    Schoolkid, Mark, Chastisement, Lesson, Commendation
)


PRAISES = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!',
]


def get_schoolkid(name_pattern='Фролов Иван'):
    kid = Schoolkid.objects.filter(full_name__contains='Фролов Иван').get()
    return kid


def fix_marks(schoolkid):
    Mark.objects.filter(
        schoolkid=schoolkid,
        points__in=[2, 3],
    ).update(points=randint(4, 5))


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def commendation(schoolkid):
    last_lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title='Музыка'
    ).order_by('-date')[0]
    Commendation.objects.create(
        schoolkid=schoolkid,
        created=last_lesson.date,
        teacher=last_lesson.teacher,
        subject=last_lesson.subject,
        text=choice(PRAISES),
    )
