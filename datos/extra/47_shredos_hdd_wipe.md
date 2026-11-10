# Secure Wiping an HDD with ShredOS { #shredos-hdd-wipe }

Several utilities are recommended (like the old unmaintained DBAN[^463] or System Rescue CD (<https://www.system-rescue.org/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.system-rescue.org/)</sup>)) for this but we will recommend the use of ShredOS.

Feel free to go with DBAN instead if you want (using this tutorial: <https://www.lifewire.com/how-to-erase-a-hard-drive-using-dban-2619148> <sup>[[Archive.org]](https://web.archive.org/web/https://www.lifewire.com/how-to-erase-a-hard-drive-using-dban-2619148)</sup>), the process is basically the same but will not work out of the box with UEFI laptops.

If you want to go with System-Rescue, just head to their website and follow the instructions.

## Windows { #secure-wipe-windows }

- Download ShredOS from <https://github.com/PartialVolume/shredos.x86_64> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/PartialVolume/shredos.x86_64)</sup>

- Unzip the ISO file

- Download Rufus from <https://rufus.ie/> <sup>[[Archive.org]](https://web.archive.org/web/https://rufus.ie/)</sup>

- Launch Rufus

- Select the ShredOS IMG file

- Write it to a USB key

- When done, reboot and boot the USB key (you might have to go into your BIOS settings to change the boot order for this).

- Follow the instructions on the screen

## Linux { #secure-wipe-linux }

- Follow instructions on <https://github.com/PartialVolume/shredos.2020.02> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/PartialVolume/shredos.x86_64)</sup>

- Reboot and boot the USB key

- Follow the instructions on the screen

