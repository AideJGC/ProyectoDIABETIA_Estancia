import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="diabetia_hta",
    version="0.0.1",
    author="Aide Jazmín González Cruz",
    description="Aplicación para predecir que pacientes diabeticos tendrán hipertensión el siguiente año o el próximo mes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AideJGC/ProyectoDIABETIA_Estancia",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        'numpy>=1.21.0'
        ],
    python_requires=">=3.7.12",
)
