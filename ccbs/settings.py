import os
from dotenv import load_dotenv


class Settings(object):

    def __init__(self, root_dir):
        self._root_dir = root_dir
        dotenv_path = os.path.join(self._root_dir, '.env')
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        self._typeform_token = os.getenv('TYPEFORM_TOKEN')
        self._docs_path = os.path.join(self._root_dir, 'docs')
        self._owner_form_id = 'A4nDvf'
        self._owner_form_filename = 'owner-form.json'
        self._dog_form_id = 'b6s4oE'
        self._dog_form_filename = 'dog-form.json'

    @property
    def root_dir(self):
        return self._root_dir

    @property
    def typeform_token(self):
        return self._typeform_token

    @property
    def docs_path(self):
        return self._docs_path

    @property
    def owner_form_id(self):
        return self._owner_form_id

    @property
    def owner_form_filename(self):
        return self._owner_form_filename

    @property
    def dog_form_id(self):
        return self._dog_form_id

    @property
    def dog_form_filename(self):
        return self._dog_form_filename
