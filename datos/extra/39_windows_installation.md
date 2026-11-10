# Windows Installation { #windows-installation }

This is the Windows 10/11 installation process that should be valid for any Windows 10/11  install within this guide.

## Windows 10 (See below for Windows 11) { #using-win10 }

## Installation { #installing-win10 }

DO NOT CONNECT WINDOWS TO ANY NETWORK DURING THE INSTALLATION PROCESS (This will allow us to create a Local Account and not use a Microsoft account and it will also prevent any telemetry from being sent out during the install process).

- (Only for VirtualBox VM Install) Go into the VirtualBox Machine Settings menu. Select network. Unplug the cable.

- Click "Install Now"

- Select "I don't have a product key"

- Select the flavor you want:

    - You intend to use Plausible Deniability: Windows Home
    - You do not intend to use Plausible Deniability: Windows Pro
    - VM OS: Use Windows Pro or Windows Pro N

- Select Custom

- Storage:

    - If this is a simple OS installation (Host OS with Simple Encryption) or VM without encryption, **select the whole disk** and proceed with the installation (skip the next step).

    - If this is part of a plausible deniability encryption set up on the Host OS:

        + If you are installing Windows for the first time (Hidden OS):

            * Delete the current partitions

            * Create the First partition with at least 50GB of disk space (about a third of the total disk space).

            * Create a second partition with the remaining two-thirds of the total disk space.

        + If you are installing Windows for the second time (Decoy OS):

            * Do not Delete the current partitions

            * Install Windows on the first partition you created during the first install.

        + Proceed with the install in the first partition

- Start the install process

- Select the Region "United States"

- Skip the additional Keyboard Layout

- Select "I don't have internet"

- Select "Continue with limited setup"

- Create a username of your choice.

- Use a password of your choice.

- Select all three security questions and answer whatever you want (not real data).

- Do not use Online Speech Recognition

- Do not let the app use your location

- Do not enable "find my device"

- Only send "required diagnostic data"

- Do not improve Inking and Typing

- Do not get any improved tailored experience.

- Do not let apps use Advertising ID

- Select "Now" at the Cortana prompt

## Privacy Settings { #win10-privacy }

