# Bennu Official Homepage

- Official Homepage for Bennu

***

## System Requirements

- Runtime and Component versions
  - Python : 3.6.4
  - Django : 2.2.6
  - `pip3` is used as package management: version 19.2.3

***

## Running and debug locally

- Requirements
  - Install `pyenv`
    - Refer to GitHub repository and its descriptions
    - https://github.com/pyenv/pyenv
  - Setting up required packages with pip
    - `pip install -r requirements.txt`

- Run Django applications locally
  - Check Python & pip versions
    - `Python -V` & `pip -V`
      - This application would be run only under the environments described above
  - Run with local web server
    - `python manage.py runserver`
      - The default ports for djang use is `TCP/8000`
      - If you have already used TCP/8000, you could specify another one with the command : `python manage.py runserver <YOUR_LOCAL_PORT>`

***

## License

- This application is licensed by BSD License since basically using Django framework.
