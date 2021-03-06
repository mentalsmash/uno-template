###############################################################################
# (C) Copyright 2020-2021 Andrea Sorbini
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################
import setuptools

with open("README.md", "r") as readme_f:
    readme_contents = readme_f.read()

setuptools.setup(
    name="uno_template",
    version="0.1.0",
    author="Andrea Sorbini",
    author_email="support@mentalsmash.org",
    description="uno templating library",
    license="License :: OSI Approved :: Apache Software License",
    long_description=readme_contents,
    long_description_content_type="text/markdown",
    url="https://github.com/mentalsmash/uno-template.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    python_requires='>=3.6, <4',
    install_requires=[
        "yaml-serde",
        "uno-log",
        "jinja2"
    ],
)
