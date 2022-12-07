from hub import app
from flask import render_template, request, redirect, url_for, session
from hub.models import Physics
from hub.app_fun import acceleration, abs_pres, electric_field, force, mass, velocity, work, stress, power


@app.route('/')
def home():
    physics = Physics.query.all()
    return render_template('homepage.html', physics=physics)

@app.route('/acceleration', methods=['GET', 'POST'])
def acc_search():
    if request.method == 'POST':
        session['initial'] = request.form.get("initial", False)
        session['final'] = request.form.get("final", False)
        session['time'] = request.form.get("time", False)
        session['acc'] = request.form.get("acc", False)
        session['results'] = acceleration(float( session['initial']), float( session['final']), float(session['time']), float(session['acc']))
        return redirect (url_for('acc_search'))
        
    return render_template('acceleration.html',
                            the_result1=str(session.get('results')), 
                            initial=session.get('initial'),
                            final=session.get('final'),
                            time=session.get('time'),
                            acc=session.get('acc'))

@app.route('/abs_pressure', methods=['GET', 'POST'])
def abs_search():
    if request.method == 'POST':
        session['guage_press'] = request.form.get("guage_press", False)
        session['atm_press'] = request.form.get("atm_press", False)
        session['abs_press'] = request.form.get("abs_press", False)
        session['results'] = abs_pres(float(session['abs_press']), float(session['guage_press']), float(session['atm_press']))
        return redirect (url_for('abs_search'))
    
    return render_template('absolute.html',
                            the_result2=session.get('results'), 
                            guage=session.get('guage_press'), 
                            atm=session.get('atm_press'), 
                            abs=session.get('abs_press'))

@app.route('/electric', methods=['GET', 'POST'])
def electric_search():
    if request.method == 'POST':
        session['electric'] = request.form.get("electric", False)
        session['force'] = request.form.get("force", False)
        session['charge'] = request.form.get("charge", False)
        session['results'] = electric_field(float(session['electric']), float(session['force']), float(session['charge']))
        return redirect (url_for('electric_search'))
    
    return render_template('electric.html', 
                            the_result3=session.get('results'), 
                            electric=session.get('electric'), 
                            forc=session.get('force'), 
                            charge=session.get('charge'))

@app.route('/force', methods=['GET', 'POST'])
def force_search():
    if request.method == 'POST':
        session['force'] = request.form.get('force', False)
        session['mass'] = request.form.get('mass', False)
        session['acceleration'] = request.form.get('acceleration', False)
        session['results'] = force(float(session['force']), float(session['mass']), float(session['acceleration']))
        return redirect (url_for('force_search'))
    
    return render_template('force.html',
                            the_result4=session.get('results'),
                            forc=session.get('force'),
                            mass=session.get('mass'),
                            acc=session.get('acceleration'))


@app.route('/mass', methods=['GET', 'POST'])
def mass_search():
    if request.method == 'POST':
        session['mass'] = request.form.get('mass', False)
        session['density'] = request.form.get('density', False)
        session['velocity'] = request.form.get('velocity', False)
        session['results'] = mass(float(session['mass']), float(session['density']), float(session['velocity']))
        return redirect (url_for('mass_search'))

    return render_template('mass.html',
                            the_result5=session.get('results'),
                            mass=session.get('mass'),
                            dens=session.get('density'),
                            vel=session.get('velocity'),)


@app.route('/velocity', methods=['GET', 'POST'])
def velocity_search():
    if request.method == 'POST':
        session['initial'] = request.form.get("initial", False)
        session['velocity'] = request.form.get("velocity", False)
        session['time'] = request.form.get("time", False)
        session['acc'] = request.form.get("acc", False)
        session['results'] = velocity(float(session['velocity']), float( session['initial']), float(session['acc']), float(session['time']))
        return redirect (url_for('velocity_search'))
        
    return render_template('velocity.html',
                            the_result6=session.get('results'),
                            final=session.get('velocity'), 
                            initial=session.get('initial'),
                            acc=session.get('acc'),
                            time=session.get('time'))


@app.route('/work', methods=['GET', 'POST'])
def work_search():
    if request.method == 'POST':
        session['work'] = request.form.get('work', False)
        session['force'] = request.form.get('force', False)
        session['distance'] = request.form.get('distance', False)
        session['results'] = work(float(session['work']), float(session['force']), float(session['distance']))
        return redirect (url_for('work_search'))

    return render_template('work.html',
                            the_result7=session.get('results'),
                            works=session.get('work'),
                            forces=session.get('force'),
                            distances=session.get('distance'))


@app.route('/stress', methods=['GET', 'POST'])
def stress_search():
    if request.method == 'POST':
        session['stress'] = request.form.get('stress', False)
        session['force'] = request.form.get('force', False)
        session['area'] = request.form.get('area', False)
        session['results'] = stress(float(session['stress']), float(session['force']), float(session['area']))
        return redirect (url_for('stress_search'))

    return render_template('stress.html',
                            the_result8=session.get('results'),
                            stres=session.get('stress'),
                            forces=session.get('force'),
                            areas=session.get('area'))


@app.route('/power', methods=['GET', 'POST'])
def power_search():
    if request.method == 'POST':
        session['power'] = request.form.get('power', False)
        session['work'] = request.form.get('work', False)
        session['time'] = request.form.get('time', False)
        session['results'] = power(float(session['power']), float(session['work']), float(session['time']))
        return redirect (url_for('power_search'))

    return render_template('power.html',
                            the_result9=session.get('results'),
                            powers=session.get('power'),
                            works=session.get('work'),
                            time=session.get('time'),)

