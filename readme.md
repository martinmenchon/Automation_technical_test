# Automation - Technical Test

## How to run it?

1. Move to the folder where you want to clone the repository<br>
	`cd folder/to/clone-into/`
2. Download repo<br>
    `git clone https://github.com/martinmenchon/Automation_technical_test.git`
3. Move to this folder<br>
	`cd Automation_technical_test`
4. Build container<br>
	`docker build -t selenium-python .`
5. Pull selenium container<br>
	`docker pull selenium/standalone-firefox`
6. Run selenium container<br>
	`docker run -d -p 5555:4444 -p 7900:7900 --shm-size 2g -e SE_NODE_MAX_SESSIONS=5 selenium/standalone-firefox:4.0.0-beta-3-20210426`
7. To run the exercises<br>
	`docker run -v $PWD/exercises:/exercises --net=host selenium-python <exercise>` <exercise> is the name of the exercise
    for example:
    `docker run -v $PWD/exercises:/exercises --net=host selenium-python exercise2`
8. If you want to see container you can use the path<br>
	`http://localhost:7900/` the password is "secret"