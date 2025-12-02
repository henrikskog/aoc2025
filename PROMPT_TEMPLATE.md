Solve Advent of Code 2025 Day {DAY} Part {PART} in {LANGUAGE}.

## Setup
1. Create the solution in `day-{DAY}/vibe/{LANGUAGE}/`
2. Fetch input using: `curl 'https://adventofcode.com/2025/day/{DAY}/input' -b 'session={SESSION_ID}' -o input.txt`
3. Create a Dockerfile that:
   - Uses an appropriate base image for {LANGUAGE}
   - Installs all dependencies
   - Copies and runs the solution
   - Prints the answer to stdout

fetch description using 
curl 'https://adventofcode.com/2025/day/{DAY}' \
        -b 'session={SESSION_ID}'

## Code Requirements
- Write the most **idiomatic** {LANGUAGE} code possible
- Use language-specific patterns, idioms, and best practices
- Prefer the standard library where appropriate
- Add brief comments explaining non-obvious idioms
- Name the solution file idiomatically for the language (e.g., `solve.py`, `solve.clj`, `main.go`, `Solution.hs`)

## Verification
The expected answer is: {ANSWER}
Verify your solution outputs this exact answer.

## Execution
Create a `run.sh` script that:
```bash
#!/bin/bash
docker build -t aoc-day{DAY}-{LANGUAGE} . && docker run --rm aoc-day{DAY}-{LANGUAGE}
```

## Example Structure
```
day-{DAY}/vibe/{PART}/{LANGUAGE}/
├── Dockerfile
├── run.sh
├── input.txt
├── solution.{ext}
└── README.md (brief notes on idioms used)
```


Think about stuff like this:

- **Rust**: "Use iterators, Result/Option chaining, no unwrap in main logic"
- **Haskell**: "Use applicative/monadic parsing, point-free where readable"
- **Go**: "Keep it simple, use standard library, proper error handling"
- **Clojure**: "Threading macros, transducers where appropriate, destructuring"
- **Python**: "List comprehensions, generators, dataclasses, type hints"
- **OCaml**: "Pattern matching, pipelines, modules"
- **Elixir**: "Pipes, pattern matching, recursion over loops"
- **Zig**: "Comptime, slices, explicit allocators"
- **APL/J/K**: "Go full array programming, minimal explicit loops"