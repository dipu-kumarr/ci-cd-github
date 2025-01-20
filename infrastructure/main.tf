provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "app_instance" {
  ami           = "ami-00bb6a80f01f03502" # Amazon Linux 2
  instance_type = "t2.micro"

  tags = {
    Name = "CI-CD-App-Instance"
  }
}
