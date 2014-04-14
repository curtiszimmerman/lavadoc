#!/usr/bin/python3
##
# @project LavaDoc Documentation Generator
# @doc python.docstring
"""LavaDoc is a general purpose documentation generator developed by 
Red Division Development. It is written in Python 3 and currently 
supports documentation for JavaScript, C/C++, PHP and Python. Running 
`lavadoc.py filename` a single HTML file named 'filename-doc.html' 
with the documentation contained therein. By running 
`lavadoc.py ./directory`, LavaDoc will generate a complete project 
documentation set in a subdirectory called 'lavadoc' with a root 
'index.html' file. Please note that if you intend to generate 
documentation for an entire project, your main source file (main.cpp, 
for example) must contain the @@project label, which anchors LavaDoc 
to that file in relation to the rest of your project.
"""
# @author Curtis Zimmerman
# @copyright (C)2014 Red Division Development
# @contact contact@reddivision.net
# @license GPLv3
# @version 0.0.4-alpha
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
# @license GPLv3
# @version 0.0.4-alpha
# @todo Integrate command-line options.
##
# @task input Accept source code input file and verify code type.
# @task parse Parse source code.
# @task genDoc Generate source code documentation.
# @task output Output documentation file.

import argparse
import re
import sys
# ldclasses.py brings the document objects into this space
import ldclasses

## @variable string lavadoc version
__version__ = 'v0.0.4-alpha'

##
# @function make_parser
# @returns parser object
def make_parser():
    ## @doc python.docstring
    """Make argument parser object and return it for parsing.
    """
    parser = argparse.ArgumentParser(
        description='LavaDoc Source Code Documentation Generator',
        usage='lavadoc.py [options] [basefile]'
    )
    parser.add_argument('--css',
        help='css template of documentation output'
    )
    parser.add_argument('--html',
        help='html template of documentation output'
    )
    parser.add_argument('basefile',
        help='file used for root of project tree (e.g. main.c)',
        metavar='basefile'
    )
    parser.add_argument('-v', '--version',
        action='version',
        version='lavadoc.py '+__version__+' by curtis.zimmerman@gmail.com'
    )
    return parser

##
# @function output_content
# @param object output object constructed by parse_file()
# @returns int status of operation
def output_content( output_object ):
    ## @doc python.docstring
    """ Output the constructed content object to web content.
    """
    return 0

##
# @function parse_file
# @param string name of file to parse
# @returns object output object
def parse_file( infile ):
    ## @doc python.docstring
    """Parse input file.
    """
    output = base_object
    infile_handle = open(infile, 'r')
    infile_data = infile_handle.readlines()
    for line in infile_data:   
         #foo
        sysprint(line)
    return output

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

def main():
    ## @doc python.docstring
    """Entry point orchestrating what module does when run as script.
    """
    parser = make_parser()
    args = parser.parse_args()
    output = parse_file(args.basefile)
    #status = output_content(output)
    sys.exit(status or 0)

if __name__ == "__main__":
    main()

#EOF