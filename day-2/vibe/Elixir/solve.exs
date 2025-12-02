#!/usr/bin/env elixir

# Advent of Code 2025 Day 2 Part 2 - Elixir Solution
#
# Idiomatic Elixir patterns used:
# - Pipes (|>) for data transformation pipelines
# - Pattern matching in function heads and case expressions
# - Enum functions (map, reduce, filter, sum) for collection processing
# - String functions and regex for pattern matching
# - Guards for function clauses
# - Function composition and partial application

defmodule Solve do
  @moduledoc """
  Solves AOC 2025 Day 2 Part 2: Find sum of invalid IDs (numbers with repeating patterns)
  across all ranges.
  """

  @doc """
  Checks if a string consists entirely of repeating a prefix pattern.

  Examples:
    - "1212" repeats "12" -> true
    - "111" repeats "1" -> true
    - "123" has no repeating pattern -> false

  Uses pattern matching and Enum.any? for early termination.
  """
  def invalid_id?(s) when is_binary(s) do
    len = String.length(s)
    # Need at least 2 characters to have a repeating pattern
    if len < 2 do
      false
    else
      # Try each possible prefix length from 1 to length-1
      1..(len - 1)
      |> Enum.any?(fn prefix_len ->
        # Check if length is divisible by prefix length
        if rem(len, prefix_len) == 0 do
          prefix = String.slice(s, 0, prefix_len)
          num_repeats = div(len, prefix_len)
          # Check if all parts match the prefix
          Enum.all?(1..(num_repeats - 1), fn i ->
            start_pos = i * prefix_len
            String.slice(s, start_pos, prefix_len) == prefix
          end)
        else
          false
        end
      end)
    end
  end

  @doc """
  Sums all invalid IDs in a range [a, b] (inclusive).

  Uses Enum.sum with Enum.filter for idiomatic collection processing.
  """
  def invalid_ids_in_range(a, b) when is_integer(a) and is_integer(b) do
    a..b
    |> Enum.filter(&invalid_id?(Integer.to_string(&1)))
    |> Enum.sum()
  end

  @doc """
  Parses a range string like "5529687-5587329" into {start, end}.

  Uses pattern matching on String.split result and Integer.parse.
  """
  def parse_range(range_str) when is_binary(range_str) do
    case String.split(range_str, "-") do
      [start_str, end_str] ->
        {start, _} = Integer.parse(start_str)
        {end_val, _} = Integer.parse(end_str)
        {start, end_val}

      _ ->
        raise ArgumentError, "Invalid range format: #{range_str}"
    end
  end

  @doc """
  Main entry point. Reads input, parses ranges, and sums invalid IDs.

  Demonstrates a complete pipeline using pipes:
  1. Read file
  2. Trim whitespace
  3. Split by commas
  4. Parse each range
  5. Sum invalid IDs in each range
  6. Sum all results
  """
  def main do
    "input.txt"
    |> File.read!()
    |> String.trim()
    |> String.split(",")
    |> Enum.map(&parse_range/1)
    |> Enum.map(fn {a, b} -> invalid_ids_in_range(a, b) end)
    |> Enum.sum()
    |> IO.puts()
  end
end

# Run when executed as a script
Solve.main()
