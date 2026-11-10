### Pick your guest workstation Virtual Machine { #guest-vm-choice }

Using Whonix/Linux will require more skills on your side as these are Linux distributions. You will also encounter more difficulties if you intend to use specific software that might be harder to use on Whonix/Linux. Setting up a VPN over Tor on Whonix will also be more complicated than on Windows as well.

#### If you can use Tor { #guest-tor-yes }

You can decide if you prefer to conduct your sensitive activities from the Whonix Workstation provided in the earlier section **(highly recommended)** or from a Custom VM that will use the Whonix Gateway like the Whonix Workstation (less secure but might be required depending on what you intend to do).

#### If you cannot use Tor { #guest-tor-no }

If you cannot use Tor, you can use a Custom VM of your choice that will ideally use an anonymous VPN, if possible, to then connect to the Tor network. Or you could go with the risky route: See [What about when Tor and VPNs aren't possible?](#tor-vpn-not-possible)

### Linux Virtual Machine (Whonix or Linux) { #linux-vm }

#### Whonix Workstation **(recommended and preferred)** { #whonix-workstation }

**Skip this step if you cannot use Tor.**

Just use the provided Whonix Workstation VM. **It is the safest and most secure way to go on this route.**

**It is also the only VM that will provide Stream Isolation pre-configured for most apps by default**[^358]**.**

If you want additional software on the Workstation (such as another Browser), follow their guide here <https://www.whonix.org/wiki/Install_Software> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Install_Software)</sup>

Consider running Whonix in Live Mode if for extra malware protection, See <https://www.whonix.org/wiki/Anti-Forensics_Precautions> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Anti-Forensics_Precautions)</sup>

Do not forget to apply the VM hardening recommendations here: [Virtualbox Hardening recommendations].

Consider using AppArmor on your Whonix Workstations by following this guide: <https://www.whonix.org/wiki/AppArmor> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/AppArmor)</sup>

#### Linux (any distro) { #linux-any-distro }

**Be careful, any customization you make to the non-Whonix guest VMs (keyboard layout, language, time zone, screen resolution, or other) could be used to fingerprint your VMs later. See <https://www.whonix.org/wiki/VM_Fingerprinting>** <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/VM_Fingerprinting)</sup>

##### If you can use Tor (natively or over a VPN) { #linux-vm-tor }

Use the Linux Distro of your choice. We would recommend Ubuntu or Fedora for convenience but any other would work too. Be sure to not enable any telemetry.

Refer to this tutorial <https://www.whonix.org/wiki/Other_Operating_Systems> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Other_Operating_Systems)</sup> for detailed instructions.

Consider hardening the VM as recommended in [Hardening Linux].

##### If you cannot use Tor { #linux-vm-no-tor }

Use the Linux Distro of your choice. We would recommend Ubuntu or Fedora for convenience but any other would work too. Be sure to not enable any telemetry. You could go with the risky route: See [What about when Tor and VPNs aren't possible?](#tor-vpn-not-possible)

##### Choose a browser within the VM { #linux-vm-browser }

This time, we will recommend Brave browser.

See why here: [What browser to use in your Guest VM/Disposable VM](#guest-vm-browser-choice)

See [Hardening your Browsers](#hardening-browsers) as well.

### Windows 10/11 Virtual Machine { #windows-vm }

**Be careful, any customization you make to the non-Whonix guest VMs (keyboard layout, language, time zone, screen resolution, or other) could be used to fingerprint your VMs later. See <https://www.whonix.org/wiki/VM_Fingerprinting>** <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/VM_Fingerprinting)</sup>

#### Windows 10 and 11 ISO download { #windows-iso-download }

Go with the Official Windows 10/11 Pro VM and harden it yourself: see [Windows Installation Media Creation](#win-installation-media) and go with the ISO route.

#### If you can use Tor (natively or over a VPN) { #windows-vm-tor }

Refer to this tutorial <https://www.whonix.org/wiki/Other_Operating_Systems> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Other_Operating_Systems)</sup> for detailed instructions.

##### Install { #windows-vm-install }

- Shut down the Whonix Gateway VM (this will prevent Windows from sending out telemetry and allow you to create a local account).

- Open Virtualbox

- Select Machine > New > Select Windows 10 or Windows 11 64bit

- Allocate a minimum amount of 2GB for Windows 10 and 4GB for Windows 11

- Create a Virtual Disk using the VDI format and select Dynamically Allocated

- Keep the disk size at 50GB for Windows 10 and 80GB for Windows 11 (this is a maximum; it should not reach that much)

- Make sure PAE/NX is enabled in System > Processor

- Select the VM and click Settings, Go into the Network Tab

- Select "Internal Network" in the "Attached to" Field and select Whonix.

- Go into the Storage Tab, Select the Empty CD and click the icon next to SATA Port 1

- Click on "Choose a disk file" and select the Windows ISO you previously downloaded

- Click ok and start the VM

- Virtualbox will prompt you to either push a button to boot the ISO or ask you what to boot, select the ISO or click.

- Follow the steps in Windows Installation](#windows-installation)

- Start the Whonix Gateway VM

##### Network Settings { #windows-vm-network }

- Back to your Windows

- Windows 10: Go back into Settings then Network & Internet. Windows 11: Go into settings, click the upper left menu and pick "Network and Internet"

- Windows 10: Click Properties (Below Ethernet). Windows 11: Click Ethernet

- Windows 10: Edit IP settings. Windows 11: Edit IP assignment.

- Windows 10: Enable IPv4 and set the following, Windows 11: Switch from DHCP to Manual and set the following:

    - IP address ```10.152.152.50``` (increase this IP by one for any other VM)

    - Subnet prefix length ```18``` (```255.255.192.0```)

    - Gateway ```10.152.152.10``` (this is the Whonix Gateway)

    - (Windows 10) DNS ```10.152.152.10``` (this is again the Whonix Gateway)

    - (Windows 11) exit the IP assignment and select DNS server assignment and set it to ```10.152.152.10``` (this is again the Whonix Gateway)

    - Save

- Windows might prompt you if you want to be "discoverable" on this network. Click NO. Always stay on a "public network" if prompted.

**Every time you will power on this VM in the future, you should make sure to change its Ethernet Mac Address before each boot. You can do this in Virtualbox > Settings > Network > Advanced > Click the refresh button next to the MAC address. You can only do this while the VM is powered off.**

#### If you cannot use Tor { #windows-vm-no-tor }

See [What about when Tor and VPNs aren't possible?](#tor-vpn-not-possible)

##### Install { #windows-vm-no-tor-install }

- Open Virtualbox

- Select Machine > New > Select Windows 10 or 11 64bit

- Allocate a minimum amount of 4GB of RAM for 11 , 2GB of RAM for 10.

- Create a Virtual Disk using the VDI format and select Dynamically Allocated

- In the System/Processor tab, make sure PAE/NX is enabled.

- Keep the disk size at 80GB for 11, 50GB for 10 (this is a maximum; it should not reach that much)

- Go into the Storage Tab, Select the Empty CD and click the icon next to SATA Port 1

- Click on "Choose a disk file" and select the Windows ISO you previously downloaded

- Click ok and start the VM

- Virtualbox will prompt you to either push a button to boot the ISO or ask you what to boot, select the ISO or click.

- Follow the steps in [Windows Installation](#windows-installation)

##### Network Settings { #windows-vm-no-tor-network }

- Windows will prompt you if you want to be discoverable on this network. Click NO.

**Every time you will power on this VM in the future, you should make sure to change its Ethernet Mac Address before each boot. You can do this in Virtualbox > Settings > Network > Advanced > Click the refresh button next to the MAC address. You can only do this while the VM is powered off.**

#### Choose a browser within the VM { #windows-vm-browser }

This time, we will recommend Brave browser.

See why here: [What browser to use in your Guest VM/Disposable VM](#guest-vm-browser-choice)

See [Hardening your Browsers](#hardening-browsers) as well.

#### Additional Privacy settings in Windows 10/11 { #windows-vm-privacy }

See [Windows Additional Privacy Settings](#win-additional-privacy)

### Android Virtual Machine { #android-vm }

Because sometimes you want to run mobile Apps anonymously too. You can also set up an Android VM for this purpose. As in other cases, ideally, this VM will also be sitting behind the Whonix Gateway for Tor network connectivity. But this can also be set up as VPN over Tor over VPN

#### If you can use Tor (natively or over a VPN) { #android-vm-tor }

Later in the VM settings during creation, go into Network and select Internal Network, Whonix.

Then on Android itself:

- Select Wi-Fi

- Select VirtWifi to connect

- Go into the advanced Wi-Fi properties

- Switch from DHCP to Static

    - IP address ```10.152.152.50``` (increase this IP by one for any other VM)

    - Subnet prefix length ```18``` (```255.255.192.0```)

    - Gateway ```10.152.152.10``` (this is the Whonix Gateway)

    - DNS ```10.152.152.10``` (this is again the Whonix Gateway)

#### If you cannot use Tor { #android-vm-no-tor }

Just use the tutorials as is and see [What about when Tor and VPNs aren't possible?](#tor-vpn-not-possible)

#### Installation { #android-vm-install }

Two possibilities: AnBox or Android-x86

Personally, We would recommend AnBox over Android-x86 but it requires Linux

##### AnBox { #anbox }

Basically follow the tutorial here for installing AnBox on the Whonix Workstation: <https://www.whonix.org/wiki/Anbox> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Anbox)</sup> for running Android Applications within an AnBox VM.

Or follow the instructions here <https://anbox.io/> to install on any other VM **(Linux Only)**

##### Android-x86 { #android-x86 }

Basically, follow the tutorial here: <https://www.android-x86.org/documentation/virtualbox.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.android-x86.org/documentation/virtualbox.html)</sup>

- Download the ISO file of your choice

- Create a New VM.

- Select Linux and Linux 2.6 / 3.x / 4.x 64 Bit.

- In System:

    - Allocate at least 2048MB (2GB) memory

    - Uncheck the Floppy drive

    - In the Processor Tab, select at least 1 or more CPUs

    - Enable PAE/NX

- In Display Settings, Change the adapter to VBoxVGA

- In Audio Settings, Change to Intel HD Audio

- Start the VM

- Select Advanced if you want persistence, Live if you want a disposable Boot (and skip the next steps).

- Select Auto Install on Selected Hard Disk

- Select Run Android

- Set up as you wish (disable all prompts for data collections). **I recommend using the TaskBar Home.**

- Go into Settings, Android-x86 Options, and disable all collections.

- Connect to VirtWifi Wi-Fi Network **(see the above section if you are behind Whonix and want to use Tor)**

You are now done and can now install any Android app.

### macOS Virtual Machine { #macos-vm }

Yes, you can actually run macOS within Virtualbox (on Windows/Linux/macOS host systems) if you want to use macOS. You can run any version of macOS you want.

#### If you can use Tor (natively or over a VPN) { #macos-vm-tor }

During the following tutorials, before starting the macOS VM, make sure you do put the macOS VMs on the Whonix Network.

- Select the VM and click Settings, Go into the Network Tab

- Select "Internal Network" in the "Attached to" Field and select Whonix

Afterward, and during the install, you will need to input an IP address manually to connect through the Whonix Gateway.

Use these settings when prompted in the macOS installation process:

- IP address ```10.152.152.50``` (increase this IP by one for any other VM)

- Subnet prefix length ```18``` (```255.255.192.0```)

- Gateway ```10.152.152.10``` (this is the Whonix Gateway)

- DNS ```10.152.152.10``` (this is again the Whonix Gateway)

#### If you cannot use Tor { #macos-vm-no-tor }

Just use the tutorials as is and see [What about when Tor and VPNs aren't possible?](#tor-vpn-not-possible)

#### Installation { #macos-vm-install }

- Windows Host OS:

    - Virtualbox Catalina Tutorial: <https://www.wikigain.com/install-macos-catalina-on-virtualbox-on-windows/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.wikigain.com/install-macos-catalina-on-virtualbox-on-windows/)</sup>

    - Virtualbox Big Sur Tutorial: <https://www.wikigain.com/how-to-install-macos-big-sur-on-virtualbox-on-windows-pc/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.wikigain.com/how-to-install-macos-big-sur-on-virtualbox-on-windows-pc/)</sup>

    - Virtualbox Monterey Tutorial: <https://www.wikigain.com/install-macos-monterey-on-virtualbox/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.wikigain.com/install-macos-monterey-on-virtualbox/)</sup>

- macOS Host OS:

    - Just use the same tutorials as above but execute the various commands in the terminal. It should work without issue.

- Linux Host OS:

    - Just use the same tutorials as above but execute the various commands in the terminal. It should work without issue.

There are some drawbacks to running macOS on Virtual Machines. The main one is that they do not have a serial number (0 by default) and you will be unable to log in to any Apple-provided service (iCloud, iMessage...) without a genuine ID. You can set such IDs using this script: <https://github.com/myspaghetti/macos-virtualbox> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/myspaghetti/macos-virtualbox)</sup> but keep in mind that randomly generated IDs will not work and using the ID of someone else will break their Terms of Services and could count as impersonation (and therefore could be illegal).

Note: We also ran in multiple issues with running these on AMD processors. This can be fixed so here is the configurationWeused which worked fine with Catalina, Big Sur and Monterey which will tell Virtualbox to emulate an Intel Processor instead:

- ```VBoxManage modifyvm "macOSCatalina" ---cpuidset 00000001 000106e5 00100800 0098e3fd bfebfbff```

- ```VBoxManage setextradata "macOSCatalina" "VBoxInternal/Devices/efi/0/Config/DmiSystemProduct" "MacBookPro15,1" ```

- ```VBoxManage setextradata "macOSCatalina" "VBoxInternal/Devices/efi/0/Config/DmiBoardProduct" "Mac-551B86E5744E2388"```

- ```VBoxManage setextradata "macOSCatalina" "VBoxInternal/Devices/smc/0/Config/DeviceKey" "ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc"```

- ```VBoxManage setextradata "macOSCatalina" "VBoxInternal/Devices/smc/0/Config/GetKeyFromRealSMC" 1```

- ```VBoxManage modifyvm "macOSCatalina" --cpu-profile "Intel Core i7-6700K"```

- ```VBoxManage setextradata "macOSCatalina" VBoxInternal2/EfiGraphicsResolution 1920x1080```

#### Hardening macOS { #macos-vm-hardening }

Refer to [Hardening macOS].

#### Choose a browser within the VM { #macos-vm-browser }

This time, we will recommend Brave browser.

See why here: [What browser to use in your Guest VM/Disposable VM](#guest-vm-browser-choice)

See [Hardening your Browsers](#hardening-browsers) as well.

### KeepassXC { #keepassxc }

You will need something to store your data (logins/passwords, identities, and TOTP[^359] information).

For this purpose, we strongly recommend KeePassXC because of its integrated TOTP feature. This is the ability to create entries for 2FA[^360] authentication with the authenticator feature.

Remember this should ideally be installed on your Guest VM and not on your Host OS. You should never do any sensitive activities from your Host OS.

Here are the tutorials:

- Tails: KeePassXC is integrated by default

- Whonix: <https://www.whonix.org/wiki/Keepassxc> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Keepassxc)</sup>

- Linux:

    - Download from <https://keepassxc.org/download/> <sup>[[Archive.org]](https://web.archive.org/web/https://keepassxc.org/download/)</sup>

    - Follow the tutorial here <https://keepassxc.org/docs/KeePassXC_GettingStarted.html#_linux> <sup>[[Archive.org]](https://web.archive.org/web/https://keepassxc.org/docs/KeePassXC_GettingStarted.html)</sup>

- Windows:

    - Download from <https://keepassxc.org/download/> <sup>[[Archive.org]](https://web.archive.org/web/https://keepassxc.org/download/)</sup>

    - Follow the tutorial here <https://KeePassXC.org/docs/KeePassXC_GettingStarted.html#_microsoft_windows/> <sup>[[Archive.org]](https://web.archive.org/web/https://keepassxc.org/docs/KeePassXC_GettingStarted.html)</sup>

- macOS:

    - Download from <https://keepassxc.org/download/> <sup>[[Archive.org]](https://web.archive.org/web/https://keepassxc.org/download/)</sup>

    - Follow the tutorial here <https://keepassxc.org/docs/KeePassXC_GettingStarted.html#_macos> <sup>[[Archive.org]](https://web.archive.org/web/https://keepassxc.org/docs/KeePassXC_GettingStarted.html)</sup>

Test that KeePassXC is working before going to the next step.

### VPN client installation (cash/Monero paid) { #vpn-client-install }

**If you decided to not use a cash-paid VPN and just want to use Tor, skip this step.**

**If you cannot use a VPN at all in a hostile environment, skip this step.**

Otherwise, see [Installing a VPN on your VM or Host OS](#vpn-installation) to install a VPN client on your client VM.

This should conclude the Route and you should now be ready.

#### About VPN Client Data Mining/Leaks { #vpn-client-leaks }

You might be asking yourself if those VPN clients are trustworthy not to leak any information about your local environment to the VPN provider when using them in the "VPN over Tor" context.

This is a valid concern but should be taken with a grain of salt.

Remember that all VPN activities are happening from a sandboxed VM on an internal network behind a Network Gateway (the Whonix Gateway). It does not matter much if the VPN client leaves some identifiers on your guest VM. The guest VM is still sandboxed and walled-off from the Host OS. The attack surface is small especially when using the reputable and recommended VPN providers within the guides (iVPN, Mullvad, Proton VPN, and maybe Safing.io).

At best, the VPN client would know your local IP (internal IP) and some randomized identifiers but should not be able to get anything from the Host OS. And in theory, the VPN client should not send any telemetry back to the VPN provider. If your VPN client does this or asks this, you should consider changing the provider.

