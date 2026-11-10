# Diskpart { #diskpart }

Diskpart is a Windows utility that can be used to perform various operations on your hard drive. In this case, You will use Diskpart to show the Disk ID but also change it if necessary.

This could be needed if you restore a backup on a new HDD/SSD that has an ID that differs from the one backed up and Windows could refuse to boot.

Diskpart can be run from any Windows environment using a command prompt. This includes recovery disks created by utilities such as Macrium Reflect, any Windows Installation media, EaseUS Todo Free rescue disks.

- **Displaying the disk ID**

    - Run Diskpart to enter the Diskpart utility

    - Issue the ```list disk``` command to list the disks

    - Issue the ```sel disk x``` (replace x with your system disk) to select your system disk

    - Issue the ```detail disk``` to show the details of this disk

    - Take note of the disk ID (this should be done BEFORE backing up your disks).

- **Changing the disk ID**

    - This step should only be done if, after restoring a full disk backup to a new hard drive, Windows refuses to boot

    - Issue the same commands as above on the target new disk

    - Issue, in addition, the command ```uniqueid disk id=02345678``` (where you replace the id by the one you noted before)

