## The Tails route { #tails-route }

This part of the guide will help you in setting up Tails if one of the following is true:

- You cannot afford a dedicated laptop

- Your dedicated laptop is just too old and too slow

- You have very low IT skills

- You decide to go with Tails anyway

Tails[^301] stands for **The Amnesic Incognito Live System**. It is a bootable Live Operating System running from a USB key that is designed for leaving no traces and forcing all connections through the Tor network.

You insert the Tails USB key into your laptop, boot from it and you have a full operating system running with privacy and anonymity in mind. As soon as you shut down the computer, everything will be gone unless you saved it somewhere.

Tails is an amazingly straightforward way to get going in no time with what you have and without much learning. It has extensive documentation and tutorials.

**WARNING: Tails is not always up to date with their bundled software. And not always up to date with the Tor Browser updates either. You should always make sure you are using the latest version of Tails and you should use extreme caution when using bundled apps within Tails that might be vulnerable to exploits and reveal your location**[^302]**.**

It does however have some drawbacks:

- Tails uses Tor and therefore you will be using Tor to access any resource on the internet. This alone will make you suspicious to most platforms where you want to create anonymous accounts (this will be explained in more detail later).

- Your ISP (whether it is yours or some public Wi-Fi) will also see that you are using Tor, and this could make you suspicious in itself.

- Tails does not include (natively) some of the software you might want to use later which will complicate things quite a bit if you want to run some specific things (Android Emulators for instance).

- Tails uses Tor Browser which while it is very secure will be detected as well by most platforms and will hinder you in creating anonymous identities on many platforms.

- Tails will not protect you more from the 5$ wrench[^11].

- Tor in itself might not be enough to protect you from an adversary with enough resources as explained earlier.

