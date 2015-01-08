# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2013 - KMEE- Luis Felipe Miléo (<http://www.kmee.com.br>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from distutils.core import setup
setup(
    name="PyApogeus",
    packages=['pyapogeus',
        'pyapogeus.importacao',
        'pyapogeus.exportacao'],
    version="0.0.1",
    description="Apogeus Mobile",
    author="Luis Felipe Miléo",
    author_email="mileo@kmee.com.br",
    url="http://www.kmee.com.br/",
    download_url="http://www.kmeec.com.br/download/python-apogeus-0.0.1.tgz",
    keywords=["mobile", "android", "apogeus","progressiva"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License",
        "Operating System :: OS Independent",
        ],
    long_description="""\
Apogeus Mobile helper to export files and get data from impoted files
-------------------------------------
"""
)
