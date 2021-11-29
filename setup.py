import setuptools

setuptools.setup(
    name="pubutils",
    version="0.0.1",
    author="Fredrik Feyling",
    author_email="fredrik.feyling@hotmail.com",
    description="Utilities for phd related writing",
    package_dir={'': '.'},
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
    install_requires = [
        'numpy',
        'shlib',
        'click',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'pubutils = pubutils:cli',
        ],
    },
)
