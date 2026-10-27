import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
subprocess.run(['git', 'config', '--local', 'core.hooksPath', '.githooks'], cwd=root, check=True)
subprocess.run(['git', 'config', '--local', 'privacy.python', sys.executable.replace('\\', '/')], cwd=root, check=True)
for hook in ('pre-commit', 'pre-push'):
    (root / '.githooks' / hook).chmod(0o755)
print('Privacy hooks enabled for this checkout. Run privacy_check.py before the initial commit.')
