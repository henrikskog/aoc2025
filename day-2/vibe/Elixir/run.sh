#!/bin/bash

docker build -t aoc-day2-elixir . && docker run --rm aoc-day2-elixir && docker rmi aoc-day2-elixir

