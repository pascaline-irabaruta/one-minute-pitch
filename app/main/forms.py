

class PitchForm(FlaskForm):

    title = StringField('Pitch title', validators=[Required()])
    text = TextAreaField('Text', validators=[Required()])
    category = SelectField('Type', choices=[('business', 'Business pitch'), (
        'promotion', 'Promotion pitch'), ('product', 'Product pitch')], validators=[Required()])
    submit = SubmitField('Create pitch')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.', validators=[Required()])
    submit = SubmitField('Submit')
