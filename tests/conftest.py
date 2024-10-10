# This file is part of bitesize-notebook-financial-advisor.
#
# AI Financial Advisor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# AI Financial Advisor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with AI Financial Advisor. If not, see <https://www.gnu.org/licenses/>.
#
# Copyright (C) 2024 Vincent Koc (https://github.com/vincentkoc)

import pytest
import openai

@pytest.fixture(autouse=True)
def mock_openai(mocker):
    mock_completion = mocker.Mock()
    mock_completion.choices = [mocker.Mock(message=mocker.Mock(content="Mocked response"))]
    mocker.patch('openai.ChatCompletion.create', return_value=mock_completion)
    mocker.patch('openai.api_key', 'dummy_key')
