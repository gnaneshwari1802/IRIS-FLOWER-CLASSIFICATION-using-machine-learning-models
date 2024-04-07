# IRIS-FLOWER-CLASSIFICATION-using-machine-learning-models
# Software And Tools Requirements
1. [Github Account](https://github.com)
2. [Hugging Face](https://www.huggingface.com/)
3. [VSCodeIDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

Create a new environment

```
conda create -p venv python==3.10.14 -y

```

Activating Environment

```
conda activate venv/

```

Install Requirements

```

pip install -r requirements.txt

```
Docker image run steps

```
docker build -t flask .
docker run  -it -p 7860:7860 flask

docker ps

```
Hugging face deployment steps
https://huggingface.co/docs/transformers/model_doc/pegasus

```

pip install transformers

pip install torch
import torch
git clone https://github.com/huggingface/transformers.git
huggingface-cli login 

```
Configure user name

```
git config --global user.name "Gnaneshwari"
git config --global user.name

```

Configure user email

```
git config --global user.email "gnaneshwari.m2009@gmail.com"
git config --global user.email 

```

Adding Files to github

```
git init

git add requirements.txt     
git add .

```

Checking the Status of git push

```
git status

```

Commit files to git

```
git commit -m "This commit includes requirements.txt and readme files"

```

Config email for first time

```
git config --global user.email "gnaneshwari.m2009@gmail.com"

```

Pushing files in git

```
git push origin main

```

To Validate Json

```
https://jsonlint.com/

```
