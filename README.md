
# TEST MACH EIGHT

This is a technical test carried out for the company MACH EIGHT.

For this project we used the python programming language, specifically version 3.9.6, it is recommended that you use the same.

To run the project follow the steps below:


## Create Virtual Enviroment (OPTIONAL)

If you do not want to globally install the packages needed to run this project, you can create a virtualenv using the following command.

```bash
python -m venv venv
```

Then, you must activate the environment using the following command.

```bash
venv\Scripts\activate
```

If you want to disable the environment you can use the following command.

```bash
venv\Scripts\deactivate
```
## Installation

Install python dependencies

```bash
  pip install -r requirements.txt
```


## Execution

to run this project you must execute the main.py file followed by the `list_of_numbers` followed by the `target_sum` as shown in the following command.

```bash
python main.py {list_of_numbers} {target_sum}
```

`list_of_numbers` must be a comma-separated list of numbers and must not contain spaces.

`target_sum` must be an integer.

Here is an example of how it should be executed.

```bash
python main.py 1,9,5,0,20,-4,12,16,7 12
```



## Run Tests

In this project unit tests were added to test the functionality. to run them you must run the following command in the root of the project.

```bash
pytest test_pairs.py
```

If you want an output with more information you can execute the following command.

```bash
pytest -v test_pairs.py
```
## Support

For support, email carlos.escudero.corpas@gmail.com.


## Acknowledgments

Thank you for reading these instructions, greetings and blessings.