#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys, os
import codecs
from xml.etree import ElementTree as ET
from base import Base,ParserBase
from c_paser import CParser

#sbp_id class
class ParseSbpId(CParser):
    def __init__(self, node):
        super(ParseSbpId, self).__init__(node)
        self.name="ParseSbpId"

