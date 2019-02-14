#!/usr/bin/env python

import json
import os
import pprint
import tempfile
from unittest.mock import patch

from cookiecutter.main import cookiecutter


upstream_template = 'gh:DAI-Lab/cookiecutter-pypackage'


def main():
    # load the context
    project_root = os.path.realpath(os.path.curdir)
    replay_file = os.path.join(project_root, '.cookiecutter_replay.json')

    if not os.path.exists(replay_file):
        raise RuntimeError('Couldn\'t find replay file in project directory')

    with open(replay_file, 'r') as f:
        context = json.load(f)

    print('Using context: {}'.format(pprint.pformat(context)))

    # patch cookiecutter.replay.load to just return the context above
    with patch('cookiecutter.main.load') as mock_load:
        mock_load.return_value = context

        # write project to temporary directory
        with tempfile.TemporaryDirectory() as d:
            print('Replaying project to {}'.format(d))
            cookiecutter(upstream_template, output_dir=d, replay=True)

    print('Done')


if __name__ == '__main__':
    main()

