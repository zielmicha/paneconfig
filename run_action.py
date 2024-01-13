import glob, os, subprocess, shlex, glob
os.chdir(os.path.expanduser('~'))

paths = [
    '~/paneconfig/actions/*',
    '~/r/actions/*',
    '~/config/actions/*',
]

commands = {}
for path in paths:
    for command in glob.glob(os.path.expanduser(path)):
        commands[os.path.basename(command)] = command

cmd = subprocess.check_output(['rofi', '-dmenu'], input='\n'.join(commands).encode()).decode().strip()
if cmd in commands:
    full = commands[cmd]
    r = subprocess.run(['zsh', '-c', '. ~/.zshrc; ' + full], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if r.returncode != 0:
        subprocess.check_call(['notify-send', '--', 'ERROR: %s' % r.stdout.decode('utf8', 'replace')])
