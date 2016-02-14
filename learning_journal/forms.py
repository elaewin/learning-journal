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


class EntryEditForm(Form):
    # entry_id = IntegerField(widget=HiddenInput())
    entry_id = HiddenField(
        'entry_id',
        [validators.Required()],
        filters=[strip_filter])
    title = TextField(
        'Entry title',
        [validators.Length(min=1, max=255)],
        filters=[strip_filter])
    body = TextAreaField(
        'Entry body',
        [validators.Length(min=1)],
        filters=[strip_filter])
