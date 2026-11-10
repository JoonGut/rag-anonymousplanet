# Windows Cleaning Tools { #windows-cleaning-tools }

In this guide we will recommend two-third native tools and two third-party tools:

- Native Tools:

    - Windows 10/11 Disk Cleanup Utility: <https://support.microsoft.com/en-us/windows/disk-cleanup-in-windows-10-8a96ff42-5751-39ad-23d6-434b4d5b9a68> <sup>[[Archive.org]](https://web.archive.org/web/https://support.microsoft.com/en-us/windows/disk-cleanup-in-windows-10-8a96ff42-5751-39ad-23d6-434b4d5b9a68)</sup>

> This tool will clean up a bunch of things natively. It is not enough, and we instead recommend using the third-party tools below to clean more stuff. PrivaZer for instance will use the disk cleanup utility directly itself and BleachBit will use its own mechanisms.

- Windows 10/11 Optimize Utility (Defrag on HDD Drives): <https://support.microsoft.com/en-us/windows/defragment-your-windows-10-pc-048aefac-7f1f-4632-d48a-9700c4ec702a> <sup>[[Archive.org]](https://web.archive.org/web/https://support.microsoft.com/en-us/windows/defragment-your-windows-10-pc-048aefac-7f1f-4632-d48a-9700c4ec702a)</sup> (yes the tutorial is for Windows 10 but should work on 11 too)

> For security, this tool is particularly useful on SSD drives at this "Optimize" function will in fact force a Disk wide Trim operation to occur. This will most likely be more than enough to make sure any deleted data that was not trimmed before for any reason will be this time. Deleted data with Trim is very unlikely to be recovered as explained before in this guide.

- Third-Party Tools:

    - The open-source utility BleachBit <https://www.bleachbit.org/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.bleachbit.org/)</sup>

    - The closed-source utility PrivaZer <https://privazer.com/> <sup>[[Archive.org]](https://web.archive.org/web/https://privazer.com/)</sup>

I prefer PrivaZer because it has more customization and smarter features, but we would understand if you do not trust them and prefer open-source software in which case we would recommend BleachBit which offers a bit less customization but similar functionalities.

Both these tools can be used for cleaning many things such as:

- The Windows USN journal which stores plenty of information.

- The Windows System Resource Usage Monitor (SRUM)[^461].

- Various histories of various programs (such as the recent lists).

- Various logs

- The free (unallocated) space of your hard drive[^462].

- Secure deletion of files

- Secure wiping of USB drives

Both these utilities can delete files and can overwrite the free space after deletion to improve secure deletion even on SSD drives. Remember this can reduce the lifespan of your SSD drives a bit.

