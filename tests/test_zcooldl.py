#!/usr/bin/env python
"""Tests for `zcooldl` package."""
import unittest
from click.testing import CliRunner

from zcooldl import cli


class TestZcooldl(unittest.TestCase):
    """Tests for `zcooldl` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'Must give an <id> or <username>!' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert 'Show this message and exit.' in help_result.output
