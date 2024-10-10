import pytest
import openai

@pytest.fixture(autouse=True)
def mock_openai(mocker):
    mock_completion = mocker.Mock()
    mock_completion.choices = [mocker.Mock(message=mocker.Mock(content="Mocked response"))]
    mocker.patch('openai.ChatCompletion.create', return_value=mock_completion)
    mocker.patch('openai.api_key', 'dummy_key')
