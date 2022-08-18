# smart_stack

## What is that project?
This project will be used to absorve and devolop more things about financial data management

## Main ideas
This is our first scrath of a lot of ideas for our aplication

![first_ideas](https://github.com/MateusMartins/smart_stack/blob/development/documentation/brain_storming.png)

## Team 
- Mateus Martins Ferreira | @MateusMartins | mateusmferreira@live.com
- Ariel Vaz de Alcantara Marinho | 
@arielmarinho | arielmarinho1@gmail.com


### Python Libraries
    pandas
    lxml

### How to use
##### Windows users
###### Install WSL
    wsl --install
###### make
    sudo apt install make
###### Docker
    sudo apt-get update
    sudo apt-get install ca-certificates curl gnupg lsb-release
    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    echo   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \ $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
    apt-cache madison docker-ce
    sudo apt-get install docker-ce=5:20.10.17~3-0~ubuntu-focal docker-ce-cli=5:20.10.17~3-0~ubuntu-focal containerd.io docker-compose-plugin
    sudo groupadd docker
    sudo usermod -aG docker $(whoami)
    sudo service docker start
    sudo docker run hello-world

### Recomended extensions on vscode
    Black
    Rainbow brackets
    Markdown Preview Enhanced
    Makefile Tools
