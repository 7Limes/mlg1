# TODO

## Features
- Make the user pass in all files to compile instead of having the compiler find them
  - this is better because users won't have to compile from a specific directory every time
  - And the initial listener won't have to raise file not found errors
- Const arrays stored as data entries
- Omit unused globals and data entries
- Use function call tree to optimize local var allocation
  - Any two functions that are not present in the same branch may share local var space
- inline functions?
- better function call register use
  - if there's only 1 function call in an expression, it can use the return register
  - if there's more than 1, then we have to use the arithmetic registers
- Check for reserved names on constants and file load identifiers

- Option to include user-written comments in generated code

## Refactors
- Organize constants.py
- Make a new base token class that contains source file and source lines
  - FunctionToken will then extend this base class
  - All tokens now have access to their source information
  - Makes comment generation easier

## Bugs
- Duplicate string values create duplicate data entries
  - Just make them reference the same one
- trying to assign before declaration doesnt have a proper error message
- compiler should throw an error when you try to reference an undefined var, but it doesn't
- function calls within expressions may fail at times
  - if a function is called from 2 different locations, the registers it uses may conflict with the expression's registers
  - Solutions:
    - When parsing a function, check all calls to that function and determine if registers are used when calling it. If so, then only use the unused ones.