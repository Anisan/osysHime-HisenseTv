from flask import render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField

from app.database import db
from plugins.HisenseTv.models.Data import Data
from app.core.lib.object import removeLinkFromObject, setLinkToObject

class DataForm(FlaskForm):
    title = StringField('Title')
    linked_object = StringField('Linked object')
    linked_property = StringField('Linked property')

def routeData(request):
    data = request.args.get("data",None)
    if data:
        item = Data.query.get_or_404(data)  # Получаем объект из базы данных или возвращаем 404, если не найден
        form = DataForm(obj=item)  # Передаем объект в форму для редактирования
    else:
        form = DataForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            if data:
                removeLinkFromObject(item.linked_object, item.linked_property, "HisenseTv")
                form.populate_obj(item)  # Обновляем значения объекта данными из формы
                setLinkToObject(item.linked_object, item.linked_property, "HisenseTv")
            else:
                item = Data()
                form.populate_obj(item)
                db.session.add(item)
            db.session.commit()  # Сохраняем изменения в базе данных
            return redirect("HisenseTv?op=edit&device="+str(item.device_id))

    
    
    return render_template("hisense_data.html", form=form)