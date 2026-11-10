# Secure Wiping an SSD with System Rescue { #system-rescue-ssd-wipe }

These instructions are valid for all Operating Systems:

- System Rescue:

    - Create a System Rescue USB disk following these instructions <https://www.system-rescue.org/Installing-SystemRescue-on-a-USB-memory-stick/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.system-rescue.org/Installing-SystemRescue-on-a-USB-memory-stick/)</sup> (download the ISO and write to a USB stick with Rufus).

    - Disable Secure Boot in your BIOS/UEFI settings and change the boot order to the USB disk (System Rescue bootloader is not signed and will not boot with secure boot enabled).

    - Follow the instructions to change the keyboard layout by typing "stkmap".

    - (optional) Run startx afterward to start a graphical environment.

- SATA SSD:

    - (If you ran startx) Open a terminal

    - ATA Secure Erase:

        + Follow one of these tutorials

            * <https://wiki.archlinux.org/index.php/Solid_state_drive/Memory_cell_clearing> <sup>[[Archive.org]](https://web.archive.org/web/https://wiki.archlinux.org/index.php/Solid_state_drive/Memory_cell_clearing)</sup>

            * <https://ata.wiki.kernel.org/index.php/ATA_Secure_Erase> <sup>[[Archive.org]](https://web.archive.org/web/https://ata.wiki.kernel.org/index.php/ATA_Secure_Erase)</sup>

            * <https://tinyapps.org/docs/wipe_drives_hdparm.html> <sup>[[Archive.org]](https://web.archive.org/web/https://tinyapps.org/docs/wipe_drives_hdparm.html)</sup>

    - ATA Sanitize:

        + Follow this tutorial <https://tinyapps.org/docs/ata_sanitize_hdparm.html> <sup>[[Archive.org]](https://web.archive.org/web/https://tinyapps.org/docs/ata_sanitize_hdparm.html)</sup>

- NVMe SSD:

    - (If you ran startx) Open a terminal

    - Follow one of these tutorials:

        + <https://wiki.archlinux.org/index.php/Solid_state_drive/Memory_cell_clearing> <sup>[[Archive.org]](https://web.archive.org/web/https://wiki.archlinux.org/index.php/Solid_state_drive/Memory_cell_clearing)</sup>

        + <https://tinyapps.org/docs/nvme-secure-erase.html> <sup>[[Archive.org]](https://web.archive.org/web/https://tinyapps.org/docs/nvme-secure-erase.html)</sup>

        + <https://tinyapps.org/docs/nvme-sanitize.html> <sup>[[Archive.org]](https://web.archive.org/web/https://tinyapps.org/docs/nvme-sanitize.html)</sup>

