
import paramiko
import psutil

def connect_ssh(host, user, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print(f"Trying to connect to {host}")
        client.connect(hostname=host, username=user, password=password)
        return client
    except Exception as e:
        print(f"Erreur de connexion SSH : {e}")
        return None

def get_system_info(client):
    stdin, stdout, stderr = client.exec_command("wmic cpu get loadpercentage && wmic OS get FreePhysicalMemory && wmic logicaldisk get freespace")
    output = stdout.read().decode()
    return output

if __name__ == "__main__":
    ssh_client = connect_ssh("102.152.139.21", "ayari hamza", "dhiabouzid92")
    if ssh_client:
        print(get_system_info(ssh_client))
        ssh_client.close()

