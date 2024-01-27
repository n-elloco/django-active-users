from setuptools import setup

setup(
    name='django-active-users',
    version='0.4.1',
    packages=['active_users', 'active_users.api'],
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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
