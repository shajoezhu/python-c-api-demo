from setuptools import setup, Extension

demo_module = Extension(
    'demo',
    sources=["demomodule.c"],
    libraries=["m", "gsl", "gslcblas"],
)

setup(
    name="demo",
    description="Demo C module",
    ext_modules=[demo_module])

