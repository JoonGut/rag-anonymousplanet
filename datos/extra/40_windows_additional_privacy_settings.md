# Windows Additional Privacy Settings { #win-additional-privacy }

As written earlier in this guide and as noted by PrivacyGuides.org[^458], Windows 10/11 is a privacy nightmare. And disabling everything during and after the installation using the settings available to you is not enough. The amount of telemetry data collected by Microsoft is staggering and could defeat your attempts at keeping secrets. You will need to download and use a couple of utilities to (hopefully) force Windows 10/11 into not sending data back to Microsoft.

Here are the steps in detail:

- **DO NOT EVER USE A MICROSOFT ACCOUNT TO LOG IN: If you are, you should be re-installing this Windows Machine without connecting to a network and use a local account instead.**

- Do these steps from a different computer. Do not connect Windows 10/11 to the internet before those settings are applied. You can download and copy those to the USB key (for transfer onto a Windows 10/11 fresh installation) or if it is a VM, you can transfer them to the VM within Virtualbox (VM Settings > General > Advanced > Drag n Drop > Enable Host to Guest).

- (For more advanced users) Download and install W10Privacy from <https://www.w10privacy.de/english-home/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.w10privacy.de/english-home/)</sup>

    - Open the app as Administrator (right-click > more > run as administrator)
    - Check all the recommended (Green) settings and save.
    - Optional but recommended (but could break things, use at your own risk), also check the orange/red settings, and save.
    - Reboot

- Download and run WindowsSpyBlocker from <https://crazymax.dev/WindowsSpyBlocker/download/> <sup>[[Archive.org]](https://web.archive.org/web/https://crazymax.dev/WindowsSpyBlocker/download/)</sup>

    - Type 1 and go into Telemetry
    - Type 1 and go into Firewall
    - Type 2 and add Spy Rules
    - Reboot

- Also, consider using ShutUp10++ from <https://www.oo-software.com/en/shutup10> <sup>[[Archive.org]](https://web.archive.org/web/https://www.oo-software.com/en/shutup10)</sup>

    - Enable at least all the recommended settings

- Finally, again for users with moderate skills, consider installing Safing Portmaster from <https://safing.io/portmaster/> <sup>[[Archive.org]](https://web.archive.org/web/https://safing.io/portmaster)</sup> **(Warning: there might be issues with some VPN clients. See: <https://docs.safing.io/portmaster/install/status/vpn-compatibility>** <sup>[[Archive.org]](https://web.archive.org/web/https://safing.io/portmaster/)</sup>

- Go back one last time to the settings to delete Diagnostic and Delete all Data.

These measures added to the settings during installation should be hopefully sufficient to prevent Microsoft from snooping on your OS.

**You will need to update and re-run those utilities frequently and after any Windows major update as they tend to silently re-enable telemetry using those updates.**

**As a bonus, it could be interesting to also consider Hardening your Windows Host OS somewhat. See <https://github.com/beerisgood/windows10_hardening>** <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/beerisgood/windows10_hardening)</sup> (This is a security guide, not a privacy guide. If you use this guide, do not enable Hyper-V as it does not play well with Virtualbox, and do not enable features that were specifically disabled for privacy reasons earlier. Such as SmartScreen, cloud protection...)

