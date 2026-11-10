# External SSD Drive Considerations { #on-external-ssd }

**I do not recommend using external SSDs due to the uncertainty about their support for Trim, ATA Secure Erase, and Sanitize options through USB controllers. Instead, we recommend using external HDD disks which can be cleaned/wiped safely and securely without hassle (albeit much slower than SSD drives).**

Please do not buy or use gimmicky self-encrypting devices such as these: <https://syscall.eu/blog/2018/03/12/aigo_part1/> <sup>[[Archive.org]](https://web.archive.org/web/https://syscall.eu/blog/2018/03/12/aigo_part1/)</sup>

Some might be very efficient[^464] but many are gimmicky gadgets.

If you want to use an external SSD drive for sensitive storage:

- Please consider the support for:

    - Trim operations and ATA/NVMe secure erase operations from your Laptop USB controller.

    - Trim operations and ATA/NVMe secure erase operations from your USB SSD disk itself.

- Always use full disk encryption on those disks

- **Use the manufacturer-provided tools to securely erase them if possible (see [Considerations for using external SSD drives](#on-external-ssd)).**

- Consider manually wiping data on them after use by doing a full decryption/encryption or filling them completely with random data.

So how to check if your external USB SSD supports Trim and other ATA/NVMe operations from your Host OS?

## Windows { #external-windows }

### Trim Support { #external-win-trim }

It is possible Windows will detect your external SSD properly and enable Trim by default. Check if Optimize works using the Windows Native disk utility as explained in the internal SSD section of Windows.

### ATA/NVMe Operations (Secure Erase/Sanitize) { #external-win-ata }

**Use the manufacturer-provided tools to check and perform these operations** ... It is pretty much the only way to be sure it is not only supported but actually works. Some utilities can tell you whether it is supported or not like CrystalDiskInfo <sup>[[Archive.org]](https://web.archive.org/web/https://element.io/)</sup> but will not actually check if it is working. See [Manufacturer tools for Wiping HDD and SSD drives](#manufacturer-wipe-tools).

If it does not work. Just decrypt and re-encrypt the whole drive or fill up the free space as instructed in the guide. There is no other way AFAIK. Besides booting up a System Rescue Linux CD and see the next section.

## Linux { #external-linux }

### Trim Support { #external-linux-trim }

Follow this good tutorial: <https://www.glump.net/howto/desktop/enable-trim-on-an-external-ssd-on-linux> <sup>[[Archive.org]](https://web.archive.org/web/https://www.glump.net/howto/desktop/enable-trim-on-an-external-ssd-on-linux)</sup>

### ATA/NVMe Operations (Secure Erase/Sanitize) { #external-linux-ata }

**It is not "recommended". Please read the disclaimers here <https://ata.wiki.kernel.org/index.php/ATA_Secure_Erase>** <sup>[[Archive.org]](https://web.archive.org/web/https://ata.wiki.kernel.org/index.php/ATA_Secure_Erase)</sup> **and here <https://wiki.archlinux.org/index.php/Solid_state_drive/Memory_cell_clearing>** <sup>[[Archive.org]](https://web.archive.org/web/https://wiki.archlinux.org/index.php/Solid_state_drive/Memory_cell_clearing)</sup>

But this seems to be based on anecdotal experiences. So, if you are sure your external SSD supports Trim (see vendor documentation). You could just **try at your own risk** to use nvme-cli or hdparm to issue secure erases.

See also this tutorial <https://code.mendhak.com/securely-wipe-ssd/> <sup>[[Archive.org]](https://web.archive.org/web/https://code.mendhak.com/securely-wipe-ssd/)</sup>

**Your mileage may vary. Use at your own risk.**

## macOS { #external-macos }

### Trim Support { #external-macos-trim }

According to Apple Documentation[^455], Trim is supported on APFS (asynchronously) and HFS+ (through period trim or first-aid).

So, if it is supported (and enabled on your external SSD), you should be able to issue a Trim on a non-APFS drive using Disk Utility and First Aid which should issue a Trim.

If your disk supports it but it is not enabled in macOS. You could try issuing a "sudo trimforce enable" command from the Terminal and see if it enables Trim on your external SSD. And then again check the first aid command if it is not APFS (see this Tutorial for info <https://www.lifewire.com/enable-trim-for-ssd-in-os-x-yosemite-2260789> <sup>[[Archive.org]](https://web.archive.org/web/https://www.lifewire.com/enable-trim-for-ssd-in-os-x-yosemite-2260789)</sup>)

If it does not work, we are not aware of any reliable method to enable TRIM besides the commercial utility Trim Enabler here <https://cindori.org/trimenabler/> <sup>[[Archive.org]](https://web.archive.org/web/https://cindori.org/trimenabler/)</sup> which claims support for external drives.

### ATA/NVMe Operations (Secure Erase/Sanitize) { #external-macos-ata }

We are not aware of any method of doing so reliably and safely on macOS. So, you will have to try one of these options:

- Use a bootable System Rescue USB Linux to do it

- Just decrypt and re-encrypt the drive using Disk Utility or Veracrypt

- Fill up the free space of the disk using the Linux method (dd)

