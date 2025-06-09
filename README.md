# mlg1

A Mid Level complexity language for developing [g1](https://github.com/7Limes/g1) programs.

Main Caveats:
- No stack frames (no recursion allowed)
- While loops only


## Documentation

Like g1, mlg1 contains two code entrypoints: `start` and `tick`.
`start` is called once when the program is run, and `tick` is called `tickrate` times every second.
The `start` function is optional, but `tick` is not.


Here's the basic layout of a program:
```
[meta variables]

[includes]

[file loading]

[constant definitions]

[functions]
```

As an example, here's a program that fills the window with white every tick.
```
#width 100
#height 100
#tickrate 60

fn tick() {
    color(255, 255, 255)
    rect(0, 0, WIDTH, HEIGHT)
}
```


### Meta Variables

Meta variables are denoted with a `#` character, followed by an identifier and an integer.
Here's a list of valid meta variables:

- `#width` - The width of the window (default: 100)
- `#height` - The height of the window (default: 100)
- `#tickrate` - The rate at which `tick` will be called. (default: 60)
- `#memory` - The amount of additional memory to allocate for the program. (default: 0)


### Including

Functions and variables from other files can be included using the `include` directive:
```
// === main.mlg1 ===
include "math"

fn start() {
  let result = do_math(1, 2, 3)
  print(result)  // 7
}

// === math.mlg1 ===
fn do_math(a, b, c) {
  return a + b * c
}

```


### File Loading

Files can be loaded by specifying an identifier and file path:

```
$PLACEHOLDER_IMG "assets/placeholder.png"
```

The identifier will be registered as a constant variable containing the address of the loaded file. To access the data, use the `get` function.
The compiler will output a `.g1d` file alongside the code file that can be used with the assembler.

### Builtin Functions

- `color(r, g, b)`
  - Set the current color.
- `point(x, y)`
  - Draw a single pixel.
- `line(x1, y1, x2, y2)`
  - Draw a line.
- `rect(x, y, width, height)`
  - Draw a rectangle.
- `get(address)`
  - Get a value from open memory.
  - Requires that `#memory` is set to something greater than `0` or a file is loaded into memory.
- `set(address, value)`
  - Set a value in open memory.
  - Requires that `#memory` is set to something greater than `0` or a file is loaded into memory.

