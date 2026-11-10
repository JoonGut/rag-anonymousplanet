# Backing up your work securely { #secure-backups }

**Do not ever upload encrypted file containers with plausible deniability (hidden containers within them) to most cloud services (iCloud, Google Drive, OneDrive, Dropbox) without safety precautions. This is because most cloud services keep backups/versioning of your files, and such backups/versioning of your encrypted containers can be used for differential analysis to prove the existence of a hidden container.**

Instead, this guide will recommend other methods of backing up your stuff safely.

## Offline Backups { #offline-backups }

These backups can be done on an external hard drive or a USB key. Here are the various possibilities.

### Selected Files Backups { #selected-files-backup }

**Requirements**

For these back-ups, you will need a USB key or an external hard drive with enough storage capacity to store the files you want to back up.

#### Veracrypt { #backup-veracrypt }

For this purpose, we will recommend the use of Veracrypt on all platforms (Linux/Windows/macOS) for convenience, security, and portability.

#### Normal File containers { #normal-file-containers }

The process is fairly simple and all you will need is to follow Veracrypt tutorial here: <https://www.veracrypt.fr/en/Beginner%27s%20Tutorial.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.veracrypt.fr/en/Beginner%27s%20Tutorial.html)</sup>

In this container, you can then store sensitive data manually and or use any backup utility you want to backup files from the OS to that container.

You can then store this container anywhere safely.

#### Hidden File containers with plausible deniability { #hidden-file-containers }

The process is also fairly simple and similar to the earlier tutorial except for this time you will use the Veracrypt wizard to create a Hidden Veracrypt Volume instead of a Standard Veracrypt Volume.

You can create a Hidden volume within an existing Standard Volume or just use the wizard to create a new one.

Let us say you want a container of 8GB, the Wizard will first create an "outer volume" where you will be able to store decoy information when prompted. Some decoy files (somewhat sensible, plausible but not what you want to hide) should be stored in the decoy volume.

Then Veracrypt will ask you to create a smaller hidden container (for instance 2GB or 4GB) within the outer volume where you can store your actual hidden files.

When you select the file for mounting in Veracrypt, depending on which password you provide, it will mount the Outer decoy volume or the Hidden volume.

You can then mount your hidden volume and use it to store sensitive files normally.

**Be careful when mounting the Outer decoy volume to update its content. You should protect the hidden volume from being overwritten when doing this as working in the decoy volume could overwrite data in the hidden volume.**

To do this, when mounting the Decoy Volume, select Mount Options and Check the "Protect hidden volume" option and provide the hidden volume password on the same screen. Then mount the decoy volume. This will protect the hidden volume from being overwritten when changing the decoy files. This is also explained here in Veracrypt documentation: <https://www.veracrypt.fr/en/Protection%20of%20Hidden%20Volumes.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.veracrypt.fr/en/Protection%20of%20Hidden%20Volumes.html)</sup>

**Be extremely cautious with these file containers:**

- **Do not store multiple versions of them or store them anywhere where some versioning is being done (by the file system or the storage system). These file containers should be identical everywhere you store them. If you have a backup of such containers somewhere, it needs to be absolutely identical to the one you are using. If you do not take this precaution, an adversary could compare two different versions of this container and prove the existence of hidden data. Follow carefully the recommendations here <https://www.veracrypt.fr/en/Security%20Requirements%20for%20Hidden%20Volumes.html>** <sup>[[Archive.org]](https://web.archive.org/web/https://www.veracrypt.fr/en/Security%20Requirements%20for%20Hidden%20Volumes.html)</sup>**. Remember the [Local Data Leaks and Forensics](#local-data-leaks) section.**

