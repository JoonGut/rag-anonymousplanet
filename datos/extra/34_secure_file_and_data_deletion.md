## How to securely delete specific files/folders/data on your HDD/SSD and Thumb drives { #secure-delete-files }

The same principles from the earlier chapters apply to this one. The same issues arise too.

With an HDD drive, you can securely delete files by just deleting them and then apply one or more "passes" to overwrite the data in question. This can be done with many utilities on all OSes.

With an SSD drive, however, again everything becomes a bit complicated because you are never sure anything is really deleted due to wear leveling, reliance on the Trim operation, and garbage collection of the drive. An adversary that has the decryption key of your SSD (whether it is LUKS, Filevault 2, Veracrypt, or Bitlocker) could unlock your drive and then attempt a recovery using classic recovery utilities[^442] and could succeed if the data were not trimmed properly. But this is again highly unlikely.

Since the Trim operation is not continuous on most recent hard drives but scheduled, simply forcing a Trim operation should be enough. But again, the only way to be 100% sure a file is securely deleted from your unlocked encrypted SSD is to again overwrite all the free space after deletion of the files in question or to decrypt/re-encrypt the drive. But this is overkill and not necessary. A simple disk-wide Trim should be sufficient.

**Remember tho that no matter the deletion method you use for any file on any medium (HDD drive, SSD, USB Thumb drive). It will probably leave other traces (logs, indexing, shellbags ...) within your system and those traces will also need to be cleaned. Also, remember that your drives should be fully encrypted and so this is most likely an extra measure. More on that later in the [Some additional measures against forensics](#anti-forensics) section.**

### Windows { #secure-delete-windows }

**Remember you cannot use Trim at all if you are using Plausible Deniability on an SSD drive against all recommendations.**

#### System/Internal SSD drive { #secure-delete-windows-ssd }

At this stage, and just delete the file permanently (empty the recycle bin) and trim/garbage collection will do the rest. This should be sufficient.

If you do not want to wait for the periodic Trim (set to Weekly by default in Windows 10/11), you could also force a disk-wide Trim using the Windows native Optimize tool (see [Windows Cleaning Tools](#windows-cleaning-tools)).

If data were deleted by some utility (for instance by Virtualbox when reverting a snapshot), you could also issue a disk-wide Trim to clean anything remaining using the same Optimize tool.

Just open Windows Explorer, Right Click on your System Drive and click Properties. Select Tools. Click Optimize and then Optimize again to force a Trim. You are done. That is probably enough in my opinion.

![image45](../media/image45.png)

If you want more security and do not trust the Trim operation, then you will have no option but to either:

- Decrypt and re-encrypt (using Veracrypt or Bitlocker) the whole drive to overwrite all free space after data deletion. This will ensure overwriting of all the free space.

- Trim and then fill up the entire free space of the disk using a utility such as BleachBit or PrivaZer.

**Keep in mind all these options need to be applied on the entire physical drive and not on a specific partition/volume. If you do not, wear-leveling mechanisms might prevent this from working properly.**

#### Internal/External HDD or a USB Thumb Drive { #secure-delete-windows-hdd }

Please refer to [Windows Cleaning Tools](#windows-cleaning-tools) and pick a utility before going ahead.

The process is quite simple depending on the tool you picked from the Appendix:

- Right-click a file/folder:

    - PrivaZer: Delete without a trace

    - BleachBit: Shred with BleachBit (or see this tutorial from the EFF <https://ssd.eff.org/en/module/how-delete-your-data-securely-windows> <sup>[[Archive.org]](https://web.archive.org/web/https://ssd.eff.org/en/module/how-delete-your-data-securely-windows)</sup>)

In the case of USB thumb drives, consider wiping free space using one of the above utilities after file deletion or wiping them completely using Eraser / KillDisk as instructed previously.

#### External SSD drive { #secure-delete-windows-ext-ssd }

First please see [Considerations for using external SSD drives](#on-external-ssd)

If Trim is supported and enabled by Windows for your external SSD drive. There should be no issue in securely deleting data normally just with normal delete commands. Additionally, you could also force a Trim using the Windows native Optimize tool (see [Windows Cleaning Tools](#windows-cleaning-tools)):

Just open Windows Explorer, Right Click on your System Drive and click Properties. Select Tools. Click Optimize and then Optimize again to force a Trim. You are done. That is probably enough in my opinion.

If Trim is not supported or you are not sure, you might have to ensure secure data deletion by:

- Filling up all the free space after any deletion (using BleachBit or PrivaZer for instance).

- Decrypt and Re-encrypt the disk with a different key after each deletion (using Veracrypt or Bitlocker).

**Keep in mind all these options need to be applied on the entire physical drive and not on a specific partition/volume. If you do not, wear-leveling mechanisms might prevent this from working properly.**

### Linux (non-Qubes OS) { #secure-delete-linux }

#### System/Internal SSD drive { #secure-delete-linux-ssd }

Just permanently delete the file (and empty recycle bin) and it should be unrecoverable due to Trim operations and garbage collection.

If you do not want to wait for the periodic Trim (set to Weekly by default in Ubuntu), you could also force a disk-wide Trim by running ```fstrim --all``` from a terminal. This will issue an immediate trim and should ensure sufficient security. This utility is part of the ```util-linux``` package on Debian/Ubuntu and should be installed by default on Fedora.

If you want more security and do not trust the Trim operation, then you will have no option but to either:

- Decrypt and re-encrypt (using LUKS for instance following this tutorial <https://wiki.archlinux.org/index.php/dm-crypt/Device_encryption#Re-encrypting_devices> <sup>[[Archive.org]](https://web.archive.org/web/https://wiki.archlinux.org/index.php/dm-crypt/Device_encryption)</sup>) the whole drive to overwrite all free space after data deletion. This will ensure overwriting of all the free space.

- Trim using ```fstrim --all``` and then fill up the entire free space of the disk using a utility such as:

    - BleachBit <https://www.bleachbit.org/download/linux> <sup>[[Archive.org]](https://web.archive.org/web/https://www.bleachbit.org/download/linux)</sup>

    - Install secure-delete package and use sfill on the root of the drive:

        + ```sudo sfill -l -l /``` for instance should do the trick (this will take a substantial amount of time)

    - Use the old school dd method (taken from this answer <https://superuser.com/questions/19326/how-to-wipe-free-disk-space-in-linux> <sup>[[Archive.org]](https://web.archive.org/web/https://superuser.com/questions/19326/how-to-wipe-free-disk-space-in-linux)</sup>) run these commands on the drive you want to fill:

        + ```dd if=/dev/zero of=zero.small.file bs=1024 count=102400```

        + ```dd if=/dev/zero of=zero.file bs=1024```

        + ```sync ; sleep 60 ; sync```

        + ```rm zero.small.file```

        + ```rm zero.file```

**Keep in mind all these options need to be applied on the entire physical drive and not on a specific partition/volume. If you do not, wear-leveling mechanisms might prevent this from working properly.**

#### Internal/External HDD drive or a Thumb Drive { #secure-delete-linux-hdd }

- You can do this the graphical way with BleachBit following this tutorial from the EFF: <https://ssd.eff.org/en/module/how-delete-your-data-securely-linux> <sup>[[Archive.org]](https://web.archive.org/web/https://ssd.eff.org/en/module/how-delete-your-data-securely-linux)</sup>

- Or you can do this from the command line following this tutorial: <https://linuxhint.com/completely_wipe_hard_drive_ubuntu/> <sup>[[Archive.org]](https://web.archive.org/web/https://linuxhint.com/completely_wipe_hard_drive_ubuntu/)</sup> (For this purpose we recommend wipe and shred).

#### External SSD drive { #secure-delete-linux-ext-ssd }

First please see [Considerations for using external SSD drives](#on-external-ssd)

If Trim is supported and enabled by your Linux Distribution for your external SSD drive. There should be no issue in securely deleting data normally and just issue an ```fstrim --all``` from the terminal to trim the drive. This utility is part of the "util-linux" package on Debian/Ubuntu and should be installed by default on Fedora.

If Trim is not supported or you want to be sure, you might have to ensure secure data deletion by filling up the entire free space of the disk using a utility such as:

- Decrypt and re-encrypt (using LUKS using this tutorial <https://wiki.archlinux.org/index.php/dm-crypt/Device_encryption#Re-encrypting_devices> <sup>[[Archive.org]](https://web.archive.org/web/https://wiki.archlinux.org/index.php/dm-crypt/Device_encryption)</sup> or Veracrypt from the graphical interface for instance) the whole drive to overwrite all free space after data deletion. This will ensure overwriting of all the free space.

- Fill the free space using one of those methods:

    - BleachBit <https://www.bleachbit.org/download/linux> <sup>[[Archive.org]](https://web.archive.org/web/https://www.bleachbit.org/download/linux)</sup>

    - Install secure-delete package and use sfill on the root of the drive:

        + ```sudo sfill -l -l /``` for instance should do the trick (this will take a substantial amount of time)

    - Use the old school dd method (taken from this answer <https://superuser.com/questions/19326/how-to-wipe-free-disk-space-in-linux> <sup>[[Archive.org]](https://web.archive.org/web/https://superuser.com/questions/19326/how-to-wipe-free-disk-space-in-linux)</sup>) run these commands:

        + ```dd if=/dev/zero of=zero.small.file bs=1024 count=102400```

        + ```dd if=/dev/zero of=zero.file bs=1024```

        + ```sync ; sleep 60 ; sync```

        + ```rm zero.small.file```

        + ```rm zero.file```

**Keep in mind all these options need to be applied on the entire physical drive and not on a specific partition/volume. If you do not, wear-leveling mechanisms might prevent this from working properly.**

### Linux (Qubes OS) { #secure-delete-qubes }

#### System/Internal SSD drive { #secure-delete-qubes-ssd }

As with other Linux distros, normal deletion and trim should be sufficient on most SSD drives. So just permanently delete the file (and empty any recycle bin) and it should be unrecoverable due to periodic Trim operations and garbage collection.

Please follow this documentation to Trim within Qubes OS: <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/disk-trim.md> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/disk-trim.md)</sup>

As with other Linux Systems, if you want more security and do not trust the Trim operation then you will have no option but to either:

- Decrypt and re-encrypt the whole drive to overwrite all free space after data deletion. This will ensure overwriting of all the free space. We didn't find a reliable tutorial on how to do this safely on Qubes OS but it is possible this tutorial could work: <https://wiki.archlinux.org/index.php/dm-crypt/Device_encryption#Re-encrypting_devices> <sup>[[Archive.org]](https://web.archive.org/web/https://wiki.archlinux.org/index.php/dm-crypt/Device_encryption)</sup> (at your own risk, this has not been tested yet).

- Refer to this Documentation (<https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/disk-trim.md> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/disk-trim.md)</sup>) and then trim using "fstrim --all" and then fill up the entire free space of the disk using a utility such as:

    - BleachBit <https://www.bleachbit.org/download/linux> <sup>[[Archive.org]](https://web.archive.org/web/https://www.bleachbit.org/download/linux)</sup>

    - Install secure-delete package and use sfill on the root of the drive:

        + ```sudo sfill -l -l /``` for instance should do the trick (this will take a substantial amount of time)

    - Use the old school dd method (taken from this answer <https://superuser.com/questions/19326/how-to-wipe-free-disk-space-in-linux> <sup>[[Archive.org]](https://web.archive.org/web/https://superuser.com/questions/19326/how-to-wipe-free-disk-space-in-linux)</sup>) run these commands on the drive you want to fill:

        + ```dd if=/dev/zero of=zero.small.file bs=1024 count=102400```

        + ```dd if=/dev/zero of=zero.file bs=1024```

        + ```sync ; sleep 60 ; sync```

        + ```rm zero.small.file```

        + ```rm zero.file```

**Keep in mind all these options need to be applied on the entire physical drive and not on a specific partition/volume. If you do not, wear-leveling mechanisms might prevent this from working properly.**

#### Internal/External HDD drive or a Thumb Drive { #secure-delete-qubes-hdd }

Use the same method as Linux from a Qube connected to that specific USB device

- You can do this the graphical way with BleachBit following this tutorial from the EFF: <https://ssd.eff.org/en/module/how-delete-your-data-securely-linux> <sup>[[Archive.org]](https://web.archive.org/web/https://ssd.eff.org/en/module/how-delete-your-data-securely-linux)</sup>

- Or you can do this from the command line following this tutorial: <https://linuxhint.com/completely_wipe_hard_drive_ubuntu/> <sup>[[Archive.org]](https://web.archive.org/web/https://linuxhint.com/completely_wipe_hard_drive_ubuntu/)</sup> (For this purpose we recommend wipe and shred).

#### External SSD drive { #secure-delete-qubes-ext-ssd }

First please see [Considerations for using external SSD drives](#on-external-ssd)

If Trim is supported and enabled by your Linux Distribution for your external SSD drive. There should be no issue in securely deleting data normally and just issue a "fstrim --all" from the terminal to trim the drive. Refer to this Documentation (<https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/disk-trim.md> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/disk-trim.md)</sup>) to enable trim on a drive.

If Trim is not supported or you want to be sure, you might have to ensure secure data deletion by filling up the entire free space of the disk using a utility from a Qube connected to the USB device in question:

- Decrypt and re-encrypt (using LUKS using this tutorial <https://wiki.archlinux.org/index.php/dm-crypt/Device_encryption#Re-encrypting_devices> <sup>[[Archive.org]](https://web.archive.org/web/https://wiki.archlinux.org/index.php/dm-crypt/Device_encryption)</sup> or Veracrypt from the graphical interface for instance) the whole drive to overwrite all free space after data deletion. This will ensure overwriting of all the free space.

- Fill the free space using one of those methods:

    - BleachBit <https://www.bleachbit.org/download/linux> <sup>[[Archive.org]](https://web.archive.org/web/https://www.bleachbit.org/download/linux)</sup>

    - Install secure-delete package and use sfill on the root of the drive:

        + ```sudo sfill -l -l /``` for instance should do the trick (this will take a substantial amount of time)

    - Use the old school dd method (taken from this answer <https://superuser.com/questions/19326/how-to-wipe-free-disk-space-in-linux> <sup>[[Archive.org]](https://web.archive.org/web/https://superuser.com/questions/19326/how-to-wipe-free-disk-space-in-linux)</sup>) run these commands:

        + ```dd if=/dev/zero of=zero.small.file bs=1024 count=102400```

        + ```dd if=/dev/zero of=zero.file bs=1024```

Repeat these steps on any other partition if there are separate partitions on the same SSD drive before deleting the files.

- ```sync ; sleep 60 ; sync```

- ```rm zero.small.file```

- ```rm zero.file```

Repeat these steps on any other partition if there are separate partitions on the same SSD drive.

**Keep in mind all these options need to be applied on the entire physical drive and not on a specific partition/volume. If you do not, wear-leveling mechanisms might prevent this from working properly.**

### macOS { #secure-delete-macos }

#### System/Internal SSD drive { #secure-delete-macos-ssd }

Just permanently delete the file (and empty recycle bin) and it should be unrecoverable due to trim operations and garbage collection.

- If your file system is APFS, you do not need to worry about Trim, it happens asynchronously as the OS writes data[^443] according to their documentation.

"Does Apple File System support TRIM operations?

Yes. TRIM operations are issued asynchronously from when files are deleted or free space is reclaimed, which ensures that these operations are performed only after metadata changes are persisted to stable storage".

- If your file system is HFS+, you could run First Aid on your System Drive from the Disk Utility which should perform a Trim operation in the details (<https://support.apple.com/en-us/HT210898> <sup>[[Archive.org]](https://web.archive.org/web/https://support.apple.com/en-us/HT210898)</sup>)

![image46](../media/image46.png)

#### System/Internal, External HDD drive or a Thumb Drive { #secure-delete-macos-hdd }

Unfortunately, Apple has removed the secure erase options from the trash bin even for HDD drives[^444]. So, you are left with using other tools:

- Permanent Eraser <http://www.edenwaith.com/products/permanent%20eraser/> <sup>[[Archive.org]](https://web.archive.org/web/http://www.edenwaith.com/products/permanent%20eraser/)</sup>

- From the terminal, you can use the "rm --P filename" command which should erase the file and overwrite it as explained in this EFF tutorial <https://ssd.eff.org/en/module/how-delete-your-data-securely-macos> <sup>[[Archive.org]](https://web.archive.org/web/https://ssd.eff.org/en/module/how-delete-your-data-securely-macos)</sup>.

In the case of USB thumb drives, consider wiping them completely using Disk Utility as instructed previously.

#### External SSD drive { #secure-delete-macos-ext-ssd }

First please see [Considerations for using external SSD drives](#on-external-ssd)

If Trim is supported and enabled by macOS for your external SSD drive. There should be no issue in securely deleting data.

If Trim is not supported, you might have to ensure secure data deletion by:

- Filling up all the free space after any deletion using the Linux Method above (dd).

- Decrypt and Re-encrypt the disk with a different key after each deletion (using Disk Utility or Veracrypt).

