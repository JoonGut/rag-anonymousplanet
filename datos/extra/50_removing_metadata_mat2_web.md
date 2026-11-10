# Removing Metadata with mat2-web { #mat2-web-metadata }

Download the latest Debian testing amd64 netinst ISO from <https://www.debian.org/CD/netinst/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.debian.org/CD/netinst/)</sup>

**(Get testing to get the latest mat2 release, stable is a few versions back)**

This is very lightweight, and we recommend doing it from a VM (VM inside a VM) to benefit from Whonix Tor Gateway. While it is possible to put this VM directly behind a Whonix Gateway, Whonix will not easily allow communications between VMs on its network by default. You could also just leave it on Clearnet during the install process and then leave it on the Host-Only network later, or install it from a VM within a VM then move it to host OS for Host-Only usage like we show below:

1. Create a new machine with any name like **Mat2**.
2. Select **Linux** for the Type.
3. Select **Debian (64-bit)** as the Version.
4. Leave the default options and click **Create**.
5. Select the VM and click **Settings**.
6. Select **System** and disable the **Floppy disk** on the Motherboard tab.
7. Select the Processor tab and **enable PAE/NX**.
8. Select **Audio** and **disable Audio**.
9. Select **USB** and **disable the USB controller**.
10. Select **Storage** and select the CD drive to mount the Debian Netinst ISO.
11. Select **Network** and **Attach to NAT**.
12. Launch the VM.
13. Select **Install** (not Graphical install).
14. Select **Language**, **Location**, and **Keyboard layout** as you wish.
15. Wait for the network to configure (automatic DHCP). This takes a few seconds.
16. Pick a name like **Mat2**.
17. Leave the **domain** empty.
18. Set a **root** password as you wish (preferably a good one).
19. Create a new **user** and **password** as you wish (preferably a good one).
20. Select the **Time Zone** of your choice.
21. Select **Guided - Use the entire disk**.
22. Select the only disk available (**/dev/sda** in our case).
23. Select **All files in one partition**.
24. Confirm and write changes to the disk.
25. Select **No** to scan any other CD or DVD.
26. Select any region and any mirror of your choice and leave **proxy** blank.
27. Select **No** to take part in any survey.
28. Select **only System Standard Utilities**. Uncheck everything else using **space**.
29. Select **Yes** to install GRUB bootloader.
30. Select **/dev/sda** and continue.
31. Complete the install and reboot.
32. Log in with your **user** or **root**. You should never use root directly as a best security practice but in this case, it is okay.
33. Update your install by running ```apt upgrade```. It should be upgraded since it is a net install, but we're double checking.
34. Install the necessary packages for mat2 by running ```apt install ffmpeg uwsgi python3-pip uwsgi-plugin-python3 lib35rsvg2-dev git mat2 apache2 libapache2-mod-proxy-uwsgi```.
35. Go to the **/var/www** directory by running ```cd /var/www/```.
36. **Clone mat2-web** from the mat2-web repository by issuing ```git clone https://0xacab.org/jvoisin/mat2-web.git```.
37. **Create a directory for uploads** by running ```mkdir ./mat2-web/uploads/```.
38. **Give permissions to Apache2** to read the files by running ```chown -R www-data:www-data ./mat2-web```.
39. **Enable apache2 uwsgi proxy** by running ```/usr/sbin/a2enmod proxy_uwsgi```.
40. **Upgrade pip** by running ```python3 -m pip install pip --upgrade```.
41. **Install these Python modules** by running ```python3 -m pip install flasgger pyyaml flask-restful flask cerberus flask-cors jinja2```.
42. **Move to the config directory** of mat2 by running ```cd /var/www/mat2-web/config/```.
43. **Copy the apache2 config file** to **/etc** by running ```cp apache2.config /etc/apache2/sites-enabled/apache2.conf```.
44. **Remove the default config file** by running ```rm /etc/apache2/sites-enabled/000-default.conf```.
45. **Edit the apache2 config file** provided by mat2-web by running ```nano /etc/apache2/sites-enabled/apache2.conf```.
46. **Remove the first line** ```Listen 80``` by typing **Ctrl+K** to cut the line.
47. **Change the uwsgi path** from ```/var/www/mat2-web/mat2-web.sock``` to ```/run/uwsgi/uwsgi.sock``` and type **Ctrl+X** to exit, followed by **Y** then **Enter**.
48. **Copy the uwsgi config file** to **/etc** by running ```cp uwsgi.config /etc/uwsgi/apps-enabled/uwsgi.ini```.
49. **Edit the uwsgi config file** by typing ```nano /etc/uwsgi/apps-enabled/uwsgi.ini``` and change **uid** and **guid** to ```nobody``` and ```nogroup``` respectively. Save and exit with **Ctrl+X**, followed by **Y**, then **Enter**.
50. Run ```chown -R 777 /var/www/mat2-web``` to change ownership to **mat2-web**.
51. **Restart uwsgi** by running ```systemctl restart uwsgi```. There should be no errors.
52. **Restart apache2** by running ```systemctl restart apache2```. There should be no errors.
53. Now navigate to **Settings** > **Network** > **Attached to** and **select Host-only Adapter**. Click **OK** to save.
54. Reboot the VM via **Machine** > **Reset**. Confirm the reset.
55. Log into the VM as the **user** from **Step 19** and type ```ip a```. Note the IP address it was assigned under link/ether, the one that has **192.168.\*.\***.
56. From the VM Host OS, **open a Browser** and navigate to the IP of your Debian VM. It will be something like: **http://192.168.1.55**.
57. You should now see a Mat2-Web website running smoothly.
58. **Shutdown the Mat2 guest VM** by running ```shutdown -h now``` to halt the machine.
59. **Take a snapshot of the VM** within Virtualbox while the guest VM is shutdown.

__Restart the Mat2 VM_ and you are ready to use Mat2-web to remove metadata from most files!_*

After use, shut down the VM and revert to the snapshot to remove traces of the uploaded files. This VM does not require any internet access unless you want to update it, in which case, you need to place it back on the **NAT network** and do the next steps.

For updates of Debian, **start the VM** and run ```apt update``` followed by ```apt upgrade```.

For updates of mat2-web, type ```cd /var/www/mat2-web``` and run ```git pull```.

After updates, shutdown, change to the **Host-only Adapter**, take a new snapshot, remove the earlier one.

You are done.

Now you can just start this small Mat2 VM when needed. Browse to it from your Guest VM and use the interface to remove any metadata from most files. After each use of this VM, you should revert to the Snapshot to erase all traces.

**Do not ever expose this VM to any network unless temporarily for updates. This web interface is not suitable for any direct external access.**

