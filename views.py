import json

from script_sql import get_from_db


def more_than_twice(name1="Jack Black", name2="Dustin Hoffman"):
    sql = f'''
                select title, "cast"
                from netflix
                where "cast" like '%{name1}%' and "cast" like '%{name2}%'
            '''

    result = get_from_db(sql)

    tmp = []
    names_dict = {}
    for item in result:
        names = set(dict(item).get("cast").split(", ")) - set([name1, name2])

        for name in names:
            names_dict[name.strip()] = names_dict.get(name.strip(), 0) + 1  # 1:00:00

    for key, values in names_dict.items():
        if values > 2:
            tmp.append(key)

    return tmp


def type_of_painting(typ, year, genre):
    sql = f'''
            select * from netflix
            where type = '{typ}' and
            release_year = {year} and
            listed_in like '%{genre}%'
            '''

    result = get_from_db(sql)

    tmp = []
    for item in result:
        tmp.append(dict(item))

    return json.dumps(tmp,
                      ensure_ascii=False,  # чтобы отображались русские символы
                      indent=4  # отступ в пробелах
                      )

#  types='TV Show', year=2020, genre='Dramas'

print(type_of_painting(typ='TV Show', year=2020, genre='ramas'))
