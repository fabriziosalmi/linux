```
provider "aws" {
  region = "eu-south-1"
}

data "aws_ip_ranges" "cloudflare" {
  service = "CLOUDFLARE"
}

resource "aws_security_group" "example" {
  name        = "allow-cloudflare"
  description = "Allow incoming traffic from Cloudflare IPs"
}

resource "aws_security_group_rule" "example" {
  count       = length(data.aws_ip_ranges.cloudflare.cidr_blocks)
  security_group_id = aws_security_group.example.id
  type        = "ingress"
  from_port   = 0
  to_port     = 65535
  protocol    = "tcp"
  cidr_blocks = [data.aws_ip_ranges.cloudflare.cidr_blocks[count.index]]
}
```
