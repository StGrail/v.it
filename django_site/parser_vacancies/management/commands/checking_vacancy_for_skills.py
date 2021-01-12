from bs4 import BeautifulSoup
from parser_vacancies.management.commands import config_parser


def processing_long_skill_name(skill_list):
    for skill in skill_list:
        if skill in config_parser.PROCESSING_SKILLS:
            return skill


def is_skill_in_list(vacancy):
    '''
    Функция принимает на вход полное представление вакансии в виде словаря. 
    Возвращает словарь скиллов, содержащихся в ключевых навыках и описании вакансии
    '''
    contains_skills = False
    skills = {
            'sql': False,
            'linux': False,
            'git': False,
            'postgresql': False,
            'django': False,
            'flask': False,
            'css': False,
            'html': False,
            'bash': False,
            'mysql': False,
            'oop': False,
            'docker': False,
            'mongodb': False,
            'pandas': False,
            'numpy': False,
            'jira': False,
            'kubernetes': False,
            'http': False,
            'tcp_ip': False,
            'trello': False,
            'unix': False,
            'redis': False,
            }
    vacancy_skill_list = vacancy['key_skills']
    for skill_dict in vacancy_skill_list:
        skill = skill_dict['name'].lower()
        skill_list = skill.split()
        if len(skill_list) > 1:
            skill = processing_long_skill_name(skill_list)
        else:
            skill = skill_list[0]
        if skill in config_parser.PROCESSING_SKILLS:
            skills[skill] = True
            contains_skills = True
    description = vacancy['description']
    description = BeautifulSoup(description, 'html.parser').text.lower()
    for skill in config_parser.PROCESSING_SKILLS:
        if description.find(skill) != -1:
            skills[skill] = True
    return skills, contains_skills      
