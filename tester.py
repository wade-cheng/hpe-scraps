import datetime
import os
import sys

from subprocess import run, TimeoutExpired, CalledProcessError

###
### YOU MIGHT NEED TO CHANGE THE FOLLOWING
### --------------------------------------
### This program assumes that the program under test is called 'probXX.py' where XX is the problem id
###
### Run this program "FROM YOUR student_datasets DIRECTORY" by doing:
###
###   python3 tester.py XX
###
### where XX is the 2-digit problem id
###

if len(sys.argv) < 2:
    print("Usage (run this program from the student_datasets directory):")
    print("   python tester.py <two-digit-problem-id>")
    print()
    quit()

prob_id = sys.argv[1]                    # The 2-digit problem id

python_exec = 'python'                   # Change this if you run python using different executable, e.g., python3

prog_under_test = f'./{prob_id}.py'    # If you want to put your probXX.py in another directory, you need to change it over here.
                                         # For example, if you have:
                                         # - a directory called CodeWars2023 where you want to put your solutions under, and
                                         # - a directory called CodeWars2023/student_datasets where you have all the test data for the contest
                                         # Then you want to run this tester program from the CodeWars2023/student_datasets directory, but before
                                         # doing so, you need to change this prog_under_test to:
                                         # prog_under_test = f'../prob{prob_id}.py'

test_dir = '../d'  # We always assume for this contest, we will always run this program from the student_datasets as the current directory

testfile_prefix = f'prob{prob_id}'       # We assume each test file pertaining to the problem id is prefixed by 'probXX', if it is not, change this variable.

def print_all(input, output, expected_output):
    print()
    print("-----")
    print("INPUT")
    print("-----")
    for x in input:
      print(x)
    print("-------------------")
    print("YOUR PROGRAM OUTPUT")
    print("-------------------")
    for x in output:
      print(x)
    print("---------------")
    print("EXPECTED_OUTPUT")
    print("---------------")
    for x in expected_output:
      print(x)
    print("---------------")
    print()

def run_one(input_filename, input_data, expected_output):
    print(f"Running {input_filename} ... ", end="")

    res = 0
    seconds = 0.0
    try:
        start = datetime.datetime.now()
        proc = run([python_exec, prog_under_test], capture_output=True, input=input_data, timeout=10, check=True, text=True)
        delta = datetime.datetime.now() - start
        seconds = delta.total_seconds()

        if proc.stdout:
            output = proc.stdout.split('\n')
            if len(output) and output[-1] == '': output = output[:-1]

            line = 1
            for x, y in zip(output, expected_output):
                if x != y:
                    res = -3
                    print_all(input_data.split('\n'), output, expected_output)
                    print(f"Wrong Answer. Mismatched on line {line}!")
                    print(f"Expected: [{y}]")
                    print(f"Actual:   [{x}]")
                    break
                line += 1
            else:
                if len(output) < len(expected_output):
                    res = -3
                    print_all(input_data.split('\n'), output, expected_output)
                    print(f"Wrong Answer. Need more line(s), expected: [{expected_output[len(output)]}] on line {len(output)+1}")
                elif len(output) > len(expected_output):
                    res = -3
                    print_all(input_data.split('\n'), output, expected_output)
                    print(f"Wrong Answer. Too many lines, actual: [{output[len(expected_output)]}] on line {len(expected_output)+1}")
            if res == 0:
                print(f"OK {seconds} seconds")
        else:
            print("Wrong Answer. No output produced.")
            res = -3
    except TimeoutExpired:
        res = -1
        print("Time Limit Exceeded")
    except CalledProcessError as proc:
        res = -2
        if proc.stderr:
            print(proc.stderr)
        print("Runtime Error")
    return res, seconds

for filename in os.listdir(test_dir):
    if not filename.startswith(testfile_prefix): continue

    if filename.find('out') >= 0:
        with open(f"{test_dir}/{filename}") as f:
            expected_output = [line.rstrip() for line in f]

        input_file = filename.replace('out', 'in')
        input_data = None
        if os.path.isfile(f"{test_dir}/{input_file}"):
            with open(f"{test_dir}/{input_file}") as f:
                input_data = f.read()
        else:
            input_file = "<no-input>"

        res, seconds = run_one(input_file, input_data, expected_output)
        if res != 0:
            break

