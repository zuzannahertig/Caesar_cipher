from unittest.mock import patch
import pytest

from features.manage import Manager, Mapper


@pytest.fixture
def mock_manager():
    return Manager()


class TestMapper:
    @patch("manage.Menu.choose", side_effect=["1"])
    @patch.object(Manager, "execute_default_path")
    def test_map_actions_executes_default_path(
        self, mock_method, mock_choose, mock_manager
    ):
        mapper = Mapper(mock_manager)
        mapper.map_actions("1")
        mock_method.assert_called_once()

    @patch("manage.Menu.choose", side_effect=["3"])
    @patch.object(Manager, "save_and_quit")
    def test_map_actions_executes_save_and_quit(
        self, mock_method, mock_choose, mock_manager
    ):
        mapper = Mapper(mock_manager)
        mapper.map_actions("3")
        mock_method.assert_called_once()

    @patch("manage.Menu.choose", side_effect=["2", "1", "2"])
    @patch.object(Manager, "execute_custom_path")
    def test_map_actions_executes_change_settings(self, mock_method, mock_choose):
        mapper = Mapper(Manager())
        mapper.map_actions("5")
        mock_method.assert_called_once_with(cipher_type="1", shift="2")

    @patch("manage.Menu.choose", side_effect=["4"])
    @patch.object(Manager, "quit")
    def test_map_actions_executes_quit(self, mock_method, mock_choose, mock_manager):
        mapper = Mapper(mock_manager)
        mapper.map_actions("4")
        mock_method.assert_called_once()
