## Steps for all other routes { #steps-other-routes }

### Get a dedicated laptop { #dedicated-laptop }

Ideally, you should get a dedicated laptop that will not be tied to you in any effortless way (ideally paid with cash anonymously and using the same precautions as previously mentioned for the phone and the SIM card). It is recommended but not mandatory. This guide will help you harden your laptop as much as possible to prevent data leaks through various means. There will be several lines of defense standing between your online identities and yourself which should prevent most adversaries from de-anonymizing you - besides state/global actors. It will take considerable resources.

This laptop should ideally be a clean, freshly installed laptop (running Windows, Linux, or macOS); which is clean of your normal day-to-day activities; and which is offline (never connected to your home network). In the case of a Windows laptop, and if you used it before such a clean install, it should also not be activated. Simply reinstall without a product key in the case that it came pre-activated. Specifically, in the case of MacBooks, it should never have been tied to your identity before in any means. So, buy secondhand with cash from an unknown stranger who does not know your identity.

This is to mitigate some future issues in case of online leaks (including telemetry from your OS or Apps) that could compromise any unique identifiers of the laptop while using it (MAC Address, Bluetooth Address, and Product key ...). But also, to avoid being tracked back if you need to dispose of the laptop.

If you used this laptop before for different purposes (like your day-to-day activities), all its hardware identifiers are probably known and registered by Microsoft or Apple. If later any of those identifiers is compromised (by malware, telemetry, exploits, human errors ...) they could lead back to you.

The laptop should have at least 250GB of Disk Space **at least 6GB (ideally 8GB or 16GB)** of RAM and should be able to run a couple of Virtual Machines at the same time. It should have a working battery that lasts a few hours. You should aim for something with large storage (1TB+) if possible because we will need as much as possible.

This laptop could have an HDD (7200rpm) or an SSD/NVMe drive. Both possibilities have their benefits and issues that will be detailed later.

