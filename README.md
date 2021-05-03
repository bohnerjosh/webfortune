# webfortune

This is a repository for my Final Project for CMSC 190 DevOps course (Spring 2021)

The core of this repository features a web application that serves users outputs of the `fortune` and `cowsay` commands in Linux.

# Dependencies

This assumes you have `docker` installed.
In case of use of testing, this assumes you have `pytest` installed, as well as `virtualenv` if you do not have flask and its dependencies installed locally.

# Installation

To run this application in a docker container, run `docker build -t <NAME> .`, where `<NAME>` is the name of your docker image. This is your docker image.

To run the docker image in a container, run `docker run -dp <PORT>:5000 <NAME>`, where `<PORT>` is the port you want to run the application on, and where `<NAME>` is the name of your docker image.

When you are done with your application, don't forget to stop the container. You can check to see if your docker container is running by typing `docker ps`

After typing `docker ps`, look for the container ID associated with your docker container's `<NAME>` from before. Then, to stop your container, run `docker kill <ID>`, where `<ID>` is the container ID of your container.

# Running

In a web browser - go to `http://<IP>:<PORT>` to access the web application. `<IP>` is the IP of the machine running the application, and `<PORT>` is the port from the `docker run` command before.

`/` or `/fortune/` - gives the user the output of the `fortune` command.

`/cowsay/<MESSAGE>` - gives the user the output of the `cowsay` command, where `<MESSAGE>` is the text you want to pass to `cowsay`.

`/cowfortune/` - gives the user the result of the `fortune` command piped into the `cowsay` command.

# Testing
Make sure you have `flask` and its dependencies installed before testing yourself. 

Otherwise, make sure `virtualenv` is installed. To install flask and its dependencies, make sure you are in a virtual environment, and run `pip install -r requirements.txt`.

After making changes to appserver.py or adding tests yourself, you can test them with `pytest`. To do this, run `pytest <TEST_FILE>`, where `<TEST_FILE>` is the name of the python file that has the test code in it.
