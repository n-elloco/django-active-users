from setuptools import setup

setup(
    name='django-active-users',
    version='0.1',
    packages=['active_users'],
    url='https://github.com/n-elloco/django-active-users',
    license='MIT',
    author='Nikita Ekaterinchuk',
    author_email='en.elloco@gmail.com',
    description='Monitoring of active users in Django using Redis',
    long_description=open('README.rst').read(),
    install_requires=open('REQUIREMENTS').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
