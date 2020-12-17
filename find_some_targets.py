import requests
import json


first_20 = requests.get('https://api.hh.ru/vacancies?text=python').text
first_20_json = json.loads(first_20)
only_one_job = first_20_json['items'][0]

items = []
for keys in only_one_job.keys():
    items.append(keys)

lst = ''
for i in items:
    lst += i + '\n'
print(f'То, что мы можем использовать вообще для поиска вакансий: \n{lst}')


'''
Используем:

    id - string нужен для перехода в "тело" вакансии  https://github.com/hhru/api/blob/master/docs/vacancies.md;
    name - string	Название вакансии;
    area - object	Регион размещения вакансии (имеет несколько параметров);
    salary - object или null Оклад (имеет несколько параметров, По умолчанию будут также найдены вакансии, 
        в которых вилка зарплаты не указана, чтобы такие вакансии отфильтровать, используйте only_with_salary=true);
    published_at - string Дата и время публикации вакансии;
    archived - boolean Находится ли данная вакансия в архиве;
    alternate_url - Ссылка на представление вакансии на сайте;
    snippet - объект Дополнительные текстовые снипеты (отрывки) по найденной вакансии (snippet.requirement строка - 
        Отрывок из требований по вакансии, если они найдены в тексте описания.);
    contacts - 	object или null Контактная информация;

Возможно используем:

    has_test - boolean	Информация о наличии прикрепленного тестового задании к вакансии;
    response_letter_required - boolean Обязательно ли заполнять сообщение при отклике на вакансию;
    type - object Тип вакансии. Элемент справочника (имеет несколько параметров);
    address - object или null Адрес вакансии;
    response_url - string или null На вакансии с типом direct нельзя откликнуться на сайте hh.ru, 
        у этих вакансий в ключе response_url выдаётся URL внешнего сайта (чаще всего это сайт 
        работодателя с формой отклика);
    employer - object Короткое представление работодателя;
    apply_alternate_url - string Ссылка на отклик на вакансию на сайте;
    schedule - график работы;
    working_days - object или null	Рабочие дни. Элемент справочника working_days;
    accept_temporary - boolean или null	Указание, что вакансия доступна для соискателей с временным трудоустройством.


Не используем:

    premium - boolean Является ли данная вакансия премиум-вакансией;
    department - Департамент, от имени которого размещается вакансия;
    sort_point_distance - число, null Расстояние в метрах между центром сортировки 
        (заданной параметрами sort_point_lat, sort_point_lng) и указанным в вакансии адресом;
    created_at - string	Дата и время создания вакансии;
    insider_interview - объект с информацией об интервью о жизни в компании или null, 
        если для данной вакансии отсутствует интервью;
    relations - array При авторизации соискателем, возвращает связи с вакансией;
    working_time_intervals - object или null Временные интервалы работы. Элемент справочника working_time_intervals;
    working_time_modes - object или null Режимы времени работы. Элемент справочника working_time_modes;
'''
