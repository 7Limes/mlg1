# TODO

## Features
- arrays
- importing files

## Bugs
- function call identitfier validation seems to not be working
- function calls within expressions may fail at times
  - if a function is called from 2 different locations, the registers it uses may conflict with the expression's registers
  - Solutions:
    - When parsing a function, check all calls to that function and determine if registers are used when calling it. If so, then only use the unused ones.