import requests
import json


header = {'User-Agent': 'api-test-agent'}
vacancy_id = 40847256
json_request = json.loads(requests.get(f'https://api.hh.ru/vacancies/{str(vacancy_id)}', header).text)

for elmnt in json_request:  #  Вариант без list comprehension, что лучше? И непонятно, где мы используем сам elmnt
    lst = '\n'.join(json_request)
print(f'То, что мы можем использовать вообще для поиска в каждой вакансии: \n{lst}')
        
'''
Даем пользователю выбрать на сайте:
    area - object Регион размещения вакансии(area.id string Идентификатор региона, area.name)
        Москва = 1, Санкт-П = 2, пока можно оставить только мск и питер
        https://api.hh.ru/areas
    salary — размер заработной платы;
        only_with_salary=true&salary=30000
    experience - object	Требуемый опыт работы.({"id":"between1And3","name":"От 1 года до 3 лет"});
        "experience":[{"id":"noExperience","name":"Нет опыта"},
        {"id":"between1And3","name":"От 1 года до 3 лет"},
        {"id":"between3And6","name":"От 3 до 6 лет"},
        {"id":"moreThan6","name":"Более 6 лет"}]
    key_skills - Информация о ключевых навыках, заявленных в вакансии. Список может быть пустым. [{"name":"Python"},{"name":"   "},{"name":"Flask"}];
        text = Python+Git+PostgreSQL+Django или Python+AND+somethng+OR+sddasdkdksa+OR+das
        GET /skills?id={id1}&id={id2}&id={id3}
    has_test - boolean Информация о наличии прикрепленного тестового задании к вакансии;
    не смог сделать нормальный запрос 


Не даем пользователю выбирать, но можем использоватьсами:
    name - string Название вакансии;
    type - object Тип вакансии. Элемент справочника vacancy_type({"id":"open","name":"Открытая"});
    address - object или null	Адрес вакансии;
    schedule — график работы.({"id":"remote","name":"Удаленная работа"});
    employment — тип занятости.({"id":"full","name":"Полная занятость"})??? Нужно ли вообще использовать?;
    description - Описание вакансии, содержит html;
    archived - Находится ли данная вакансия в архиве;
    employer - object	Короткое представление работодателя;
    published_at - string Дата и время публикации вакансии;
    apply_alternate_url - string Ссылка на отклик на вакансию на сайте;
    alternate_url - string Ссылка на представление вакансии на сайте;

Не используем вовсе:
    insider_interview - объект с информацией об интервью о жизни в компании или null, если для данной вакансии отсутствует интервью;
    response_letter_required - boolean Обязательно ли заполнять сообщение при отклике на вакансию;
    relations - array При авторизации соискателем, возвращает связи с вакансией;
    billing_type -  object Биллинговый тип вакансии. Элемент справочника vacancy_billing_type({"id":"standard","name":"Стандарт"});
    allow_messages - boolean Включена ли возможность соискателю писать сообщения работодателю, после приглашения/отклика на вакансию;
    department - Департамент, от имени которого размещается вакансия (если данная возможность доступна для компании);
    id
    premium
    site
    contacts - Контактная информация. Может быть Null; 
    branded_description - брендированое описание вакансии;
    vacancy_constructor_template - Нет описания.Null;
    accept_handicapped - Указание, что вакансия доступна для соискателей с инвалидностью;
    accept_kids - Указание, что вакансия доступна для детей;
    response_url - На вакансии с типом direct нельзя откликнуться на сайте hh.ru, 
    у этих вакансий в ключе response_url выдаётся URL внешнего сайта (чаще всего это сайт работодателя с формой отклика);
    specializations - array Специализации;
    code - Внутренний код вакансии работадателя;
    hidden - удалена ли вакансия (скрыта из архива);
    quick_responses_allowed - нет информации;
    driver_license_types - Список требуемых категорий водительских прав;
    accept_incomplete_resumes - Разрешен ли отклик на вакансию неполным резюме;
    created_at - Дата и время создания вакансии;
    negotiations_url - string	Cсылка для получения списка откликов/приглашений;
    suitable_resumes_url - string	Подходящие резюме на вакансию;
    test -  В данный момент отклик на вакансии с обязательным тестом через API невозможен;
    working_days - object или null Рабочие дни;
    working_time_intervals -  object или null	Временные интервалы работы;
    working_time_modes - object или null Режимы времени работы;
    accept_temporary - boolean или null	Указание, что вакансия доступна для соискателей с временным трудоустройством.
'''
