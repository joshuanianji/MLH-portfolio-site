# MLH Portfolio Site

Welcome to the MLH Fellowship! During Week 1, we worked with Flask to build a portfolio site. This site will be the foundation for activities we do in future weeks so spend time this week making it our own and reflect our personality!

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

*Note: The portfolio site will only work on your local machine while you have it running inside of your terminal. We'll go through how to host it in the cloud in the next few weeks!* 

## Inspiration
We were inspired by various designs we found on Figma, after which we decided to model one for ourselves based on the inspiration of others.

## What it does
The code stand-alone allows you to host a website on your computer, which is your portfolio with easy-to-change elements that allow it to be user-friendly in terms of changing the portfolio itself to match what you have individually.

## How we built it
We built it using a series of HTML files with their respective CSS files for styling all (except the hobby section which was written in tailwind css) the while having python flask as routing and object creation.

## Challenges we ran into
We had to learn flask from the beginning, which wasn't hard. After which we had to experience how GitHub works, such as its pull requests and its issues page. We then had to design the web pages themselves to make them look like professional portfolio websites. We also had to coordinate efforts among the 4 of us and assign each member's respective parts to be finished.

## Accomplishments that we're proud of
How the webpage looks, and how well we worked together.

## What we learned
how to create a portfolio website using flask

## What's next for Portfolio Template - Chad Wojak
Adding our individualized content within it, as well as making it look better.

### Contributors
Joshua Ji, Ailun Yu, Carrie Kam and Sunny Kim