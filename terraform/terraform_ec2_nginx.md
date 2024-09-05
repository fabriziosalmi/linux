```
provider "aws" {
  region = "eu-south-1"
}

resource "aws_instance" "instance_a" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  availability_zone = "eu-south-1a"

  connection {
    host = "backend"
    type = "tcp"
    port = 443
  }

  tags = {
    Name = "instance_a"
  }

  user_data = <<-EOF
  #!/bin/bash
  sudo apt-get update
  sudo apt-get install -y docker.io
  sudo docker run -p 443:443 --name nginx_reverse_proxy -d nginx:latest
  EOF
}

resource "aws_instance" "instance_b" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  availability_zone = "eu-south-1b"

  connection {
    host = "backend"
    type = "tcp"
    port = 443
  }

  tags = {
    Name = "instance_b"
  }

  user_data = <<-EOF
  #!/bin/bash
  sudo apt-get update
  sudo apt-get install -y docker.io
  sudo docker run -p 443:443 --name nginx_reverse_proxy -d nginx:latest
  EOF
}

resource "aws_eip" "instance_a_eip" {
  instance = aws_instance.instance_a.id
}

resource "aws_eip" "instance_b_eip" {
  instance = aws_instance.instance_b.id
}
```
