##########################################################################################
# Connection à la machine distance
##########################################################################################

# Process standard
aws ec2 start-instances --instance-ids i-09b8b509f157dda30
ssh -i "/Users/thibaud/.ssh/MyFirstAWSKey.pem" ec2-user@ec2-54-164-234-223.compute-1.amazonaws.com
aws ec2 stop-instances --instance-ids i-09b8b509f157dda30