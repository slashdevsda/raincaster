from setuptools import setup, find_packages

setup(
    name='raincast',
    version='0.1',
    author='Thomas.'
    packages=find_packages('.'),
    package_dir={'':'.'},
    install_requires=["requests==2.22.0"],

    # include everything
    include_package_data=True,
    exclude_package_data={'': ['README.md']},
    scripts=['raincastcli'],
)    
