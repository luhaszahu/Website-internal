from flask import Flask, render_template
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


@app.route('/webpages')
def render_webpages_page():  # put application's code here

    query = "SELECT Years, Drivers, Class, Team, Car, Tyre, Laps, Km, Mi, Series, Driver_nationality, Team_nationality, Average_speed_kmh, Average_speed_mph, Average_lap_time FROM LeMans_Winners WHERE Years >= 2000"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()

    return render_template('webpages.html', data=data_list)


@app.route('/styles')
def redner_styles_page():  # put application's code here


    query = "SELECT Years, Drivers, Class, Team, Car, Tyre, Laps, Km, Mi, Series, Driver_nationality, Team_nationality, Average_speed_kmh, Average_speed_mph, Average_lap_time FROM LeMans_Winners WHERE Years <= 1999"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()

    return render_template('webpages.html', data=data_list)



if __name__ == '__main__':
    app.run()
