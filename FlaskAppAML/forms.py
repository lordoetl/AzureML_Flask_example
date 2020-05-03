from wtforms import Form, StringField, TextAreaField, validators


class SubmissionForm(Form):
    title = StringField('Title', [validators.Length(min=2, max=30)])
    category = StringField('Category', [validators.Length(min=0, max=30)])
    text = TextAreaField('Text', [validators.Length(min=1, max=500)])