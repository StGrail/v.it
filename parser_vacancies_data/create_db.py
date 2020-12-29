import config
import psycopg2

con = psycopg2.connect(**config.DATABASE)
cur = con.cursor()
cur.execute("""
    CREATE TABLE vacancies(
    id INT PRIMARY KEY UNIQUE,
    id_vacancy INT NOT NULL UNIQUE,
    key_skills VARCHAR, 
    experience VARCHAR NOT NULL,
    salary_from INT,
    salary_to INT,
    name_vacancy VARCHAR NOT NULL,
    area VARCHAR NOT NULL,
    published VARCHAR NOT NULL,
    alternate_url VARCHAR NOT NULL,
    contains_skills BOOL NOT NULL);
    """)
cur.execute("""
    CREATE TABLE skills(
    id INT PRIMARY KEY UNIQUE,
    id_vacancy INT NOT NULL UNIQUE,
    sql BOOL NOT NULL,
    linux BOOL NOT NULL,
    git BOOL NOT NULL,
    postgresql BOOL NOT NULL,
    django BOOL NOT NULL,
    flask BOOL NOT NULL,
    css BOOL NOT NULL,
    html BOOL NOT NULL,
    bash BOOL NOT NULL,
    mysql BOOL NOT NULL,
    ооп BOOL NOT NULL,
    docker BOOL NOT NULL,
    mongodb BOOL NOT NULL,
    pandas BOOL NOT NULL,
    numpy BOOL NOT NULL,
    jira BOOL NOT NULL,
    kubernetes BOOL NOT NULL,
    http BOOL NOT NULL,
    tcp_ip BOOL NOT NULL,
    trello BOOL NOT NULL,
    unix BOOL NOT NULL,
    redis BOOL NOT NULL);
    """)
con.commit()
con.close()
