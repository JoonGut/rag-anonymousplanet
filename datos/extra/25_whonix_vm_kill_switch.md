### (Optional) VM kill switch { #vm-kill-switch }

This step will allow you to configure your Host OS so that only the Whonix Gateway VM will have access to the internet. This will therefore prevent any "leak" from your Host OS while letting the Whonix Gateway establish the tor connectivity. The other VMs (Whonix Workstation or any other VM you installed behind it will not be affected)

There are three ways to do this:

- The Lazy Way (not really recommended): not supported by Whonix and might have some security implications as you will expose the Whonix Gateway VM to the Public Wi-Fi network. We would recommend against this unless you are in a hurry or very lazy.

    - **This method will not work with Wi-Fi captive portals requiring any registration to connect.**

- The Better Way (see further down): still not supported by Whonix but it will not expose the Whonix Gateway VM to the Public Wi-Fi network. This should keep things in check in terms of security.

- The Best Way: Using an external USB Wi-Fi dongle and just disabling Wi-Fi on the Host OS/Computer.

#### The Lazy Way { #kill-switch-lazy }

> Not supported by Whonix

**This way is not supported by the Whonix project**[^361] but I will go ahead and give this option anyway. This is helpful to prevent your Host OS from leaking any information while you are using the Whonix VMs.

**Note that this option as-is will only work on Wi-Fis without a captive portal (where you must enter some information to unlock access).**

The illustration below shows the result of this step:

![image29](../media/image29.png)

##### Configuration of the Whonix Gateway VM { #lazy-whonix-gw-config }

For this to work, we will need to change some configurations on the Whonix Gateway VM. we will need to add a DHCP client to the Whonix Gateway to receive IP addresses from the network. To do those changes the Host OS will still have to have internet access allowed for now.

So here is how:

- Be sure to have your Host OS connected to a safe Wi-Fi.

- Through VirtualBox, start the Whonix Gateway VM

- Start a Terminal on the VM

- Install a DHCP client on the Whonix Gateway VM using the following command:

    - ```sudo apt install dhcpcd5```

- Now edit the Whonix Gateway VM network configuration using the following command:

    - ```sudo nano /etc/network/interfaces.d/30_non-qubes-whonix```

- Within the file change the following lines:

    - ```# auto eth0``` to ```auto eth0```

    - ```# iface eth0 inet dhcp``` to ```iface eth0 inet dhcp```

    - ```iface eth0 inet static``` to ```# iface eth0 inet static```

    - ``` address 10.0.2.15``` to ```# address 10.0.2.15```

    - ``` netmask 255.255.255.0``` to ```# netmask 255.255.255.0```

    - ``` gateway 10.0.2.2``` to ```# gateway 10.0.2.2```

- Save (using Ctrl+X and confirm with Y) and power off the VM from the top left menu

- Go into the VirtualBox Application and select the Whonix Gateway VM

- Click Settings

- Click the Network Tab

- For Adapter 1, change the "Attached To" value from "NAT" to "Bridged Adapter"

- As "Name", select your Wi-Fi network Adapter

- Click OK and you are done with the VM configuration part

##### Configuration of the Host OS { #lazy-host-config }

Now you must block internet access from your Host OS while still allowing the VM to connect. This will be done by connecting to Wi-Fi with the Host OS but without assigning itself an IP address. The VM will then use your Wi-fi association to get an IP address.

###### Windows Host OS { #lazy-windows-host }

The goal here is to associate with a Wi-Fi network without having an internet connection. You will achieve this by deleting the Gateway from the connection after you are connected:

- First, connect to the safe Wi-Fi of your choice

- Open an administrative command prompt (right-click on Command Prompt and Run as Administrator)

- Run the following command: ```route delete 0.0.0.0``` (this deletes the Gateway from your IP configuration)

- You are done, your Host OS will now be unable to access the internet while still connected to the Wi-Fi

    - Note that this will reset at each disconnect/reconnection to a network, and you will have to delete the route again. This is not permanent.

- You can now start the Whonix Gateway VM which should now obtain an IP automatically from the Wi-Fi network and should provide Network to the other VMs behind (Whonix Workstation or other).

