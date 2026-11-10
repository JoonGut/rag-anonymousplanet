## Some additional measures against forensics { #anti-forensics }

Note that the same SSD issue discussed in the earlier section will arise here. You can never really be 100% sure your SSD data is deleted when you ask it to do so unless you wipe the whole drive using specific methods above.

We are not aware of any 100% reliable method to delete single files selectively and securely on SSD drives unless overwriting ALL the free space (which might reduce the lifespan of your SSD) after Deletion + Trim of these files. Without doing that, you will have to trust the SSD Trim operation **which in my opinion is enough**. **It is reasonable and again very unlikely that forensics will be able to restore your files after a Deletion with Trim.**

In addition, most of these measures here should not be needed since your whole drive should be encrypted and therefore your data should not be accessible for forensic analysis through SSD/HDD examination anyway. So, these are just "bonus measures" for weak/unskilled adversaries.

Consider also reading this documentation if you're going with Whonix <https://www.whonix.org/wiki/Anti-Forensics_Precautions> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Anti-Forensics_Precautions)</sup> as well as their general hardening tutorial for all platforms here <https://www.whonix.org/wiki/System_Hardening_Checklist> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/System_Hardening_Checklist)</sup>

### Metadata auditing { #metadata-auditing }

**Format conversion does not reliably strip metadata.** Converting a DOCX to PDF using Word embeds the Word document metadata into the PDF. Printing to PDF is somewhat cleaner but still retains producer information. The safe path is to use a purpose-built tool.

| File type | Tool | What to check and remove |
|-----------|------|--------------------------|
| JPEG / TIFF / HEIC | `exiftool -all= file.jpg` | EXIF, XMP, IPTC - all containers |
| PNG | `exiftool -all= file.png` | tEXt/iTXt chunks, XMP |
| DOCX / XLSX / PPTX | MAT2 or Word's Document Inspector | Author, revision history, tracked changes, template path, comments |
| PDF | `exiftool -all= file.pdf` or MAT2 | XMP packet, producer string, author, keywords |
| Any untrusted file | Dangerzone[^446] | Convert to safe PDF via isolated container, stripping all metadata |
| Video (MP4 / MOV) | `exiftool -all= file.mp4` | GPS, device info, creation time, encoder version |

**The safest workflow for sharing sensitive documents:** open the original in Dangerzone, which renders it in an isolated container and exports a clean PDF with metadata stripped. For images, run `exiftool -all= -overwrite_original filename` and verify with `exiftool filename` that the output is clean before sharing.

#### Pictures and videos { #exif-pictures-video }

EXIF[^222] is the metadata standard used by digital cameras and smartphones. A typical smartphone photo contains: GPS coordinates at the moment of capture (latitude, longitude, altitude, and sometimes bearing); camera make, model, and serial number; lens focal length; timestamp including timezone offset; and software version used to process the image.

The GPS data alone is frequently sufficient to identify a specific room in a specific building. Several high-profile source identification cases have turned on EXIF geolocation in images sent to journalists or posted online.

**Why stripping EXIF is not always enough:** EXIF is one metadata container. JPEG and TIFF files also support **XMP** (Extensible Metadata Platform)[^540], an Adobe-developed metadata format embedded as an XML packet inside the file. Tools that strip EXIF do not necessarily strip XMP. XMP can carry the same geolocation, authorship, and device information - sometimes more. ExifTool reads and writes both; many simpler "EXIF removers" do not touch XMP at all. Additionally, some camera manufacturers embed proprietary metadata in their own namespace inside XMP that persists even after standard EXIF removal.

A further subtlety: some platforms (notably older versions of Twitter and Facebook) strip EXIF server-side before serving images - but they store the original. Do not rely on platform stripping as a privacy control.