All future online steps performed with this laptop should ideally be done from a safe network such as Public Wi-Fi in a safe place (see [Find some safe places with decent public Wi-Fi](#safe-wifi)). But several steps will have to be taken offline first.

### Some laptop recommendations { #laptop-recommendations }

We would strongly recommend getting a "business grade" laptop (meaning not consumer/gaming-grade laptop) if you can. For instance, some ThinkPad from Lenovo (my personal favorite).

This is because those business laptops usually offer better and more customizable security features (especially in the BIOS/UEFI settings) with longer support than most consumer laptops (Asus, MSI, Gigabyte, Acer...). The interesting features to look for are:

- Better custom Secure Boot **settings (where you can selectively manage all the keys and not just use the Standard ones)**

- HDD/SSD passwords in addition to just BIOS/UEFI passwords.

- AMD laptops could be more interesting as some provide the ability to disable AMD PSP (the AMD equivalent of IME) from the BIOS/UEFI settings by default. And, because AFAIK, AMD PSP was audited and contrary to IME was not found to have any "evil" functionalities[^304]. However, if you are going for the Qubes OS Route consider Intel CPUs as Qubes OS does not support AMD with their anti-evil-maid system[^305].

- Secure Wipe tools from the BIOS (especially useful for SSD/NVMe drives, see [BIOS/UEFI options to wipe disks in various Brands](#bios-disk-wipe-options)).

- Better control over the disabling/enabling of select peripherals (USB ports, Wi-Fis, Bluetooth, Camera, Microphone ...).

- Better security features with Virtualization.

- Native anti-tampering protections.

- Longer support with BIOS/UEFI updates (and subsequent BIOS/UEFI security updates).

- Some are supported by Libreboot

### Bios/UEFI/Firmware Settings of your laptop { #bios-uefi-settings }

#### PC { #bios-pc }

These settings can be accessed through the boot menu of your laptop. Here is a good tutorial from HP explaining all the ways to access the BIOS on various computers: <https://store.hp.com/us/en/tech-takes/how-to-enter-bios-setup-windows-pcs> <sup>[[Archive.org]](https://web.archive.org/web/https://store.hp.com/us/en/tech-takes/how-to-enter-bios-setup-windows-pcs)</sup>

Usually how to access it is by pressing a specific key (F1, F2, or Del) at boot (before your OS).

Once you are in there, you will need to apply a few recommended settings:

- Disable Bluetooth completely if you can.

- Disable Biometrics (fingerprint scanners) if you have any if you can. However, you could add a biometric additional check for booting only (pre-boot) but not for accessing the BIOS/UEFI settings.

- Disable the Webcam and Microphone if you can.

- Enable BIOS/UEFI password and use a long passphrase instead of a password (if you can) and make sure this password is required for:

    - Accessing the BIOS/UEFI settings themselves

    - Changing the Boot order

    - Startup/Power-on of the device

- Enable HDD/SSD password if the feature is available. This feature will add another password on the HDD/SSD itself (not in the BIOS/UEFI firmware) that will prevent this HDD/SSD from being used in a different computer without the password. Note that this feature is also specific to some manufacturers and could require specific software to unlock this disk from a completely different computer.

- Prevent accessing the boot options (the boot order) without providing the BIOS/UEFI password if you can.

- Disable USB/HDMI or any other port (Ethernet, Firewire, SD card ...) if you can.

- Disable Intel ME if you can (odds are very high you can't).

- Disable AMD PSP if you can (AMD's equivalent to IME, see [Your CPU](#cpu))

- Disable Secure Boot if you intend to use Qubes OS as they do not support it out of the box[^306]. Keep it on if you intend to use Linux/Windows.

- Check if your laptop BIOS has a secure erase option for your HDD/SSD that could be convenient in case of need.

Only enable those on a "need to use" basis and disable them again after use. This can help mitigate some attacks in case your laptop is seized while locked but still on OR if you had to shut it down rather quickly and someone took possession of it (this topic will be explained later in this guide).

##### About Secure boot { #secure-boot }

So, what is Secure Boot[^307]? In short, it is a UEFI security feature designed to prevent your computer from booting an operating system from which the bootloader was not signed by specific keys stored in the UEFI firmware of your laptop.

When the operating system (or the Bootloader[^308]) supports it, you can store the keys of your bootloader in your UEFI firmware, and this will prevent booting up any unauthorized Operating System (such as a live OS USB or anything similar).

Secure Boot settings are protected by the password you set up to access the BIOS/UEFI settings. If you have that password, you can disable Secure Boot and allow unsigned OSes to boot on your system. This can help mitigate some Evil-Maid attacks (explained later in this guide).

In most cases, Secure Boot is disabled by default or is enabled but in "setup" mode which will allow any system to boot. For Secure Boot to work, your Operating System will have to support it and then sign its bootloader and push those signing keys to your UEFI firmware. After that, you will have to go to your BIOS/UEFI settings and save those pushed keys from your OS and change the Secure Boot from setup to user mode (or custom mode in some cases).

After doing that step, only the Operating Systems from which your UEFI firmware can verify the integrity of the bootloader will be able to boot.

Most laptops will have some default keys already stored in the secure boot settings. Usually, those are from the manufacturer itself or some companies such as Microsoft. So, this means that by default, it will always be possible to boot some USB disks even with secure boot. These include Windows, Fedora, Ubuntu, Mint, Debian, CentOS, OpenSUSE, Tails, Clonezilla, and many others. Secure Boot is however not supported at all by Qubes OS at this point.

In some laptops, you can manage those keys and remove the ones you do not want with a "custom mode" to only authorize your bootloader that you could sign yourself if you want to.

So, what is Secure Boot protecting you from? It will protect your laptop from booting unsigned bootloaders (by the OS provider) with for instance injected malware.

What is Secure Boot **not** protecting you from?

- Secure Boot is not encrypting your disk and an adversary can still just remove the disk from your laptop and extract data from it using a different machine. Secure Boot is therefore useless without full disk encryption.

- Secure Boot is not protecting you from a signed bootloader that would be compromised and signed by the manufacturer itself (Microsoft for example in the case of Windows). Most mainstream Linux distributions are signed these days and will boot with Secure Boot enabled.

- Secure Boot can have flaws and exploits like any other system. If you are running an old laptop that does not benefit from new BIOS/UEFI updates, these can be left unfixed.

Additionally, several attacks could be possible against Secure Boot as explained (in-depth) in these technical videos:

- Defcon 22, <https://www.youtube.com/watch?v=QDSlWa9xQuA> <sup>[[Invidious]](https://yewtu.be/watch?v=QDSlWa9xQuA)</sup>

- BlackHat 2016, <https://www.youtube.com/watch?v=0fZdL3ufVOI> <sup>[[Invidious]](https://yewtu.be/watch?v=0fZdL3ufVOI)</sup>

**So, it can be useful as an added measure against some adversaries but not all. Secure Boot in itself is not encrypting your hard drive. It is an added layer but that is it.**

**I still recommend you keep it on if you can.**

#### Mac { #bios-mac }

Take a moment to set a firmware password according to the tutorial here: <https://support.apple.com/en-au/HT204455> <sup>[[Archive.org]](https://web.archive.org/web/https://support.apple.com/en-au/HT204455)</sup>

You should also enable firmware password reset protection (available from Catalina) according to the documentation here: <https://support.apple.com/en-gb/guide/security/sec28382c9ca/web> <sup>[[Archive.org]](https://web.archive.org/web/https://support.apple.com/en-gb/guide/security/sec28382c9ca/web)</sup>

This feature will mitigate the possibility for some adversaries to use hardware hacks to disable/bypass your firmware password. Note that this will also prevent Apple themselves from accessing the firmware in case of repair.

### Physically Tamper protect your laptop { #tamper-protection }

At some point, you will inevitably leave this laptop alone somewhere. You will not sleep with it and take it everywhere every single day. You should make it as hard as possible for anyone to tamper with it without you noticing it. This is mostly useful against some limited adversaries that will not use a 5$ wrench against you[^11].

It is important to know that it is trivially easy for some specialists to install a key logger in your laptop, or to just make a clone copy of your hard drive that could later allow them to detect the presence of encrypted data in it using forensic techniques (more on that later).

Here is a good cheap method to make your laptop tamper-proof using Nail Polish (with glitter) <https://mullvad.net/en/help/how-tamper-protect-laptop/> <sup>[[Archive.org]](https://web.archive.org/web/https://mullvad.net/en/help/how-tamper-protect-laptop/)</sup> [^309] (with pictures).

While this is a good cheap method, it could also raise suspicions as it is quite "noticeable" and might just reveal that you "have something to hide". So, there are more subtle ways of achieving the same result. You could also for instance make a close-up macro photography of the back screws of your laptop or just use a small amount of candle wax within one of the screws that could just look like usual dirt. You could then check for tampering by comparing the photographs of the screws with new ones. Their orientation might have changed a bit if your adversary was not careful enough (Tightening them exactly the same way they were before). Or the wax within the bottom of a screw head might have been damaged compared to before.

![image20](../media/image20.png)

![image21](../media/image21.png)

The same techniques can be used with USB ports where you could just put a tiny amount of candle wax within the plug that would be damaged by inserting a USB key in it.

In riskier environments, check your laptop for tampering before using it regularly.

