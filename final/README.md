# IT3038C - Final Project

A simple, easy-to-use, watermarking tool made with Python.

## Built on Flask and Pillow

This project utilizes the Python Imaging Library (Pillow) to perform image manipulation.

There is also a basic Web Interface that is built on Flask.

### How can I use this myself?

This code is open-source and free to use, however I won't provide much help if you modify the source.

Clone this directory and make sure you have Flask and Pillow installed (pip install or pip3 install).

This has only been tested on Linux, I am not really sure if it will work on Windows.

You'll need to set some config options based on your needs. This is what I ran on my system:

```bash
export FLASK_APP=main.py
export FLASK_DEBUG=1
```

Lastly, here is what you run to start the application:

If running on a localhost:
```bash
flask run
```
If running from a server on your local network:
```
python3 -m flask run --host=<Your Host IP>
```

### Examples

Once, your server is running, open your browser to http://localhost:5000 or http://Server_IP_Address:5000

![Sample Image 1](https://raw.githubusercontent.com/visudo20179C/IT30308C/master/projects/final/img/ex1.JPG)

Choose an image from your filesystem and what text you wish to mark it with

![Sample Image 2](https://raw.githubusercontent.com/visudo20179C/IT30308C/master/projects/final/img/ex2.JPG)

View the image in the browser (right-click on it to save)

![Sample Image 1](https://raw.githubusercontent.com/visudo20179C/IT30308C/master/projects/final/img/ex3.JPG)

