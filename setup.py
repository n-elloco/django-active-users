from setuptools import setup, find_packages

setup(
    name='active-users',
    version='0.0.1a',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    url='',
    license='MIT',
    author='BARS Group',
    author_email='',
    description='Monitoring of active users in Django using Redis',
    install_requires=open('REQUIREMENTS'),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Framework:: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ]
)
