# Day 2 · Building a VPC by hand

![Resource map](<../../Vpc .PNG>)

**Built:** MyVPC (10.0.0.0/16) with 4 subnets across 2 AZs:
- Public-1A 10.0.1.0/24 · Public-1B 10.0.2.0/24 → Main RT (local + 0.0.0.0/0 → IGW)
- Private-1A 10.0.3.0/24 · Private-1B 10.0.4.0/24 → Private-RT (local only)

**Learned:**
- A subnet is "public" because of its route table, not the subnet itself
- AWS reserves 5 IPs per subnet (251 usable in a /24)
- Deleting an IGW leaves a blackhole route behind
- Teardown order matters: IGW → subnets → route tables → VPC

**Skipped on purpose:** NAT gateway (costs money hourly), launching EC2 (Week 3)
