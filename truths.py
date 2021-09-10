#!/usr/bin/env python
#
# Copyright 2016 Trey Morris
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

import itertools
from prettytable import PrettyTable
import re


class Gob(object):
    pass


class Truths(object):
    def __init__(self, base=None, phrases=None, headers=None, ints=True):
        if not base:
            raise Exception('Base items are required')
        self.base = base
        self.phrases = phrases or []
        self.ints = ints
        self.headers = headers
        if not headers:
            headers = phrases

        # generate the sets of booleans for the bases
        self.base_conditions = list(itertools.product([True, False],repeat=len(base)))

        # regex to match whole words defined in self.bases
        # used to add object context to variables in self.phrases
        self.p = re.compile(r'(?<!\w)(' + '|'.join(self.base) + ')(?!\w)')

    def calculate(self, *args):
        # store bases in an object context
        g = Gob()
        for a, b in zip(self.base, args):
            setattr(g, a, b)

        # add object context to any base variables in self.phrases
        # then evaluate each
        eval_phrases = []
        for item in self.phrases:
            item = self.p.sub(r'g.\1', item)
            eval_phrases.append(eval(item))

        # add the bases and evaluated phrases to create a single row
        row = [getattr(g, b) for b in self.base] + eval_phrases
        if self.ints:
            return [int(item) for item in row]
        else:
            return row

    def __str__(self):
        t = PrettyTable(self.base + self.phrases)
        for conditions_set in self.base_conditions:
            t.add_row(self.calculate(*conditions_set))
        return str(t)
    
    #RandomTT Author: added this because PrettyTables objects are easier to use than simple string
    #takes separate list of strings for column headers
    def just_table(self):
        t = PrettyTable(self.base + self.headers)
        for conditions_set in self.base_conditions:
            t.add_row(self.calculate(*conditions_set))
        return t