- And finally, after that, you can start the Whonix Workstation VM (or any other VM you configured to work behind the Whonix Gateway VM) and it should be connected to the internet through Tor.

###### Linux Host OS { #lazy-linux-host }

The goal here is to associate with a Wi-Fi network without having an internet connection. You will achieve this by deleting the Gateway from the connection after you are connected:

- First, connect to the safe Wi-Fi of your choice

- Open a Terminal

- Run the following command: ```sudo ip route del default``` (this deletes the Gateway from your IP configuration)

- You are done, your Host OS will now be unable to access the internet while still connected to the Wi-Fi

    - Note that this will reset at each disconnect/reconnection to a network, and you will have to delete the route again. This is not permanent.

- You can now start the Whonix Gateway VM which should now obtain an IP automatically from the Wi-Fi network and should provide Network to the other VMs behind (Whonix Workstation or other).

- And finally, after that, you can start the Whonix Workstation VM (or any other VM you configured to work behind the Whonix Gateway VM) and it should be connected to the internet through Tor.

###### macOS Host OS { #lazy-macos-host }

The goal here is to associate with a Wi-Fi network without having an internet connection. You will achieve this by deleting the Gateway from the connection after you are connected:

- First, connect to the safe Wi-Fi of your choice

- Open a Terminal

- Run the following command: ```sudo route delete default``` (this deletes the Gateway from your IP configuration)

- You are done, your Host OS will now be unable to access the internet while still connected to the Wi-Fi

    - Note that this will reset at each disconnect/reconnection to a network, and you will have to delete the route again. This is not permanent.

- You can now start the Whonix Gateway VM which should now obtain an IP automatically from the Wi-Fi network and should provide Network to the other VMs behind (Whonix Workstation or other).

- And finally, after that, you can start the Whonix Workstation VM (or any other VM you configured to work behind the Whonix Gateway VM) and it should be connected to the internet through Tor.

#### The Better Way (recommended) { #kill-switch-better }

This way will not go against Whonix recommendations (as it will not expose the Whonix Gateway to the Host OS) and will have the advantage of allowing connections not only to open Wi-Fis but also to the ones with a Captive Portal where you need to enter some information to access the internet.

Yet this will still not be supported by the Whonix project, but it is fine as the main concern for the earlier Lazy Way is to have the Whonix Gateway VM exposed to the Host Network, and it will not be the case here.

This option will require an additional VM between the Host OS and the Whonix Gateway to act as a Network Bridge.

For this purpose, I will recommend the use of a lightweight Linux Distro. Any will do but the easiest will be an Ubuntu-based distro and I would recommend the lightweight XUbuntu as it will be extremely easy to configure this setup.

Why XUbuntu and not Ubuntu or KUbuntu? Because XUbuntu uses an XFCE desktop environment which is lightweight and this VM will only serve as a proxy and nothing else.

Of course, you can also achieve this with any other Linux distro if you so decide you do not like XUbuntu.

This is how it will look at the end:

![image30](../media/image30.png)

##### Installing XUbuntu VM { #xubuntu-install }

XUbuntu was picked due the performance of XFCE.

Make sure you are connected to a safe Wi-Fi for this operation.

First, you will need to download the latest XUbuntu Stable release ISO from <https://xubuntu.org/download/>

When you are done with the download, it is time to create a new VM:

- Start VirtualBox Manager

- Create a new VM and name it as you want, for example, "XUbuntu Bridge"

- Select type "Linux"

- Select Version "Ubuntu (64-bit)"

- Leave other options to default and click Create

- On the next screen, leave the default options and click Create

- Select the newly create VM and click Settings

- Select Network

- For Adapter 1, Switch to Bridged Mode and pick your Wi-Fi adapter in the Name

- Select Adapter 2 and enable it

- Attach it to "Internal Network" and name it "XUbuntu Bridge"

- Select Storage

- Select the Empty CD drive

- On the right side, click the CD icon and select "Choose a disk file"

- Select the ISO of XUbuntu you previously downloaded and Click Ok

- Start the VM

- Select Start XUbuntu

- Select Install XUbuntu

