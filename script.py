from random import randint, choice

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from datacenter.models import (
    Schoolkid,
    Mark,
    Chastisement,
    Lesson,
    Commendation
)


def find_schoolkid(name_pattern):
    try:
        return Schoolkid.objects.get(full_name__contains=name_pattern)
    except Schoolkid.MultipleObjectsReturned:
        print('Нашлось больше одного ученика, уточните запрос')
    except Schoolkid.DoesNotExist:
        print('Такой ученик не найден, уточните запрос')


def fix_marks(schoolkid):
    Mark.objects.filter(
        schoolkid=schoolkid,
        points__in=[2, 3],
    ).update(points=randint(4, 5))


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def add_random_commendation(schoolkid, subject_title):
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
    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject_title,
    ).order_by('?')
    if not lessons:
        return print('Такого предмета нет, повторите запрос')
    lesson = lessons.first()
    Commendation.objects.create(
            text=choice(PRAISES),
            created=lesson.date,
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher,
        )


if __name__ == '__main__':
    print('Не запускайте скрипт напрямую, импортируйте необходимые функции')
