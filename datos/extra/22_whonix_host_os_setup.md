## The Whonix route { #whonix-route }

**Note on Whonix Version**: Whonix has been upgraded from version 17 to 18 (Whonix 18.1.4.x at the time of writing) with automated release upgrade support. See [Upgrading to Whonix 18](#qubes-whonix18) for the upgrade path if you currently use Whonix 17.x or earlier versions.

### Picking your Host OS { #host-os-choice }

This route will make extensive use of Virtual Machines[^310], they will require a host OS to run the Virtualization software. You have three recommended choices in this part of the guide:

- Your Linux distribution of choice (excluding Qubes OS)

- Windows 10/11 (preferably Home edition due to the absence of Bitlocker)

- macOS (Catalina or higher up to Monterey)

In addition, chances are high that your Mac is or has been tied to an Apple account (at the time of purchase or after signing-in) and therefore its unique hardware identifiers could lead back to you in case of hardware identifiers leak.

Linux is also not necessarily the best choice for anonymity depending on your threat model. This is because using Windows will allow us to **conveniently** use Plausible Deniability[^311] (aka Deniable Encryption[^312]) easily at the OS level. Windows is also unfortunately at the same time a privacy nightmare[^313] but is the only easy to set up option for using OS-wide plausible deniability. Windows telemetry and telemetry blocking are also widely documented which should mitigate many issues.

**So, what is Plausible Deniability?** You can cooperate with an adversary requesting access to your device/data without revealing your true secret. All this using Deniable Encryption[^314].

A soft lawful adversary could ask for your encrypted laptop password. At first, you could refuse to give out any password (using your "right to remain silent", "right not to incriminate yourself") but some countries are implementing laws[^315]'[^316] to exempt this from such rights (because terrorists and "think of the children"). In that case, you might have to reveal the password or face jail time in contempt of court. This is where plausible deniability will come into play.

You could then reveal a password, but that password will only give access to "plausible data" (a decoy OS). The forensics will be well aware that it is possible for you to have hidden data but should not be able to prove this **(if you do this right)**. You will have cooperated, and the investigators will have access to something but not what you actually want to hide. Since the burden of proof should lie on their side, they will have no options but to believe you unless they have proof that you have hidden data.

This feature can be used at the OS level (a plausible OS and a hidden OS) or at the files level where you will have an encrypted file container (similar to a zip file) where different files will be shown depending on the encryption password you use.

This also means you could set up your own advanced "plausible deniability" setup using any Host OS by storing for instance Virtual Machines on a Veracrypt hidden volume container (be careful of traces in the Host OS tho that would need to be cleaned if the host OS is persistent, see [Some additional measures against forensics](#anti-forensics) section later). There is a project for achieving this within Tails (<https://github.com/aforensics/HiddenVM> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/aforensics/HiddenVM)</sup>) which would make your Host OS non-persistent and use plausible deniability within Tails.

In the case of Windows, plausible deniability is also the reason you should ideally have Windows 10/11 Home (and not Pro). This is because Windows 10/11 Pro natively offers a full-disk encryption system (Bitlocker[^317]) where Windows 10/11 Home offers no full-disk encryption at all. You will later use third-party open-source software for encryption that will allow full-disk encryption on Windows 10/11 Home. This will give you a good (plausible) excuse to use this software. While using this software on Windows 10/11 Pro would be suspicious.

**Note about Linux:** So, what about Linux and plausible deniability? Yes, it is possible to achieve plausible deniability with Linux too. More information within the Linux Host OS section later.

Unfortunately, encryption is not magic and there are some risks involved:

#### Threats with encryption { #encryption-threats }

**The 5$ Wrench Attack**

Remember that encryption with or without plausible deniability is not a silver bullet and will be of little use in case of torture. As a matter a fact, depending on who your adversary would be (your threat model), it might be wise not to use Veracrypt (formerly TrueCrypt) at all as shown in this demonstration: <https://defuse.ca/truecrypt-plausible-deniability-useless-by-game-theory.htm> <sup>[[Archive.org]](https://web.archive.org/web/https://defuse.ca/truecrypt-plausible-deniability-useless-by-game-theory.htm)</sup>

Plausible deniability is only effective against soft lawful adversaries that will not resort to physical means. **Avoid, if possible, the use of plausible deniability-capable software (such as Veracrypt) if your threat model includes hard adversaries. So, Windows users should in that case install Windows Pro as a Host OS and use Bitlocker instead.**

See <https://en.wikipedia.org/wiki/Rubber-hose_cryptanalysis> <sup>[[Wikiless]](https://wikiless.tiekoetter.com/wiki/Rubber-hose_cryptanalysis)</sup> <sup>[[Archive.org]](https://web.archive.org/web/https://en.wikipedia.org/wiki/Rubber-hose_cryptanalysis)</sup>

##### Evil-Maid Attack { #evil-maid-attack }

Evil Maid Attacks[^318] are conducted when someone tampers with your laptop while you are away. To install to clone your hard drive, install malware or a key logger. If they can clone your hard drive, they can compare one image of your hard drive at the time they took it while you were away with the hard drive when they seize it from you. If you used the laptop again in between, forensics examiners might be able to prove the existence of the hidden data by looking at the variations between the two images in what should be an empty/unused space. This could lead to compelling evidence of the existence of hidden data. If they install a key logger or malware within your laptop (software or hardware), they will be able to simply get the password from you for later use when they seize it. Such attacks can be done at your home, your hotel, a border crossing, or anywhere you leave your devices unattended.

You can mitigate this attack by doing the following (as recommended earlier):

- Have basic tamper protection (as explained previously) to prevent physical access to the internals of the laptop without your knowing. This will prevent them from cloning your disks and installing a physical key logger without your knowledge.

- Disable all the USB ports (as explained previously) within a password-protected BIOS/UEFI. Again, they will not be able to turn them on (without physically accessing the motherboard to reset the BIOS) to boot a USB device that could clone your hard drive or install a software-based malware that could act as a key logger.

- Set up BIOS/UEFI/Firmware passwords to prevent any unauthorized boot of an unauthorized device.

- Some OSes and Encryption software have the [Anti Evil Maid (AEM)](#qubes-aem) protection that can be enabled. This is the case with Windows/Veracrypt and QubeOS (only on Intel CPUs).

##### Cold-Boot Attack { #cold-boot-attack }

Cold Boot attacks[^319] are trickier than the Evil Maid Attack but can be part of an Evil Maid attack as it requires an adversary to come into possession of your laptop while you are actively using your device or shortly afterward.

The idea is rather simple, as shown in this video[^320], an adversary could theoretically quickly boot your device on a special USB key that would copy the content of the RAM (the memory) of the device after you shut it down. If the USB ports are disabled or if they feel like they need more time, they could open it and "cool down" the memory using a spray or other chemicals (liquid nitrogen for instance) preventing the memory from decaying. They could then be able to copy its content for analysis. This memory dump could contain the key to decrypt your device. You will later apply a few principles to mitigate these.

In the case of Plausible Deniability, there have been some forensics studies[^321] about technically proving the presence of the hidden data with a simple forensic examination (without a Cold Boot/Evil Maid Attack) but these have been contested by other studies[^322] and by the maintainer of Veracrypt[^323] so we would not worry too much about those yet.

The same measures used to mitigate Evil Maid attacks should be in place for Cold Boot attacks with some added ones:

- If your OS or Encryption software allows it, you should consider encrypting the keys within RAM too (this is possible with Windows/Veracrypt and will be explained later). Again see <https://sourceforge.net/p/veracrypt/discussion/technical/thread/3961542951/> <sup>[[Archive.org]](https://web.archive.org/web/https://sourceforge.net/p/veracrypt/discussion/technical/thread/3961542951/)</sup>

- Do enable the option to Wipe keys from memory if a device is inserted in Veracrypt.

- You should limit the use of Sleep stand-by and instead use Shutdown or Hibernate to prevent the encryption keys from staying in RAM when your computer goes to sleep. This is because sleep will maintain power in your memory for resuming your activity faster. Only hibernation and shutdown will actually clear the key from the memory[^324].

See also [Cold Boot Attack Defense](https://www.whonix.org/wiki/Cold_Boot_Attack_Defense) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Cold_Boot_Attack_Defense)</sup> and [Protection Against Physical Attacks](https://www.whonix.org/wiki/Protection_Against_Physical_Attacks) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Protection_Against_Physical_Attacks)</sup>.

Here are also some interesting tools to consider for Linux users to defend against these:

- <https://github.com/0xPoly/Centry> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/0xPoly/Centry)</sup> (unfortunately unmaintained it seems)

- <https://github.com/hephaest0s/usbkill> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/hephaest0s/usbkill)</sup> (unfortunately unmaintained as well it seems)

- <https://github.com/Lvl4Sword/Killer> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/Lvl4Sword/Killer)</sup>

- <https://askubuntu.com/questions/153245/how-to-wipe-ram-on-shutdown-prevent-cold-boot-attacks> <sup>[[Archive.org]](https://web.archive.org/web/https://askubuntu.com/questions/153245/how-to-wipe-ram-on-shutdown-prevent-cold-boot-attacks)</sup>

- (Qubes OS, Intel CPU only) <https://github.com/QubesOS/qubes-antievilmaid> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/QubesOS/qubes-antievilmaid)</sup>

##### About Sleep, Hibernation, and Shutdown { #sleep-hibernation-shutdown }

If you want better security, you should shut down your laptop completely every time you leave it unattended or close the lid. This should clean and/or release the RAM and provide mitigations against cold boot attacks. However, this can be a bit inconvenient as you will have to reboot completely and type in a ton of passwords into various apps. Restart various VMs and other apps. So instead, you could also use hibernation (not supported on Qubes OS). Since the whole disk is encrypted, hibernation in itself should not pose a large security risk but will still shut down your laptop and clear the memory while allowing you to conveniently resume your work afterward. **What you should never do is using the standard sleep feature which will keep your computer on, and the memory powered. This is an attack vector against evil-maid and cold-boot attacks discussed earlier. This is because your powered-on memory holds the encryption keys to your disk (encrypted or not) and could then be accessed by a skilled adversary.**

This guide will provide guidance later on how to enable hibernation on various host OSes (except Qubes OS) if you do not want to shut down every time.

##### Local Data Leaks (traces) and forensics examination { #host-local-data-leaks }

As mentioned briefly earlier, these are data leaks and traces from your operating system and apps when you perform any activity on your computer. These mostly apply to encrypted file containers (with or without plausible deniability) than OS-wide encryption. Such leaks are less "important" if your whole OS is encrypted (if you are not compelled to reveal the password).

Let us say for example you have a Veracrypt encrypted USB key with plausible deniability enabled. Depending on the password you use when mounting the USB key, it will open a decoy folder or the sensitive folder. Within those folders, you will have decoy documents/data within the decoy folder and sensitive documents/data within the sensitive folder.

In all cases, you will (most likely) open these folders with Windows Explorer, macOS Finder, or any other utility and do whatever you planned to do. Maybe you will edit a document within the sensitive folder. Maybe you will search for a document within the folder. Maybe you will delete one or watch a sensitive video using VLC.

Well, all those Apps and your Operating System might keep logs and traces of that usage. This might include the full path of the folder/files/drives, the time those were accessed, temporary caches of those files, the "recent" lists in each app, the file indexing system that could index the drive, and even thumbnails that could be generated

Here are some examples of such leaks:

###### Windows { #host-local-leaks-windows }

- Windows ShellBags that are stored within the Windows Registry silently storing various histories of accessed volumes/files/folders[^325].

- Windows Indexing keeping traces of the files present in your user folder by default[^326].

- Recent lists (aka Jump Lists) in Windows and various apps keeping traces of recently accessed documents[^327].

- Many more traces in various logs, please see this convenient interesting poster for more insight: <https://www.sans.org/security-resources/posters/windows-forensic-analysis/170/download> <sup>[[Archive.org]](https://web.archive.org/web/https://www.sans.org/security-resources/posters/windows-forensic-analysis/170/download)</sup>

###### macOS { #host-local-leaks-macos }

- Gatekeeper[^328] and XProtect keeping track of your download history in a local database and file attributes.

- Spotlight Indexing

- Recent lists in various apps keeping traces of recently accessed documents.

- Temporary folders keeping various traces of App usage and Document usage.

- macOS Logs

###### Linux { #host-local-leaks-linux }

- Tracker Indexing

- Bash History

- USB logs

- Recent lists in various apps keeping traces of recently accessed documents.

- Linux Logs

Forensics could' use all those leaks (see [Local Data Leaks and Forensics](#local-data-leaks)) to prove the existence of hidden data and defeat your attempts at using plausible deniability and to find out about your various sensitive activities.

It will be therefore important to apply various steps to prevent forensics from doing this by preventing and cleaning these leaks/traces and more importantly by using whole disk encryption, virtualization, and compartmentalization.

Forensics cannot extract local data leaks from an OS they cannot access. And you will be able to clean most of those traces by wiping the drive or by securely erasing your virtual machines (which is not as easy as you think on SSD drives).

Some cleaning techniques will nevertheless be covered in the "Cover your Tracks" part of this guide at the very end.

##### Online Data Leaks { #host-online-data-leaks }

Whether you are using simple encryption or plausible deniability encryption. Even if you covered your tracks on the computer itself. There is still a risk of online data leaks that could reveal the presence of hidden data.

**Telemetry is your enemy**. As explained earlier in this guide, the telemetry of Operating Systems but also from Apps can send staggering amounts of private information online.

In the case of Windows, this data could for instance be used to prove the existence of a hidden OS / Volume on a computer and would be readily available at Microsoft. Therefore, it is critically important that you disable and block telemetry with all the means at your disposal. No matter what OS you are using.

#### Conclusion { #host-os-conclusion }

You should never conduct sensitive activities from a non-encrypted system. And even if it is encrypted, you should never conduct sensitive activities from the Host OS itself. Instead, you should use a VM to be able to efficiently isolate and compartmentalize your activities and prevent local data leaks.

If you have little to no knowledge of Linux or if you want to use OS-wide plausible deniability, we recommend going for Windows (or back to [the Tails route](#tails-route)) for convenience. This guide will help you hardening it as much as possible to prevent leaks. This guide will also help you hardening macOS and Linux as much as possible to prevent similar leaks.

If you have no interest in OS-wide plausible deniability and want to learn to use Linux, we will strongly recommend going for Linux or the Qubes OS route if your hardware allows it.

**In all cases, the host OS should never be used to conduct sensitive activities directly. The host OS will only be used to connect to a public Wi-Fi Access Point. It will be left unused while you conduct sensitive activities and should ideally not be used for any of your day-to-day activities.**

Consider also reading **<https://www.whonix.org/wiki/Full_Disk_Encryption#Encrypting_Whonix_VMs>** <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Full_Disk_Encryption)</sup>

### Linux Host OS { #linux-host-os }

As mentioned earlier, we do not recommend using your daily laptop for sensitive activities. Or at least we do not recommend using your in-place OS for these. Doing that might result in unwanted data leaks that could be used to de-anonymize you. If you have a dedicated laptop for this, you should reinstall a fresh clean OS. If you do not want to wipe your laptop and start over, you should consider the Tails route or proceed at your own risk.

I also recommend that you do the initial installation completely offline to avoid any data leak.

You should always remember that despite the reputation, Linux mainstream distributions (Ubuntu for instance) are not necessarily better at security than other systems such as macOS and Windows. See this reference to understand why <https://madaidans-insecurities.github.io/linux.html> <sup>[[Archive.org]](https://web.archive.org/web/https://madaidans-insecurities.github.io/linux.html)</sup>.

#### Full disk encryption { #linux-fde }

There are two routes here with Ubuntu or Debian based distros:

- Using LUKS:

    - Without plausible deniability:

        + (Recommended and easy) Encrypt as part of the installation process: <https://ubuntu.com/tutorials/install-ubuntu-desktop> <sup>[[Archive.org]](https://web.archive.org/web/https://ubuntu.com/tutorials/install-ubuntu-desktop)</sup>

            * This process requires the full erasure of your entire drive (clean install).

            * Just check the "Encrypt the new Ubuntu installation for security"

        + (Tedious but possible) Encrypt after installation: <https://help.ubuntu.com/community/ManualFullSystemEncryption> <sup>[[Archive.org]](https://web.archive.org/web/https://help.ubuntu.com/community/ManualFullSystemEncryption)</sup>

    - With plausible deniability: See the next section [The Detached Headers Way]

- Using Veracrypt:

    - With or without plausible deniability: See the next section [The Veracrypt Way]

For other distros, you will have to document yourself, but it will likely be similar. Encryption during install is just much easier in the context of this guide.

#### Note about plausible deniability on Linux { #linux-deniability-note }

There are several ways to achieve plausible deniability on Linux[^329] and it is possible to achieve. Here are some more details about some of the ways we would recommend. All these options require some higher level of skills at using Linux.

##### The Detached Headers Way { #detached-headers }

While not supported yet by this guide, it is possible to achieve a form of deniability on Linux using LUKS by using detached LUKS headers. For now, we will redirect you toward this page for more information: <https://wiki.archlinux.org/title/Dm-crypt/Specialties#Encrypted_system_using_a_detached_LUKS_header> <sup>[[Archive.org]](https://web.archive.org/web/https://wiki.archlinux.org/title/Dm-crypt/Specialties#Encrypted_system_using_a_detached_LUKS_header)</sup>

##### The Veracrypt Way { #veracrypt-way }

It is technically possible to not only use Veracrypt but also to achieve plausible deniability on a Linux Host OS by using Veracrypt for system full-disk encryption (instead of LUKS). This is not supported by Veracrypt (System encryption is only supported on Windows) and requires some tinkering with various commands. This is not recommended at all for unskilled users and should only be used at your own risk.

The steps to achieve this are not yet integrated into this guide but can be found here: <http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion/post/5779e55aae7fc06e4758> (this is a .onion address and requires Tor Browser).

#### Reject/Disable any telemetry { #linux-disable-telemetry }

- During the install, just make sure you do not allow any data collection if prompted.

- If you are not sure, just make sure you did not enable any telemetry and follow this tutorial if needed <https://vitux.com/how-to-force-ubuntu-to-stop-collecting-your-data-from-your-pc/> <sup>[[Archive.org]](https://web.archive.org/web/https://vitux.com/how-to-force-ubuntu-to-stop-collecting-your-data-from-your-pc/)</sup>

- Any other distro: you will need to document yourself and find out how to disable telemetry.

#### Disable anything unnecessary { #linux-disable-unnecessary }

- Disable Bluetooth if enabled by following this guide <https://www.addictivetips.com/ubuntu-linux-tips/disable-bluetooth-in-ubuntu/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.addictivetips.com/ubuntu-linux-tips/disable-bluetooth-in-ubuntu/)</sup> or issuing the following command:

    - ```sudo systemctl disable bluetooth.service --force```

- Disable Indexing if enabled by default (Ubuntu >19.04) by following this guide <https://www.linuxuprising.com/2019/07/how-to-completely-disable-tracker.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.linuxuprising.com/2019/07/how-to-completely-disable-tracker.html)</sup> or issuing the following commands:

    - ```sudo systemctl --user mask tracker-store.service tracker-miner-fs.service tracker-miner-rss.service tracker-extract.service tracker-miner-apps.service tracker-writeback.service```

        + You can safely ignore any error if it says some service does not exist

    - ```sudo tracker reset -hard```

##### Hibernation { #linux-hibernation }

As explained previously, you should not use the sleep features but shut down or hibernate your laptop to mitigate some evil-maid and cold-boot attacks. Unfortunately, this feature is disabled by default on many Linux distros including Ubuntu. It is possible to enable it, but it might not work as expected. Follow this information at your own risk. If you do not want to do this, you should never use the sleep function and power off instead (and set the lid closing behavior to power off instead of sleep).

Follow one of these tutorials to enable Hibernate:

- <https://www.how2shout.com/linux/how-to-hibernate-ubuntu-20-04-lts-focal-fossa/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.how2shout.com/linux/how-to-hibernate-ubuntu-20-04-lts-focal-fossa/)</sup>

- <http://www.lorenzobettini.it/2020/07/enabling-hibernation-on-ubuntu-20-04/> <sup>[[Archive.org]](https://web.archive.org/web/http://www.lorenzobettini.it/2020/07/enabling-hibernation-on-ubuntu-20-04/)</sup>

- <https://blog.ivansmirnov.name/how-to-set-up-hibernate-on-ubuntu-20-04/> <sup>[[Archive.org]](https://web.archive.org/web/20211011215449/https://blog.ivansmirnov.name/how-to-set-up-hibernate-on-ubuntu-20-04/)</sup>

After Hibernate is enabled, change the behavior so that your laptop will hibernate when you close the lid by following this tutorial for Ubuntu 20.04 <http://ubuntuhandbook.org/index.php/2020/05/lid-close-behavior-ubuntu-20-04/> <sup>[[Archive.org]](https://web.archive.org/web/http://ubuntuhandbook.org/index.php/2020/05/lid-close-behavior-ubuntu-20-04/)</sup> and this tutorial for Ubuntu 18.04 <https://tipsonubuntu.com/2018/04/28/change-lid-close-action-ubuntu-18-04-lts/> <sup>[[Archive.org]](https://web.archive.org/web/https://tipsonubuntu.com/2018/04/28/change-lid-close-action-ubuntu-18-04-lts/)</sup>. There is no tutorial yet for Ubuntu 21.04 or 21.10 but the above for 20.04 should probably work too.

Unfortunately, this will not clean the key from memory directly when hibernating. To avoid this at the cost of some performance, you might consider encrypting the swap file by following this tutorial: <https://help.ubuntu.com/community/EnableHibernateWithEncryptedSwap> <sup>[[Archive.org]](https://web.archive.org/web/https://help.ubuntu.com/community/EnableHibernateWithEncryptedSwap)</sup>

These settings should mitigate cold boot attacks if you can hibernate fast enough.

#### Enable MAC address randomization { #linux-mac-randomization }

- For Ubuntu, follow these steps <https://help.ubuntu.com/community/AnonymizingNetworkMACAddresses> <sup>[[Archive.org]](https://web.archive.org/web/https://help.ubuntu.com/community/AnonymizingNetworkMACAddresses)</sup>.

- Consider this tutorial which should still work: <https://josh.works/shell-script-basics-change-mac-address> <sup>[[Archive.org]](https://web.archive.org/web/https://josh.works/shell-script-basics-change-mac-address)</sup>

#### Hardening Linux { #hardening-linux }

As a light introduction for new Linux users, consider <https://www.youtube.com/watch?v=Sa0KqbpLye4> <sup>[[Invidious]](https://yewtu.be/watch?v=Sa0KqbpLye4)</sup>

For more in-depth and advanced options, refer to:

- This excellent guide: <https://madaidans-insecurities.github.io/guides/linux-hardening.html> <sup>[[Archive.org]](https://web.archive.org/web/https://madaidans-insecurities.github.io/guides/linux-hardening.html)</sup>

- This excellent wiki resource: <https://wiki.archlinux.org/title/Security> <sup>[[Archive.org]](https://web.archive.org/web/https://wiki.archlinux.org/title/Security)</sup>

- These excellent scripts are based on the guide and wiki above: <https://codeberg.org/SalamanderSecurity/PARSEC> <sup>[[Archive.org]](https://web.archive.org/web/https://codeberg.org/SalamanderSecurity/PARSEC)</sup>

- These tools that can help you harden your Linux Kernel:

    - Lynis: <https://github.com/CISOfy/lynis>

    - Kconfig-hardened-check: <https://github.com/a13xp0p0v/kconfig-hardened-check>

- Consider installing Safing Portmaster from <https://safing.io/portmaster/> <sup>[[Archive.org]](https://web.archive.org/web/https://safing.io/portmaster/)</sup> **(Warning: there might be issues with some VPN clients. See: <https://docs.safing.io/portmaster/install/status/vpn-compatibility>** <sup>[[Archive.org]](https://web.archive.org/web/https://docs.safing.io/portmaster/install/status/vpn-compatibility)</sup>

- Consider the use of KickSecure when using Debian: [Kicksecure](https://www.whonix.org/wiki/Kicksecure) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Kicksecure)</sup>

- This interesting article: <http://0pointer.net/blog/authenticated-boot-and-disk-encryption-on-linux.html> <sup>[[Archive.org]](https://web.archive.org/web/http://0pointer.net/blog/authenticated-boot-and-disk-encryption-on-linux.html)</sup>

#### Setting up a safe Browser { #linux-safe-browser }

See [Safe Browser on the Host OS](#safe-browser-host-os)

### macOS Host OS { #macos-host-os }

**Note: Mac M1/M2 chips are now supported natively, or, if you wish to use commercial tools like VMWare Fusion or Parallels Desktop, but those are not covered in this guide. Seek this information yourself.**

As mentioned earlier, we do not recommend using your daily laptop for sensitive activities. Or at least we do not recommend using your in-place OS for these. Doing that might result in unwanted data leaks that could be used to de-anonymize you. If you have a dedicated laptop for this, you should reinstall a fresh clean OS. If you do not want to wipe your laptop and start over, you should consider [the Tails route](#tails-route) or proceed at your own risk.

We also recommend that you do the initial installation completely offline to avoid any data leak.

**Do not ever sign in with your Apple account using that Mac.**

#### During the install { #macos-install }

- Stay Offline

- Disable all data sharing requests when prompted including location services

- Do not sign in with Apple

- Do not enable Siri

#### Hardening macOS { #hardening-macos }

As a light introduction for new macOS users, consider <https://www.youtube.com/watch?v=lFx5icuE6Io> <sup>[[Invidious]](https://yewtu.be/watch?v=lFx5icuE6Io)</sup>

Now to go more in-depth in securing and hardening your macOS, we recommend reading this guide which covers many of the issues: <https://www.bejarano.io/hardening-macos/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.bejarano.io/hardening-macos/)</sup>

Here are the basic steps you should take after your offline installation:

##### Enable Firmware password with "disable-reset-capability" option { #macos-firmware-password }

First, you should set up a firmware password following this guide from Apple: <https://support.apple.com/en-us/HT204455> <sup>[[Archive.org]](https://web.archive.org/web/https://support.apple.com/en-us/HT204455)</sup>

Unfortunately, some attacks are still possible and an adversary could disable this password so you should also follow this guide to prevent disabling the firmware password from anyone including Apple: <https://support.apple.com/en-gb/guide/security/sec28382c9ca/web> <sup>[[Archive.org]](https://web.archive.org/web/https://support.apple.com/en-gb/guide/security/sec28382c9ca/web)</sup>

##### Enable Hibernation instead of sleep { #macos-hibernation }

Again, this is to prevent some cold-boot and evil-maid attacks by powering down your RAM and cleaning the encryption key when you close the lid. You should always either hibernate or shut down. On macOS, the hibernate feature even has a special option to specifically clear the encryption key from memory when hibernating (while you might have to wait for the memory to decay on other Operating Systems). Once again there are no easy options to do this within the settings so instead, we will have to do this by running a few commands to enable hibernation:

- Open a Terminal

- Run: ```sudo pmset -a destroyfvkeyonstandby 1```

    - This command will instruct macOS to destroy the Filevault key on Standby (sleep)

- Run: ```sudo pmset -a hibernatemode 25```

    - This command will instruct macOS to power off the memory during sleep instead of doing a hybrid hibernate that keeps the memory powered on. It will result in slower wakes but will increase battery life.

Now when you close the lid of your MacBook, it should hibernate instead of sleep and mitigate attempts at performing cold-boot attacks.

In addition, you should also set up an automatic sleep (Settings > Energy) so that your MacBook will hibernate automatically if left unattended.

##### Disable unnecessary services { #macos-disable-services }

Disable some unnecessary settings within the settings:

- Disable Bluetooth

- Disable the Camera and Microphone

- Disable Location Services

- Disable Airdrop

- Disable Indexing

##### Prevent Apple OCSP calls { #macos-ocsp }

These are the infamous "unblockable telemetry" calls from macOS Big Sur disclosed here: <https://sneak.berlin/20201112/your-computer-isnt-yours/> <sup>[[Archive.org]](https://web.archive.org/web/https://sneak.berlin/20201112/your-computer-isnt-yours/)</sup>

You could block OCSP reporting by issuing the following command in Terminal:

- ``` sudo sh -c 'echo "127.0.0.1 ocsp.apple.com" >> /etc/hosts'```

But you should document yourself on the actual issue before acting. This page is a good place to start: <https://blog.jacopo.io/en/post/apple-ocsp/> <sup>[[Archive.org]](https://web.archive.org/web/https://blog.jacopo.io/en/post/apple-ocsp/)</sup>

Up to you really. We would block it because we do not want any telemetry at all from my OS to the mothership without my specific consent. None.

##### Enable Full Disk encryption (Filevault) { #filevault }

You should enable full disk encryption on your Mac using Filevault according to this part of the guide: <https://github.com/drduh/macOS-Security-and-Privacy-Guide#full-disk-encryption> <sup>[[Archive.org]](https://web.archive.org/web/https://www.bejarano.io/hardening-macos/)</sup>

**Be careful when enabling. Do not store the recovery key at Apple if prompted (should not be an issue since you should be offline at this stage). You do not want a third party to have your recovery key.**

##### MAC Address Randomization { #macos-mac-randomization }

Unfortunately, macOS does not offer a native convenient way of randomizing your MAC Address and so you will have to do this manually. This will be reset at each reboot, and you will have to re-do it each time to ensure you do not use your actual MAC Address when connecting to various Wi-Fis

You can do this by issuing the following commands in terminal (without the parentheses):

- (Turn the Wi-Fi off) ```networksetup -setairportpower en0 off```

- (Change the MAC Address) ```sudo ifconfig en0 ether 88:63:11:11:11:11```

- (Turn the Wi-Fi back on) ```networksetup -setairportpower en0 on```

#### Setting up a safe Browser { #macos-safe-browser }

See [Safe Browser on the Host OS](#safe-browser-host-os)

### Windows Host OS { #windows-host-os }

As mentioned earlier, we do not recommend using your daily laptop for sensitive activities. Or at leastWedo not recommend using your in-place OS for these. Doing that might result in unwanted data leaks that could be used to de-anonymize you. If you have a dedicated laptop for this, you should reinstall a fresh clean OS. If you do not want to wipe your laptop and start over, you should consider [the Tails route](#tails-route) or proceed at your own risk.

I also recommend that you do the initial installation completely offline to avoid any data leak.

#### Installation { #windows-host-install }

You should follow [Windows Installation](#windows-installation)

As a light introduction, consider watching <https://www.youtube.com/watch?v=vNRics7tlqw> <sup>[[Invidious]](https://yewtu.be/watch?v=vNRics7tlqw)</sup>

#### Enable MAC address randomization { #windows-mac-randomization }

You should randomize your MAC address as explained earlier in this guide:

Go into Settings > Network & Internet > Wi-Fi > Enable Random hardware addresses

Alternatively, you could use this free piece of software: <https://technitium.com/tmac/> <sup>[[Archive.org]](https://web.archive.org/web/https://technitium.com/tmac/)</sup>

#### Setting up a safe Browser { #windows-safe-browser }

See [Safe Browser on the Host OS](#safe-browser-host-os)

#### Enable some additional privacy settings on your Host OS { #windows-privacy-settings }

See [Windows Additional Privacy Settings](#win-additional-privacy)

##### Windows Host OS encryption { #windows-encryption }

###### If you intend to use system-wide plausible deniability { #windows-with-deniability }

Veracrypt[^330] is the software we will recommend for full-disk encryption, file encryption, and plausible deniability. It is a fork of the well-known but deprecated and unmaintained TrueCrypt. It can be used for:

- Full Disk simple encryption (your hard drive is encrypted with one passphrase).

- Full Disk encryption with plausible deniability (this means that depending on the passphrase entered at boot, you will either boot a decoy OS or a hidden OS).

- File container simple encryption (it is a large file that you will be able to mount within Veracrypt as if it were an external drive to store encrypted files within).

- File container with plausible deniability (it is the same large file but depending on the passphrase you use when mounting it, you will either mount a "hidden volume" or the "decoy volume").

It is to my knowledge the only (convenient and usable by anyone) free, open-source, and openly audited[^331] encryption software that also provides plausible deniability for widespread use and it works with Windows Home Edition.

Go ahead and download and install Veracrypt from: <https://www.veracrypt.fr/en/Downloads.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.veracrypt.fr/en/Downloads.html)</sup>

After installation, please take a moment to review the following options that will help mitigate some attacks:

- Encrypt the memory with a Veracrypt option[^332] (settings > performance/driver options > encrypt RAM) at a cost of 5-15% performance. This setting will also disable hibernation (which does not actively clear the key when hibernating) and instead encrypt the memory altogether to mitigate some cold-boot attacks. More details about this feature here: <https://sourceforge.net/p/veracrypt/discussion/technical/thread/3961542951/> <sup>[[Archive.org]](https://web.archive.org/web/https://sourceforge.net/p/veracrypt/discussion/technical/thread/3961542951/)</sup>

- Enable the Veracrypt option to wipe the keys from memory if a new device is inserted (system > settings > security > clear keys from memory if a new device is inserted). This could help in case your system is seized while still on (but locked).

- Enable the Veracrypt option to mount volumes as removable volumes (Settings > Preferences > Mount volume as removable media). This will prevent Windows from writing some logs about your mounts in the Event logs[^333] and prevent some local data leaks.

- Be careful and have a good situational awareness if you sense something weird. Shut your laptop down as fast as possible.

If you do not want to use encrypted memory (because performance might be an issue), you should at least enable hibernation instead of sleep. This will not clear the keys from memory (you are still vulnerable to cold boot attacks) but at least should mitigate them if your memory has enough time to decay.

More details later in [Route A and B: Simple Encryption using Veracrypt (Windows tutorial)].

###### If you do not intend to use system-wide plausible deniability { #windows-no-deniability }

For this case, we will recommend the use of BitLocker instead of Veracrypt for the full disk encryption. The reasoning is that BitLocker does not offer a plausible deniability possibility contrary to Veracrypt. A hard adversary has then no incentive in pursuing his "enhanced" interrogation if you reveal the passphrase.

Normally, you should have installed Windows Pro in this case and the BitLocker setup is quite straightforward.

Basically, you can follow the instructions here: <https://support.microsoft.com/en-us/windows/turn-on-device-encryption-0c453637-bc88-5f74-5105-741561aae838> <sup>[[Archive.org]](https://web.archive.org/web/https://support.microsoft.com/en-us/windows/turn-on-device-encryption-0c453637-bc88-5f74-5105-741561aae838)</sup>

But here are the steps:

- Click the Windows Menu

- Type "Bitlocker"

- Click "Manage Bitlocker"

- Click "Turn on Bitlocker" on your System Drive

- Follow the instructions

    - **Do not save your recovery key to a Microsoft Account if prompted.**

    - **Only save the recovery key to an external encrypted drive. To bypass this, print the recovery key using the Microsoft Print to PDF printer and save the key within the Documents folder. Delete that file later.**

    - **Encrypt Entire Drive (do not encrypt the used disk space only).**

    - **Use "New Encryption Mode"**

    - **Run the BitLocker Check**

    - **Reboot**

- Encryption should now be started in the background (you can check by clicking the Bitlocker icon on the lower right side of the taskbar).

Unfortunately, this is not enough. With this setup, your Bitlocker key can just be stored as-is in the TPM chip of your computer. This is rather problematic as the key can be extracted in some cases with ease[^334]'[^335]'[^336]'[^337].

To mitigate this, you will have to enable a few more options as per the recommendations of Microsoft[^338]:

- Click the Windows icon

- Type Run

- Type "gpedit.msc" (this is the group policy editor)

- Navigate to Computer Configuration > Administrative Templates > Windows Components > BitLocker > Operating System Drives

    - Double Click the "Require Additional Authentication at Startup"

        + Click the "Configure TPM Startup PIN" and set it to "Require Startup PIN with TPM"

    - Double Click the "Allow enhanced PINs for startup"

        + Click the "Enable" (this will allow us to set a password rather than a PIN)

- Close the Group Policy Editor

- Click the Windows icon

- Type Command to display the "Command Prompt"

- Right Click on it and click "Run as Administrator"

- Run ```manage-bde -protectors -delete c:``` (this will delete current protection: the recovery key you will not need)

- Run ```manage-bde -protectors -add c: -TPMAndPIN``` (this will prompt you for a pre-boot password)

    - Enter a password or passphrase of your choice (a good one)

- Run ```manage-bde -status```

    - You should now see at your C: drive below "Key Protectors" the option "TPM and PIN"

- You are done

Now when you reboot your computer, you should ideally be prompted for:

- A BIOS/UEFI boot password

- An SSD/HDD unlock password (if the feature is available on your BIOS)

- A Bitlocker Pre-Boot Pin Screen where you need to enter the password/passphrase you just set-up

- And finally, the Windows Logon Screen where you can enter the credentials you set-up earlier

##### Enable Hibernation (optional) { #windows-hibernation }

Again, as explained earlier. You should never use the sleep/stand-by feature to mitigate some cold-boot and evil-maid attacks. Instead, you should Shut down or hibernate. You should therefore switch your laptop from sleeping to hibernating when closing the lid or when your laptop goes to sleep.

(**Note that you cannot enable hibernation if you previously enabled RAM encryption within Veracrypt)**

The reason is that Hibernation will actually shut down your laptop completely and clean the memory. Sleep on the other hand will leave the memory powered on (including your decryption key) and could leave your laptop vulnerable to cold-boot attacks.

By default, Windows 10/11 might not offer you this possibility so you should enable it by following this Microsoft tutorial: <https://docs.microsoft.com/en-us/troubleshoot/windows-client/deployment/disable-and-re-enable-hibernation> <sup>[[Archive.org]](https://web.archive.org/web/https://docs.microsoft.com/en-us/troubleshoot/windows-client/deployment/disable-and-re-enable-hibernation)</sup>

- Open an administrator command prompt (right-click on Command Prompt and "Run as Administrator")

- Run: powercfg.exe /hibernate on

- Now run the additional command: ```powercfg /h /type full```

    - **This command will make sure your hibernate mode is full and will fully clean the memory (not securely tho).**

After that you should go into your power settings:

- Open the Control Panel

- Open System & Security

- Open Power Options

- Open "Choose what the power button does"

- Change everything from sleep to hibernate or shutdown

- Go back to the Power Options

- Select Change Plan Settings

- Select Advanced Power Settings

- Change all the Sleep Values for each Power Plan to 0 (Never)

- Make sure Hybrid Sleep is Off for each Power Plan

- Enable Hibernate After the time you would like

- Disable all the Wake timers

#### Deciding which sub-route you will take { #windows-subroute }

Now you will have to pick your next step between two options:

- Route A: Simple encryption of your current OS

    - Pros:

        + Does not require you to wipe your laptop

        + No issue with local data leaks

        + Works fine with an SSD drive

        + Works with any OS

        + Simple

    - Cons:

        + You could be compelled by an adversary to reveal your password and all your secrets and will have no plausible deniability.

        + The danger of Online data leaks

- Route B: Simple encryption of your current OS with later use of plausible deniability on files themselves:

    - Pros:

        + Does not require you to wipe your laptop

        + Works fine with an SSD drive

        + Works with any OS

        + Plausible deniability is possible with "soft" adversaries

    - Cons:

        + The danger of Online Data leaks

        + The danger of Local Data leaks (that will lead to more work to clean up those leaks)

- Route C: Plausible Deniability Encryption of your Operating system (you will have a "hidden OS" and a "decoy OS" running on the laptop):

    - Pros:

        + No issues with local Data leaks

        + Plausible deniability is possible with "soft" adversaries

    - Cons:

        + Requires Windows (this feature is not "easily" supported on Linux).

        + The danger of online Data leaks

        + Requires full wipe of your laptop

        + No use with an SSD drive due to the requirement of disabling Trim[^339] Operations[^340]. This will severely degrade the performance/health of your SSD drive over time.

**As you can see, Route C only offers two privacy advantages over the others, and it will only be of use against a soft lawful adversary. Remember <https://en.wikipedia.org/wiki/Rubber-hose_cryptanalysis>** <sup>[[Wikiless]](https://wikiless.tiekoetter.com/wiki/Rubber-hose_cryptanalysis)</sup> <sup>[[Archive.org]](https://web.archive.org/web/https://en.wikipedia.org/wiki/Rubber-hose_cryptanalysis)</sup>**.**

Deciding which route you will take is up to you. Route A is a minimum.

**Always be sure to check for new versions of Veracrypt frequently to ensure you benefit from the latest patches. Especially check this before applying large Windows updates that might break the Veracrypt bootloader and send you into a boot loop.**

**NOTE THAT BY DEFAULT VERACRYPT WILL ALWAYS PROPOSE A SYSTEM PASSWORD IN QWERTY (display the password as a test). This can cause issues if your boot input is using your laptop's keyboard (AZERTY for example) as you will have set up your password in QWERTY and will input it at boot time in AZERTY. So, make sure you check when doing the test boot what keyboard layout your BIOS is using. You could fail to log in just because of the QWERTY/AZERTY mix-up. If your BIOS boots using AZERTY, you will need to type the password in QWERTY within Veracrypt.**

##### Route A and B: Simple Encryption using Veracrypt (Windows tutorial) { #veracrypt-simple-encryption }

**Skip this step if you used BitLocker instead earlier.**

You do not have to have an HDD for this method, and you do not need to disable Trim on this route. Trim leaks will only be of use to forensics in detecting the presence of a Hidden Volume but will not be of much use otherwise.

This route is rather straightforward and will just encrypt your current Operating System in place without losing any data. Be sure to read all the texts Veracrypt is showing you, so you have a full understanding of what is going on. Here are the steps:

- Launch VeraCrypt

- Go into Settings:

    - Settings > Performance/driver options > Encrypt RAM

    - System > Settings > Security > Clear keys from memory if a new device is inserted

    - System > Settings > Windows > Enable Secure Desktop

- Select System

- Select Encrypt System Partition/Drive

- Select Normal (Simple)

- Select Single-Boot

- Select AES as encryption Algorithm (click the test button if you want to compare the speeds)

- Select SHA-512 as hash Algorithm (because why not)

- Enter a strong passphrase (longer the better, remember [Guidelines for passwords and passphrases](#password-guidelines))

- Collect some entropy by randomly moving your cursor around until the bar is full

- Click Next as the Generated Keys screen

- To rescue disk[^341] or not rescue disk, well that is up to you. We recommend making one (just in case), just make sure to store it outside your encrypted drive (USB key for instance or wait and see the end of this guide for guidance on safe backups). This rescue disk will not store your passphrase and you will still need it to use it.

- Wipe mode:

    - If you have no sensitive data yet on this laptop, select None

    - If you have sensitive data on an SSD, Trim alone should take care of it[^342] but we would recommend one pass (random data) just to be sure.

    - If you have sensitive data on an HDD, there is no Trim, and we Swould recommend at least 1-pass.

- Test your setup. Veracrypt will now reboot your system to test the bootloader before encryption. This test must pass for encryption to go forward.

- After your computer rebooted and the test is passed. You will be prompted by Veracrypt to start the encryption process.

- Start the encryption and wait for it to complete.

- You are done, skip Route B and go to the next steps.

There will be another section on creating encrypted file containers with Plausible Deniability on Windows.

##### Route B: Plausible Deniability Encryption with a Hidden OS (Windows only) { #veracrypt-hidden-os }

**This is only supported on Windows.**

**This is only recommended on an HDD drive. This is not recommended on an SSD drive.**

**Your Hidden OS should not be activated (with an MS product key). Therefore, this route will recommend and guide you through a full clean installation that will wipe everything on your laptop.**

Read the Veracrypt Documentation <https://www.veracrypt.fr/en/VeraCrypt%20Hidden%20Operating%20System.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.veracrypt.fr/en/VeraCrypt%20Hidden%20Operating%20System.html)</sup> (Process of Creation of Hidden Operating System part) and <https://www.veracrypt.fr/en/Security%20Requirements%20for%20Hidden%20Volumes.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.veracrypt.fr/en/Security%20Requirements%20for%20Hidden%20Volumes.html)</sup> (Security Requirements and Precautions Pertaining to Hidden Volumes).

This is how your system will look after this process is done:

![image22](../media/image22.png)

(Illustration from Veracrypt Documentation, <https://veracrypt.fr/en/VeraCrypt%20Hidden%20Operating%20System.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.veracrypt.fr/en/VeraCrypt%20Hidden%20Operating%20System.html)</sup>)

As you can see this process requires you to have two partitions on your hard drive from the start.

This process will do the following:

- Encrypt your second partition (the outer volume) that will look like an empty unformatted disk from the decoy OS.

- Prompt you with the opportunity to copy some decoy content within the outer volume.

    - This is where you will copy your decoy Anime/Porn collection from some external hard drive to the outer volume.

- Create a hidden volume within the outer volume of that second partition. This is where the hidden OS will reside.

- Clone your currently running Windows 10/11 installation onto the hidden volume.

- Wipe your currently running Windows 10/11.

- This means that your current Windows 10/11 will become the hidden Windows 10/11 and that you will need to reinstall a fresh decoy Windows 10/11 OS.

**Mandatory if you have an SSD drive and you still want to do this against the recommendation: Disable SSD Trim in Windows**[^343] **(again this is NOT recommended at all as** **disabling Trim in itself is highly suspicious**). **Also** **as mentioned earlier, disabling Trim will reduce the lifetime of your SSD drive and will significantly impact its performance over time (your laptop will become slower and slower over several months of use until it becomes almost unusable, you will then have to clean the drive and re-install everything). But you must do it to prevent data leaks**[^344] **that could allow forensics to defeat your plausible deniability**[^345][^346]**. The only way around this at the moment is to have a laptop with a classic HDD drive instead.**

###### Step 1: Create a Windows 10/11 install USB key { #hidden-os-step1 }

See [Windows Installation Media Creation](#win-installation-media) and go with the USB key route.

###### Step 2: Boot the USB key and start the Windows 10/11 install process (Hidden OS) { #hidden-os-step2 }

- Insert the USB key into your laptop

- See [Windows Installation](#windows-installation) and proceed with installing Windows 10/11 Home.

###### Step 3: Privacy Settings (Hidden OS) { #hidden-os-step3 }

See [Windows Additional Privacy Settings](#win-additional-privacy)

###### Step 4: Veracrypt installation and encryption process start (Hidden OS) { #hidden-os-step4 }

Remember to read <https://www.veracrypt.fr/en/VeraCrypt%20Hidden%20Operating%20System.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.veracrypt.fr/en/VeraCrypt%20Hidden%20Operating%20System.html)</sup>

Do not connect this OS to your known Wi-Fi. You should download the Veracrypt installer from a different computer and copy the installer here using a USB key. Here are the steps:

- Install Veracrypt

- Start Veracrypt

- Go into Settings:

    - Settings > Performance/driver options > Encrypt RAM (**note that this option is not compatible with Hibernation your laptop and means you will have to shut down completely)**

    - System > Settings > Security > Clear keys from memory if a new device is inserted

    - System > Settings > Windows > Enable Secure Desktop

- Go into System and select Create Hidden Operating System

- Read all the prompts thoroughly

- Select Single-Boot if prompted

- Create the Outer Volume using AES and SHA-512.

- Use all the space available on the second partition for the Outer Volume

- Use a strong passphrase (remember [Guidelines for passwords and passphrases](#password-guidelines))

- Select yes to Large Files

- Create some Entropy by moving the mouse around until the bar is full and select NTFS (do not select exFAT as you want this outer volume to look "normal" and NTFS is normal).

- Format the Outer Volume

- Open Outer Volume:

    - At this stage, you should copy decoy data onto the outer volume. So, you should have some sensitive but not so sensitive files/folders to copy there. In case you need to reveal a password to this Volume**.** This is a good place for your Anime/Mp3/Movies/Porn collection.

    - We recommend you do not fill the outer volume too much or too little (about 40%). Remember you must leave enough space for the Hidden OS (which will be the same size as the first partition you created during installation).

- Use a strong passphrase for the Hidden Volume (obviously a different one than the one for the Outer Volume).

- Now you will create the Hidden Volume, select AES and SHA-512

- Fill the entropy bar until the end with random mouse movements

- Format the hidden Volume

- Proceed with the Cloning

- Veracrypt will now restart and Clone the Windows where you started this process into the Hidden Volume. This Windows will become your Hidden OS.

- When the cloning is complete, Veracrypt will restart within the Hidden System

- Veracrypt will inform you that the Hidden System is now installed and then prompt you to wipe the Original OS (the one you installed previously with the USB key).

- Use 1-Pass Wipe and proceed.

- Now your Hidden OS will be installed, proceed to the next step

###### Step 5: Reboot and boot the USB key and start the Windows 10/11 install process again (Decoy OS) { #decoy-os-step5 }

Now that the Hidden OS is fully installed, you will need to install a Decoy OS:

- Insert the USB key into your laptop

- See [Windows Installation](#windows-installation) and proceed with installing Windows 10/11 Home again (do not install a different version and stick with Home).

###### Step 6: Privacy settings (Decoy OS) { #decoy-os-step6 }

See [Windows Additional Privacy Settings](#win-additional-privacy)

###### Step 7: Veracrypt installation and encryption process start (Decoy OS) { #decoy-os-step7 }

Now you will encrypt the Decoy OS:

- Install Veracrypt

- Launch VeraCrypt

- Select System

- Select Encrypt System Partition/Drive

- Select Normal (Simple)

- Select Single-Boot

- Select AES as encryption Algorithm (click the test button if you want to compare the speeds)

- Select SHA-512 as hash Algorithm (because why not)

- Enter a short weak password (yes this is serious, do it, it will be explained later).

- Collect some entropy by randomly moving your cursor around until the bar is full

- Click Next as the Generated Keys screen

- To rescue disk[^347] or not rescue disk, well that is up to you. We recommend making one (just in case), just make sure to store it outside your encrypted drive (USB key for instance or wait and see the end of this guide for guidance on safe backups). This rescue disk will not store your passphrase and you will still need it to use it.

- Wipe mode: Select 1-Pass just to be safe

- Pre-Test your setup. Veracrypt will now reboot your system to test the bootloader before encryption. This test must pass for encryption to go forward.

- After your computer rebooted and the test is passed. You will be prompted by Veracrypt to start the encryption process.

- Start the encryption and wait for it to complete.

- Your Decoy OS is now ready for use.

###### Step 8: Test your setup (Boot in Both) { #veracrypt-step8-test }

Time to test your setup:

- Reboot and input your Hidden OS passphrase, you should boot within the Hidden OS.

- Reboot and input your Decoy OS passphrase, you should boot within the Decoy OS.

- Launch Veracrypt on the Decoy OS and mount the second partition using the Outer Volume Passphrase (mount it as read-only, by going into Mount Options and Selecting Read-Only) and it should mount the second partition as a read-only displaying your decoy data (your Anime/Porn collection). You are mounting it as read-only now because if you were to write data on it, you could override content from your Hidden OS.

###### Step 9: Changing the decoy data on your Outer Volume safely { #veracrypt-step9-decoy-data }

Before going to the next step, you should learn the way to mount your Outer Volume safely for writing content on it. This is also explained in this official Veracrypt Documentation <https://www.veracrypt.fr/en/Protection%20of%20Hidden%20Volumes.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.veracrypt.fr/en/Protection%20of%20Hidden%20Volumes.html)</sup>

**You should do this from a safe, trusted space.**

Basically, you are going to mount your Outer Volume while also providing the Hidden Volume passphrase within the Mount Options to protect the Hidden Volume from being overwritten:

- Open Veracrypt

- Select your Second Partition

- Click Mount

- Click Mount Options

- Check the "Protect the Hidden volume..." Option

- Enter the Hidden OS passphrase

- Click OK

- Enter your Outer Volume passphrase

- Click OK

- You should now be able to open and write to your Outer Volume to change the content (copy/move/delete/edit...)

This operation will not actually mount the Hidden Volume and should prevent the creation of any forensic evidence that could lead to the discovery of the Hidden OS. However, while you are performing this operation, both passwords will be stored in your RAM. You could still be vulnerable to a Cold-Boot Attack. To mitigate this, be sure to have the option to encrypt your RAM as instructed before.

###### Step 10: Leave some forensics evidence of your Outer Volume (with the decoy Data) within your Decoy OS { #veracrypt-step10-forensics }

We must make the Decoy OS as plausible as possible. We also want your adversary to underestimate your intelligence.

It is important to voluntarily leave some forensic evidence of your Decoy Content within your Decoy OS. This evidence will let forensic examiners see that you mounted your Outer Volume frequently to access its content.

Here are useful tips to leave some forensics evidence:

- Play the content from the Outer Volume from your Decoy OS (using VLC for instance). Be sure to keep a history of those.

- Edit documents and work on them.

- Enable file indexing again on the Decoy OS and include the mounted Outer Volume.

- Unmount it and mount it frequently to watch some content or move files around.

- Copy some content from your Outer Volume to your Decoy OS and then delete it unsafely. Just put it in the Recycle Bin, which only someone who is naive would do, thinking it were deleted.

- Have a Torrent Client installed on the Decoy OS; use it from time to time to download some similar stuff that you will leave on the Decoy OS.

- You could have a VPN client installed on the Decoy OS with a known VPN of yours (non-cash paid).

Do not put anything suspicious on the Decoy OS such as:

- This guide

- Any links to this guide

- Any suspicious anonymity software such as Tor Browser

- Any Veracrypt volumes

- Any documents on anonymity or security

The intention is to make your adversary believe you are not as smart as they thought, to deter them from searching deeper.

###### Notes { #veracrypt-notes }

**Remember that you will need valid excuses for this plausible deniability scenario to work:**

- **You are using Veracrypt because you are using Windows 10/11 Home, which do not feature Bitlocker, but you still wanted reasonable Privacy.**

- **You have two partitions because you wanted to separate the system from the data for easy organization, and because some geeky friend told you this was better for performance.**

- **You have used a weak password for easy convenient booting of the system and a strong, long passphrase on the Outer Volume. You were too lazy to type a strong passphrase at each boot.**

- **You encrypted the second partition with a different password than the system because you do not want anyone in your group/domain to see your stuff. You did not want that data available to anyone.**

Take some time to read again the "Possible Explanations for Existence of Two Veracrypt Partitions on Single Drive" of the Veracrypt documentation here <https://www.veracrypt.fr/en/VeraCrypt%20Hidden%20Operating%20System.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.veracrypt.fr/en/VeraCrypt%20Hidden%20Operating%20System.html)</sup>

**Be careful:**

- **You should never mount the Hidden Volume from the Decoy OS (NEVER EVER). If you did this, it would create forensic evidence of the Hidden Volume within the Decoy OS which could jeopardize your attempt at plausible deniability**. If you did this anyway (intentionally or by mistake) from the Decoy OS, there are ways to erase forensic evidence that will be explained later at the end of this guide, so this mistake alone isn't a huge deal if you follow the steps in [Some additional measures against forensics](#anti-forensics).

- **Never use the Decoy OS from the same network (public Wi-Fi) as the Hidden OS.**

- **When you do mount the Outer Volume from the Decoy OS, do not write any data within the Outer Volume. This could override what looks like empty space, but is in fact your Hidden OS. You should always mount it as read-only.**

- **If you want to change the decoy content of the Outer Volume, you should use a Live OS USB Key that will run Veracrypt.**

- **Note that you will not use the Hidden OS to perform sensitive activities, this will be done later from a VM within the Hidden OS. The Hidden OS is only meant to protect you from soft lawful adversaries that could gain access to your laptop and compel you to reveal your password.**

- **Be careful of any tampering with your laptop. Evil-Maid Attacks can reveal your Hidden OS.**