On Windows, macOS, and Linux we would recommend ExifTool (<https://exiftool.org/> <sup>[[Archive.org]](https://web.archive.org/web/https://exiftool.org/)</sup>) and/or ExifCleaner (<https://exifcleaner.com/> <sup>[[Archive.org]](https://web.archive.org/web/https://exifcleaner.com/)</sup>) that allows viewing and/or removing those properties.

**ExifTool is natively available on Tails and Whonix Workstation.**

#### PDF metadata { #pdf-metadata }

PDFs carry their own metadata layer. The **XMP packet** in a PDF can contain author, creator application (including version number), producer (the software that generated the PDF, e.g. "Microsoft Word 16.0.1" or a specific version of LibreOffice), creation and modification timestamps, and document title. The **producer string** is particularly useful to investigators because specific software versions are associated with specific time windows and installations.

Less obviously, **font embedding** in PDFs can fingerprint a document to a specific installation. Font subsets - the specific character outlines embedded in the PDF - vary slightly depending on which fonts are installed, which renderer is used, and which version of the software generated the file. Comparing embedded font data across multiple documents can link them to the same author even with no other identifying metadata present.[^541]

##### PDFParanoia (Linux/Windows/macOS/QubesOS) { #pdfparanoia }

Consider using <https://github.com/kanzure/pdfparanoia> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/kanzure/pdfparanoia)</sup> which will remove metadata and watermarks on any PDF.

##### ExifCleaner (Linux/Windows/macOS/QubesOS) { #exifcleaner-pdf }

Just install it from <https://exifcleaner.com/> <sup>[[Archive.org]](https://web.archive.org/web/https://exifcleaner.com/)</sup>, run and drag and drop the files into the GUI.

##### ExifTool (Linux/Windows/macOS/QubesOS) { #exiftool-pdf }

It is actually simple, just install exiftool and run:

- To display metadata: ```exiftool filename.pdf```

- To remove all metadata: ```exiftool -All= filename.pdf```

#### ExifCleaner { #exifcleaner }

Just install it from <https://exifcleaner.com/> <sup>[[Archive.org]](https://web.archive.org/web/https://exifcleaner.com/)</sup>, run and drag and drop the files into the GUI.

#### ExifTool { #exiftool }

It is actually simple, just install exiftool and run:

- To display metadata: ```exiftool filename.jpg```

- To remove all metadata: ```exiftool -All= filename.jpg```

**Remember that ExifTool is natively available on Tails and Whonix Workstation.**

#### Windows Native tool { #windows-exif-native }

Here is a tutorial to remove metadata from a Picture using OS provided tools: <https://www.purevpn.com/internet-privacy/how-to-remove-metadata-from-photos> <sup>[[Archive.org]](https://web.archive.org/web/https://www.purevpn.com/internet-privacy/how-to-remove-metadata-from-photos)</sup>

#### Cloaking/Obfuscating to prevent picture recognition { #image-cloaking }

Consider the use of Fawkes <https://sandlab.cs.uchicago.edu/fawkes/> <sup>[[Archive.org]](https://web.archive.org/web/https://sandlab.cs.uchicago.edu/fawkes/)</sup> (<https://github.com/Shawn-Shan/fawkes> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/Shawn-Shan/fawkes)</sup>) to cloak the images from picture recognition tech on various platforms.

Or if you want online versions, consider:

- <https://lowkey.umiacs.umd.edu/> <sup>[[Archive.org]](https://web.archive.org/web/https://lowkey.umiacs.umd.edu/)</sup>

- <https://adversarial.io/> <sup>[[Archive.org]](https://web.archive.org/web/https://adversarial.io/)</sup>

#### DOCX and Office Documents { #office-metadata }

Microsoft Office documents are ZIP archives containing XML files, and those XML files contain extensive metadata. This includes: author name and initials (from the Office profile at creation time); last-modified-by name; creation and modification timestamps; revision count; total editing time; company name from the Office installation; the path of the document template used at creation (which can include a username or network path); and, critically, **revision history and tracked changes** - deletions and edits that the author thought were removed may be stored in the document and recoverable by anyone who opens it in a sufficiently capable viewer.

Several cases of documents leaked to journalists have resulted in source identification because the author's name or network username was embedded in the XML. John Doe metadata has identified real people. The fix is to use **File → Inspect Document** in Word before sharing (it will show hidden data and offer to remove it) or to use MAT2[^446] to strip metadata entirely. Converting to PDF does not reliably remove this information - see below.

Alternatively, on Windows, macOS, Qubes OS, and Linux we would recommend ExifTool (<https://exiftool.org/> <sup>[[Archive.org]](https://web.archive.org/web/https://exiftool.org/)</sup>) and/or ExifCleaner (<https://exifcleaner.com/> <sup>[[Archive.org]](https://web.archive.org/web/https://exifcleaner.com/)</sup>) that allows viewing and/or removing those properties

##### ExifCleaner { #exifcleaner-office }

Just install it from <https://exifcleaner.com/> <sup>[[Archive.org]](https://web.archive.org/web/https://exifcleaner.com/)</sup>, run and drag and drop the files into the GUI.

##### ExifTool { #exiftool-office }

It is actually simple, just install exiftool and run:

- To display metadata: ```exiftool filename.docx```

- To remove all metadata: ```exiftool -All= filename.docx```

##### LibreOffice Documents { #libreoffice-metadata }

- select Files in the upper menu

    - Select Properties

    - Uncheck "Apply User Data"

    - Uncheck "Save Preview image with the Document"

    - Click "Reset Properties"

    - Make sure there is nothing on the Description and Custom Properties tabs

- Select Tools in the upper menu

    - Select Options

    - Select Security

    - Click "Security Options and Warning"

    - Check:

        + "When printing"

        + "When saving or sending"

        + "When creating PDF files"

        + "Remove personal information on saving"

In addition, on Windows, macOS, Qubes OS, and Linux we would recommend ExifTool (<https://exiftool.org/> <sup>[[Archive.org]](https://web.archive.org/web/https://exiftool.org/)</sup>) and/or ExifCleaner (<https://exifcleaner.com/> <sup>[[Archive.org]](https://web.archive.org/web/https://exifcleaner.com/)</sup>) that allows viewing and/or removing additional properties

##### ExifCleaner { #exifcleaner-libreoffice }

Just install it from <https://exifcleaner.com/> <sup>[[Archive.org]](https://web.archive.org/web/https://exifcleaner.com/)</sup>, run and drag and drop the files into the GUI.

##### ExifTool { #exiftool-libreoffice }

It is actually simple, jut install exiftool and run:

- To display metadata: ```exiftool filename.odt```

- To remove all metadata: ```exiftool -All= filename.odt```

#### All-in-one Tool { #allinone-metadata-tool }

Another option good tool to remove metadata from various documents is the open-source mat2 recommended by privacyguides.org[^445] (<https://0xacab.org/jvoisin/mat2> <sup>[[Archive.org]](https://web.archive.org/web/https://0xacab.org/jvoisin/mat2)</sup>) which you can use on Linux quite easily. I never managed to make it work properly within Windows due to various dependencies issues despite the provided instructions. It is however very straightforward to install and use on Linux.

So, we would suggest creating a small Debian VM within Virtualbox (behind your Whonix Gateway) which you can then use from your other VMs to analyze various files from a convenient web interface. For this see [Creating a mat2-web guest VM for removing metadata from files](#mat2-web-metadata)

![image47](../media/image47.png)

Mat2 is also pre-installed on the Whonix Workstation VM[^446] and available on Tails by default[^447].

### Tails { #metadata-tails }

Tails is great for this; you have nothing to worry about even if you use an SSD drive. Shut it down and it is all gone as soon as the memory decays.

### Whonix { #metadata-whonix }

Note that it's possible to run Whonix in Live mode leaving no traces when you shut down the VMs. For more information, see their [VM Live Mode](https://www.whonix.org/wiki/VM_Live_Mode) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/VM_Live_Mode)</sup> and [Warning](https://www.whonix.org/wiki/Warning#Whonix_-_Persistence_vs_Live_vs_Amnesic) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Warning)</sup>.

### macOS { #metadata-macos }

#### Guest OS { #macos-guest-os }

Revert to an earlier snapshot on Virtualbox (or any other VM software you are using) and perform a Trim command on your Mac using Disk Utility by executing a first-aid on the Host OS again as explained at the end of the next section.

#### Host OS { #macos-host-os-tracks }

Most of the info from this section can also be found at this nice guide <https://github.com/drduh/macOS-Security-and-Privacy-Guide> <sup>[[Archive.org]](https://web.archive.org/web/https://www.bejarano.io/hardening-macos/)</sup>

##### Quarantine Database (used by Gatekeeper and XProtect) { #macos-quarantine-db }

macOS (up to and including Big Sur) keeps a Quarantine SQL Database of all the files you ever downloaded from a Browser. This database is located at ```~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2```.

You can query it yourself by running the following command from terminal: ``` sqlite3 ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2 "select * from LSQuarantineEvent" ```

This is a goldmine for forensics, and you should disable this:

- Run the following command to clear the database completely: ```:>~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2```

- Run the following command to lock the file and prevent further download history from being written there: ```sudo chflags schg ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2```

Lastly, you can also disable Gatekeeper altogether by issuing the following command in the terminal[^448]:

- ```sudo spctl --master-disable```

Refer to this section of this guide for further information <https://github.com/drduh/macOS-Security-and-Privacy-Guide#gatekeeper-and-xprotect> <sup>[[Archive.org]](https://web.archive.org/web/https://www.bejarano.io/hardening-macos/)</sup>

In addition to this convenient database, each saved file will also carry detailed file system HFS+/APFS attributes showing for instance when it was downloaded, with what, and from where.

You can view these just by opening a terminal and typing ```mdls filename``` and ```xattr -l filename``` on any downloaded file from any browser.

To remove such attributes, you will have to do it manually from the terminal:

- Run ```xattr -d com.apple.metadata:kMDItemWhereFroms filename``` to remove the origin

    - You can also just use -dr to do it recursively on a whole folder/disk

- Run ```xattr -d com.apple.quarantine filename``` to remove the quarantine reference

    - You can also just use -dr to do it recursively on a whole folder/disk

- Verify by running ```xattr --l filename``` and there should be no output

(Note that Apple has removed the convenient xattr --c option that would just remove all attributes at once so you will have to do this for each attribute on each file)

**These attributes and entries will stick even if you clear your browser history, and this is obviously bad for privacy (right?), and we are not aware of any convenient tool that will deal with those at the moment.**

Fortunately, there are some mitigations for avoiding this issue in the first place as these attributes and entries are set by the browsers. So, we tested various browsers (On macOS Catalina, Big Sur, and Monterey), and here are the results as of the date of this guide:

| **Browser**                  | **Quarantine DB Entry**      | **Quarantine File Attribute** | **Origin File Attribute** |
|------------------------------|------------------------------|-------------------------------|---------------------------|
| **Safari (Normal)**          | **Yes**                      | **Yes**                       | **Yes**                   |
| **Safari (Private Window)**  | **No**                       | **No**                        | **No**                    |
| **Firefox (Normal)**         | **Yes**                      | **Yes**                       | **Yes**                   |
| **Firefox (Private Window)** | **No**                       | **No**                        | **No**                    |
| **Chrome (Normal)**          | **Yes**                      | **Yes**                       | **Yes**                   |
| **Chrome (Private Window)**  | **Partial (timestamp only)** | **No**                        | **No**                    |
| **Brave (Normal)**           | **Partial (timestamp only)** | **No**                        | **No**                    |
| **Brave (Private Window)**   | **Partial (timestamp only)** | **No**                        | **No**                    |
| **Brave (Tor Window)**       | **Partial (timestamp only)** | **No**                        | **No**                    |
| **Tor Browser**              | **No**                       | **No**                        | **No**                    |

As you can see for yourself the easiest mitigation is to just use Private Windows. These do not write those origin/quarantine attributes and do not store the entries in the QuarantineEventsV2 database.

Clearing the QuarantineEventsV2 is easy as explained above. Removing the attributes takes some work. **Brave is the only tested browser that will not store those attributes by default in normal operations.**

##### Various Artifacts { #macos-artifacts }

In addition, macOS keeps various logs of mounted devices, connected devices, known networks, analytics, documents revisions...

See this section of this guide for guidance on where to find and how to delete such artifacts: <https://github.com/drduh/macOS-Security-and-Privacy-Guide#metadata-and-artifacts> <sup>[[Archive.org]](https://web.archive.org/web/https://www.bejarano.io/hardening-macos/)</sup>

Many of those can be deleted using various commercial third-party tools but we would personally recommend using the free and well-known Onyx which you can find here: <https://www.titanium-software.fr/en/onyx.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.titanium-software.fr/en/onyx.html)</sup>. Unfortunately, it is closed-source, but it is notarized, signed, and has been trusted for many years.

##### Force a Trim operation after cleaning { #macos-trim }

- If your file system is APFS, you do not need to worry about Trim, it happens asynchronously as the OS writes data.

- If your file system is HFS+ (or any other than APFS), you could run First Aid on your System Drive from the Disk Utility which should perform a Trim operation in the details (<https://support.apple.com/en-us/HT210898> <sup>[[Archive.org]](https://web.archive.org/web/https://support.apple.com/en-us/HT210898)</sup>).

![image46](../media/image46.png)

### Linux (Qubes OS) { #tracks-qubes }

Please consider their guidelines <https://github.com/Qubes-Community/Contents/blob/master/docs/security/security-guidelines.md> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/Qubes-Community/Contents/blob/master/docs/security/security-guidelines.md)</sup>

If you are using Whonix on Qubes OS, please consider following some of their guides:

- Whonix System Hardening guide <https://www.whonix.org/wiki/System_Hardening_Checklist> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/System_Hardening_Checklist)</sup>

- Enabling App Armor on Qubes <https://www.whonix.org/wiki/Qubes/AppArmor> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Qubes/AppArmor)</sup>

- Also, consider the use of Linux Kernel Guard <https://www.whonix.org/wiki/Linux_Kernel_Runtime_Guard_LKRG> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Linux_Kernel_Runtime_Guard_LKRG)</sup>

### Linux (non-Qubes) { #tracks-linux }

#### Guest OS { #linux-guest-os-tracks }

Revert to an earlier snapshot of the Guest VM on Virtualbox (or any other VM software you are using) and perform a trim command on your laptop using ```fstrim --all```. This utility is part of the ```util-linux``` package on Debian/Ubuntu and should be installed by default on Fedora. Then switch to the next section.

#### Host OS { #linux-host-os-tracks }

Normally you should not have traces to clean within the Host OS since you are doing everything from a VM if you follow this guide.

Nevertheless, you might want to clean some logs. Consider having a look this convenient (but unfortunately unmaintained) tool: <https://github.com/sundowndev/covermyass> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/sundowndev/covermyass)</sup>

After cleaning up, make sure you have the fstrim utility installed (should be by default on Fedora) and part of the ```util-linux``` package on Debian/Ubuntu. Then just run ```fstrim --all``` on the Host OS. This should be sufficient on SSD drives as explained earlier.

Consider the use of Linux Kernel Guard as an added measure <https://www.whonix.org/wiki/Linux_Kernel_Runtime_Guard_LKRG> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Linux_Kernel_Runtime_Guard_LKRG)</sup>

### Windows { #tracks-windows }

#### Guest OS { #windows-guest-os-tracks }

Revert to an earlier snapshot on Virtualbox (or any other VM software you are using) and perform a trim command on your Windows using the Optimize as explained at the end of the next section

#### Host OS { #windows-host-os-tracks }

Now that you had a bunch of activities with your VMs or Host OS, you should take a moment to cover your tracks. **Most of these steps should not be undertaken on the Decoy OS in case of the use of plausible deniability. This is because you want to keep decoy/plausible traces of sensible but not secret activities available for your adversary. If everything is clean, then you might raise suspicion.**

##### Diagnostic Data and Telemetry { #windows-telemetry-tracks }

First, let us get rid of any diagnostic data that could still be there:

- After each use of your Windows devices, go into Settings, Privacy, Diagnostic & Feedback, and Click Delete.

Then let us re-randomize the MAC addresses of your Virtual Machines and the Bluetooth Address of your Host OS.

- After each shutdown of your Windows VM, change its MAC address for next time by going into Virtualbox > Select the VM > Settings > Network > Advanced > Refresh the MAC address.

- After each use of your Host OS Windows (your VM should not have Bluetooth at all), Go into the Device Manager, Select Bluetooth, Disable the Device and Re-Enable the device (this will force a randomization of the Bluetooth Address).

##### Event logs { #windows-event-logs }

Windows Event logs will keep many various pieces of information that could contain traces of your activities such as the devices that were mounted (including Veracrypt NTFS volumes for instance[^333]), your network connections, app crash information, and various errors. It is always best to clean those up regularly. Do not do this on the Decoy OS.

- Start, search for Event Viewer, and launch Event Viewer:

    - Go into Windows logs.

    - Select and clear all five logs using a right-click.

##### Veracrypt History { #windows-veracrypt-history }

By default, Veracrypt saves a history of recently mounted volumes and files. You should make sure Veracrypt never saves History. Again, do not do this on the Decoy OS if you are using plausible deniability for the OS. We need to keep the history of mounting the decoy Volume as part of the plausible deniability:

- Launch Veracrypt

- Make sure the "Never saves history" checkbox is checked (this should not be checked on the Decoy OS)

Now you should clean the history within any app that you used including Browser history, Cookies, Saved Passwords, Sessions, and Form History.

##### Browser History { #windows-browser-history }

- Brave (in case you did not enable cleaning on exit)

    - Go into Settings

    - Go into Shields

    - Go into Clear Browsing Data

    - Select Advanced

    - Select "All Time"

    - Check all the options

    - Clear Data

- Tor Browser

    - Just close the Browser and everything is cleaned

##### Wi-Fi History { #windows-wifi-history }

Now it is time to clear the history of the Wi-Fi you connect to. Unfortunately, Windows keeps storing a list of past Networks in the registry even if you "forgot" those in the Wi-Fi settings. As far as we know, no utilities clean those yet (BleachBit or PrivaZer for instance) so you will have to do it the manual way:

- Launch Regedit using this tutorial: <https://support.microsoft.com/en-us/windows/how-to-open-registry-editor-in-windows-10-deab38e6-91d6-e0aa-4b7c-8878d9e07b11> <sup>[[Archive.org]](https://web.archive.org/web/https://support.microsoft.com/en-us/windows/how-to-open-registry-editor-in-windows-10-deab38e6-91d6-e0aa-4b7c-8878d9e07b11)</sup>

- Within Regedit, enter this to the address bar: ```Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles```

- There you will see a bunch of folders to the right. Each of those folders is a "Key". Each of those keys will contain information about your current known Wi-Fi or past networks you used. You can explore them one by one and see the description on the right side.

- Delete all those keys.

##### Shellbags { #windows-shellbags }

As explained earlier, Shellbags are basically histories of accessed volumes/files on your computer. Remember that shellbags are exceptionally useful sources of information for forensics[^325] and you need to clean those. Especially if you mounted any "hidden volume" anywhere. Again, you should not do this on the Decoy OS:

- Download Shellbag Analyzer & Cleaner from <https://privazer.com/en/download-shellbag-analyzer-shellbag-cleaner.php> <sup>[[Archive.org]](https://web.archive.org/web/https://privazer.com/en/download-shellbag-analyzer-shellbag-cleaner.php)</sup>

    - Launch it

    - Analyze

    - Click Clean and select:

        + Deleted Folders

        + Folders on Network / External devices

        + Search Results

    - Select advanced

        + Check all except the two backup options (do not backup)

        + Select SSD cleanup (if you have an SSD)

        + Select one pass (All zero)

        + Clean

##### Extra Tools Cleaning { #windows-extra-cleaning }

After cleaning those earlier traces, you should also use third-party utilities that can be used to clean various traces. These include the traces of the files/folders you deleted.

Please refer to [Windows Cleaning Tools](#windows-cleaning-tools) before continuing.

###### PrivaZer { #privazer }

Here are the steps for PrivaZer:

- Download and install PrivaZer from <https://privazer.com/en/download.php> <sup>[[Archive.org]](https://web.archive.org/web/https://privazer.com/en/download.php)</sup>

    - Run PrivaZer after install

    - Do not use their Wizard

    - Select Advanced User

    - Select Scan in Depth and pick your Target

    - Select Everything you want to Scan and push Scan

    - Select What you want to be cleaned (skip the shell bag part since you used the other utility for that)

        + **You should just skip the free space cleaning part if using an SSD and instead just use the native Windows Optimize function (see below) which should be more than enough. We would only use this on an HDD drive.**

    - (If you did select Free Space cleaning) Select Clean Options and make sure your type of Storage is well detected (HDD vs SSD).

    - (If you did select Free Space cleaning) Within Clean Options **(Be careful with this option as it will erase all the free space on the selected partition, especially if you are running the decoy OS. Do not erase the free space or anything else on the second partition as you risk destroying your Hidden OS)**

        + If you have an SSD drive:

            * Secure Overwriting Tab: We would just pick Normal Deletion + Trim (Trim itself should be enough[^342]). Secure Deletion with Trim[^339] (1 pass) might be redundant and overkill here if you intend to overwrite the free space anyway.

            * Free Space Tab: Personally, and again "just to be sure", we would select Normal Cleanup which will fill the entire free space with Data. We do not really trust Smart Cleanup as it does not actually fill all the free space of the SSD with Data. But again, this is probably not needed and overkill in most cases.

        + If you have an HDD drive:

            * Secure Overwriting Tab: We would just pick Secure Deletion (1 pass).

            * Free Space: We would just pick Smart Cleanup as there is no reason to overwrite sectors without data on an HDD drive.

    - Select Clean and Pick your flavor:

        + Turbo Cleanup will only do normal deletion (on HDD/SSD) and will not clean free space. It is not secure on an HDD nor an SSD.

        + Quick Cleanup will do secure deletion (on HDD) and normal deletion + trim (on SSD) but will not clean free space. This is secure enough for SSD but not for HDD.

        + Normal Cleanup will do secure deletion (on HDD) and normal deletion + trim (on SSD) and will then clean the whole free space (Smart Cleanup on HDD and Full Cleanup on SSD) and should be secure. This option is the best for HDD but completely overkill for SSD.

    - Click Clean and wait for cleaning to finish. Could take a while and will fill your whole free space with data.

###### BleachBit { #bleachbit }

Here are the steps for BleachBit:

- Get and install the latest version from BleachBit here <https://www.bleachbit.org/download> <sup>[[Archive.org]](https://web.archive.org/web/https://www.bleachbit.org/download)</sup>

- Run BleachBit

- Clean at least everything within those sections:

    - Deep Scan

    - Windows Defender

    - Windows Explorer (including Shellbags)

    - System

    - Select any other traces you want to remove from their list

        + Again, as with the earlier utility, we would not clean the free space on an SSD drive because we think the Windows native "optimize" utility is enough (see below) and that filling up the free space on a trim enabled SSD is just completely overkill and unnecessary.

    - Click Clean and wait. This will take a while and will fill your whole free space with data on both HDD and SSD drives.

##### Force a Trim with Windows Optimize (for SSD drives) { #windows-trim }

With this Native Windows 10/11 utility, you can just trigger a Trim on your SSD which should be more than enough to securely clean all deleted files that somehow would have escaped Trim when deleting them.

Just open Windows Explorer, Right Click on your System Drive and click Properties. Select Tools. Click Optimize and Defragment. You are done as this will not defragment but only optimize. Meaning it will initiate a Trim operation (<https://en.wikipedia.org/wiki/Trim_(computing)> <sup>[[Wikiless]](https://wikiless.tiekoetter.com/wiki/Trim_(computing))</sup> <sup>[[Archive.org]](https://web.archive.org/web/20220804150134/https://en.wikipedia.org/wiki/Trim_(computing))).

![image45](../media/image45.png)

