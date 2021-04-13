import datetime

from parser_vacancies.models import Vacancies_count


def vacancies_counter(request):
    try:
        qs_counter = Vacancies_count.objects.filter(date=datetime.date.today()).values('added_today',
                                                                                       'total_vacancies_count')
        counter_today = qs_counter[0]['added_today']
        counter_total = qs_counter[0]['total_vacancies_count']
        counter = {
            'today': counter_today,
            'total': counter_total
        }
    except (SyntaxError, IndexError, TypeError):
        counter = {
            'today': 0,
            'total': 0
        }
    return counter
