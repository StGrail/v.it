import config
import psycopg2




def check_skills_in_vacancy(vacancy):
    check_list = []
    id_vacancy = vacancy[0]
    skills_str = vacancy[1]
    skills_list = skill_str.split(',')
    table_columns = config.SKILL_TABLE_COLUMNS
    table_columns_list = table_columns.split(',')
    for table_column in table_columns_list:
        for skill in skills_list:
            

    

count = 0
con = psycopg2.connect(**config.DATABASE)
cur = con.cursor()
cur.execute("SELECT id_vacancy, key_skills FROM vacancies WHERE contains_skills = 'True'")
vacancies = cur.fetchall()
for vacancy in vacancies:
    id_vacancy = row[0]
    skill_str = row[1]
    skills_list = skill_str.split(',')
    for skill in skills_list:
        print(skill, end=' ')
        if skill in table_columns:
            print(skill)
        else:
            print('None')