# Covering your tracks { #covering-tracks }

## Understanding HDD vs SSD { #hdd-vs-ssd }

![image41](../media/image41.png)

If you intend to wipe your whole HDD laptop, the process is rather straightforward. The data is written at a precise location on a magnetic (hard) platter (why it is called a hard drive) and your OS knows precisely where it is on the platter, where to delete it, and where to overwrite it for secure deletion using simple processes (like just overwriting that location over and over until no traces are left).

On the other hand, if you are using an SSD drive, the process is not as simple as the drive uses several internal mechanisms to extend its lifespan and performance. Three of those processes are of particular interest when it comes to us in this guide. SSD drives are divided themselves into two main categories:

- ATA Drives (usually SATA and usually 2.5" format as the image above).

- NVMe Drives (usually M.2 format as the illustration below).

Here are examples of the most common formats:

![image42](../media/image42.png)

All of these are sold as internal and external drives within enclosures.

The methods and utilities to manage/wipe them will vary depending on the type of drive you are using. So, it is important you know which one you have inside your laptop.

**On most recent laptops, chances are high that it will be one of the middle options (M.2 SATA or M.2 NVMe).**

### Wear-Leveling { #wear-leveling }

These drives use a technique called wear leveling[^426]. At a high level, wear leveling works as follows. The space on every disk is divided into blocks that are themselves divided into pages, like the chapters in a book are made of pages. When a file is written to disk, it is assigned to a certain set of pages and blocks. If you wanted to overwrite the file in an HDD, then all you would have to do is tell the disk to overwrite those blocks. But in SSDs and USB drives, erasing and re-writing the same block can wear it out. Each block can only be erased and rewritten a limited number of times before that block just will not work anymore (the same way if you keep writing and erasing with a pencil and paper, eventually the paper might rip and be useless). To counteract this, SSDs and USB drives will try to make sure that the number of times each block has been erased and rewritten is about the same so that the drive will last as long as possible (thus the term wear leveling). As a side effect, sometimes instead of erasing and writing the block, a file was originally stored on, the drive will instead leave that block alone, mark it as invalid, and just write the modified file to a different block. This is like leaving the chapter in the book unchanged, writing the modified file on a different page, and then just updating the book's table of contents to point to the new location. All of this occurs at a very low level in the electronics of the disk, so the operating system does not even realize it has happened. This means, however, that even if you try to overwrite a file, there is no guarantee the drive will actually overwrite it, and that's why secure deletion with SSDs is so much harder.

Wear-leveling alone can therefore be a disadvantage for security and an advantage for adversaries such as forensics examiners. This feature makes classic "secure deletion" counter-productive and useless and is why this feature was removed on some Operating Systems like macOS (as from version 10.11 El Capitan) where you could enable it before on the Recycle Bin.

Most of those old secure deletion utilities were written with HDD in mind and have no control over wear-leveling and are completely pointless when using an SSD. Avoid them on an SSD drive.

### Trim Operations { #trim-operations }

So, what now? Well here comes the Trim[^427] operation. When you delete data on your SSD, your OS should support what is called a Trim operation command and **could (should)** issue this Trim command to the SSD drive periodically (daily, weekly, monthly...). This Trim command will then let know the SSD drive controller that there are pages within blocks containing data that are now free to be really deleted without deleting anything itself.

Trim should be enabled by default on all modern Operating Systems detecting an SSD drive covered in this guide (macOS, Windows 10/11, Ubuntu, Qubes OS 4.1.x ...).

If Trim operations are not done regularly (or at all), then the data is never deleted pro-actively and at some point, all the blocks and pages will be occupied by data. Your OS will not see this and will just see free space as you delete files, but your SSD controller will not (this is called Write Amplification[^428]). This will then force the SSD controller to erase those pages and blocks on the fly which will reduce the write performance. This is because while your OS/SSD can write data to any free page in any bock, erasure is only possible on entire blocks, therefore, forcing your SSD to perform many operations to write new data. Overwriting is just not possible. This will defeat the wear-leveling system and cause performance degradation of your SSD over time. Every time you delete a file on an SSD, your OS should issue a Trim command along with the deletion to let the SSD controller know the pages containing the file data are now free for deletion.

**So, Trim itself does not delete any data but just marks it for deletion.** Data deleted without using Trim (if Trim has been disabled/blocked/delayed for instance) will still be deleted at some point by the SSD garbage collection or if you want to overwrite what the OS sees at free space. But it might stick around for a bit longer than if you use Trim.

Here is an illustration from Wikipedia showing how it works on an SSD drive:

![image43](../media/image43.png)

As you can see in the above illustration, data (from a file) will be written to the four first pages of Block X. Later new data will be written to the remaining pages and the data from the first files will be marked as invalid (for instance by a Trim operation when deleting a file). As explained on <https://en.wikipedia.org/wiki/Trim_(computing)> <sup>[[Wikiless]](https://wikiless.tiekoetter.com/wiki/Trim_(computing))</sup> <sup>[[Archive.org]](https://web.archive.org/web/https://en.wikipedia.org/wiki/Trim_(computing))</sup>; the erase operation can only be done on entire blocks (and not on single pages).

In addition to marking files for deletion (on reputable SSD drives), Trim usually makes those unreadable using a method called "Deterministic Read After Trim" or "Deterministic Zeroes After Trim". This means that if an adversary tries to read data from a trimmed page/block and somehow manages to disable garbage collection, the controller will not return any meaningful data.

**Trim is your ally and should always be enabled when using an SSD drive and should offer sufficient reasonable protection**. And this is also the reason you should not use Veracrypt Plausible deniability on a Trim enabled SSD as this feature is incompatible with Trim[^429].

### Garbage Collection { #garbage-collection }

Garbage collection[^430] is an internal process running within your SSD drive that looks for data marked for erasure. This process is done by the SSD controller, and you have no control over it. If you go back to the illustration above, you will see that Garbage collection is the last step and will notice that some pages are marked for deletion in a specific block, then copy the valid pages (not marked for deletion) to a different free destination block and then will be able to erase the source block entirely.

Garbage collection in itself does NOT require Trim to function, but it will be much faster and more efficient if Trim is performed. Garbage collection is one of the processes that will actually erase data from your SSD drive permanently.

### Conclusion { #storage-conclusion }

So, the fact is that it is very unlikely[^431]'[^432] and difficult for a forensic examiner to be able to recover data from a Trimmed SSD but it is not completely impossible either[^433]'[^434]'[^435] if they are fast enough and have access to extensive equipment, skills, and motivation[^436].

Within the context of this guide which also uses full disk encryption. Deletion and Trim should be reasonably secure enough on any SSD drive and will be recommended as the standard method of deletion.

## How to securely wipe your whole Laptop/Drives { #secure-wipe-drives }

![image44](../media/image44.png)

So, you want to be sure. To achieve 100% secure deletion on an SSD drive, you will need to use specific SSD techniques (If you are using an HDD drive, skip this part and go to your OS of choice):

- Easy options for less experienced people:

    - If available, just use the Secure Erase option available from your BIOS/UEFI (ATA/NVME Secure Erase or Sanitize).
        + It's worth noting that this relies on your drive's firmware. Some drive manufacturers have messed up the implementation, causing data to still be recoverable.

    - Just re-install a fresh operating system (delete/quick format the drive) and re-encrypt it. The full disk encryption process should erase all previous data from the disk.

    - Buy PartedMagic[^437] for 11$ and use it to erase any disk.

- Technical options for more advanced people:

    - Overwrite the entire drive's contents
        + HDDs:
            * Overwrite the drive's contents using a tool like [srm](https://www.howtogeek.com/425232/how-to-securely-delete-files-on-linux/), [wipe](https://linux.die.net/man/1/wipe), [shred, etc.](https://recoverit.wondershare.com/harddrive-tips/format-and-wipe-linux-disk.html). Ideally you want to use the Gutmann method, which was created for most effective data erasure on all drives. This method also works on SSDs, although it is overkill.
            * Simply overwriting the drive's contents is not always enough. Dedicated secure deletion tools are designed to perform multiple passes to more effectively wipe data. This is expecially important on older drives. we recommend using either `wipe` or `srm`.
                - If using `wipe`, just use its default options (`wipe /dev/sdX`), as the defaults are tuned to most effectively wipe data on HDDs.
                - If using `srm`, make sure to manually specify that it should perform a Gutmann wipe (`srm -G /dev/sdX`).
        + SSDs:
            * Overwrite the drive's contents. Tools like wipe or shred are often overkill, as they perform up to 35 passes. While they work, most SSDs require no more than a couple passes.
            * Use `wipe` with only a couple passes: `wipe -qQ2 /dev/sdX`.
                - `-qQ2` means 2 passes. Replace `2` with the desired number of passes.
            * Use `srm` with a 3-pass overwrite: `srm -P /dev/sdX`.
            * Use `dd`: `dd if=/dev/urandom of=/dev/sdX bs=8M status=progress conv=fsync`. This command will overwrite the drive with random data. To perform multiple passes (I recommend at least 2), simply run the command again until you're satisfied.
                - The reason you run it twice is because SSDs have hidden ("overprovisioned") storage which can contain remnants of deleted data. Wiping twice forces the drive to wipe its overprovisioned storage. This is only guaranteed to work if each pass writes different data (which is why we wipe with random data on each pass).
                - `bs=8M` writes 8MiB blocks at a time. This doesn't affect the quality of the data deletion, but adjusting it could affect how long it takes to wipe the drive.

    - ATA/NVMe Secure Erase: This method will remove the mapping table that keeps track of allocated data on the storage Blocks but does not destroy the actual data.

    - ATA/NVMe Sanitize Crypto Scramble (aka Instant Secure Erase, Crypto Erase), which applies to self-encrypting SSD drives: This method will change the encryption key of the self-encrypting SSD drive and render all the data stored in it unreadable.

    - ATA/NVMe Sanitize Block Erase: This method performs an actual block erase on every storage block and will destroy the data and change the encryption key if present.

    - ATA/NVMe Sanitize Overwrite **(terribly slow, could be dangerous and not recommended)**: This method performs a block erase and then overwrite every storage block (it is the same as Block Erase but will overwrite data in addition). This method is overkill and not necessary.

- Physical Destruction:
    - HDDs:

        1. Open the drive (with a screwdriver, usually Torx T8)

        2. Remove platters (with a screwdriver, usually Torx T6)

        3. Rub the platters with a rare earth magnet

        4. Break/Deform/Crush the platters

        5. Burn the platters or cook them in an oven (**do not** skip this step)

        6. Separate the debris

        7. Throw away in separate places

    - SSDs:
        + Ideally you should wipe the drive through other means first, as this method alone is not known to be secure against all attackers

        1. Open the drive

        2. Break/Crush the board and memory cells

        3. Burn them

        4. Separate the debris

        5. Throw away in separate places

    - Bonus: See <https://www.youtube.com/watch?v=-bpX8YvNg6Y> <sup>[[Invidious]](https://yewtu.be/watch?v=-bpX8YvNg6Y)</sup>

For maximum overkill paranoia security, Sanitize Block Erase option should be preferred but Secure Erase is probably more than enough when considering your drive is already encrypted. Unfortunately, are no **free** easy (bootable with a graphical menu) all-in-one tools available and you will be left with either going with drive manufacturers provided tools, the free manual hdparm[^438] , and nvme-cli[^439] utilities or going with a commercial tool such as PartedMagic.

This guide will therefore recommend the use of the free utilities hdparm and nvme-cli using a Live System Rescue system.

If you can afford it, just buy Parted Magic for 11$ which provides an easy-to-use graphical tool for wiping SSD drives using the option of your choice[^440]'[^441].

**Note:** **Again, before proceeding, you should check your BIOS as some will offer a built-in tool to securely erase your drive (ATA/NVMe Secure Erase or ATA/NVMe Sanitize). If this is available, you should use that, and the following steps will not be necessary. Check this before going ahead to avoid the hassle, see [BIOS/UEFI options to wipe disks in various Brands](#bios-disk-wipe-options)).**

### Linux (all versions including Qubes OS) { #wipe-linux }

#### System/Internal SSD { #wipe-linux-ssd }

- Option A: Check if your BIOS/UEFI has a built-in option to do so and if it does, use the correct option ("ATA/NVMe Secure Erase" or "ATA/NVMe Sanitize"). Do not use wipe with passes on an SSD drive.

- Option B: See [Using System Rescue to securely wipe an SSD drive](#system-rescue-ssd-wipe)

- Option C: Wipe your disk and re-install Linux with new full disk encryption to overwrite all sectors with new encrypted data. **This method will be terribly slow compared to Option A and B as it will slowly overwrite your whole SSD. Also, note that this might not be the default behavior when using LUKS. You might have to check the option to also encrypt the empty space for this effectively wipe the drive.**

**Keep in mind all these options need to be applied on the entire physical drive and not on a specific partition/volume. If you do not, wear-leveling mechanisms might prevent this from working properly.**

#### External SSD { #wipe-linux-ext-ssd }

First please see [Considerations for using external SSD drives](#on-external-ssd)

Trim should be sufficient in most cases and you could just use the blkdiscard command to force an entire device trim as explained here: <https://wiki.archlinux.org/index.php/Solid_state_drive#Trim_an_entire_device> <sup>[[Archive.org]](https://web.archive.org/web/https://wiki.archlinux.org/index.php/Solid_state_drive)</sup>

If your USB controller and USB SSD disk support Trim and ATA/NVMe secure erase, you could wipe them cautiously using hdparm using the same method as the System Disk above except you will not install Linux on it obviously. Keep in mind tho that this is not recommended (see Considerations above).

If it does not support Trim and/or ATA secure erase, you could (not securely) wipe the drive normally (without passes like an HDD) and re-encrypt it completely using your utility of choice (LUKS or Veracrypt for instance). The full disk decryption and re-encryption process will overwrite the entirety of the SSD disk and should ensure a secure wipe.

Alternatively, you could also (not securely) wipe the disk normally and then fill it completely with pseudorandom data which should also ensure secure deletion (this can be done with BleachBit <https://www.bleachbit.org/download/linux> <sup>[[Archive.org]](https://web.archive.org/web/https://www.bleachbit.org/download/linux)</sup> or from the command line using secure-delete using this tutorial <https://superuser.com/questions/19326/how-to-wipe-free-disk-space-in-linux> <sup>[[Archive.org]](https://web.archive.org/web/https://superuser.com/questions/19326/how-to-wipe-free-disk-space-in-linux)</sup>).

**Keep in mind all these options need to be applied on the entire physical drive and not on a specific partition/volume. If you do not, wear-leveling mechanisms might prevent this from working properly.**

#### Internal/System HDD { #wipe-linux-hdd }

- Option A: Check if your BIOS/UEFI has a built-in option and use them and if it does, use the correct option (Wipe + Passes in the case of an HDD).

- Option B: See [Using ShredOS to securely wipe an HDD drive](#shredos-hdd-wipe)

- Option C: Wipe your disk and re-install Linux with new full disk encryption to overwrite all sectors with new encrypted data. **This method will be terribly slow compared to Option A and B as it will slowly overwrite your whole HDD.**

#### External/Secondary HDD and Thumb Drives { #wipe-linux-ext-hdd }

- Option A: Follow one of these tutorials:

    - <https://linuxhint.com/completely_wipe_hard_drive_ubuntu/> <sup>[[Archive.org]](https://web.archive.org/web/https://linuxhint.com/completely_wipe_hard_drive_ubuntu/)</sup>

    - <https://linoxide.com/linux-command/commands-wipe-disk-linux/> <sup>[[Archive.org]](https://web.archive.org/web/https://linoxide.com/linux-command/commands-wipe-disk-linux/)</sup>

    - <https://wiki.archlinux.org/index.php/Securely_wipe_disk> <sup>[[Archive.org]](https://web.archive.org/web/https://wiki.archlinux.org/index.php/Securely_wipe_disk)</sup>

I recommend using dd or shred for this purpose.

- Option B: Install and use BleachBit <https://www.bleachbit.org/download/linux> <sup>[[Archive.org]](https://web.archive.org/web/https://www.bleachbit.org/download/linux)</sup> or follow this EFF tutorial <https://ssd.eff.org/en/module/how-delete-your-data-securely-linux> <sup>[[Archive.org]](https://web.archive.org/web/https://ssd.eff.org/en/module/how-delete-your-data-securely-linux)</sup>

- Option C: See [Using ShredOS to securely wipe an HDD drive](#shredos-hdd-wipe)

### Windows { #wipe-windows }

Unfortunately, you will not be able to wipe your Host OS using the Microsoft built-in tools within the settings. This is because your bootloader was modified with Veracrypt and will make the operation fail. In addition, this method would not be effective with an SSD drive.

#### System/Internal SSD { #wipe-windows-ssd }

- Option A: Check if your BIOS/UEFI has a built-in option to do so and if it does, use the correct option ("ATA/NVMe Secure Erase" or "ATA/NVMe Sanitize"). Do not use wipe with passes on an SSD drive.

- Option B: Check [Manufacturer tools for Wiping HDD and SSD drives.](#manufacturer-wipe-tools)

- Option C: See [Using System Rescue to securely wipe an SSD drive](#system-rescue-ssd-wipe)

- Option D: Wipe your disk and re-install Windows before performing new full disk encryption (using Veracrypt or Bitlocker) to overwrite all sectors with new encrypted data. **This method will be slower compared to Option A and B as it will overwrite your whole SSD.**

**Keep in mind all these options need to be applied on the entire physical drive and not on a specific partition/volume. If you do not, wear-leveling mechanisms might prevent this from working properly.**

#### External SSD { #wipe-windows-ext-ssd }

First please see [Considerations for using external SSD drives](#on-external-ssd)

Use the manufacturer-provided tools if possible. Those tools should provide support for safe secure erase or sanitize over USB and are available for most brands: See [Manufacturer tools for Wiping HDD and SSD drives.](#manufacturer-wipe-tools)

If you are not sure about the Trim support on your USB disk, (not securely) wipe it normally (simple quick format will do) and then encrypt the disk again using Veracrypt or Bitlocker. The full disk decryption and re-encryption process will overwrite the entirety of the SSD disk and should ensure a secure wipe.

Alternatively, you could also (not securely) wipe the disk normally and then fill it completely with pseudorandom data which should also ensure secure deletion (this can be done with BleachBit or PrivaZer free space erase options). See [Extra Tools Cleaning].

**Keep in mind all these options need to be applied on the entire physical drive and not on a specific partition/volume. If you do not, wear-leveling mechanisms might prevent this from working properly.**

#### Internal/System HDD { #wipe-windows-hdd }

- Option A: Check if your BIOS/UEFI has a built-in option to do so and if it does, use the correct option (Wipe + Passes).

- Option B: Check [Manufacturer tools for Wiping HDD and SSD drives](#manufacturer-wipe-tools)

- Option C: See [Using ShredOS to securely wipe an HDD drive](#shredos-hdd-wipe)

#### External/Secondary HDD and Thumb Drives { #wipe-windows-ext-hdd }

- Option A: Check [Manufacturer tools for Wiping HDD and SSD drives](#manufacturer-wipe-tools)

- Option B: Use external tools such as:

    - Eraser (open-source): <https://eraser.heidi.ie/download/> <sup>[[Archive.org]](https://web.archive.org/web/https://eraser.heidi.ie/download/)</sup>

    - KillDisk Free: <http://killdisk.com/killdisk-freeware.htm> <sup>[[Archive.org]](https://web.archive.org/web/http://killdisk.com/killdisk-freeware.htm)</sup>

- Option C: See [Using ShredOS to securely wipe an HDD drive](#shredos-hdd-wipe)

### macOS { #wipe-macos }

#### System/Internal SSD { #wipe-macos-ssd }

Unfortunately, the macOS Recovery disk utility will not be able to perform a secure erase of your SSD drive as stated in Apple documentation <https://support.apple.com/en-gb/guide/disk-utility/dskutl14079/mac> <sup>[[Archive.org]](https://web.archive.org/web/https://support.apple.com/en-gb/guide/disk-utility/dskutl14079/mac)</sup>.

In most cases, if your disk was encrypted with Filevault and you just perform a normal erase, it should be "enough" according to them. It is not according to me, so you have no option besides re-installing macOS again and re-encrypt it with Filevault again after re-installing. This should perform a "crypto erase" by overwriting your earlier install and encryption. This method will be quite slow, unfortunately.

If you want to do a faster secure erase (or have no time to perform a re-install and re-encryption), you can try using the method described in [Using System Rescue to securely wipe an SSD drive](#system-rescue-ssd-wipe) **(This will not work on M1 Macs)**. **Be careful tho as this will also erase your recovery partition which is needed to reinstall macOS.**

#### External SSD { #wipe-macos-ext-ssd }

First please see [Considerations for using external SSD drives](#on-external-ssd)

If your USB controller and USB SSD disk support Trim and ATA secure erase, and if Trim is enabled on the disk by macOS, you can just wipe the whole disk normally and data should not be recoverable on recent disks.

If you are not sure about Trim support or want more certainty, you can (not securely) wipe it using macOS disk utility before fully re-encrypting them again using these two tutorials from Apple:

- <https://support.apple.com/guide/disk-utility/erase-and-reformat-a-storage-device-dskutl14079/mac> <sup>[[Archive.org]](https://web.archive.org/web/https://support.apple.com/guide/disk-utility/erase-and-reformat-a-storage-device-dskutl14079/mac)</sup>

- <https://support.apple.com/guide/disk-utility/encrypt-protect-a-storage-device-password-dskutl35612/mac> <sup>[[Archive.org]](https://web.archive.org/web/https://support.apple.com/guide/disk-utility/encrypt-protect-a-storage-device-password-dskutl35612/mac)</sup> or using Veracrypt full disk encryption.

The full disk re-encryption process will overwrite the entirety of the SSD disk and should ensure a secure wipe.

**Keep in mind all these options need to be applied on the entire physical drive and not on a specific partition/volume. If you do not, wear-leveling mechanisms might prevent this from working properly.**

#### External HDD and Thumb Drives { #wipe-macos-ext-hdd }

Follow this tutorial: <https://support.apple.com/guide/disk-utility/erase-and-reformat-a-storage-device-dskutl14079/mac> <sup>[[Archive.org]](https://web.archive.org/web/https://support.apple.com/guide/disk-utility/erase-and-reformat-a-storage-device-dskutl14079/mac)</sup> and use the secure erase option from Disk Utility which should work fine on HDD and Thumb drives.

