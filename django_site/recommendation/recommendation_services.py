import math

from users.models import Vacancies, User
from parser_vacancies.models import Skills
from recommendation.config_recommendation import DEFAULT_SKILL_NAME, NUM_TOP_VACANCIES


def cos_distance(user_vector: list, vacancy_vector: list) -> float:
    """Функция, расчитывает косинусное расстояние между вектором скиллов юзера и вакансии """
    summ_user_i_vacancy_i = 0
    summ_user_i = 0
    summ_vacancy_i = 0
    for user, vacancy in zip(user_vector, vacancy_vector):
        user_vacancy = user*vacancy
        summ_user_i_vacancy_i += user_vacancy
        summ_user_i += user**2
        summ_vacancy_i += vacancy**2
    cos_similarity = summ_user_i_vacancy_i/(math.sqrt(summ_user_i)*math.sqrt(summ_vacancy_i))
    return 1 - cos_similarity


DEFAULT_SKILL_NAME = DEFAULT_SKILL_NAME
def create_user_skills_vector(user_skills: 'QuerySet') -> list:
    """Функция, которая формирует вектор скиллов юзера """
    user_skills_vector = []
    user_skills = list(user_skills)
    user_skills = user_skills[0]['skills'].lower()
    if not user_skills:
        return False
    for skill_name in DEFAULT_SKILL_NAME:
        if skill_name in user_skills:
            user_skills_vector.append(True)
        else:
            user_skills_vector.append(False)
    return user_skills_vector

def create_vacancies_vector(selected_vacancies: 'QuerySet') -> dict:
    """Функция, которая формирует вектор скиллов вакансии """
    vacancies_skills_vectors = {}
    vacancies = list(selected_vacancies)
    for vacancy in vacancies:
        vacancy_skills_vector = []
        vacancy_table_id = vacancy['id']
        vacancy_skills = list(Skills.objects.filter(id_vacancy_id=vacancy_table_id,
                                            ).values('sql', 'linux', 'git',
                                                        'postgresql', 'django', 
                                                        'flask', 'css', 'html', 
                                                        'bash', 'mysql', 'oop', 
                                                        'docker', 'mongodb', 
                                                        'pandas', 'numpy', 'jira', 
                                                        'kubernetes', 'http', 
                                                        'tcp_ip', 'trello', 'unix', 
                                                        'redis',
                                                    ))[0]
        for skill in DEFAULT_SKILL_NAME:
            if vacancy_skills[skill]:
                vacancy_skills_vector.append(True)
            else:
                vacancy_skills_vector.append(False)
        vacancies_skills_vectors[vacancy_table_id] = vacancy_skills_vector
    return vacancies_skills_vectors


def calculate_cosine_distance(vacancies_skills_vectors: dict, user_skill_vector: list) -> list:
    """
    Функция, которая формирует список рекомендованных вакансий, используя вектор скиллов юзера user_skill_vector и
    набор векторов вакансий vacancies_skills_vectors
    """
    cosine_distancies = {}
    for vacancy_table_id in vacancies_skills_vectors:
        cosine_distance = cos_distance(user_skill_vector, vacancies_skills_vectors[vacancy_table_id])
        cosine_distancies[vacancy_table_id] = cosine_distance
    sorted_vacancy_table_id = sorted(cosine_distancies, key=cosine_distancies.get)
    return sorted_vacancy_table_id
    

def recommendations(user_data: 'QuerySet') -> list:
    """Основная функция, принимающая на вход данные вакансии user_data и возвращающая список id рекомендованных вакансий"""
    user_skill_vector = create_user_skills_vector(user_data)
    user_area = list(user_data)[0]['area']
    user_experience = list(user_data)[0]['experience']
    user_salary = list(user_data)[0]['salary']
    if not user_skill_vector:
        return False
    else:
        selected_vacancies = Vacancies.objects.filter(area=user_area,
                                                    experience=user_experience,
                                                    contains_skills=True,
                                                    salary_from__lte=user_salary,
                                                    salary_to__gte=user_salary,
                                                    ).values('id')
        vacancies_skills_vectors = create_vacancies_vector(selected_vacancies)
        recommended_vacancies_id = calculate_cosine_distance(vacancies_skills_vectors, user_skill_vector)
        if len(recommended_vacancies_id) >= 5:
            return recommended_vacancies_id[:NUM_TOP_VACANCIES]
        else:
            return recommended_vacancies_id
