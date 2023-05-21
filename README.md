# AWS Project of the subject Cloud Computing of the course of Computer Engineering of INSPER.
## Student: [Guilherme Fontana Louro](https://github.com/guifl2001)

## Project: AWS Lambda

Using AWS Lambda, batch, EC2, AWS ParallelCluster and API Gateway to create a machine learning contanier of production inside S3 bucket

![Schema](schema.png)

## Install Terraform

### Linux

```bash
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common
wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update
sudo apt-get install terraform
```

### Windows or Mac

[Follow the tutorial](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)

## Check Terraform version

```bash
terraform --version
```

## Configure AWS credentials

[Follow the tutorial](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)

create your access key and secret access key in the IAM service of AWS and save it in a safe place for later use.

## Install AWS CLI

[Follow the tutorial](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

## Check AWS CLI version

```bash
aws --version
```

if the answer is something like this:

```bash
aws-cli/2.11.21 Python/3.11.3 Linux/5.19.0-35-generic exe/x86_64.ubuntu.22 prompt/off
```

we are good to go!

## Configure AWS CLI

```bash
aws configure
```

now you will be asked to enter your access key and secret access key, enter them and then enter the region you want to use, in this case I will use us-east-1, and finally enter the output format, I will use json.

## Let's now test out Terraform and AWS CLI project

```bash
git clone https://github.com/guifl2001/AWS-lambda
```

Now with the project cloned, let's go to the project folder and run the following commands:

```bash
terraform init
```

```bash
terraform validate
```

With the validate command we can check if there are any errors in the code, if there are no errors we can proceed to the next step.



## References

- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Using Aws ParallelCluster Serveless API for Aws Batch](https://aws.amazon.com/pt/blogs/compute/using-aws-parallelcluster-serverless-api-for-aws-batch/)
- [Amazon API Gateway for HPC job submission](https://aws.amazon.com/pt/blogs/opensource/aws-api-gateway-hpc-job-submission/)
- [Deploy Serveless Aplications with AWS Lambda and API gateway](https://developer.hashicorp.com/terraform/tutorials/aws/lambda-api-gateway)
