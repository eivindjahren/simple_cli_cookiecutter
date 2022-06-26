import pytest
from {{cookiecutter.project_slug}}.__main__ import parse_args_and_run


def test_help_message(capsys):
    with pytest.raises(SystemExit) as system_exit:
        parse_args_and_run(["{{cookiecutter.project_slug}}", "-h"])
        assert system_exit.code == 0
    assert "{{cookiecutter.project_slug}}" in capsys.readouterr().out