- When the install is finished, get into Settings > Go on the top left menu icon and sekect Privacy and Security

    - When the install is finished, get into Settings > Privacy and do the following:

    - General: All Off

    - Speech: Off

    - Inking and Typing: Off

    - Diagnostic: Required level at off, options on OFF, **Delete your data**, frequency set to Never

    - Activity History: all Off and Clear the history

    - Location, all Off (change button) and clear it

    - Camera: Disable it (change button)

    - Microphone: Disable it (change button)

    - Voice Activation: All Off

    - Notification: Disable it (change button)

    - Account info: Disable it (change button)

    - Contact info: Disable it (change button)

    - Calendar access: Disable it (change button)

    - Phone calls: Disable it (change button)

    - Call History: Disable it (change button)

    - E-mail: Disable it (change button)

    - Tasks: Disable it (change button)

    - Messaging: Disable it (change button)

    - Radios: Disable it (change button)

    - Other devices: Set to Off

    - Background Apps: Disable it (change button)

    - App Diagnostics: Disable it (change button)

    - Automatic file download disabled

    - Documents: Disable it (change button)

    - Pictures: Disable it (change button)

    - Videos: Disable it (change button) and set to off

    - File system: Disable it (change button)

    - Disable File Indexing by going into the "Indexing Options" (Go into Windows 11 Control Panel, Switch the view to "Large Icons" and select Indexing Options.

    - Modify the list and remove all locations.

    - Go into Advanced and click Rebuild.

    - (Host OS only) Disable Bluetooth in the settings:

    - Go into Settings

    - Go into Devices

    - Select Bluetooth and turn it off

- (Host OS Only) Tape the Webcam and Microphone anyway for extra paranoia.

- (Host OS Only) Go into Settings > Network & Internet > Wi-Fi and Enable Random Hardware Address.

### Windows 11 { #using-win11 }

## Installation { #win11-install }

DO NOT CONNECT WINDOWS TO ANY NETWORK DURING THE INSTALLATION PROCESS (This will allow us to create a Local Account and not use a Microsoft account and it will also prevent any telemetry from being sent out during the install process).

- (Only for VirtualBox VM Install) Go into the VirtualBox Machine Settings menu. Select network. Unplug the cable. For this task, you can also follow this excellent tutorial by Oracle <https://blogs.oracle.com/virtualization/post/install-microsoft-windows-11-on-virtualbox> <sup>[[Archive.org]](https://web.archive.org/web/https://blogs.oracle.com/virtualization/post/install-microsoft-windows-11-on-virtualbox)</sup>

- Select your language, currency and keyboard layout

- Click "Install Now"

- (Only for VirtualBox VM Install) Push Shift and F10 at the same time

- (Only for VirtualBox VM Install) Launch "regedit" in the command prompt

- (Only for VirtualBox VM Install) When the Registry Editor opens, navigate to ```HKEY_LOCAL_MACHINE\SYSTEM\Setup```, right-click on the "Setup" key and select "New => Key". When prompted to name the key, enter "LabConfig" and press enter.

- (Only for VirtualBox VM Install) Now right-click on the "LabConfig" key and select "New => DWORD  (32-bit)" value and create a value named "BypassTPMCheck", and set its data to "1". With the same steps create the "BypassRAMCheck" and "BypassSecureBootCheck"

- Select "I don't have a product key"

- Accept the agreement

- Select the flavor you want:

    - You intend to use Plausible Deniability: Windows Home
    - You do not intend to use Plausible Deniability: Windows Pro
    - VM OS: Use Windows Pro or Windows Pro N

- Select Custom Install

- Storage:

    - If this is a simple OS installation (Host OS with Simple Encryption) or VM without encryption, **select the whole disk** and proceed with the installation (skip the next step).

    - If this is part of a plausible deniability encryption set up on the Host OS:

        + If you are installing Windows for the first time (Hidden OS):

            * Delete the current partitions

            * Create the First partition with at least 50GB of disk space (about a third of the total disk space).

            * Create a second partition with the remaining two-thirds of the total disk space.

        + If you are installing Windows for the second time (Decoy OS):

            * Do not Delete the current partitions

            * Install Windows on the first partition you created during the first install.

        + Proceed with the install in the first partition

- Start the install process

- Select the Region "United States"

- Select the Keyboard Layout and skip a second layout

- Select "I don't have internet"

- Select "Continue with limited setup"

- Create a username of your choice.

- Use a password of your choice.

- Select all three security questions and answer whatever you want (not real data).

- Ddisable Location

- Disable find my device

- Disable optional diagnostic data

- Only send "required diagnostic data"

- Do not improve Inking and Typing

- Disable the tailored experience.

- Disable the Advertising ID

- Click Accept

## Privacy Settings { #win11-privacy }

- When the install is finished, get into Settings > Privacy and do the following:

    - General: All Off

    - Speech: Off

    - Inking and Typing: Off

    - Diagnostic: Required level at off, options on OFF, **Delete your data**, frequency set to Never

    - Activity History: all Off and Clear the history

    - Location, all Off (change button) and clear it

    - Camera: Disable it (change button)

    - Microphone: Disable it (change button)

    - Voice Activation: All Off

    - Notification: Disable it (change button)

    - Account info: Disable it (change button)

    - Contact info: Disable it (change button)

    - Calendar access: Disable it (change button)

    - Phone calls: Disable it (change button)

    - Call History: Disable it (change button)

    - E-mail: Disable it (change button)

    - Tasks: Disable it (change button)

    - Messaging: Disable it (change button)

    - Radios: Disable it (change button)

    - Other devices: Set to Off

    - Background Apps: Disable it (change button)

    - App Diagnostics: Disable it (change button)

    - Automatic file download disabled

    - Documents: Disable it (change button)

    - Music Library: Disable it (change button)

    - Pictures: Disable it (change button)

    - Videos: Disable it (change button) and set to off

    - File system: Disable it (change button)

    - Disable File Indexing by going into the "Indexing Options" (Go into Windows 11 Control Panel, Switch the view to "Large Icons" and select Indexing Options.

    - Modify the list and remove all locations.

    - Go into Advanced and click Rebuild.

    - (Host OS only) Disable Bluetooth in the settings:

    - Go into Settings

    - Go into Devices

    - Select Bluetooth and turn it off

- (Host OS Only) Tape the Webcam and Microphone anyway for extra paranoia.

- (Host OS Only) Go into Settings > Network & Internet > Wi-Fi and Enable Random Hardware Address.

