# CSV Feed for openCTI with the latest TOR nodes
## Note: nodes are extracted from this url: [onionoo.torproject.org](https://onionoo.torproject.org/details?search=type:relay%20running:true)
As per the description, _"Onionoo is a web-based protocol to learn about currently running Tor relays and bridges."_

These CSV files contain the following information for each node:
> fingerprint,ipaddr,port,stix_pattern

To use it in OpenCTI, create the following CSV mapper (IPV4 example):
![image](https://github.com/user-attachments/assets/e07c9f70-d25a-4867-89cd-b9a92bf28109)
![image](https://github.com/user-attachments/assets/3d6f8af7-40a2-4760-be5c-f2a1cccfed3b)
![image](https://github.com/user-attachments/assets/76af5373-4128-43c1-aebd-d194f70f3814)
![image](https://github.com/user-attachments/assets/6c0fb59c-6c68-4ce8-ad60-5f7c5ecfffa0)
For the indicator, set the default pattern type as **"stix"** and the main observable type as **"IPV4"**
![image](https://github.com/user-attachments/assets/bda03a71-edc2-4754-bdab-e6e449ca641a)
![image](https://github.com/user-attachments/assets/686a23a3-9e67-4019-a2b1-d978546b3f59)

Then, create a CSV feed:
![image](https://github.com/user-attachments/assets/882696d5-7843-488c-8d72-cd905d868563)