- Pick your Keyboard Layout and click Continue

- Select Minimal Installation and Download Updates while installing XUbuntu

- Select Erase Disk and install XUbuntu and click Install Now

- Select the Time Zone of your choice and click Continue

- Pick some random names unrelated to you (my favorite username is "NoSuchAccount")

- Pick a password and require a password to login

- Click Continue and wait for the install to finish and Restart

- When you are done rebooting, log-in

- Click the upper right connection icon (it looks like two rotating spheres)

- Click Edit Connections

- Select Wired Connection 2 (Adapter 2 previously configured in VirtualBox settings)

- Select the IPv4 Tab

- Change the Method to "Shared to other computers" and click Save

- You are now done setting up the XUbuntu Bridge VM

##### Configuring the Whonix Gateway VM { #better-whonix-gw-config }

By default, the Whonix Gateway has no DHCP client and will require one to get an IP from a shared network you configured earlier:

- Through VirtualBox, start the Whonix Gateway VM

- Start a Terminal on the VM

- Install a DHCP client on the Whonix Gateway VM using the following command:

    - ```sudo apt install dhcpcd5```

- Now edit the Whonix Gateway VM network configuration using the following command:

    - ```sudo nano /etc/network/interfaces.d/30_non-qubes-whonix```

- Within the file change the following lines:

    - ```# auto eth0``` to ```auto eth0```

    - ```# iface eth0 inet dhcp``` to ```iface eth0 inet dhcp```

    - ```iface eth0 inet static``` to ```# iface eth0 inet static```

    - ``` address 10.0.2.15``` to ```# address 10.0.2.15```

    - ``` netmask 255.255.255.0``` to ```# netmask 255.255.255.0```

    - ``` gateway 10.0.2.2``` to ```# gateway 10.0.2.2```

- Save (using Ctrl+X and confirm with Y) and power off the VM from the top left menu

- Go into the VirtualBox Application and select the Whonix Gateway VM

- Click Settings

- Click the Network Tab

- For Adapter 1, change the "Attached To" value from "NAT" to "Internal Network"

- As "Name", select the internal network "XUbuntu Bridge" you created earlier and click OK

- Reboot the Whonix Gateway VM

- From the upper left menu, select System, Tor Control Panel, and check that you are connected (you should be)

- You are done configuring the Whonix Gateway VM

##### Configuration of the Host OS { #better-host-config }

Now you must block internet access from your Host OS while still allowing the XUbuntu Bridge VM to connect. This will be done by connecting to Wi-Fi with the Host OS but without assigning itself a gateway address. The VM will then use your Wi-fi association to get an IP address.

If necessary, from the XUbuntu Bridge VM, you will be able to launch a Browser to enter information into any captive/registration portal on the Wi-Fi network.

Only the XUbuntu Bridge VM should be able to access the internet. The Host OS will be limited to local traffic only.

###### Windows Host OS { #better-windows-host }

The goal here is to associate with a Wi-Fi network without having an internet connection. You will achieve this by deleting the Gateway from the connection after you are connected:

- First, connect to the safe Wi-Fi of your choice

- Open an administrative command prompt (right-click on Command Prompt and Run as Administrator)

- Run the following command: ```route delete 0.0.0.0``` (this deletes the Gateway from your IP configuration)

- You are done, your Host OS will now be unable to access the internet while still connected to the Wi-Fi

    - Note that this will reset at each disconnect/reconnection to a network, and you will have to delete the route again. This is not permanent.

- You can now start the XUbuntu Bridge VM which should now obtain an IP automatically from the Wi-Fi network and should provide Network to the other VMs behind (Whonix Workstation or other).

- If necessary, you can use the XUbuntu Bridge VM Browser to fill in any information on any captive/registration portal to access the Wi-Fi.

- After that, you can start the Whonix Gateway VM which should obtain the Internet Connection from the XUbuntu Bridge VM.

- And finally, after that, you can start the Whonix Workstation VM (or any other VM you configured to work behind the Whonix Gateway VM) and it should be connected to the internet through Tor.

###### Linux Host OS { #better-linux-host }

