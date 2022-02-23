# Wordle Solver
## Author: Leo

## Environment Requirements
* Python3 (Python2 is NOT accepted.)

## Demo Video
* [Link](https://youtu.be/_JfcOB2PsCU)

## Getting Started
1. clone the repo
```bash
git clone https://github.com/LeoTheBestCoder/wordle-solver
```

2. go into the directory
``` bash
cd wordle-solver
```

3. execute the python script **run.py** (Please ignore ```construct.py```)
```bash
python3 run.py
```
It should look like this.
![](readme_img/1.png)

Press ```ENTER``` to continue. 

> Later, if the result is `GREEN` (correct character + correct position), enter `0`. </br>
> If the result is `YELLOW` (correct character + wrong position), enter `1`. </br>
> If the result is `RED` (wrong character), enter `2`.


> **CAUTION!!!** </br>
> If the result isn't correctly entered, the program will be terminated right away. So, refer to the following example or [demo video](https://youtu.be/_JfcOB2PsCU), and be extremely careful when entering the result. 


It tells you to guess "laxer" as the first attempt, so enter `laxer` into the wordle game.

<img src=readme_img/2.png>
<img src=readme_img/3.png width = 70%>



The result is **`YELLOW YELLOW GRAY GRAY YELLOW`**, so enter **`11221`** in the terminal. Then, go back to website and guess next word, `gnarl`.

<img src=readme_img/4.png>
<img src=readme_img/5.png width = 70%>

The result is **`GRAY GRAY YELLOW GREEN YELLOW`**, so enter **`22101`** in the terminal. Then, go back to website and guess next word, `flora`.

<img src=readme_img/6.png>
<img src=readme_img/7.png width = 70%>

The result is **`GRAY GREEN GRAY GREEN GREEN`**, so enter **`20200`** in the terminal. Then, go back to website and guess next word, `ultra`.

<img src=readme_img/8.png>
<img src=readme_img/9.png width = 70%>

We got the correct answer!! Since the result is all **`GREEN`**, so enter **`00000`** in the terminal and the program will congratulate you!

<img src=readme_img/10.png>