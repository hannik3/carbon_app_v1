from flask import render_template, Blueprint, request, redirect, url_for, flash
from capp.models import Transport
from capp import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from capp.carbon_app.forms import BusForm, CarForm, PlaneForm, MotorbikeForm, BicycleForm, WalkForm, TrainForm
import json

carbon_app=Blueprint('carbon_app',__name__)

#Emissions factor per transport in kg per passemger km
efco2 = {
    'Bus': {
        'Diesel': 0.030  # Diesel buses emit ~30g CO₂ per passenger-km
    },
    'Car': {
        'Petrol': 0.153,           # Petrol cars emit 153g CO₂ per km
        'Diesel': 0.145,           # Diesel cars emit 145g CO₂ per km
        'LNG': 0.133,              # LNG-fueled cars emit 133g CO₂ per km
        'Electric': 0.003006,      # Electric cars: 18g CO₂/kWh * 0.167 kWh/km = ~3g CO₂/km
        'Sports Car': 0.250,       # Sports cars (usually petrol) emit 250g CO₂ per km
        'Family Car': 0.158,       # Family cars emit 158g CO₂ per km
        'Small Car': 0.104,        # Small cars emit 104g CO₂ per km
        'No Fossil Fuel': 0        # Zero emissions for non-fossil fuel cars
    },
    'Plane': {
        'Economy': 0.128,          # Economy class flights emit 128g CO₂ per passenger-km
        'Business/First': 0.280    # Business/first class flights emit 280g CO₂ per passenger-km
    },
    'Train': {
        'Electric': 0.007,         # Electric trains in Norway emit 7g CO₂ per passenger-km
        'Diesel': 0.091            # Diesel trains emit 91g CO₂ per passenger-km
    },
    'Motorbike': {
        'Petrol': 0.114,           # Motorcycles emit 114g CO₂ per km
        'No Fossil Fuel': 0        # Very rare; but counted as zero emissions if electric
    },
    'Bicycle': {
        'No Fossil Fuel': 0        # Bicycles have zero direct emissions
    },
    'Walk': {
        'No Fossil Fuel': 0        # Walking has zero direct emissions
    }
}


#Carbon app, main page
@carbon_app.route('/carbon_app')
@login_required
def carbon_app_home():
    return render_template('carbon_app/carbon_app.html', title='carbon_app')

#New entry bus
@carbon_app.route('/carbon_app/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_bus.html', title='new entry bus', form=form)

#New entry car
@carbon_app.route('/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Car'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_car.html', title='new entry car', form=form)    

#New entry plane
@carbon_app.route('/carbon_app/new_entry_plane', methods=['GET','POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Plane'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_plane.html', title='new entry plane', form=form)  

#New entry motorbike
@carbon_app.route('/carbon_app/new_entry_motorbike', methods=['GET','POST'])
@login_required
def new_entry_motorbike():
    form = MotorbikeForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Motorbike'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_motorbike.html', title='new entry motorbike', form=form) 

#New entry bicycle
@carbon_app.route('/carbon_app/new_entry_bicycle', methods=['GET','POST'])
@login_required
def new_entry_bicycle():
    form = BicycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bicycle'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_bicycle.html', title='new entry bicycle', form=form)

#New entry walk
@carbon_app.route('/carbon_app/new_entry_walk', methods=['GET','POST'])
@login_required
def new_entry_walk():
    form = WalkForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Walk'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_walk.html', title='new entry walk', form=form)

#Your data
@carbon_app.route('/carbon_app/your_data')
@login_required
def your_data():
    #Table
    entries = Transport.query.filter_by(author=current_user). \
        filter(Transport.date> (datetime.now() - timedelta(days=5))).\
        order_by(Transport.date.desc()).order_by(Transport.transport.asc()).all()
    
    #Emissions by category
    emissions_by_transport = db.session.query(db.func.sum(Transport.total), Transport.transport). \
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        group_by(Transport.transport).order_by(Transport.transport.asc()).all()
    emission_transport = [0, 0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in emissions_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Bus' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Bus')
        emission_transport[1]=first_tuple_elements[index_bus]
    else:
        emission_transport[1]

    if 'Car' in second_tuple_elements:
        index_car = second_tuple_elements.index('Car')
        emission_transport[2]=first_tuple_elements[index_car]
    else:
        emission_transport[2]

    if 'Motorbike' in second_tuple_elements:
        index_motorbike = second_tuple_elements.index('Motorbike')
        emission_transport[4]=first_tuple_elements[index_motorbike]
    else:
        emission_transport[4]

    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        emission_transport[5]=first_tuple_elements[index_plane]
    else:
        emission_transport[5]

    #Kilometers by category
    kms_by_transport = db.session.query(db.func.sum(Transport.kms), Transport.transport). \
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        group_by(Transport.transport).order_by(Transport.transport.asc()).all()
    kms_transport = [0, 0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in kms_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Bicycle' in second_tuple_elements:
        index_bicycle = second_tuple_elements.index('Bicycle')
        kms_transport[0]=first_tuple_elements[index_bicycle]
    else:
        kms_transport[0] 

    if 'Bus' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Bus')
        kms_transport[1]=first_tuple_elements[index_bus]
    else:
        kms_transport[1]

    if 'Car' in second_tuple_elements:
        index_car = second_tuple_elements.index('Car')
        kms_transport[2]=first_tuple_elements[index_car]
    else:
        kms_transport[2]

    if 'Motorbike' in second_tuple_elements:
        index_motorbike = second_tuple_elements.index('Motorbike')
        kms_transport[4]=first_tuple_elements[index_motorbike]
    else:
        kms_transport[4]

    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        kms_transport[5]=first_tuple_elements[index_plane]
    else:
        kms_transport[5]

    if 'Scooter' in second_tuple_elements:
        index_scooter = second_tuple_elements.index('Scooter')
        kms_transport[6]=first_tuple_elements[index_scooter]
    else:
        kms_transport[6]     

    if 'Walk' in second_tuple_elements:
        index_walk = second_tuple_elements.index('Walk')
        kms_transport[7]=first_tuple_elements[index_walk]
    else:
        kms_transport[7]    

    #Emissions by date (individual)
    emissions_by_date = db.session.query(db.func.sum(Transport.total), Transport.date). \
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        group_by(Transport.date).order_by(Transport.date.asc()).all()
    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_emissions.append(total)    

    #Kms by date (individual)
    kms_by_date = db.session.query(db.func.sum(Transport.kms), Transport.date). \
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        group_by(Transport.date).order_by(Transport.date.asc()).all()
    over_time_kms = []
    dates_label = []
    for total, date in kms_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_kms.append(total)      


    return render_template('carbon_app/your_data.html', title='your_data', entries=entries,
        emissions_by_transport_python_dic=emissions_by_transport,     
        emission_transport_python_list=emission_transport,             
        emissions_by_transport=json.dumps(emission_transport),
        kms_by_transport=json.dumps(kms_transport),
        over_time_emissions=json.dumps(over_time_emissions),
        over_time_kms=json.dumps(over_time_kms),
        dates_label=json.dumps(dates_label))

#Delete emission
@carbon_app.route('/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('carbon_app.your_data'))
    
  