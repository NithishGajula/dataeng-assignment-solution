# Data Engineering Coding Challenges

## Judgment Criteria

- Beauty of the code (beauty lies in the eyes of the beholder)
- Testing strategies
- Basic Engineering principles

## Problem 1

### Parse fixed width file

- Generate a fixed width file using the provided spec (offset provided in the spec file represent the length of each field).
- Implement a parser that can parse the fixed width file and generate a delimited file, like CSV for example.
- DO NOT use python libraries like pandas for parsing. You can use the standard library to write out a csv file (If you feel like)
- Language choices (Python or Scala)
- Deliver source via github or bitbucket
- Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
- Pay attention to encoding


## Steps to run the solution for Problem 1
To make it really easy for the evaluators to run this solution regardless of their operating system, I have provided a containerised way to run the exercise. To make use of this, you'll need to have Docker (or a free equivalent like Rancher or Colima) installed on your system.

To start the process, there is a Dockerfile in the root of the project. This defines a linux-based container that includes Python 3.11

To build the container:
```shell
docker build -t file-generator-from-fixed-width .
```

To run the container after building it:

_Mac or Linux, or Windows with WSL:_
```shell
docker run --rm -v $(pwd):/usr/src/app file-generator-from-fixed-width
```

_Windows (without WSL):_
```shell
docker run --rm -v %cd%:/usr/src/app file-generator-from-fixed-width
```


## Problem 2

### Data processing

- Generate a csv file containing first_name, last_name, address, date_of_birth
- Process the csv file to anonymise the data
- Columns to anonymise are first_name, last_name and address
- You might be thinking  that is silly
- Now make this work on 2GB csv file (should be doable on a laptop)
- Demonstrate that the same can work on bigger dataset
- Hint - You would need some distributed computing platform

## Choices

- Any language, any platform
- One of the above problems or both, if you feel like it.