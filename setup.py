#
# Copyright 2021 zero323
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os

from setuptools import setup

if os.path.exists("README.md"):
    with open("README.md") as fr:
        long_description = fr.read()
else:
    long_description = ""

setup(
    name="graphframes-stubs",
    version="0.8.0",
    description="Stub files for graphframes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/zero323/graphframes-stubs",
    packages=["graphframes", "graphframes.lib", "graphframes.examples"],
    package_data={"": ["*.pyi", "py.typed"]},
    extras_require={
        "graphframes": ["graphframes~=0.8"],
    },
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Typed",
    ],
)
