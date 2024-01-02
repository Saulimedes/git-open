import unittest
import subprocess
import sys
from os.path import dirname, abspath, join
from tempfile import TemporaryDirectory

class TestGitOpen(unittest.TestCase):

    def setUp(self):
        self.script_path = join(dirname(abspath(__file__)), 'git-open')

    def run_script(self, args, working_dir=None):
        command = [sys.executable, self.script_path] + args
        return subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=working_dir)

    def test_open_specific_branch(self):
        branch_name = "main"
        result = self.run_script(['--branch', branch_name, '--print'])
        expected_url = 'https://github.com/Saulimedes/git-open/tree/main'
        self.assertIn(expected_url, result.stdout)

    def test_open_current_commit(self):
        result = self.run_script(['--commit', '--print'])
        # Replace 'commit_sha' with the actual commit SHA you expect
        expected_url_part = 'https://github.com/Saulimedes/git-open/commit/'
        self.assertIn(expected_url_part, result.stdout)

    def test_open_issues_page(self):
        result = self.run_script(['--issue', '--print'])
        expected_url = 'https://github.com/Saulimedes/git-open/issues'
        self.assertIn(expected_url, result.stdout)

if __name__ == '__main__':
    unittest.main()
