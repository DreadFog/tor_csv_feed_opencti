# CSV Feed for openCTI with the latest TOR nodes and their ports
## Note: nodes are extracted from this url: [onionoo.torproject.org](https://onionoo.torproject.org/details?search=type:relay%20running:true)
As per the description, _"Onionoo is a web-based protocol to learn about currently running Tor relays and bridges."_

These CSV files contain the following information for each node:
> fingerprint,ipaddr,port,stix_pattern\
> _(and then label_name,label_color,marking_type,marking_value,marking_priority for the CSV mapper)_

To use it in OpenCTI, create the following CSV mapper (IPV4 example):
![image](https://github.com/user-attachments/assets/e51b9147-61f6-4523-9004-4ca77177b1ce)
![image](https://github.com/user-attachments/assets/1306ca74-ef8c-4606-95d9-a6ed1d033d75)
![image](https://github.com/user-attachments/assets/d28d90a3-67a2-45bd-b009-0b7d78c83572)
![image](https://github.com/user-attachments/assets/914631d3-7404-4f27-8aad-82ab3632192e)
![image](https://github.com/user-attachments/assets/d53cfff5-d98d-4faf-89c3-884463b0b121)
![image](https://github.com/user-attachments/assets/2e48fdf5-045a-40c9-8056-7e2b9ab42a63)
![image](https://github.com/user-attachments/assets/fe3ff273-8357-4571-9bbd-3b2b40c0f75a)
![image](https://github.com/user-attachments/assets/4560720a-9147-4467-89d8-d6b3cf962d70)

### Note: You can add the label and the marking as attributes of any object or relationship

Then, create a CSV feed:
![image](https://github.com/user-attachments/assets/882696d5-7843-488c-8d72-cd905d868563)



