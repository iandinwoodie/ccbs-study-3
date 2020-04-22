import os


class Form(object):

    def __init__(self, id_, docs_path, filename):
        self._id = id_
        self._filepath = os.path.join(docs_path, filename)
        self._contents = None

    @property
    def id(self):
        return self._id

    @property
    def filepath(self):
        return self._filepath

    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, value):
        self._contents = value


def get_requested_form(args, settings):
    if args['owner']:
        return Form(settings.owner_form_id, settings.docs_path,
                    settings.owner_form_filename)
    else:
        return Form(settings.dog_form_id, settings.docs_path,
                    settings.dog_form_filename)
