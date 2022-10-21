#!/bin/bash

#uses test_url from sharedlibrary that must be in path

apply () {
  terraform init -upgrade
  terraform plan
  terraform apply -auto-approve
}

cd ../create-cert
apply
cd -
apply

# return should be 
# public_ip = "18.219.218.110"


echo see if can access the url ${ip} and get Hello World from it

export passed_test=0

public_ips_of_asg=$(aws --region=us-east-2 ec2 describe-instances --instance-ids $(aws --region=us-east-2 autoscaling describe-auto-scaling-groups --auto-scaling-group-name terraform-20221016125635871100000002|grep -i instanceid|cut -d '"' -f 4)      --query 'Reservations[*].Instances[*].PublicIpAddress'      --output text) 


export lb_dnsname=$(terraform output alb_dns_name|cut -d '"' -f2)

echo ${lb_dnsname}



test () {
  for ip in ${public_ips_of_asg}
  do
    test_url "http://${ip}" "8080"
  done

  test_url "http://${lb_dnsname}" "80"
}

  test_url "https://${lb_dnsname}" "443"

  test_url "https://saturdaynightdj.com" "443"


test

  # add this to uniq test environment
# todo add in output for port#
# todo set timeout  curl
# add destroy
# add boto test to check state of things matches

echo  MAKE SURE enviroment is test environment right
echo sleep 5

destroy () {
  terraform destroy -auto-approve
}

destroy
cd ../create-cert
destroy
cd -

## to test lb


#  ./test_main.sh (test only)


# ab  -n 1000 terraform-asg-example-1010978256.us-east-2.elb.amazonaws.com:80/   |grep Failed

#delete an instance

#check errors and run test test only

# :successfully ran
