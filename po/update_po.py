#!/usr/bin/env python

# $Id: update_po.py 40708 2011-09-30 05:36:56Z dfelinto $
# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENSE BLOCK *****

# <pep8 compliant>

# update all po files in the LANGS

import subprocess
import os
import sys

GETTEXT_MSGMERGE_EXECUTABLE = "msgmerge"
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
DOMAIN = "blender"


def process_po(po):
    lang = os.path.basename(po)[:-3]

    # update po file
    cmd = (GETTEXT_MSGMERGE_EXECUTABLE,
           "--update",
           "--backup=none",
           "--lang=%s" % lang,
           os.path.join(CURRENT_DIR, "%s.po" % lang),
           os.path.join(CURRENT_DIR, "%s.pot" % DOMAIN),
           )

    print(" ".join(cmd))
    process = subprocess.Popen(cmd)
    process.wait()


def main():
    if len(sys.argv) > 1:
        for lang in sys.argv[1:]:
            po = os.path.join(CURRENT_DIR, lang + '.po')

            if os.path.exists(po):
                process_po(po)
    else:
        for po in os.listdir(CURRENT_DIR):
            if po.endswith(".po"):
                process_po(po)


if __name__ == "__main__":
    print("\n\n *** Running %r *** \n" % __file__)
    main()
