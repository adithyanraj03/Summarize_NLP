from setuptools import setup

def get_requirements():
    with open('requirements.txt') as f:
        packages = []
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if 'https://' in line:
                tail = line.rsplit('/', 1)[1]
                tail = tail.split('#')[0]
                line = tail.replace('@', '==').replace('.git', '')
            packages.append(line)
        return packages

setup(
    name='summarize-gpt',  # Use a valid package name with hyphens
    version='2.0',
    packages=[''],
    url='',
    license='',
    author='Adithya & Giridhar',
    author_email='adithyanraj03@gmail.com',
    description='',
    install_requires=get_requirements(),
)
