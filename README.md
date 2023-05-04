# Caesar cipher
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
<br>

The program uses the <b>Caesar cipher</b>, a simple encryption technique that substitutes each letter in the plaintext with a letter a fixed number of positions down the alphabet, to <b>encrypt and decrypt text</b> with a customizable shift value. 

The user can encrypt and decrypt text with a <b>customizable shift value</b> (ROT13, ROT47, or any other shift). The program will apply the selected transformation to the input text, and output the result.

The program provides the ability to <b>save information</b> from each session to a JSON file, or append it to existing one for future reference.

## Technologies
<ul>
<li>Python 3.11.2</li>
<li>Pytest 7.3.1</li>
</ul>

## Setup
To run this program, clone the repository and install dependencies:
```
git clone https://github.com/zuzannahertig/Caesar_cipher.git
pip install -r requirements.txt
```
