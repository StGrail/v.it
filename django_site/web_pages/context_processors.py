from datetime import date

from parser_vacancies.models import VacanciesCount


def vacancies_counter(request):
    try:
        qs_counter = VacanciesCount.objects.filter(date=date.today()).values('added_today',
                                                                             'total_vacancies_count')
        counter_today = qs_counter[0]['added_today']
        counter_total = qs_counter[0]['total_vacancies_count']
        counter = {
            'today': counter_today,
            'total': counter_total
        }
    except (SyntaxError, IndexError, TypeError) as e:
        print(e)
        counter = {
            'today': 0,
            'total': 0
        }
    return counter
