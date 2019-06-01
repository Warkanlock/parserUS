<p align="center"><img src="https://github.com/Warkanlock/TaxCodeParser/blob/master/logo.png"></p>

<p align="center"> <b>A brief generic parser for the entire US Tax Code made by Ignacio Brasca.</b> </p>

## Usage

Go into root folder and open a terminal and throw this command:

```
    python main.py -h
```

As you can see, you can use any parameter that you want, you can skip one or use all of it.

#### Example code of using to get the part VI of the Title 26

```
python main.py -title 26 -subtitle A -chap 1 -subchap B -part VI
```

## Tools used

1. **AnyTree** (https://github.com/c0fec0de/anytree)

2. **BeautifulSoup**

## Installing

You need to run:

```
pip install -r requirements.txt
```

To install all the requirements
