from setuptools import setup, Extension

#module = Extension ('dkloopsim', sources=['web/sims/dk/whole_loop_sim.pyx'])
module = Extension ('attack_table', sources=['web/sims/shared/attack_tables.py'])
# module = [Extension('attack', ['web/sims/shared/attack_tables.py', 'web/sims/dk/funct2_pc.py'],)]

setup(
    name='dksim',
    version='1.0',
    author='Krught',
    ext_modules=[module]
)
# from setuptools import setup
# from Cython.Build import cythonize
#
# setup(
#     ext_modules = cythonize("web.dk.sims.runes.pyx")
# )