The goal here is to associate with a Wi-Fi network without having an internet connection. You will achieve this by deleting the Gateway from the connection after you are connected:

- First, connect to the safe Wi-Fi of your choice

- Open a Terminal

- Run the following command: ```sudo ip route del default``` (this deletes the Gateway from your IP configuration)

- You are done, your Host OS will now be unable to access the internet while still connected to the Wi-Fi

    - Note that this will reset at each disconnect/reconnection to a network, and you will have to delete the route again. This is not permanent.

- You can now start the XUbuntu Bridge VM which should now obtain an IP automatically from the Wi-Fi network and should provide Network to the other VMs behind (Whonix Workstation or other).

- If necessary, you can use the XUbuntu Bridge VM Browser to fill in any information on any captive/registration portal to access the Wi-Fi.

- After that, you can start the Whonix Gateway VM which should obtain the Internet Connection from the XUbuntu Bridge VM.

- And finally, after that, you can start the Whonix Workstation VM (or any other VM you configured to work behind the Whonix Gateway VM) and it should be connected to the internet through Tor.

###### macOS Host OS { #better-macos-host }

The goal here is to associate with a Wi-Fi network without having an internet connection. You will achieve this by deleting the Gateway from the connection after you are connected:

- First, connect to the safe Wi-Fi of your choice

- Open a Terminal

- Run the following command: ```sudo route delete default``` (this deletes the Gateway from your IP configuration)

- You are done, your Host OS will now be unable to access the internet while still connected to the Wi-Fi

    - Note that this will reset at each disconnect/reconnection to a network, and you will have to delete the route again. This is not permanent.

- You can now start the XUbuntu Bridge VM which should now obtain an IP automatically from the Wi-Fi network and should provide Network to the other VMs behind (Whonix Workstation or other).

- If necessary, you can use the XUbuntu Bridge VM Browser to fill in any information on any captive/registration portal to access the Wi-Fi.

- After that, you can start the Whonix Gateway VM which should obtain the Internet Connection from the XUbuntu Bridge VM.

- And finally, after that, you can start the Whonix Workstation VM (or any other VM you configured to work behind the Whonix Gateway VM) and it should be connected to the internet through Tor.

#### The best way { #kill-switch-best }

This way will not go against Whonix recommendations (as it will not expose the Whonix Gateway to the Host OS) and will have the advantage of allowing connections not only to open Wi-Fis but also to the ones with a Captive Portal where you need to enter some information to access the internet. Yet this will still not be supported by the Whonix project, but it is fine as the main concern for the earlier Lazy Way is to have the Whonix Gateway VM exposed to the Host Network, and it will not be the case here. This option is the best because the network will be completely disabled on the Host OS from booting up.

This option will require an additional VM between the Host OS and the Whonix Gateway to act as a Network Bridge and to connect to the Wi-Fi network. **This option requires a working USB Wi-Fi Dongle that will be passed through to a bridge VM.**

For this purpose, I will recommend the use of a lightweight Linux Distro. Any will do but the easiest will be an Ubuntu-based distro and I would recommend the lightweight XUbuntu as it will be extremely easy to configure this setup.

Why XUbuntu and not Ubuntu or KUbuntu? Because XUbuntu uses an XFCE desktop environment which is lightweight and this VM will only serve as a proxy and nothing else.

Of course, you can also achieve this with any other Linux distro if you so decide you do not like XUbuntu.

This is how it will look at the end:

![image31](../media/image31.png)

##### Configuration of the Host OS { #best-host-config }

- Disable Networking on your Host OS completely (Turn off the on-board Wi-Fi completely)

- Plug in and install your USB Wi-Fi Dongle. Connect it to a safe Public Wi-Fi. This should be easy and automatically installed by any recent OS (Windows 10/11, macOS, Linux).

##### Configuring the Whonix Gateway VM { #best-whonix-gw-config }

By default, the Whonix Gateway has no DHCP client and will require one to get an IP from a shared network you will configure later, on a Bridge VM:

- Through VirtualBox, start the Whonix Gateway VM

- Start a Terminal on the VM

- Install a DHCP client on the Whonix Gateway VM using the following command:

    - ```sudo apt install dhcpcd5```

