# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/new_order')
def new_order():
    user = {'username': 'Miguel'}
    return render_template('new_order.html', title='new_order', user=user)


@app.route('/new_order_zip')
def new_order_zip():
    user = {'username': 'Miguel'}
    return render_template('new_order_zip.html', title='new_order_zip', user=user)


@app.route('/new_order_goods')
def new_order_goods():
    user = {'username': 'Miguel'}
    return render_template('new_order_goods.html', title='new_order_goods', user=user)


@app.route('/orders')
def orders():
    user = {'username': 'Miguel'}
    return render_template('orders.html', title='orders', user=user)


@app.route('/reports')
def reports():
    user = {'username': 'Miguel'}
    return render_template('reports.html', title='reports', user=user)


