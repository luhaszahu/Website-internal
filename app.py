from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "LeMansRaceWinners.db"


def create_connection(db_filename):
    try:
        connection = sqlite3.connect(db_filename)
        return connection
    except Error as e:
        print(e)
        return None


@app.route('/')
def render_home_page():  # put application's code here
    return render_template('index.html')


@app.route('/display/<table_type>')
def render_display_page(table_type):  # put application's code here

    query = "SELECT Years, Drivers, Class, Team, Car, Tyre, Laps, Km, Mi, Series, Driver_nationality, Team_nationality, Average_speed_kmh, Average_speed_mph, Average_lap_time FROM LeMans_Winners WHERE Driver_nationality = ?"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, (table_type, ))

    data_list = cursor.fetchall()

    return render_template('display.html', data=data_list, page_title=table_type)


@app.route('/display_full')
def render_display_full_page():  # put application's code here
    query = "SELECT Years, Drivers, Class, Team, Car, Tyre, Laps, Km, Mi, Series, Driver_nationality, Team_nationality, Average_speed_kmh, Average_speed_mph, Average_lap_time FROM LeMans_Winners"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()

    return render_template('displayFull.html', data=data_list)


@app.route('/search', methods=['GET', 'POST'])
def render_search_page():  # put application's code here

    look_up = request.form['Search']
    title = "Search for: '" + look_up + "' "
    look_up = "%" + look_up + "%"

    query = "SELECT Years, Drivers, Class, Team, Car, Tyre, Laps, Km, Mi, Series, Driver_nationality, Team_nationality, Average_speed_kmh, Average_speed_mph, Average_lap_time FROM LeMans_Winners WHERE Years LIKE ? OR Drivers LIKE ? OR Class LIKE ? OR TEAM LIKE ? OR Car LIKE ? OR Tyre LIKE ? OR LAPS LIKE ? OR Km LIKE ? OR Mi LIKE ? OR Series LIKE ? OR Driver_nationality LIKE ? OR Team_nationality LIKE ? OR Average_speed_kmh LIKE ? OR Average_speed_mph LIKE ? OR Average_lap_time LIKE ?"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, (look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up))

    data_list = cursor.fetchall()

    return render_template('display.html', data=data_list, page_title=title)


if __name__ == '__main__':
    app.run()
