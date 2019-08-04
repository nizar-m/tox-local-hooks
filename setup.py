from setuptools import setup
import tox_local_hooks

_version = tox_local_hooks.__version__

setup(
    name="tox-local-hooks",
    description='Write hooks for tox in a local file',
    packages=['tox_local_hooks', ],
    version=_version,
    py_modules=['tox_pipenv'],
    url='https://github.com/nizar-m/tox-local-hooks',
    author='Nizar Malangadan',
    classifiers=['Development Status :: 3 - Alpha`',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Apache Software License',
                 'Operating System :: POSIX',
                 'Topic :: Software Development :: Testing',
                 'Topic :: Software Development :: Libraries',
                 'Topic :: Utilities',
                 'Programming Language :: Python',
                 'Framework:: tox'
],
    entry_points={"tox": ["local_hooks = tox_local_hooks.plugin"]},
    python_requires='>3.5',
    install_requires=['tox>=3.8.0,<4.0']
)
