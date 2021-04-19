# Количество вакансий на одной странице
REQUEST_PER_PAGE = 100
# Количество запрашиваемых страниц
REQUEST_PAGE_COUNT = 20
# Базовый URL для запроса вакансий у api hh.ru
REQUEST_URL = f'https://api.hh.ru/vacancies?text=python&area=1&per_page={REQUEST_PER_PAGE}&page='
REQUEST_URL_PERIOD = f'https://api.hh.ru/vacancies?text=python&area=1&period=1&per_page={REQUEST_PER_PAGE}&page='
# Список обрабатываемых скиллов
PROCESSING_SKILLS = [
    'sql', 'linux', 'git', 'postgresql', 'django framework', 'django', 'flask',
    'css', 'html', 'bash', 'mysql', 'ооп', 'docker', 'mongodb', 'pandas',
    'numpy', 'atlassian jira', 'jira', 'kubernetes', 'http', 'tcp/ip',
    'trello', 'unix', 'redis'
]
# Список для отбраковки вакансий по названию (с кириллическим вариантом "с")
NOT_PYTHON = [
    'c++', 'с++', 'unity', 'c', 'с', 'с#', 'c#', 'recruiter', 'sql', 'devops', 'ruby', 'voip', 'bim', 'php',
    'js', 'hr', 'flutter', 'android', 'ios', 'go', 'hadoop', 'rust', 'java', '.net', 'fiori', 'преподаватель',
]

# Минимальная длинна скилла
min_lenght_skill_letter = 0
for letter in PROCESSING_SKILLS:
    if len(letter) > min_lenght_skill_letter:
        min_lenght_skill_letter = len(letter)

# Названия столбцов таблицы вакансий
VACANCY_TABLE_COLUMNS = r"""
                    id, id_vacancy, key_skills, experience, salary_from,
                    salary_to, name_vacancy, area, published,
                    alternate_url, contains_skills
                    """

# Названия столбцов таблицы скиллов
SKILL_TABLE_COLUMNS = r"""
                    id, id_vacancy, sql, linux, git, postgresql, django, flask,
                    css, html, bash, mysql, ооп, docker, mongodb, pandas,
                    numpy, jira, kubernetes, http, tcp_ip, trello, unix, redis
                    """