- We strongly recommend storing such containers on external USB keys that you will only mount from your guest VMs and never from your Host OS. **After each modification to the files, you should clean the free space on the USB disk and make sure that any backup of such containers is absolutely identical on each key and your computer. See the [How to securely delete specific files/folders/data on your HDD/SSD and Thumb drives](#bios-disk-wipe-options) section of this guide for help on doing this.**

- If you have time, **We will even recommend that you delete wipe the keys completely before making any modification on such containers on your computer (if you do not work from the USB key directly).** This is to prevent an adversary that would seize your assets before you could update the keys from having multiple versions of the containers that could lead to proving the existence of hidden data using forensics techniques.

- **Do not ever store such containers on cloud storage platforms that have backups and where you have no direct control over permanent deletion. They might keep "old versions" of your files which can then also be used by forensics to prove the existence of hidden data.**

- If you are mounting the hidden volume from your Host OS (**not recommended**), you should erase all traces of this hidden volume everywhere after use. There could be traces in various places (system logs, file systems journaling, recent documents in your applications, indexing, registry entries...). Refer to the [Some additional measures against forensics](#anti-forensics) section of this guide to remove such artifacts. Especially on Windows. Instead, you should mount them on your Guest VMs. With Virtualbox for instance, you could take a snapshot of the VM before opening/working the hidden volume and then restore the snapshot before opening/working on it after use. This should erase the traces of its presence and mitigate the issue. Your Host OS might keep logs of the USB key being inserted but not of the hidden volume usage. Therefore, we do not recommend using these from your host OS.

- Do not store these on external SSD drives if you are not sure you can use Trim on them (see the [Understanding HDD vs SSD](#hdd-vs-ssd) section).

### Full Disk/System Backups { #full-disk-backup }

**TLDR version: Just use Clonezilla as it worked reliably and consistently with all my tests on all operating systems except for Macs where you should probably use native utilities (Time Machine/Disk utility instead) to avoid compatibility issues and since you are using Native macOS encryption. When using Windows, do not back up a partition containing a hidden OS in case you use Plausible Deniability** (as explained before, this backup could allow an adversary to prove the existence of the hidden OS by comparing the last backup to the current system where data will have changed and defeat plausible deniability, use file containers instead).

You will have two options here:

- (Not recommended) Doing your backup from the live operating system using a backup utility (commercial utilities such as EaseUS Todo Free, Macrium Reflect...) or native utilities like macOS Time Machine, QubesOS Backup, Ubuntu Déjà Dup, or Windows Backup...).

    - This backup can be done while the Operating System is running.

    - This backup will not be encrypted using the disk encryption but using the Backup utility encryption algorithm (which you will have to trust and cannot really control for most). Alternatively, you could encrypt the backup media yourself separately (for instance with Veracrypt). We are not aware of any free or non-free utility that natively supports Veracrypt.

    - Some utilities will allow for differential/incremental backups instead of full backups.

    - These backup utilities will not be able to restore your encrypted drive as-is as they do not support those encrypted file systems natively. And so, these will require more work to restore your system in an encrypted state (re-encryption after restoring).

- (Recommended) Doing it offline from a boot drive (such as with the free open-source Clonezilla).

    - This backup can only be done while the Operating System is not running.

    - This backup will back up the encrypted disk as-is and therefore will be encrypted by default with the same mechanism (it is more like a fire and forget solution). The restore will also restore the encryption as-is and your system will immediately be ready to use after a restore.

    - This method will not allow incremental/differential back-ups (meaning you will have to re-do a full backup every time).

    - This method is the easiest to manage.

We made extensive testing using live backups utilities (Macrium Reflect, EaseUS Todo Reflect, Déjà Dup...) and personally we do not think it is worth it. Instead, we would recommend that you periodically back up your system with a simple Clonezilla image. It is much easier to perform, much easier to restore, and usually works reliably without issues in all cases. And contrary to many beliefs, it is not that slow with most backups taking about an hour depending on the speed of your destination media.

For backing up single files while you work, we recommend using file containers or encrypted media directly and manually as explained in the earlier section.

#### Requirements { #backup-requirements }

You will need a separate external drive with at least the same or more free space available than your source disk. If your laptop has a 250GB disk. You will need at least 250GB of free disk space for the full image backup. Sometimes this will be reduced significantly with compression by the backup utility but as a safety rule, you should have at least the same or more space on your backup drive.

#### Some general warnings and considerations { #backup-warnings }

- If you use Secure Boot, you will need a backup utility that supports Secure Boot which includes Clonezilla AMD64 versions.

- Consider the use of exFAT as the file system for your backup drives as those will provide better compatibility between various OSes (macOS, Linux, and Windows) vs NTFS/HFS/ext4...

#### Linux { #backup-linux }

##### Ubuntu { #backup-ubuntu }

We will recommend the use of the open-source Clonezilla utility for convenience and reliability but there are many other native Linux utilities and methods you could use for this purpose.

So, you should follow the steps in [Clonezilla](#clonezilla)

##### QubesOS { #backup-qubes }

Qubes OS recommends using their own utility for backups as documented here <https://www.qubes-os.org/doc/backup-restore/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.qubes-os.org/doc/backup-restore/)</sup>. But it is just a hassle and provides limited added value unless you just want to back up a single Qube. So instead, we are also recommending just making a full image with Clonezilla which will remove all the hassle and bring you back a working system in a few simple steps.

So, you should follow the steps in [Clonezilla](#clonezilla)

#### Windows { #backup-windows }

We will only recommend the use of the open-source and free Clonezilla utility for this purpose. There are commercial utilities that offer the same functionality, but we do not see any advantage in using any of them vs Clonezilla.

Some warnings:

- If you use Bitlocker for encryption with TPM[^424] enabled, you might need to save your Bitlocker Key (safely) somewhere as well as this might be needed to restore your drive if your HDD/SSD or other hardware parts changed. Another option would be to use Bitlocker without the use of TPM which would not require this option. But again, we do not recommend using Bitlocker at all.

- You should always have a backup of your Veracrypt rescue disk at hand somewhere to be able to resolve some issues that might still appear after a restore. Remember this rescue disk does not contain your passphrase or any sensitive information. You can store it as is.

- If you changed the HDD/SSD after a failure, Windows 10/11 may refuse to boot if your hard drive ID is changed. You should also save this ID before backing up as you might need to change the ID of the new drive as Windows 10/11 might require a matching ID before booting. See [Diskpart.](#diskpart)

- **In case you are using Plausible Deniability on Windows. DO NOT back up the hidden OS partition as this image could be used by Forensics to prove the existence of the hidden volume as explained earlier. It is okay to back up the Decoy OS partition without issues, but you should never back up the partition containing the Hidden OS.**

Follow the steps in [Clonezilla](#clonezilla)

#### macOS { #backup-macos }

we would recommend just using the native Time Machine backup with encryption (and a strong passphrase that could be the same as your OS) as per the guides provided at Apple: <https://support.apple.com/en-ie/guide/mac-help/mh21241/mac> <sup>[[Archive.org]](https://web.archive.org/web/https://support.apple.com/en-ie/guide/mac-help/mh21241/mac)</sup> and <https://support.apple.com/en-ie/guide/mac-help/mh11421/11.0/mac/11.0> <sup>[[Archive.org]](https://web.archive.org/web/https://support.apple.com/en-ie/guide/mac-help/mh11421/11.0/mac/11.0)</sup>.

So, plug in an external drive and it should prompt you to use it as a Time Machine backup.

**You should however consider formatting this drive as exFAT so that it is also usable by other OSes conveniently (Windows/Linux) without added software using this guide: <https://support.apple.com/en-ie/guide/disk-utility/dskutl1010/mac>** <sup>[[Archive.org]](https://web.archive.org/web/https://support.apple.com/en-ie/guide/disk-utility/dskutl1010/mac)</sup>

It is just simpler and will work online while you work. You will be able to recover your data on any other Mac from the recovery options and you will be also able to use this disk for backing up other devices.

It is possible to also use Clonezilla to clone your Mac Hard Drive, but it could bring hardware compatibility issues and probably will not add much in terms of security. So, for macOS, We are not specifically recommending Clonezilla.

## Online Backups { #online-backups }

### Files { #online-backup-files }

This is a tricky one. The problem is that it depends on your threat model.

- **TLDR: Do not store file containers with plausible deniability (Veracrypt) online.** If you use containers with plausible deniability, you should never store them on any platform where you do not have full control over the deletion process as the platform will most likely have backups of previous versions for some time. And again, these previous versions could allow forensics to prove the existence of hidden data and defeat plausible deniability. This includes platforms like DropBox, Google Drive, OneDrive, or others. The only acceptable online storage of those could be "cold storage" (meaning you will never change those files again and just keep them away untouched compared to any local version).

- If you use normally encrypted backups without plausible deniability, you could store them pretty much anywhere if they are properly encrypted locally before uploading (for example with Veracrypt, using strong passphrases and encryption). **Do not ever trust the encryption of any online provider. Only trust your own local encryption (using Veracrypt for instance).** For these cases, you could store your backups pretty much anywhere in the accounts of your online identities (iCloud, Google Drive, DropBox...) if they are strongly encrypted locally before uploading. But you could also prefer privacy caring services such as Cryptpad.fr (1GB).

Obviously do not ever do/access those backups from unsecured/unsafe devices but only from the secure environments, you picked before.

#### Self-hosting { #self-hosting-backup }

Self-hosting (using Nextcloud for instance) is also a possibility provided you do have an anonymous hosting

**Please see [Recommended VPS hosting providers](#vps-hosting-providers).**

Please also consider [Monero Disclaimer](#monero-disclaimer).

#### Cloud-hosting { #cloud-hosting-backup }

For smaller files, consider:

- Cryptpad.fr (<https://cryptpad.fr/>): Free tier limited to 1GB total and recommended by PrivacyGuides.org at <https://privacyguides.org/cloud/> <sup>[[Archive.org]](https://web.archive.org/web/https://privacyguides.org/cloud/)</sup>

- Filen (<https://filen.io/>): free tier limited to 10GB total

We are currently not aware of any online storage/hosting platform accepting cash payments unlike providers mentioned before.

If you do intend to store sensitive data on "mainstream platforms" (Dropbox, Google Drive, OneDrive...), **remember not to ever store plausible deniability containers on those and remember to encrypt and check (for metadata...) anything locally before uploading there**. Either with software like Veracrypt or with a software like Cryptomator (<https://cryptomator.org/>). Do not ever upload non-encrypted files on those platforms and repeating myself, only access them from a secure shielded VM.

### Information { #online-backup-info }

If you just want to save information (text), we will recommend the use of secure and private pastebins[^425]. Mostly we will stick to the ones recommended by PrivacyGuides.org (<https://www.privacyguides.org/productivity/#paste-services> <sup>[[Archive.org]](https://web.archive.org/web/https://www.privacyguides.org/productivity/#paste-services)</sup> ) :

- <https://privatebin.info/>

- <https://cryptpad.fr/pad/>

On these providers, you can just create a password-protected pad with the information you want to store.

Just create a pad, protect it with a password and write your info in it. Remember the address of the pad.

## Synchronizing your files between devices Online { #file-sync }

To that, the answer is very simple and a clear consensus for everyone: <https://syncthing.net/> <sup>[[Archive.org]](https://web.archive.org/web/https://syncthing.net/)</sup>

Just use SyncThing, it is the safest and most secure way to synchronize between devices, it is free and open-source, and it can easily be used in a portable way without install from a container that needs syncing.

