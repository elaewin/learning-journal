from wtforms import (
    Form,
    HiddenField,
    IntegerField,
    PasswordField,
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
    id = HiddenField()


class LoginForm(Form):
    username = TextField(
        'Username', [validators.Length(min=1, max=255)]
    )
    password = PasswordField(
        'Password', [validators.Length(min=1, max=255)]
    )
