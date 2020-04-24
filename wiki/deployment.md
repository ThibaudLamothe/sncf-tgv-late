##########################################################################################
# Connection à la machine distance
##########################################################################################

# Process standard
aws ec2 start-instances --instance-ids i-06580f90f41384b2b
ssh -i "/Users/thibaud/.ssh/MyFirstAWSKey.pem" ec2-user@ec2-54-164-234-223.compute-1.amazonaws.com
aws ec2 stop-instances --instance-ids i-06580f90f41384b2b

scp -i "/Users/thibaud/.ssh/MyFirstAWSKey.pem" -r data ec2-user@ec2-54-164-234-223.compute-1.amazonaws.com:sncf-tgv-late/