**Important Note: If your laptop is monitored/supervised and some local restrictions are in place, please read** [How to bypass (some) local restrictions on supervised computers](#bypass-local-restrictions)**.**

You should also read Tails Documentation, Warnings, and limitations, before going further <https://tails.boum.org/doc/about/warnings/index.en.html> <sup>[[Archive.org]](https://web.archive.org/web/https://tails.boum.org/doc/about/warnings/index.en.html)</sup>

Taking all this into account and the fact that their documentation is great, we will just redirect you towards their well-made and well-maintained tutorial:

<https://tails.boum.org/install/index.en.html> <sup>[[Archive.org]](https://web.archive.org/web/https://tails.boum.org/install/index.en.html)</sup>, pick your flavor and proceed.

If you're having an issue accessing Tor due to censorship or other issues, you can try using Tor Bridges by following this Tails tutorial: <https://tails.boum.org/doc/anonymous_internet/tor/index.en.html> <sup>[[Archive.org]](https://web.archive.org/web/https://tails.boum.org/doc/anonymous_internet/tor/index.en.html)</sup> and find more information about these on Tor Documentation <https://2019.www.torproject.org/docs/bridges> <sup>[[Archive.org]](https://web.archive.org/web/https://2019.www.torproject.org/docs/bridges)</sup>

**If you think using Tor alone is dangerous/suspicious, see [What about when Tor and VPNs aren't possible?](#tor-vpn-not-possible)**

### Tor Browser settings on Tails { #tails-tor-settings }

When using Tor Browser, you should click the little shield Icon (upper right, next to the Address bar) and select your Security level (see <https://tb-manual.torproject.org/security-settings/> <sup>[[Archive.org]](https://web.archive.org/web/https://tb-manual.torproject.org/security-settings/)</sup> for details). Basically, there are three.

- Standard (the default):

    - All features are enabled (including JavaScript)

- Safer:

    - JavaScript is disabled on non-HTTPS websites

    - Some fonts and symbols are disabled

    - Any media playback is "click to play" (disabled by default)

- Safest:

    - Javascript is disabled everywhere

    - Some fonts and symbols are disabled

    - Any media playback is "click to play" (disabled by default)

We would recommend the "Safer" level for most cases. The Safest level should be enabled if you think you are accessing suspicious or dangerous websites or if you are extra paranoid. The Safest mode will also most likely break many websites that rely actively on JavaScript.

If you are extra paranoid, use the "Safest" level by default and consider downgrading to Safer is the website is unusable because of Javascript blocking.

Lastly, while using Tor Browser on Tails on the "Safer" level, please consider [Additional browser precautions with JavaScript enabled](#browser-precautions-js).

When you are done and have a working Tails on your laptop, go to the [Creating your anonymous online identities](#creating-identities) step much further in this guide or if you want persistence and plausible deniability, continue with the next section.

### Persistent Plausible Deniability using Whonix & Tails { #whonix-tails-deniability }

Consider checking the <https://github.com/aforensics/HiddenVM> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/aforensics/HiddenVM)</sup> project for Tails.

This project is a clever idea of a one-click self-contained VM solution that you could store on an encrypted disk using plausible deniability[^311] (see [The Whonix route](#whonix-route) first chapters and also for some explanations about Plausible deniability, as well as the [How to securely delete specific files/folders/data on your HDD/SSD and Thumb drives:] section at the end of this guide for more understanding).

This would allow the creation of a hybrid system mixing Tails with the Virtualization options of the Whonix route in this guide.

![image19](../media/image19.png)

**Note: See** [Pick your connectivity method](#whonix-connectivity) **in the Whonix Route for more explanations about Stream Isolation**

In short:

- You could run non-persistent Tails from one USB key (following their recommendations)

- You could store persistent VMs within a secondary container that could be encrypted normally or using the Veracrypt plausible deniability feature (these could be Whonix VMs for instance or any other).

- You do benefit from the added Tor Stream Isolation feature (see [Tor over VPN] for more info about stream isolation).

In that case, as the project outlines it, there should be no traces of any of your activities on your computer and the sensitive work could be done from VMs stored into a Hidden container that should not be easily discoverable by a soft adversary.

**This option is particularly interesting for "traveling light" and to mitigate forensics attacks while keeping persistence on your work.** You only need 2 USB keys (one with Tails and one with a Veracrypt container containing persistent Whonix). The first USB key will appear to contain just Tails and the second USB will appear to contain just random garbage but will have a decoy volume which you can show for plausible deniability.

You might also wonder if this will result in a "Tor over Tor" setup, but it will not. The Whonix VMs will be accessing the network directly through clearnet and not through Tails Onion Routing.

In the future, this could also be supported by the Whonix project themselves as explained here: [Whonix-Host](https://www.whonix.org/wiki/Whonix-Host) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Whonix-Host)</sup> but it is not yet recommended for end-users.

Remember that encryption with or without plausible deniability is not a silver bullet and will be of little use in case of torture. As a matter a fact, depending on who your adversary would be (your threat model), it might be wise not to use Veracrypt (formerly TrueCrypt) at all as shown in this demonstration: <https://defuse.ca/truecrypt-plausible-deniability-useless-by-game-theory.htm> <sup>[[Archive.org]](https://web.archive.org/web/https://defuse.ca/truecrypt-plausible-deniability-useless-by-game-theory.htm)</sup>

**Plausible deniability is only effective against soft lawful adversaries that will not resort to physical means.**

**See <https://en.wikipedia.org/wiki/Rubber-hose_cryptanalysis>** <sup>[[Wikiless]](https://wikiless.tiekoetter.com/wiki/Rubber-hose_cryptanalysis)</sup> <sup>[[Archive.org]](https://web.archive.org/web/https://en.wikipedia.org/wiki/Rubber-hose_cryptanalysis)</sup>

CAUTION: Please see [**Considerations for using external SSD drives**](#on-external-ssd) and [**Understanding HDD vs SSD**](#hdd-vs-ssd) sections if you consider storing such hidden VMs on an external SSD drive:

- **Do not use hidden volumes on SSD drives as this is not supported/recommended by Veracrypt**[^303]**.**

- **Use instead file containers instead of encrypted volumes.**

- **Make sure you do know how to clean data from an external SSD drive properly.**

Here is my guide on how to achieve this:

**First Run**

- Download the latest HiddenVM release from <https://github.com/aforensics/HiddenVM/releases> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/aforensics/HiddenVM/releases)</sup>

- Download the latest Whonix XFCE release from [GitHub Releases](https://github.com/Whonix/whonix-gw-ga/releases/latest) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Download/VirtualBox/XFCE)</sup>

**Note:** As of guide v1.2.5, Whonix has been upgraded from version 17 to 18 (Whonix 18.1.4.x). See [[Upgrading to Whonix 18]](#qubes-whonix18) for the upgrade path if you currently use Whonix 17.x.

- Prepare a USB Key/Drive with Veracrypt

    - Create a Hidden Volume on the USB/Key Drive (We would recommend at least 16GB for the hidden volume)

    - In the Outer Volume, place some decoy files

    - In the Hidden Volume, place the HiddenVM appimage file

    - In the Hidden Volume, place the Whonix XFCE ova file

- Boot into Tails

- Setup the Keyboard layout as you want.

- Select Additional Settings and set an administrator (root) password (needed for installing HiddenVM)

- Start Tails

- Connect to a safe wi-fi (this is a required step for the rest to work)

- Go into Utilities and Unlock your Veracrypt (hidden) Volume (do not forget to check the hidden volume checkbox)

- Launch the HiddenVM appimage

- When prompted to select a folder, select the Root of the Hidden volume (where the Whonix OVA and HiddenVM app image files are).

- Let it do its thing (This will install Virtualbox within Tails with one click)

- When it is done, it should automatically start Virtualbox Manager.

- Import the Whonix OVA files (see [Whonix Virtual Machines](#whonix-vms))

Note, if during the import you are having issues such as "NS_ERROR_INVALID_ARG (0x80070057)", this is probably because there is not enough disk space on your Hidden volume for Whonix. Whonix themselves recommend 32GB of free space but that's probably not necessary and 10GB should be enough for a start. You can try working around this error by renaming the Whonix \*.OVA file to \*.TAR and decompressing it within Tails. When you are done with decompression, delete the OVA file and import the other files with the Import wizard. This time it might work.

**Subsequent Runs**

- Boot into Tails

- Connect to Wi-Fi

- Unlock your Hidden Volume

- Launch the HiddenVM App

- This should automatically open VirtualBox manager and show your earlier VMs from the first run

