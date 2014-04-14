#!/usr/bin/python3
##
# @file lavadoc.py
# @doc python.docstring
"""This library contains the classes used for creating documentation object
instances. It also contains the output object classes used in generating 
the documentation, and the object classes used in output templating in the 
absence of supplied HTML/CSS template files.
"""
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
# @version 0.0.2-alpha
# @todo Integrate command-line options.

import sys

##
# @function sysprint
# @param string data to print to standard output
# @returns int status of operation
def sysprint( data ):
    ## @doc python.docstring
    """Bare print specified data.
    """
	sys.stdout.write(data)
	sys.stdout.flush()

##########################################################################
##########################################################################
# Document Objects
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
##########################################################################
##########################################################################
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
##########################################################################
##########################################################################
#
# LABEL = (task)
# LABEL + TYPE = (variable)
# LABEL + PROJECT = (project)
# LABEL + PROJECT + FILE = (file)
# LABEL + CLASS = (class)
# LABEL + FUNCTION = (function)
#
##########################################################################
##########################################################################

##
# @class DocLabel
# @property string name name of the doc object
# @property string desc description of the doc object
# @property string spec special note about doc object
class DocLabel:
	## @doc python.docstring
	"""Base class for all documentation objects.
	"""
	def __init__( self, name, desc, spec ):
		self.name = name
		self.description = desc
		self.special = spec

##
# @class DocType
# @inherits DocLabel
# @property string type type of doc object
class DocType:
	## @doc python.docstring
	"""Class for variable object (inherits from DocLabel).
	"""
	def __init__( self, type ):
		DocLabel.__init__(self, name, desc, spec)
		self.type = ''

##########################################################################
##########################################################################
# Output Objects
#
# [PROJECT]
#   [PAGE]
#     [PARAGRAPH]
#       [LINE]
#
##########################################################################
##########################################################################

class OutputPage:
	def __init__( self, name ):
		self.page_name = name

class OutputProject:
	def __init__( self, name ):
		self.project_name = name

#EOF