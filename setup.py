import setuptools
import django_orm_standalone

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name=django_orm_standalone.__name__,
    version=django_orm_standalone.__version__,
    author=django_orm_standalone.__author__,
    author_email='haoyupan@aliyun.com',
    description=django_orm_standalone.__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/panhaoyu/django_orm_standalone',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
