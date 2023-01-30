#!/bin/sh

interaction=trying_scenarios
tests=elements/tests

echo "Running interactions"
echo "=============================="
for file in "$interaction"/*
do
  echo "------------------------------"
  echo
  python $file
  echo
done

echo "Running tests"
echo "=============================="
echo
pytest $tests
