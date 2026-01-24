# SSH
## Overview
- https://www.youtube.com/watch?v=s-vhqtyUF4I&ab_channel=ByteMonk
- https://www.perplexity.ai/search/ssh-https-www-youtube-com-watc-ScmhmYP.RDe3ZxozAqsjMg 
- securely connect to and control remote machines,
- all with strong encryption, protecting our session and credentials
- 2 steps process

### Step-0 :: preWork
- ssh client creates **key-pair**
  - public
  - private
  
### Step-1 :: SSL handshake
- public key exchange 
- mutual generated **same** Session key (without sharing over internet.)
- this is form secure SSH tunnel for encrypted communication.

![img.png](../SD_99_img/07/01-ssh/img.png)

### Step-2 :: Authentication

![img_1.png](../SD_99_img/07/01-ssh/img_1.png)

## real examples 
- `aws` added **.pem** file on ec2 that is **private key**
- `github`, add public key, verifies client key with every push

## bastion host
- like gateway/proxy, sits in front od SSH server
- take SSL traffic/request
- forward to backend private server