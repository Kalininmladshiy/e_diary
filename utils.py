import random
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def fix_marks(fio):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=fio)
        child = schoolkid.full_name
        Mark.objects.filter(schoolkid__full_name=full_name, points__in=[2, 3]).update(points=5)
    except ObjectDoesNotExist:
        print('Ученик не найден')
    except MultipleObjectsReturned:
        print('Найдено более одного ученика')    

def remove_chastisement(fio):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=fio)
        child = schoolkid.full_name
        chastisements = Chastisement.objects.filter(schoolkid__full_name=child)
        for chastisement in chastisements:
            chastisement.delete()        
    except ObjectDoesNotExist:
        print('Ученик не найден')
    except MultipleObjectsReturned:
        print('Найдено более одного ученика')


def create_commendation(fio):
    with open('commendations.txt') as file:
        commendations = list(map(str.strip, file.readlines()))
    commendation = random.choice(commendations)
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=fio)
        subjects = Subject.objects.filter(year_of_study=schoolkid.year_of_study)
        subject = random.choice(subjects).title
        lessons = Lesson.objects.filter(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,
            subject__title=subject,
         )
        teachers = list({lesson.teacher for lesson in lessons})
        teacher = random.choice(teachers)
        date = Lesson.objects.filter(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,
            subject__title=subject,
            teacher__full_name=teacher,
             ).order_by('date').last().date
        teacher = Teacher.objects.filter(full_name__contains=teacher)[0]
        subject = Subject.objects.filter(title=subject, year_of_study=schoolkid.year_of_study)[0]
        Commendation.objects.create(
            text=commendation,
            created=date,
            schoolkid=schoolkid,
            subject=subject,
            teacher=teacher
         )
    except ObjectDoesNotExist:
        print('Ученик не найден')
    except MultipleObjectsReturned:
        print('Найдено более одного ученика')        
