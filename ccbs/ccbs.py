"""
Usage:
  ccbs.py fetch (owner | dog)
  ccbs.py update (owner | dog)
  ccbs.py -h | --help

Options:
  -h, --help                  Show this screen.

"""


from .form import get_requested_form
from .settings import Settings
from docopt import docopt
from typeform import Typeform
import json
import os


def get_root_dir():
    return os.path.join(os.path.dirname(__file__), '..')


def main():
    args = docopt(__doc__, version=None)
    settings = Settings(get_root_dir())
    typeform = Typeform(settings.typeform_token)
    # Initialize a form based on the requested type.
    form = get_requested_form(args, settings)
    # Perform the requested action with the form.
    if args['fetch']:
        form.contents = typeform.forms.get(form.id)
        with open(form.filepath, 'w') as fout:
            json.dump(form.contents, fout, indent=2)
    elif args['update']:
        with open(form.filepath, 'r') as fin:
            form.contents = json.load(fin)
        response = typeform.forms.update(form.id, form.contents)
        if not response == form.contents:
            raise Exception('The response does not match the requested update.')
    else:
        raise Exception('Unexpected arguments were tendered.')