- Now edit the Whonix Gateway VM network configuration using the following command:

    - ```sudo nano /etc/network/interfaces.d/30_non-qubes-whonix```

- Within the file change the following lines:

    - ```# auto eth0``` to ```auto eth0```

    - ```# iface eth0 inet dhcp``` to ```iface eth0 inet dhcp```

    - ```iface eth0 inet static``` to ```# iface eth0 inet static```

    - ``` address 10.0.2.15``` to ```# address 10.0.2.15```

    - ``` netmask 255.255.255.0``` to ```# netmask 255.255.255.0```

    - ``` gateway 10.0.2.2``` to ```# gateway 10.0.2.2```

- Save (using Ctrl+X and confirm with Y) and power off the VM from the top left menu

##### Installing XUbuntu VM { #best-xubuntu-install }

Make sure you are connected to a safe Wi-Fi for this operation.

First, you will need to download the latest XUbuntu Stable release ISO from <https://xubuntu.org/download/>

When you are done with the download, it is time to create a new VM:

- Disconnect your host OS from the Wi-Fi you previously connected to with the dongle and forget the network.

- Start VirtualBox Manager

- Create a new VM and name it as you want, for example, "XUbuntu Bridge"

- Select type "Linux"

- Select Version "Ubuntu (64-bit)"

- Leave other options to default and click Create

- On the next screen, leave the default options and click Create

- Select the newly create VM and click Settings

- Select Network

- For Adapter 1, Attach it to "Internal Network" and name it "XUbuntu Bridge"

- Select Storage

- Select the Empty CD drive

- On the right side, click the CD icon and select "Choose a disk file"

- Select the ISO of XUbuntu you previously downloaded and Click Ok

- Select the USB Tab

- On the right side, click the USB icon with a + sign (the second from the top)

- Select the Wi-Fi Adapter Dongle from the list and make sure it is checked (leave the USB options to default)

- Start the VM

- Select Start XUbuntu

- Select Install XUbuntu

- Pick your Keyboard Layout and click Continue

- Select Minimal Installation and do not check the Download Updates during the install option

- Select Erase Disk and install XUbuntu and click Install Now

- Select the Time Zone of your choice and click Continue

- Pick some random names unrelated to you (my favorite username is "NoSuchAccount")

- Pick a password and require a password to login

- Click Continue and wait for the install to finish and Restart

- When you are done rebooting, log-in

- Click the upper right connection icon (it looks like two rotating spheres)

- Click Edit Connections

- Select Wired Connection 1 (normally there should only be one)

- Select the IPv4 Tab

- Change the Method to "Shared to other computers" and click Save

- Again, click the upper right connection icon

- Connect to the safe Wi-Fi of your choice and if necessary, input the necessary information into a Captive Portal.

- You are now done setting up the XUbuntu Bridge VM

At this stage, your Host OS should have no network at all and your XUbuntu VM should have a fully working Wi-Fi connection and this Wi-Fi connection will be shared to the Internal Network "XUbuntu Bridge".

##### Additional configuration of the Whonix Gateway VM { #best-whonix-gw-extra }

Now it is time to configure the Whonix Gateway VM to get access from the shared network from the bridge VM you just made on the earlier step:

- Go into the VirtualBox Application and select the Whonix Gateway VM

- Click Settings

- Click the Network Tab

- For Adapter 1, change the "Attached To" value from "NAT" to "Internal Network"

- As "Name", select the internal network "XUbuntu Bridge" you created earlier and click OK

- Reboot the Whonix Gateway VM

- From the upper left menu, select System, Tor Control Panel, and check that you are connected (you should be)

- You are done configuring the Whonix Gateway VM

At this stage, your Whonix Gateway VM should be getting internet access from the XUbuntu Bridge VM which in turn is getting internet access from the Wi-Fi Dongle and sharing it. Your Host OS should have no network connectivity at all.

All the VMs behind the Whonix Gateway should now work fine without additional configuration.

**Take a post-install VirtualBox snapshot of your VMs.**

You are done and can now skip the rest to go to the [Getting Online](#getting-online) part.

