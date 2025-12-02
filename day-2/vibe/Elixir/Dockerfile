FROM elixir:1.17-alpine

WORKDIR /app

# Copy solution file
COPY solve.exs .

# Copy input file
COPY input.txt .

# Run the solution
CMD ["elixir", "solve.exs"]

