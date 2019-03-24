# Encoder/Decoder

Create a module called `encoder`, containing a class called `Encoder`.

* It should be able to 'encode' a given message, returning an encoded version of it.
* It should also be able to 'decode' a given message, returning the decoded version of it.

## Tests
1. Please run the install script for your platform before beginning to code.
2. Please run the test script for your platform to run the [unit tests](https://en.wikipedia.org/wiki/Unit_testing). We are using the popular [pytest](https://docs.pytest.org/en/latest/contents.html) testing framework for Python.
3. Add more code to fix problems reported by pytest. Once you've written some code, run the test script again.
4. Repeat steps 2-3 above until you get no errors reported. But be sure that your code *actually* does what it should - don't just make the tests pass!

## UI (User Interface)
* Build a CLI app that asks a user to input text, and prints out the encoded version of the text.
* Think of a good sentence to use as your secret message.
* Encode it using your app, then give **only the encoded message** to your opponents.
* Their task will be to try to crack your code as soon as possible.
* You will receive a similarly encoded message from your opponents, and you will have to try to crack their code.
* Good luck!