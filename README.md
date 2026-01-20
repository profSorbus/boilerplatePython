# Boilerplate

Boilerplate is a standard repository that can be used to start any Python project for a backend application. It follows the architecture taught in class :

- a service layer which is a fastapi API that can be contacted via HTTP (main.py)
- a working layer which contains the code (nearly everything in core)
- a storage layer which contains the part that will connect you to the physical storage and manage objects (dbmanager / dbmodel)

## Installation

### 0 - Installing uv

You will need uv to install in the next parts. Check that you have uv installed by typing in your terminal : ```uv```.

- If you have it, you can move on to step1.

- If you don't have it : install it by following :

https://docs.astral.sh/uv/getting-started/installation/

If it is the first time installing uv, you might need to restart your terminal or even VScode.

### 1 - Install the virtual environment

- Open a terminal and make sure the terminal current directory is actually the boilerplatePython directory
- Type in the terminal : **```uv sync```** to install the packages

### 2 - Setup the configuration

In the app/conf directory, **copy the config_template.ini and rename it config.ini**. Open the file and fill in the correct configuration :
- the log path should be a path to a logs folder that exists
- the log_conf should be the path to the logging.ini file
- the db_type should remain sqlite
- the db_path should be a path to an empty database.db file that you created somewhere

In app/conf, **copy the logging_template.ini and rename it logging.ini** and leave it this way.

### 3 - Initialise the database

Make sure that the database.db is created at the place declared in the config.ini file.

- To initialise the database, run :

```bash
uv run app/utils/initDB.py
```

Run this command every time you want to reset the database.

## Usage

Launch the api :

```bash
uv run fastapi dev
```

You can then go to http://127.0.0.1:8000/docs to see the documentation and available methods of the application created.

## Contributing

This repository is not opened to contributions at the moment. I strongly advise you to fork this repository and make your own boilerplate out of it

## License

[MIT](https://choosealicense.com/licenses/mit/)

You can do basically anything using this code, even sell your application and close-source it. However, it comes with no warranty or liability from my side. You use this code at your own risk, and what you do with it is your own responsibility.

## Final advices

- I have made this readme with [makeareadme](https://www.makeareadme.com/) and advise you do the same when you create a new application. A repository without any readme will not be corrected.
- You should include tests in your application when possible
- I have included Python standard gitignore, if some files should not be commited (like a sqlite database ... for example !), you have to update the gitignore because I won't do it for you !
- Do not forget to update the requirements when you add a package : an incomplete package list will break the app and your users won't fix the list for you !
- Thinking and understanding what problem you are trying to solve before coding is not a choice, **it is mandatory**. If you have not done it first, close this repository, close your laptop, take a paper and a pencil and go back to conceiving your app. When the conception phase is finished, and you have a diagram, come back here.

Sincerely

Prof. Sorbus
