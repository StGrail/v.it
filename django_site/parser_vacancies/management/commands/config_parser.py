# Количество вакансий на одной странице
REQUEST_PER_PAGE = 10
# Количество запрашиваемых страниц
REQUEST_PAGE_COUNT = 5
# Базовый URL для запроса вакансий у api hh.ru
REQUEST_URL = f'https://api.hh.ru/vacancies?text=python&per_page={REQUEST_PER_PAGE}&page='
# Список обрабатываемых скиллов
PROCESSING_SKILLS = [
    'sql', 'linux', 'git', 'postgresql', 'django framework', 'django', 'flask',
    'css', 'html', 'bash', 'mysql', 'ооп', 'docker', 'mongodb', 'pandas',
    'numpy', 'atlassian jira', 'jira', 'kubernetes', 'http', 'tcp/ip',
    'trello', 'unix', 'redis'
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
