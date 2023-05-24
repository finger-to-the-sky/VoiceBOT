import subprocess

if __name__ == '__main__':
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'python3 ./bot/voicebot.py'])
