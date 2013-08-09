import paramiko,os
class apache_server:

	def setconnection(self,instance,command1):
		client =  paramiko.SSHClient()
		client.load_system_host_keys()
	# Added the following line to get the connection going
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	# Had to find hostname from AWS Management Console
	# Converted RSA key sadeep.ppk to SSH2-DSA format using puttygen
		client.connect(hostname=instance, username="ec2-user", key_filename=os.path.abspath('C:\Users\pkaur\Downloads\sadeep.dsa'))
		chan = client.get_transport().open_session()
		chan.get_pty()
		chan.exec_command(command1)
		out = chan.recv(1024)
		client.close();
		return out;
	
	def copyfiles(self,instance,local_path,remote_path):	
		privatekeyfile = os.path.abspath('C:\Users\pkaur\Downloads\sadeep.pem')
		mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
		username = 'ec2-user'
		transport = paramiko.Transport((instance, 22))
		transport.connect(username = username, pkey = mykey)
		sftp = paramiko.SFTPClient.from_transport(transport)
		sftp.put(local_path, remote_path)
		sftp.close()
		transport.close()
		return;