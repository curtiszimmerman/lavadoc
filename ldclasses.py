#!/usr/bin/python3

##
# @file lavadoc.py
# The primary Python documentation generation script. It does the heavy 
# lifting of parser magic, documentation generation, and output 
# management.
# @arg filename.ext This is the source code input file that you wish to 
# generate documentation for.
# @arg /directory Alternatively, you may specify a directory containing 
# a project or collection of related source code files, and LavaDoc will 
# generate documentation for the entire project. Please note that your 
# main source file (main.cpp or index.php, for example) must contain the 
# @@project label, where the project itself is defined. LavaDoc will use 
# this main source file as the anchor for the rest of the documentation.
# @author Curtis Zimmerman
# @copyright (C)2014 Red Division Development
# @contact contact@reddivision.net
# @license http://www.reddivision.net/license.html
# @maintainer Curtis Zimmerman
# @version 0.1.0_prealpha
# @todo Integrate command-line options.

import sys

def sysprint( data ):
  sys.stdout.write(data)
  sys.stdout.flush()

##############################################################
##############################################################
#
# project
#   name
#   description
#   special*
#   todo*
#   +author*
#   +copyright*
#   +contact*
#   +license*
#   +maintainer*
#   +version*
# file
#   name
#   description
#   special*
#   todo*
#   =arg*
#   +author*
#   +copyright*
#   +contact*
#   +license*
#   +maintainer*
#   +version*
# class
#   name
#   description
#   special*
#   todo*
#   +inherits
#   +property
# function
#   name
#   description
#   special*
#   todo*
#   +class
#   +param
#   +returns
# task
#   name
#   description
#   special*
#   todo*
# variable
#   name
#   description
#   special*
#   type
#
##################################################
##################################################
#
# [ LABEL ]
#   (str) name
#   (str) description
#   (str) *special
#
# [ TODO ]
#   (array) *todo
#
# [ TYPE ]
#   (str) type
#
# [ CLASS ]
#   (str) *inherits
#   (array) *property
#
# [ FUNCTION ]
#   (str) *class
#   (array) param
#   (str) returns
#
# [ PROJECT ]
#   (str) *author
#   (str) *copyright
#   (str) *contact
#   (str) *license
#   (str) *maintainer
#   (str) *version
#
# [ FILE ]
#   (array) *arg
#
##################################################
##################################################
#
# LABEL = (task)
# LABEL + TYPE = (variable)
# LABEL + PROJECT = (project)
# LABEL + PROJECT + FILE = (file)
# LABEL + CLASS = (class)
# LABEL + FUNCTION = (function)
#
##################################################
##################################################


##################################################
##################################################

##
# @class
# this class blah blah blah
# @inherits none
# @property
# @property
class Label:
  def __init__( self, name, desc, spec ):
    self.name = name
    self.description = desc
    self.special = spec

class Type:
  def __init__( self, type ):
    Label.__init__(self, name, desc, spec)
    self.type = ''

