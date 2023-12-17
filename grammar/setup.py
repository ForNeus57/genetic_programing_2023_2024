from setuptools import setup

setup(
    name='genetic_programming_2023_2024',
    version='0.0.1',
    packages=['antlr4', 'genetic', 'genetic.input', 'genetic.tiny_gp', 'genetic.individual',
              'genetic.individual.structure', 'genetic.individual.interfaces', 'genetic.individual.probability',
              'utilities'],
    package_dir={'': 'src/main/java'},
    url='https://github.com/ForNeus57/genetic_programing_2023_2024',
    license='',
    author='Dominik Breksa, Kaja Dzielnicka',
    author_email='',
    description=''
)
