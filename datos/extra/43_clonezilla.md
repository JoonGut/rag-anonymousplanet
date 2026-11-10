# Clonezilla { #clonezilla }

- Get Clonezilla by just following these instructions: <https://clonezilla.org/liveusb.php> <sup>[[Archive.org]](https://web.archive.org/web/https://clonezilla.org/liveusb.php)</sup> (I recommend the Alternative version AMD64 that should work with most recent laptops)

- Boot from Clonezilla

- Follow these steps to make a backup: <https://clonezilla.org/show-live-doc-content.php?topic=clonezilla-live/doc/01_Save_disk_image> <sup>[[Archive.org]](https://web.archive.org/web/https://clonezilla.org/show-live-doc-content.php?topic=clonezilla-live/doc/01_Save_disk_image)</sup>

    - **If you are backing up a disk with simple Encryption, encryption of the backup is not required since you are backing up an already encrypted disk, but you can still encrypt the backup anyway if you want additional security (and slower backup).**

    - **If you intend to back up a device with plausible deniability encryption, we strongly recommend against it as this backup image could be used to prove the existence of the hidden volume using forensics techniques as explained earlier. Do not make an image backup of the partition containing your hidden OS.**

- You are done, if you need to restore, follow these instructions: <https://clonezilla.org/show-live-doc-content.php?topic=clonezilla-live/doc/02_Restore_disk_image> <sup>[[Archive.org]](https://web.archive.org/web/https://clonezilla.org/show-live-doc-content.php?topic=clonezilla-live/doc/02_Restore_disk_image)</sup>

Each backup could take a while depending on the speed of your laptop and the speed of your external drive. In my experience, expect about 1 hour per backup depending on the drive size and the write speed of your backup media (my tests were done backing up 256GB SSDs on a USB 3.0 7200rpm HDD).

