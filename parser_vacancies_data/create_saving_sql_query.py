import config

def change_format_skills(skills):
    '''
    Принимает на входе словарь, содержащий скиллы вакансии.
    Возвращает строку скиллов, необходимую для SQL команды на запись в БД
    '''
    skills_str = ''
    for skill in skills:
        name_skill = skills[skill].lower() + ','
        skills_str += name_skill
    return skills_str[:-1]


def get_vacancy_data(id_vacancy, skills, vacancy):
    '''
    Принмает на вход id вакансии, словарь скиллов, полное представление вакансии также ввиде словаря.
    Возвращает словарь вакансий, которые будут записаны в таблицу vacancies БД.
    '''
    vacancy_data = {'id_vacancy': id_vacancy}
    skills_str = change_format_skills(skills)
    vacancy_data['skills'] = skills_str
    vacancy_data['experience'] = vacancy['experience']['name'].lower()
    if vacancy['salary'] and vacancy['salary']['from']:
        vacancy_data['salary_from'] = vacancy['salary']['from']
    else:
        vacancy_data['salary_from'] = ''
    if vacancy['salary'] and vacancy['salary']['to']:
        vacancy_data['salary_to'] = vacancy['salary']['to']
    else:
        vacancy_data['salary_to'] = ''
    vacancy_data['name'] = vacancy['name']
    vacancy_data['area'] = vacancy['area']['name']
    vacancy_data['published'] = vacancy['published_at'] # - сделать запись в формате data
    vacancy_data['alternate_url'] = vacancy['alternate_url']
    return vacancy_data


def create_SQL_query(vacancy_data):
    '''
    Принимает на вход счетчик вакансий и словарь значений, которые необходимо записать в таблицу vacancies БД.
    Возвращает кортеж, состоящий из двух строк: название колонок таблицы vacancies и значения соответствущих колонок
    '''
    table_columns = config.VACANCY_TABLE_COLUMNS
    values = ''
    if not vacancy_data['skills']:
        table_columns = table_columns.replace('key_skills, ', '')
    if not vacancy_data['salary_from']:
        table_columns = table_columns.replace('salary_from, ', '')
    if not vacancy_data['salary_to']:
        table_columns = table_columns.replace('salary_to, ', '')
    for key in vacancy_data:
        if vacancy_data[key]:
            values = values + f"'{vacancy_data[key]}', "
    values = f'{values}{True}'
    return table_columns, values