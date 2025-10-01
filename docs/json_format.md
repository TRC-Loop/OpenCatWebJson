# CatWeb Script JSON Format

**Full Credit (Made by) [someone (@sytesn)](https://discord.com/channels/1226224104370208860/1422195956824412331/1422196198194020382)**

## JSON Structure

### Root-Level Architecture

The CatWeb script format uses a **mandatory array wrapper** at the root level:

```json
[
  {
    "class": "script",
    "content": [...],
    "globalid": "script_main"
  }
]
```

**Critical Requirements:**
- Root MUST be an array (not an object)
- Multiple scripts can coexist in the array
- Each script operates independently but can share global variables

### Script Object Anatomy

```json
{
  "class": "script",           // Fixed value, identifies script type
  "content": [event_blocks...], // Array of event objects
  "globalid": "unique_id"      // Script-level unique identifier
}
```

## Event Block Specification

### Complete Event Structure

```json
{
  "y": "4695",                 // Vertical position (string numeric)
  "x": "4703",                 // Horizontal position (string numeric) 
  "globalid": "+!",            // Event unique ID (special characters allowed)
  "id": "0",                   // Event type identifier
  "text": ["When website loaded..."], // Event descriptor with parameters
  "actions": [action_objects...],     // Sequential actions array
  "width": "350",              // Visual width in editor
  "variable_overrides": [      // EXCLUSIVE to function definitions (id:6)
    {"value": "param1"},
    {"value": "param2"}
  ]
}
```

**CORRECTION:** The `warning` key does NOT exist in valid CatWeb JSON. Previous examples showing warnings were incorrect.

### Event Positioning System
- **Coordinates**: String-encoded numbers representing visual layout
- **Priority**: Events closer to workspace center execute first
- **Parallel Execution**: Multiple events can run simultaneously
- **Visual Organization**: Coordinates affect only editor display, not runtime behavior

### Special Event Properties

**Function Definition Events (ID: 6):**
```json
{
  "id": "6",
  "text": ["Define function", {"value": "funcName", "t": "string", "l": "function"}],
  "variable_overrides": [
    {"value": "arg1"},  // Local parameter names
    {"value": "arg2"}   // Created as l!arg1, l!arg2 in function body
  ],
  "actions": [...],     // Function implementation
  "width": "722"        // Typically wider for functions
}
```

## Action Block Deep Specification

### Action/Event IDs

#### Events

| ID | Event                            |
| -- | -------------------------------- |
| 0  | When website loaded...           |
| 1  | When `<button>` pressed...       |
| 2  | When `<key>` pressed...          |
| 3  | When mouse enters `<object>` ... |
| 5  | When mouse leaves `<object>` ... |
| 6  | Define function `<function>`     |
| 7  | When `<donation>` bought...      |
| 8  | When `<input>` submitted...      |
| 9  | When message received...         |
| 10 | When `<object>` changed...       |

#### Actions

| ID  | Action                                                                         |
| --- | ------------------------------------------------------------------------------ |
| 0   | Log `<any>`                                                                    |
| 1   | Warn `<any>`                                                                   |
| 2   | Error `<any>`                                                                  |
| 3   | Wait `<number>` seconds                                                        |
| 4   | Redirect to `<string>`                                                         |
| 5   | Play audio `<id>` → `<variable?>`                                              |
| 7   | Stop all audio                                                                 |
| 8   | Make `<object>` invisible                                                      |
| 9   | Make `<object>` visible                                                        |
| 10  | Set `<object>` text to `<string>`                                              |
| 11  | Set `<variable>` to `<any>`                                                    |
| 12  | Increase `<variable>` by `<number>`                                            |
| 13  | Decrease `<variable>` by `<number>`                                            |
| 14  | Multiply `<variable>` by `<number>`                                            |
| 15  | Divide `<variable>` by `<number>`                                              |
| 16  | Round `<variable>`                                                             |
| 17  | Floor `<variable>`                                                             |
| 18  | If `<any>` is equal to `<any>`                                                 |
| 19  | If `<any>` is not equal to `<any>`                                             |
| 20  | If `<any>` is greater than `<any>`                                             |
| 21  | If `<any>` is lower than `<any>`                                               |
| 22  | Repeat `<number>` times                                                        |
| 23  | Repeat forever                                                                 |
| 24  | Break                                                                          |
| 25  | end                                                                            |
| 26  | Play looped audio `<id>` → `<variable?>`                                       |
| 27  | Set `<var>` to random `<n> - <n>`                                              |
| 30  | Get text from `<input>` → `<variable>`                                         |
| 31  | Set `<property>` of `<object>` to `<any>`                                      |
| 32  | Broadcast `<message>` across page                                              |
| 33  | Broadcast `<message>` across site                                              |
| 37  | If `<string>` contains `<string>`                                              |
| 38  | If `<string>` doesn't contain `<string>`                                       |
| 39  | Get `<property>` of `<object>` → `<variable>`                                  |
| 40  | Raise `<variable>` to the power of `<number>`                                  |
| 41  | `<variable>` modulo `<number>`                                                 |
| 42  | Sub `<variable>` `<start> - <end>`                                             |
| 43  | Replace `<string>` in `<variable>` by `<string>`                               |
| 44  | If `<variable>` AND `<variable>`                                               |
| 45  | If `<variable>` OR `<variable>`                                                |
| 46  | If `<variable>` NOR `<variable>`                                               |
| 47  | If `<variable>` XOR `<variable>`                                               |
| 48  | Get length of `<string>` → `<variable>`                                        |
| 49  | Duplicate `<object>` → `<variable>`                                            |
| 50  | Delete `<object>`                                                              |
| 51  | Get local username → `<variable>`                                              |
| 52  | Get local user ID → `<variable>`                                               |
| 53  | Get local display name → `<variable>`                                          |
| 54  | Create table `<table>`                                                         |
| 55  | Set entry `<entry>` of `<table>` to `<any>`                                    |
| 56  | Get entry `<entry>` of `<table>` → `<variable>`                                |
| 57  | Split `<string>` `<separator>` → `<table>`                                     |
| 58  | Parent `<object>` under `<object>`                                             |
| 59  | Get length of `<array>` → `<variable>`                                         |
| 63  | Run function in background `<function>` `<tuple>`                              |
| 66  | Set entry `<entry>` of `<table>` to `<object>`                                 |
| 67  | Get query string parameter `<string>` → `<variable>`                           |
| 68  | Get unix timestamp → `<variable>`                                              |
| 69  | Lower `<string>` → `<variable>`                                                |
| 70  | Upper `<string>` → `<variable>`                                                |
| 71  | Format current date/time `<format>` → `<variable>`                             |
| 72  | Format from unix `<number>` `<format>` → `<variable>`                          |
| 73  | Set volume of `<variable>` to `<number>`                                       |
| 74  | Stop audio `<variable>`                                                        |
| 75  | Pause audio `<variable>`                                                       |
| 76  | Resume audio `<variable>`                                                      |
| 77  | Set speed of `<variable>` to `<number>`                                        |
| 78  | Ceil `<variable>`                                                              |
| 79  | If left mouse button down                                                      |
| 80  | If middle mouse button down                                                    |
| 81  | If right mouse button down                                                     |
| 82  | If `<key>` down                                                                |
| 83  | Get tick → `<variable>`                                                        |
| 84  | Get viewport size → `<x> <y>`                                                  |
| 85  | Get cursor position → `<x> <y>`                                                |
| 87  | Run function `<function>` `<tuple>` → `<variable?>`                            |
| 88  | Tween `<property>` of `<object>` to `<any>` - `<time>` `<style>` `<direction>` |
| 89  | Insert `<any>` at position `<number?>` of `<array>`                            |
| 90  | Delete entry `<entry>` of `<table>`                                            |
| 91  | Remove entry at position `<number?>` of `<array>`                              |
| 92  | If `<variable>` exists                                                         |
| 93  | If `<variable>` doesn't exist                                                  |
| 94  | Set `<property>` of `<variable>` to `<any>`                                    |
| 95  | Get `<property>` of `<variable>` → `<variable>`                                |
| 96  | Delete `<variable>`                                                            |
| 97  | Get parent of `<object>` → `<variable>`                                        |
| 98  | Find ancestor named `<string>` in `<object>` → `<variable>`                    |
| 99  | Find child named `<string>` in `<object>` → `<variable>`                       |
| 100 | Find descendant named `<string>` in `<object>` → `<variable>`                  |
| 101 | Get children of `<object>` → `<table>`                                         |
| 102 | Get descendants of `<object>` → `<table>`                                      |
| 103 | If `<object>` is ancestor of `<object>`                                        |
| 104 | If `<object>` is child of `<object>`                                           |
| 105 | If `<object>` is descendant of `<object>`                                      |
| 106 | Set `<object>` image to `<id>`                                                 |
| 107 | Set `<object>` image to avatar of `<userid>` `<resolution?>`                   |
| 108 | If dark theme enabled                                                          |
| 109 | Concatenate `<string>` with `<string>` → `<variable>`                          |
| 110 | Join `<array>` using `<string>` → `<variable>`                                 |
| 112 | else                                                                           |
| 113 | Iterate through `<table>` ({l!index},{l!value})                                |
| 114 | Run math function `<function>` `<tuple>` → `<variable>`                        |
| 115 | Return `<any>`                                                                 |
| 116 | Get server unix timestamp → `<variable>`                                       |
| 117 | Get URL → `<variable>`                                                         |
| 118 | Get timezone → `<variable>`                                                    |
| 119 | Convert `<hex>` to RGB → `<variable>`                                          |
| 120 | Convert `<hex>` to HSV → `<variable>`                                          |
| 121 | Convert `<RGB>` to hex → `<variable>`                                          |
| 122 | Convert `<HSV>` to hex → `<variable>`                                          |
| 123 | Lerp `<hex>` to `<hex>` by `<alpha>` → `<variable>`                            |
| 124 | `<comment>`                                                                    |

#### ID Collisions

Since events and actions have separate ID indexes, please be wary that you should use an event ID for events, and action ID for actions, here's a table of ID collisions:

| ID | Event                            | Action                            |
| -- | -------------------------------- | --------------------------------- |
| 0  | When website loaded...           | Log `<any>`                       |
| 1  | When `<button>` pressed...       | Warn `<any>`                      |
| 2  | When `<key>` pressed...          | Error `<any>`                     |
| 3  | When mouse enters `<object>` ... | Wait `<number>` seconds           |
| 5  | When mouse leaves `<object>` ... | Play audio `<id>` → `<variable?>` |
| 7  | When `<donation>` bought...      | Stop all audio                    |
| 8  | When `<input>` submitted...      | Make `<object>` invisible         |
| 9  | When message received...         | Make `<object>` visible           |
| 10 | When `<object>` changed...       | Set `<object>` text to `<string>` |

### Core Action Structure

```json
{
  "id": "18",                    // Action type identifier
  "text": [                      // Mixed array of strings and parameter objects
    "If ",
    {"value": "var1", "t": "string", "l": "any"},
    " is equal to ",
    {"value": "var2", "t": "string", "l": "any"}
  ],
  "globalid": "rU"              // Action unique identifier
}
```

### Block Control Actions

**Conditional Blocks with Else:**
```json
// If-Else-End pattern
[
  {
    "id": "18",
    "text": ["If", {"value": "this", "l": "any", "t": "string"}, "is equal to", {"value": "that", "l": "any", "t": "string"}],
    "globalid": "Fo"
  },
  // Actions for true condition...
  {
    "id": "112",      // ELSE BLOCK
    "text": ["else"],
    "globalid": "3Q"
  },
  // Actions for false condition...
  {
    "id": "25",       // END BLOCK
    "text": ["end"], 
    "globalid": "v5"
  }
]
```

**Note on Else Blocks:** While `else` blocks provide organizational clarity, they consume an action slot. For maximum efficiency, consider using multiple independent `if` conditions instead of `if-else` chains.

**Loop Structures:**
```json
[
  {
    "id": "22",
    "text": ["Repeat", {"value": "5", "t": "number"}, "times"],
    "globalid": "loop_start"
  },
  // Loop body actions...
  {
    "id": "25", 
    "text": ["end"],
    "globalid": "loop_end"
  }
]
```

### Parameter Object Specification

#### Complete Type System

| Type | JSON Representation | Validation Rules |
|------|---------------------|------------------|
| `any` | `{"value": "content", "t": "any", "l": "any"}` | Accepts any value, variables with `{}` |
| `string` | `{"value": "text", "t": "string", "l": "variable"}` | Converts input to string |
| `number` | `{"value": "123", "t": "number", "l": "any"}` | Non-numeric → 0 |
| `object` | `{"value": "Button1", "t": "object"}` | Must reference valid element |
| `variable` | `{"value": "varName", "t": "string", "l": "variable"}` | Validates variable existence |
| `tuple` | `{"value": [param1, param2...], "t": "tuple"}` | Max 6 parameters |

#### "Optional" types

Types that are not required to have **any values**. When this is the case, not setting the "value"  key won't lead to any unpredictable behaviors. To denote an optional type, add a question mark (?) at the end of the label ("l") key, without any modifications to the actual type ("t") field itself.

#### Types vs Labels

You might be wondering: "what's the difference between types and labels?", here's the actual differences: types make it so that only a specific data "type" gets accepted in an input field, while labels only describe what that value should represent. Of course, these are strict in CatWeb as well so you cannot make up your own label + type combination.

#### Advanced Parameter Patterns

**Object Reference Variants:**
```json
// Direct element selection
{"value": "SubmitButton", "t": "object"}

// Script parent reference  
{"value": "(parent)", "t": "object"}

// Object variable (runtime)
{"value": "{objVar}", "t": "object"}

// Scoped object variable  
{"value": "{o!scopedObj}", "t": "object"}
```

**Tuple Parameter Structure:**
```json
{
  "value": [
    {
      "value": "firstArg", 
      "t": "string", 
      "l": "any"
    },
    {
      "value": "secondArg", 
      "t": "number", 
      "l": "any"
    }
  ],
  "t": "tuple"
}
```

**Variable Scoping in Parameters:**
```json
// Global variable (any script)
{"value": "{globalVar}", "t": "any", "l": "any"}

// Object variable (same script)  
{"value": "{o!objectVar}", "t": "any", "l": "any"}

// Local variable (same event)
{"value": "{l!localVar}", "t": "any", "l": "any"}
```

## Complex Action Patterns

### Function Call with Tuples
```json
{
  "id": "87",
  "text": [
    "Run function",
    {"value": "calculate", "t": "string", "l": "function"},
    {
      "value": [
        {"value": "arg1", "t": "string", "l": "any"},
        {"value": "arg2", "t": "number", "l": "any"},
        {"value": "arg3", "t": "string", "l": "any"}
      ],
      "t": "tuple"
    },
    "→",
    {"value": "result", "l": "variable", "t": "string"}
  ],
  "globalid": "func_call"
}
```

### Table Operations with Iteration
```json
{
  "id": "113",
  "text": [
    "Iterate through",
    {"value": "dataTable", "t": "string", "l": "table"},
    "({l!index},{l!value})"  // Fixed local variables
  ],
  "globalid": "iterate_block"
}
// Followed by actions using {l!index} and {l!value}
```

### Property Manipulation
```json
{
  "id": "31",
  "text": [
    "Set",
    {"value": "BackgroundColor", "t": "string", "l": "property"},
    "of", 
    {"value": "TargetFrame", "t": "object"},
    "to",
    {"value": "#ff0000", "t": "string", "l": "any"}
  ],
  "globalid": "set_property"
}
```

## Special Action Types

### Comment Actions with Help Text
```json
{
  "id": "124",
  "text": [{"value": "This is a comment for documentation", "t": "string", "l": "comment"}],
  "globalid": "comment_1",
  "help": "Optional help text that appears in editor"
}
```

**CRITICAL NOTE:** The `help` key is ONLY valid for comment actions (ID: 124). Using it with any other action type will result in invalid JSON.

## JSON Validation Rules

### Structural Validation

**Required Fields:**
- All objects must have `globalid`
- Events require: `y`, `x`, `id`, `text`, `actions`, `width`  
- Actions require: `id`, `text`, `globalid`
- Scripts require: `class`, `content`, `globalid`

**Type Constraints:**
- Coordinates (`y`, `x`) must be string-encoded numbers
- IDs (`id`) must be string-encoded numbers matching known actions/events
- `globalid` must be unique across entire JSON
- `width` must be string-encoded number

### Forbidden Patterns
- `warning` key is NOT allowed in any object
- `help` key is ONLY allowed in comment actions (ID: 124)
- Invalid type combinations will cause JSON parsing errors

### Logical Validation

**Block Structure Rules:**
- Every block starter (if, repeat, iterate) must have matching `end`
- `else` (id:112) must be preceded by conditional and followed by `end`
- Function definitions cannot be nested
- Maximum 6 tuple parameters

**Variable Scope Rules:**
- Local variables (`l!`) only accessible within declaring event
- Object variables (`o!`) accessible within same script
- Global variables accessible across all scripts
- Function parameters become local variables in function body

## JSON Generation Guidelines

### ID Selection
- Use provided `ids.txt` for correct action/event IDs
- Block control IDs (18-25, 112) are critical for flow control
- Math operations (11-17, 27, 40-41, 78, 114) modify variables directly
- Object operations (8-10, 30-31, 39, 49-50, 106-108) require valid object references

### Global ID Generation
- Use short, unique strings with special characters
- Pattern: 2-3 character mix of letters, numbers, symbols
- Must be unique across entire JSON structure
- No specific algorithm required, just uniqueness

### Coordinate Strategy
- Increment `y` by 100-200 for vertical separation  
- Increment `x` by 350-400 for horizontal separation
- Maintain logical grouping through positioning
- Center important events for execution priority

### Efficiency Considerations
- **Else Blocks**: Use sparingly as they consume action slots (120 max per event)
- **Comments**: Use comment actions (ID: 124) for documentation when needed
- **Function Calls**: Balance between code organization and performance overhead

### Tips
- Try to put events closer to the center instead of near the top for accessibility, the scripting canvas is 9992*9992px in dimensions, and the fact that the scripting canvas is centered in the middle as a default

> Made by someone (discord: @sytesn)
