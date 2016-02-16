from wtforms import (
    Form,
    HiddenField,
    IntegerField,
    TextField,
    TextAreaField,
    validators,
    widgets,
    )

strip_filter = lambda x: x.strip() if x else None


class EntryCreateForm(Form):
    title = TextField(
        'Entry Title',
        [validators.Length(min=1, max=255)],
        filters=[strip_filter])
    body = TextAreaField(
        'Entry Body',
        [validators.Length(min=1)],
        filters=[strip_filter])


class EntryEditForm(EntryCreateForm):
    id = HiddenField('entry_id')

