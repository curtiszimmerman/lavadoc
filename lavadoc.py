#!/usr/bin/python3
##
# @project LavaDoc Documentation Generator
# LavaDoc is a general purpose documentation generator developed by 
# Red Division Development. It is written in Python 3 and currently 
# supports documentation for JavaScript, C/C++, PHP and Python. Running 
# `lavadoc.py filename` a single HTML file named 'filename-doc.html' 
# with the documentation contained therein. By running 
# `lavadoc.py ./directory`, LavaDoc will generate a complete project 
# documentation set in a subdirectory called 'lavadoc' with a root 
# 'index.html' file. Please note that if you intend to generate 
# documentation for an entire project, your main source file (main.cpp, 
# for example) must contain the @@project label, which anchors LavaDoc 
# to that file in relation to the rest of your project.
# @copyright (C)2014 Red Division Development
# @contact contact@reddivision.net
# @license BSD3
# @version 0.0.2a
# @todo Create Python Module from this project.
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
# @version 0.1.0
# @todo Integrate command-line options.
##
# @task input Accept source code input file and verify code type.
# @task parse Parse source code.
# @task genDoc Generate source code documentation.
# @task output Output documentation file.

import argparse
import re
# ldclasses.py brings the document objects into this space
import ldclasses

## @variable string lavadoc version
__version__ = 'v0.0.2-alpha'

##
# @function make_parser
# create argument parser
# return parser object
def make_parser():
  """Make argument parser object and return it for parsing
  """
  parser = argparse.ArgumentParser(
    description='LavaDoc Source Code Documentation Generator',
    usage='lavadoc.py [OPTIONS] [BASEFILE]'
  )
  parser.add_argument('-c', '--css',
    const=False,
    default=False,
  #  dest=cssfile,
    help='css template of documentation output',
    nargs='?',
    type=argparse.FileType('r')
  )
  parser.add_argument('-t', '--html',
    const=False,
    default=False,
  #  dest=htmlfile,
    help='html template of documentation output',
    nargs='?',
    type=argparse.FileType('r')
  )
  parser.add_argument('basefile',
    help='file used for root of project tree (e.g. main.c)',
    metavar='basefile',
    nargs=1,
    type=argparse.FileType('r')
  )
  parser.add_argument('-v', '--version',
    action='version',
    version='lavadoc.py '+__version__+' by curtis.zimmerman@gmail.com'
  )
  return parser

def sysprint( data ):
  sys.stdout.write(data)
  sys.stdout.flush()

def main():
  """Entry point orchestrating what module does when run as script
  """
  parser = make_parser()
  args = parser.parse_args()

  infile = open(args.basefile, 'r')
  indata = infile.read()

  with infile.readline() as line:
    #foo
    print(line)

if __name__ == "__main__":
  main()

#EOF