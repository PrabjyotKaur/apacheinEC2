from boto.ec2.connection import EC2Connection
import boto,os
import boto.ec2
import boto.ec2.cloudwatch
from pprint import pprint
import boto.manage.cmdshell
import paramiko,os
# aws_1='AKIAJWURUPRFI4HO4UPA'
# aws_2='ESswPWS104eO9w/2yltE9mt2qmPt2a1TmWbAw+sJ'
# ec2 = boto.connect_ec2('AKIAJWURUPRFI4HO4UPA', 'ESswPWS104eO9w/2yltE9mt2qmPt2a1TmWbAw+sJ')
# #ec2 = boto.ec2.connect_to_region('us-west-2b',aws_access_key_id=aws_1,aws_secret_access_key=aws_2);
        

                   
# # reservation = ec2.run_instances('ami-225f92b4b',
                                    # key_name=key_name,
                                    # security_groups=[group_name],
                                    # instance_type=instance_type)
                                 
# #print group.authorize
key_name='apcahekey'
key_extension='.ppk'
key_dir='~/.ssh',
conn = EC2Connection('AKIAJWURUPRFI4HO4UPA', 'ESswPWS104eO9w/2yltE9mt2qmPt2a1TmWbAw+sJ')
#conn = boto.ec2.connect_to_region('us-west-1','AKIAJWURUPRFI4HO4UPA','ESswPWS104eO9w/2yltE9mt2qmPt2a1TmWbAw+sJ');
key = conn.get_all_key_pairs(keynames=[key_name])[0]
print key
image = conn.get_all_images(image_ids='ami-0056c769')
print image
print "Spinning up instance. . ."
    # Launch the image using our desired settings.
reservation = image[0].run(key_name='apcahekey')
# # reservation = image[0].run(key_name='sadeep',
                            # # security_groups=['default'])
                            # # #instance_type='t1.micro')
print("we get this far before output freezes")
ins = reservation.instances[0]
ins.update()
print ins.state
# cmd_shell=True,
# if cmd_shell:
    # key_path = os.path.join(os.path.expanduser(key_dir),key_name+key_extension)
    # cmd = boto.manage.cmdshell.sshclient_from_instance(ins,
                                                          # 'C:\Users\pkaur\Desktop\keys',
                                                          # user_name='root')
                                                            




