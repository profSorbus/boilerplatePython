# Boilerplate

Boilerplate is a standard repository that can be used to start any Python project for a backend application. It follows the architecture taught in class : 
 
- a service layer which is a fastapi API that can be contacted via HTTP (main.py)
- a working layer which contains the code (nearly everything in core)
- a storage layer which contains the part that will connect you to the physical storage and manage objects (dbmanager / dbmodel)

## Installation

Use uv to install the requirements. If you don't know how to use uv or install it, go back to the first part of the lab.

You will need a uv virtual environment for this code to work.

To install the packages :

```bash
uv sync
```

- In app/conf, copy the config_template.ini and rename it config.ini and fill in the correct configuration.
- In app/conf, copy the logging_template.ini and rename it logging.ini and leave it this way.

run to initialise the database : 

```bash
uv run app/utils/initDB.py
```

## Usage

```bash 
uv run fastapi dev
```

You can then go to http://127.0.0.1:8000/docs to see the documentation and available methods of the application created.

## Contributing

This repository is not opened to contributions at the moment. I strongly advise you to fork this repository and make your own boilerplate : you can add a log manager, modify the data model ... 

## License

[MIT](https://choosealicense.com/licenses/mit/)

You can do basically anything using this code, even sell your application and close-source it. However, it comes with no warranty or liability from my side. You use this code at your own risk, and what you do with it is your own responsibility.

## Final advices

- I have made this readme with [makeareadme](https://www.makeareadme.com/) and advise you do the same when you create a new application. A repository without any readme will not be corrected. 
- You should include tests in your application when possible
- I have included Python standard gitignore, if some files should not be commited (like a sqlite database ... for example !), you have to update the gitignore because I won't do it for you !
- You can find the conda instructions [here](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf) if you are lost with virtual environments.
- Do not forget to update the requirements when you add a package : an incomplete package list will break the app and your users won't fix the list for you !
- Thinking and understanding what problem you are trying to solve before coding is not a choice, **it is mandatory**. If you have not done it first, close this repository, close your laptop, take a paper and a pencil and go back to conceiving your app. When the conception phase is finished, and you have a diagram, come back here.

Sincerely

Prof. Sorbus