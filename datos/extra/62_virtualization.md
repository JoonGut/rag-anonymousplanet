# Virtualization { #virtualization }

So, you might ask yourself, what is Virtualization[^519]?

Basically, it is like the Inception movie with computers. You have emulated software computers called Virtual Machines running on a physical computer. And you can even have Virtual Machines running within Virtual machines if you want to (but this will require a more powerful laptop in some cases).

Here is a little basic illustration of what Virtualization is:

![image53](../media/image53.png)

Each Virtual Machine is a sandbox. Remember the reasons for using them are to prevent the following risks:

- Mitigate local data leaks and easier clean-up in case something gets messed up or it is suspected to be compromised.

- Reduce malware/exploit attack surfaces (if your VM is compromised, the adversary still must figure out he is in a VM and then gain access to the Host OS which is not so trivial).

- Mitigate online data leaks by being able to enforce strict network rules on Virtual Machines for accessing the network (such as passing through the Tor Network).

## Nested virtualization risks { #nested-virtualization-risks }

**There is an inherently larger attack surface when nesting virtualization.**

Here's some host information that can be leaked through the Virtual Machine:

- Organizationally unique identifier or OUI - the unique identifier assigned to VMWare Guest VMs;

- Virtual Windows registry keys like `ProductID` might show the Host Machine's environment:
    `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\ProductId XXXXX-123-1234567-12345`

- HDD, GPU, and mouse drivers can be exposed through: `HKEY_LOCAL_MACHINE\System\CurrentControlSet\`

- Registry entries will show that this is a virtual mouse: `%WINDIR%\system32\drivers\vmmouse.sys`

- Descriptor Table Registers: <https://stackoverflow.com/questions/52505313/what-are-descriptor-registers/52505743#52505743>

    - Since it's a Virtual Machine using the same CPU cores, the descriptor values are relocated due to there only being space for one of each identifier per CPU. This is a dead giveaway and is used in detection by advanced malware. It's employed by malware architects to tell when the program is being ran in a forensics environment (e.g., Remnux or Flare VM) - popular tools/OS that are used by experts to analyze malware.

- Guest VMs also indirectly access the same hardware as the Host OS.

See <https://www.malwarebytes.com/blog/news/2014/02/a-look-at-malware-with-virtual-machine-detection> for more techniques used by malware to detect virtualization. These techniques are mostly prevented by appending some settings to your VM config file (.vmx). <https://blog.talosintelligence.com/2009/10/how-does-malware-know-difference.html>

