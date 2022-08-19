import json
import flask

from script_sql import get_by_title, get_by_release_year, get_by_rating, get_by_genre

app = flask.Flask(__name__)


@app.get("/movie/<title>")
def view_title(title):
    result = get_by_title(title)
    return app.response_class(
        response=json.dumps(result,
                            ensure_ascii=False,  # чтобы отображались русские символы
                            indent=4  # отступ в пробелах
                            ),
        status=200,  # все успешно
        mimetype="application/json"  # возвращаем JSON
    )


@app.get("/movie/<int:year1>/to/<int:year2>")
def view_release_year(year1, year2):
    result = get_by_release_year(year1, year2)
    return app.response_class(
        response=json.dumps(result,
                            ensure_ascii=False,  # чтобы отображались русские символы
                            indent=4  # отступ в пробелах
                            ),
        status=200,  # все успешно
        mimetype="application/json"  # возвращаем JSON
    )


@app.get("/rating/<rating>")
def view_rating(rating):
    result = get_by_rating(rating)
    return app.response_class(
        response=json.dumps(result,
                            ensure_ascii=False,  # чтобы отображались русские символы
                            indent=4  # отступ в пробелах
                            ),
        status=200,  # все успешно
        mimetype="application/json"  # возвращаем JSON
    )


@app.get("/genre/<genre>")
def view_genre(genre):
    result = get_by_genre(genre)
    return app.response_class(
        response=json.dumps(result,
                            ensure_ascii=False,  # чтобы отображались русские символы
                            indent=4  # отступ в пробелах
                            ),
        status=200,  # все успешно
        mimetype="application/json"  # возвращаем JSON
    )


if __name__ == '__main__':
    app.run(debug=True)  # что бы не перезагружать постоянно
