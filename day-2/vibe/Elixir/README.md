# Advent of Code 2025 Day 2 Part 2 - Elixir Solution

## Idiomatic Elixir Patterns Used

### 1. **Pipes (`|>`) for Data Transformation**
The pipe operator chains function calls, making data flow explicit and readable:
```elixir
"input.txt"
|> File.read!()
|> String.trim()
|> String.split(",")
```
This reads left-to-right, transforming data through each step.

### 2. **Pattern Matching**
Used extensively for destructuring and control flow:
- Function heads: `def parse_range(range_str) when is_binary(range_str)`
- Case expressions: `case String.split(range_str, "-") do [start_str, end_str] -> ...`
- Tuple destructuring: `{start, end_val} = parse_range(...)`

### 3. **Enum Functions**
- `Enum.map/2`: Transform collections
- `Enum.filter/2`: Select elements matching a predicate
- `Enum.sum/1`: Aggregate numeric collections
- `Enum.any?/2`: Early termination when condition is found
- `Enum.all?/2`: Check if all elements satisfy a condition

### 4. **Guards**
Function clauses use guards for type checking and constraints:
```elixir
def invalid_id?(s) when is_binary(s)
def invalid_ids_in_range(a, b) when is_integer(a) and is_integer(b)
```

### 5. **Range Syntax**
Elixir ranges (`a..b`) are inclusive and lazy, perfect for iteration:
```elixir
a..b |> Enum.filter(...)
```

### 6. **String Processing**
- `String.slice/3`: Extract substrings with start position and length
- `String.split/2`: Split strings by delimiter
- `Integer.parse/1`: Parse integers with pattern matching
- `Integer.to_string/1`: Convert integers to strings

### 7. **Module Organization**
- Functions organized in a module (`Solve`)
- `@moduledoc` and `@doc` for documentation
- Clear separation of concerns (parsing, validation, aggregation)

### 8. **Algorithm: Divisibility Check**
Instead of using string splitting (which can have edge cases), the solution:
1. Checks if string length is divisible by prefix length
2. Verifies all parts match the prefix by slicing and comparing
This approach is more explicit and avoids regex/split edge cases.

## Running

1. Input is already fetched in `input.txt`

2. Run with Docker:
```bash
chmod +x run.sh
./run.sh
```

Or run directly (if Elixir is installed):
```bash
elixir solve.exs
```

## Expected Output
```
46270373595
```

