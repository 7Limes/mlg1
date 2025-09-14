# TODO

## Features
- inline functions?
- better function call register use
  - if there's only 1 function call in an expression, it can use the return register
  - if there's more than 1, then we have to use the arithmetic registers
- Check for reserved names on constants and file load identifiers

- Option to include user-written comments in generated code


## Bugs
- compiler should throw an error when you try to reference an undefined var, but it doesn't
- function calls within expressions may fail at times
  - if a function is called from 2 different locations, the registers it uses may conflict with the expression's registers
  - Solutions:
    - When parsing a function, check all calls to that function and determine if registers are used when calling it. If so, then only use the unused ones.