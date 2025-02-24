import os
import re
from datetime import datetime

from flask import Flask, render_template, request, flash, redirect, url_for

from config.db_config import Config
from models.models import PlateSchedule, db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.secret_key = os.getenv('SECRET_KEY')

# Create the database tables
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedules')
def schedules():
    return render_template('schedules.html')

@app.route('/list_schedules')
def list_schedules():
    schedules = PlateSchedule.query.all()
    day_translation = {
        "Monday": "Lunes",
        "Tuesday": "Martes",
        "Wednesday": "Miércoles",
        "Thursday": "Jueves",
        "Friday": "Viernes"
    }
    for schedule in schedules:
        schedule.day = day_translation.get(schedule.day, schedule.day)
    return render_template('list_schedules.html', schedules=schedules)

@app.route('/save_schedules', methods=['POST'])
def save_schedules():
    if request.method == 'POST':
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        for day in days:
            day_numbers = request.form.get(f'{day.lower()}')

            if day_numbers and start_time and end_time:
                numbers = [num.strip() for num in day_numbers.split(',')]
                plates = []
                for number in numbers:
                    if not number.isdigit() or int(number) < 0 or int(number) > 9:
                        flash('Número inválido: {}. El número debe estar entre 0 y 9.'.format(number))
                        return redirect(url_for('schedules'))
                    plates.append(int(number))

                existing_schedule = PlateSchedule.query.filter_by(day=day).first()
                if existing_schedule:
                    existing_schedule.start_time = start_time
                    existing_schedule.end_time = end_time
                    existing_schedule.plate_numbers = plates
                    print("Ya existe un horario para el día {} y número {}".format(day, plates))
                else:
                    schedule = PlateSchedule(day=day, plate_numbers=plates, start_time=start_time, end_time=end_time)
                    db.session.add(schedule)
                    print("Se ha agregado el horario para el día {} y número {}".format(day, plates))

        db.session.commit()
        flash('Horario guardado')
    return redirect(url_for('schedules'))


@app.route('/information')
def information():
    return render_template('about.html')

@app.route('/validation')
def validation():
    return render_template('validation.html')

@app.route('/plate_validation', methods=['POST'])
def plate_validation():
    if request.method == 'POST':
        plate = request.form.get('plate')
        day = request.form.get('day')
        time = request.form.get('time')
        plate_format = r'^[A-Z]{3}-\d{4}$'
        time = datetime.strptime(time, "%H:%M").time()
        if not re.match(plate_format, plate):
            flash('Placa inválida. Formato correcto: MMM-0000')
            return redirect(url_for('validation'))

        schedule = PlateSchedule.query.filter_by(day=day).first()
        if schedule:
            if int(plate[-1]) in schedule.plate_numbers and schedule.start_time <= time <= schedule.end_time:
                flash('No puedes circular')
            else:
                flash('Puedes circular')
        return redirect(url_for('validation'))


if __name__ == '__main__':
    app.run(port=4000, debug=True)
    app.config['DEBUG'] = True




