import sqlite3


def get_from_db(sql):
    with sqlite3.connect("netflix.db") as connection:
        connection.row_factory = sqlite3.Row  # представление строк в строчном формате

        result = connection.execute(sql).fetchall()  #

        return result


def get_by_title(title):
    """
    функция, которая принимает title и возвращает  данные
    """
    sql = f'''
            select title, country, release_year, listed_in as genre, description
            from netflix
            where title = '{title}'
            order by release_year desc 
            limit 1
            '''

    result = get_from_db(sql)

    for item in result:
        return dict(item)


def get_by_release_year(year1, year2):
    """
        функция, которая принимает 2 года и возвращает  данные
    """
    sql = f'''
            select title, release_year
            from netflix
            where release_year between {year1} and {year2}
            limit 100
            '''

    result = get_from_db(sql)

    result_release_year = []
    for item in result:
        result_release_year.append(dict(item))
    return result_release_year


def get_by_rating(rating):
    """
    поиск по рейтингу
    """
    dict_rating = {
        "children": ("G"),
        "family": ("G", "PG", "PG-13"),
        "adult": ("R", "NC-17")
    }

    sql = f'''
            select title, rating, description
            from netflix
            where rating in {dict_rating.get(rating, ("G", "NC-17"))}  
            '''
    # dict_rating.get(rating, ("G", "NC-17")) через .get мы обрабатываем двойной параметр если совпадений не найдено по
    # первому аргументу, обращаемся ко второму аргументу по умолчанию

    result = get_from_db(sql)

    result_rating = []
    for item in result:
        result_rating.append(dict(item))
    return result_rating


def get_by_genre(genre):
    sql = f'''
            select title, description
            from netflix
            where listed_in like '%{str(genre)[1:]}%'
            order by release_year desc 
            limit 10
            '''
    #  {str(genre)[1:] игнорируем первый символ, на случай регистра

    result = get_from_db(sql)

    result_genre = []
    for item in result:
        result_genre.append(dict(item))
    return result_genre

















