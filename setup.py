from setuptools import setup, find_packages

setup(
    name="image_process",
    version="0.0.1",
    author="GeicyaneClemente",
    author_email="geicyaneclemente@live.com",
    url="https://github.com/GeicyaneC/image_process",
    packages=find_packages(),
    install_requires=['numpy','matplotlib','PIL'],
    python_requires='>=3.8'
)