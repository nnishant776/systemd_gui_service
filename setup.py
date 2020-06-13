from setuptools import setup, find_packages

setup(
    name='gui_systemd_service',
    version='0.1',
    author='Neeraj Nishant',
    description='An application to create systemd service files using a GUI',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Consumers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only'
    ],
    data_files=[
        (
            'share/applications/',
            [
                'data/service-creator.desktop',
            ]
        )
    ],
    python_requires='>=3.5, <4',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    entry_points={
        'console_scripts': [
            'service_creator=gui_systemd_service:main'
        ]
    }
)
