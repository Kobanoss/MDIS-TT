import datetime

import phonenumbers
from flask_wtf import FlaskForm
from wtforms.fields import DateField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError


class DataForm(FlaskForm):
    full_name = StringField(label='Full Name', validators=[
        DataRequired(),
        Length(min=5, max=60)
    ])
    birth_date = DateField(label='Birth Date', validators=[
        DataRequired(),
    ])
    address = StringField(label='Full Address', validators=[
        DataRequired(),
    ])
    phone = StringField(label='Phone', validators=[
        DataRequired(),
        Length(min=11, max=12)
    ])
    submit = SubmitField(label='Send')

    def validate_phone(self, phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')

    def jsonsify(self):
        json_obj = {attr: value for attr, value in self.__dict__}
        json_obj['birth_date'] = datetime.datetime(json_obj['birth_date']).date().ctime()
        return
