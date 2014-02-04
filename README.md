LavaDoc
=======

The LavaDoc Source Code Documentation Generator is written in Python 3 with a vision to use intuitive markup inside source code comments to generate simple, functional documentation.

Here's an example showing the most basic syntax and features of LavaDoc's comment markup and functionality:

````
/**
 * @project AwesomeProject
 * This is the description of AwesomeProject.
 * @file awesomeproject.c
 * This is the description of the source file for AwesomeProject.
 * @copyright (C)2100 Awesome Programmer
 * @contact awesome.programmer@example.com
 * @license BSD3
 * @version 1.0
 */

/// @todo the first thing on the to-do list, and showing 
//. the use of multi-line documentation markup, making it 
//. possible to write a lot of stuff using slash comments
/// @todo the second thing on the to-do list
//! @todo the third thing (but it's important!)
/// @fix the operation of this code

/**
 * @function awesomeProject
 * This is the description of this function.
 * @param int description of the input parameter
 * @returns int description of the return value
 * @special This is a special note associated with with the 
 * documentation for the awesomeProject() function.
 */
int awesomeProject( int things ) {
  return ++things;
}

/**
 * @special This specific note will appear in the docs that 
 * are automatically generated for special functions like 
 * main(), which normally use the @file or @project labels 
 * to construct their documentation.
 */
int main( int argc, char **argv ) {
  int stuff = 0;
  /// @task this label describes a block of documentation
  //. that may help decipher particularly confusing code
  stuff = awesomeProject(stuff);
  printf("Awesome Project has %d things!", stuff);
  return 0;
}
````
