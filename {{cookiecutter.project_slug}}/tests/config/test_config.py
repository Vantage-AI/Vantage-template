import os
import pytest
from io import StringIO
from dataclasses import asdict
from config import Config


TEST_CONFIG_PY = os.path.dirname(os.path.abspath(__file__))

def test_default_config() -> None:
    """Test default config param set"""

    config = Config()

    received_config = asdict(config)
    assert 'param' in received_config
    assert os.path.isdir(config.project_root)
    assert config.data_path

    # assert config.project_root == os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir))
    Config.clear()


def test_clearing_config() -> None:
    """Test clearing of config"""

    config = Config()
    assert config.param == 1
    config.param = 2
    assert config.param == 2

    Config.clear()

    config = Config()
    assert config.param == 1
    Config.clear()


def test_getting_old_config() -> None:
    """Test creating new config, without changing"""

    config = Config()
    assert config.param == 1
    config.param = 2
    assert config.param == 2

    config = Config()

    assert config.param == 2
    Config.clear()


def test_setting_project_root() -> None:
    project_root = '/tmp'

    config = Config(
        env = "DEFAULT",
        config_path=f"{os.path.join(TEST_CONFIG_PY, 'test_config.ini')}",
        project_root=project_root)

    assert config.project_root == project_root
    assert os.path.dirname(config.data_path) == project_root
    Config.clear()


def test_setting_not_existing_project_root() -> None:
    with pytest.raises(FileNotFoundError):
        config = Config(project_root='/2a12039dho2if2891f')


def test_setting_file_path_as_project_root() -> None:
    with pytest.raises(NotADirectoryError):
        config = Config(project_root='tests/config/test_config.py')



def test_dev_section_in_config() -> None:
    """Test sections in config file"""

    project_root = '/tmp'
    config = Config(env='DEVELOPMENT',
               config_path=f"{os.path.join(TEST_CONFIG_PY, 'test_config.ini')}",
               project_root = project_root)

    received_config = asdict(config)
    expected_config = {'param': 1,
                       'project_root': project_root,
                       'data_path': os.path.join(project_root, 'DEV/data/')}
    assert received_config == expected_config
    Config.clear()


def test_test_section_in_config():
    """Test sections in config file"""

    project_root = '/tmp'
    config = Config(
        env='TEST',
        config_path=f"{os.path.join(TEST_CONFIG_PY, 'test_config.ini')}",
        project_root = project_root )

    received_config = asdict(config)
    expected_config = {'param': 1,
                       'project_root': project_root,
                       'data_path': os.path.join(project_root, 'TEST/data/')}
    assert received_config == expected_config
    Config.clear()


def test_prd_section_in_config():
    """Test production section from init config file"""

    project_root = '/tmp'
    config = Config(
        env='PRODUCTION',
        config_path=f"{os.path.join(TEST_CONFIG_PY, 'test_config.ini')}",
        project_root=project_root)

    received_config = asdict(config)
    expected_config = {'param': 1,
                       'project_root': project_root,
                       'data_path': os.path.join(project_root, 'PRD/data/')}
    assert expected_config==received_config
    Config.clear()


def test_incorrect_section_name_config():
    project_root = '/tmp'
    with pytest.raises(KeyError):
        config = Config(env='INCORRECT_SESSION',
                        config_path=f"{os.path.join(TEST_CONFIG_PY, 'test_config.ini')}",
                        project_root=project_root)


def test_absolute_paths_config():
    config = Config(config_path=f"{os.path.join(TEST_CONFIG_PY,'test_config_absolute_path.ini')}")
    assert os.path.isdir(config.data_path)
    Config.clear()


def test_weird_formatting_config():
    config = Config(env='DEVELOPMENT',
                    config_path=f"{os.path.join(TEST_CONFIG_PY,'test_config_weird_formatting.ini')}",
                    project_root=TEST_CONFIG_PY)

    assert os.path.isdir(config.data_path)
    assert config.data_path == os.path.join(TEST_CONFIG_PY, os.path.pardir)
