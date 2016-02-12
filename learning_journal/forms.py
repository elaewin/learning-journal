from wtforms import Form, TextField, TextAreaField, validators

strip_filter = lambda x: x.strip() if x else None


class EntryCreateForm(Form):
    title = TextField(
        'Entry title',
        [validators.Length(min=1, max=255)],
        filters=[strip_filter])
    body = TextAreaField(
        'Entry body',
        [validators.Length(min=1)],
        filters=[strip_filter])


class EntryEditForm(Form):
    title = TextField(
        'Entry title',
        [validators.Length(min=1, max=255)],
        filters=[strip_filter],
        default= # .get the existing name for the title here)
    '''from WTForms docs: If you just need to access the data for known
    fields, you should use form.<field>.data, not this proxy property.'''
    body = TextAreaField(
        'Entry body',
        [validators.Length(min=1)],
        filters=[strip_filter],
        default= # .get the contents of the body field here)
