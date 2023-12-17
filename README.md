# Bennu Official Homepage

- Official Homepage for Bennu
  - Formerly: https://bennu-official-hp.herokuapp.com/home/

***

## System Requirements

- Runtime and Component versions
  - Python : 3.11.5
  - Django : 5.0
    - Please follow [the official documents](https://docs.djangoproject.com/en/5.0/releases/5.0/) for further information
- `pip3` is used as package management: version `23.3.2`
- `pyenv`: `2.3.27` on macOS, M1 Apple Silicon

Please setup the runtime with version above, and basically code base here would be expected to run with `pyenv` for local development,
so it is recommended to install `pyenv` first with following [the docs](https://github.com/pyenv/pyenv).

***

## Running and debug locally

- Install dependencies
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
