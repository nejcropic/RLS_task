from setuptools import setup, find_packages

setup(
    name='RLS_task',
    version='0.3',
    author='Nejc Ropič',
    author_email='nejc.ropic@gmail.com',
    description='RLS_task is a Python GUI program which collects and '
                'displays the environment data from: https://meteo.arso.gov.si/met/en/service2/.',
    long_description=open('README.md').read(),
    url='https://github.com/nejcropic/RLS_task',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PyQt5',
        'numpy',
        'beautifulsoup4',
        'urllib3',

    ],
    entry_points={
        'console_scripts': [
            'rls_task = rls_task.top_level:main',  # Adjust the import path and function
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
)
