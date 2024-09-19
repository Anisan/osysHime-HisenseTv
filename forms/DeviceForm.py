from flask import render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

from app.database import db
from plugins.HisenseTv.models.Device import Device
from plugins.HisenseTv.models.Data import Data

class DeviceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    ip = StringField('IP', validators=[DataRequired()])
    mac = StringField('MAC', validators=[DataRequired()])

def routeDevice(request):
    device = request.args.get("device",None)
    if device:
        item = Device.query.get_or_404(device)  # Получаем объект из базы данных или возвращаем 404, если не найден
        form = DeviceForm(obj=item)  # Передаем объект в форму для редактирования
    else:
        form = DeviceForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            if device:
                form.populate_obj(item)  # Обновляем значения объекта данными из формы
            else:
                item = Device()
                form.populate_obj(item)
                db.session.add(item)
            db.session.commit()  # Сохраняем изменения в базе данных
            return redirect("HisenseTv")
    
    data = Data.query.filter(Data.device_id == device).order_by(Data.title).all()

    return render_template("hisense_device.html", form=form, data=data)