import config
import config_db
import psycopg2
from psycopg2.errors import UniqueViolation, InFailedSqlTransaction



con = psycopg2.connect(**config_db.DATABASE)
cur = con.cursor()
cur.execute("SELECT id_vacancy, key_skills FROM vacancies WHERE contains_skills = 'True'")
vacancies = cur.fetchall()
print(type(vacancies))
print(len(vacancies))

count = 0
skill_table_columns = config.SKILL_TABLE_COLUMNS.split()
for vacancy in vacancies:
    count  += 1
    sql_query_value = [str(count), str(vacancy[0])]
    for skill in skill_table_columns[2:]:
        if skill in vacancy[1]:
            sql_query_value.append('True')
        else:
            sql_query_value.append('False')
    sql_query_value = ','.join(sql_query_value)
    #print(config.SKILL_TABLE_COLUMNS)
    #print(sql_query_value)
    try:
        cur.execute(f'INSERT INTO skills ({config.SKILL_TABLE_COLUMNS}) VALUES ({sql_query_value})')
    except (UniqueViolation, InFailedSqlTransaction):
            #print('Значения в столбцах id и id_vacancy должны быть уникальными')
            continue
con.commit()
con.close()
