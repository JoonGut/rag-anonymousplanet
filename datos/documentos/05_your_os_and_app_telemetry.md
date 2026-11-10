## Your OS and App telemetry services { #os-telemetry }

Whether it is Android, iOS, Windows, macOS, or even Ubuntu. Most popular Operating Systems now collect telemetry information by default even if you never opt-in or opted-out[^112] from the start. Some like Windows will not even allow disabling telemetry completely without some technical tweaks. This information collection can be extensive and include a staggering number of details (metadata and data) on your devices and their usage.

Here are good overviews of what is being collected by those five popular OSes in their last versions:

**Android/Google:**

- Just have a read at their privacy policy <https://policies.google.com/privacy> <sup>[[Archive.org]](https://web.archive.org/web/https://policies.google.com/privacy)</sup>
- School of Computer Science & Statistics, Trinity College Dublin, Ireland Mobile Handset Privacy: Measuring The Data iOS and Android Send to Apple And Google <https://www.scss.tcd.ie/doug.leith/apple_google.pdf> <sup>[[Archive.org]](https://web.archive.org/web/https://www.scss.tcd.ie/doug.leith/apple_google.pdf)</sup>

**IOS/Apple:**

- More information at <https://www.apple.com/legal/privacy/en-ww/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.apple.com/legal/privacy/en-ww/)</sup> and <https://support.apple.com/en-us/HT202100> <sup>[[Archive.org]](https://web.archive.org/web/https://support.apple.com/en-us/HT202100)</sup>
- School of Computer Science & Statistics, Trinity College Dublin, Ireland Mobile Handset Privacy: Measuring The Data iOS and Android Send to Apple And Google <https://www.scss.tcd.ie/doug.leith/apple_google.pdf> <sup>[[Archive.org]](https://web.archive.org/web/https://www.scss.tcd.ie/doug.leith/apple_google.pdf)</sup>
- Apple does claim[^109] that they anonymize this data using differential privacy[^110] but you will have to trust them on that.

**Windows/Microsoft:**

- Full list of required diagnostic data: <https://docs.microsoft.com/en-us/windows/privacy/required-windows-diagnostic-data-events-and-fields-2004> <sup>[[Archive.org]](https://web.archive.org/web/https://docs.microsoft.com/en-us/windows/privacy/required-windows-diagnostic-data-events-and-fields-2004)</sup>
- Full list of optional diagnostic data: <https://docs.microsoft.com/en-us/windows/privacy/windows-diagnostic-data> <sup>[[Archive.org]](https://web.archive.org/web/https://docs.microsoft.com/en-us/windows/privacy/windows-diagnostic-data)</sup>

**macOS:**

- More details on <https://support.apple.com/guide/mac-help/share-analytics-information-mac-apple-mh27990/mac> <sup>[[Archive.org]](https://web.archive.org/web/https://support.apple.com/guide/mac-help/share-analytics-information-mac-apple-mh27990/mac)</sup>

**Ubuntu:**

- Ubuntu despite being a Linux distribution also collects Telemetry Data nowadays. This data however is quite limited compared to the others. More details on <https://ubuntu.com/desktop/statistics> <sup>[[Archive.org]](https://web.archive.org/web/https://ubuntu.com/desktop/statistics)</sup>

Not only are Operating Systems gathering telemetry services but so are Apps themselves like Browsers, Mail Clients, and Social Networking Apps installed on your system.

It is important to understand that this telemetry data can be tied to your device and help de-anonymizing you and later can be used against you by an adversary that would get access to this data.

This does not mean for example that Apple devices are terrible choices for good Privacy (tho this might be changing[^111]), but they are certainly not the best choices for (relative) Anonymity. They might protect you from third parties knowing what you are doing but not from themselves. In all likelihood, they certainly know who you are.

Later in this guide, we will use all the means at our disposal to disable and block as much telemetry as possible to mitigate this attack vector in the Operating Systems supported in this guide. These will include Windows, macOS, and even Linux in some regard.

See [Warning about smartphones and smart devices](#smartphones-warning)

### Windows COM Class Identifiers (CLSID) and GUIDs { #your-com-class-identifiers }

Windows assigns a 128-bit GUID to every registered COM class (CLSID), interface (IID), and application (AppID). These are enumerable from user space via the registry (`HKEY_CLASSES_ROOT\CLSID\{GUID}`), no admin rights required, and in some cases can be probed from web content.

**Deanonymization vector**: The specific set of CLSIDs registered on a machine reflects the exact installed software: codecs, shell extensions, Office components, VPN client integrations, security tools, browser helper objects. This is as unique a fingerprint as font or plugin enumeration, but it persists across browser profiles and sessions since it lives at the OS level, not in browser storage.

How it's exploited:

- Software inventory fingerprinting. Enumerating registered CLSIDs reveals installed applications with far more granularity than a User-Agent string.
- Presence probing. A site can test for specific CLSIDs or associated custom URI protocol handlers to detect named applications: VPN clients, communication apps, forensic or analysis tools.
- VM/sandbox detection. Certain CLSIDs and related registry artifacts are diagnostic of VirtualBox, VMware, or known anonymity-focused environments.
- Cross-context correlation. Reusing one Windows install across anonymous and identified activity links the two, independent of browser-level compartmentalization.

Mitigations:

- Use a dedicated, minimal-install VM per identity or persona. Do not reuse one Windows install across anonymous and identified contexts.
- Prefer Linux-based isolation (Whonix, Tails, Qubes-Whonix) for high-threat-model use. This attack class is COM/Windows-specific and has no direct equivalent there.
- Revert to a clean snapshot between sessions rather than relying on manual cleanup.
- Treat this as the same fingerprinting category as font and plugin enumeration: the fix is compartmentalization, not registry editing.

### Windows Global Device Identifier (GDID) { #your-global-device-identifiers }

The GDID is a persistent, server-assigned 64-bit device identifier tied to a Windows installation. It is almost entirely undocumented by Microsoft: the only public reference is a single line in the Azure Monitor schema for the `UCDOStatus` (Delivery Optimization) table, describing a `GlobalDeviceId` column as "Microsoft global device identifier. This is an identifier used by Microsoft internally." Independent reverse-engineering, confirmed against Windows 11 build 26200, has since mapped the full chain.

!!! note "Sources"
    - _United States v. Peter Stokes_, N.D. Ill. (2026). Federal criminal complaint; primary source for the GDID's real-world use in a law enforcement investigation. Highly encourage all readers of this document to consider that this obscure device telemetry vector was not documented prior to this court case, and is mentioned in passing.
    - ["Windows GDID Fully Reverse Engineered: MSA Device PUID Exposed"](https://www.devdigest.org/articles/windows-gdid-fully-reverse-engineered-msa-device-puid-exposed), Devdigest.
    - ["You can't fully disable Microsoft's GDID Windows 11 tracker, but these settings limit what it captures"](https://www.windowslatest.com/2026/07/10/you-cant-fully-disable-microsofts-gdid-windows-11-tracker-but-these-settings-limit-what-it-captures/), Windows Latest.
    - [gdid-reversal](https://github.com/SmtimesIWndr/gdid-reversal), independent reverse-engineering write-up with ETW and registry evidence.

    !!! warning "On the gdid-reversal source"
        We have not vetted and will not vet this source, so exercise caution. This repository is user-created and its authorship is unverified. Content may be partly or wholly AI-generated. Treat specific technical claims (registry paths, binary symbols, ETW provider details) as unverified until cross-checked against a real Windows install or a more established source. It's included here because it's one of the only detailed technical accounts of an otherwise undocumented mechanism, not as an authoritative reference.

!!! danger "How it works"
    When a device signs in with a Microsoft Account, `wlidsvc` provisions it against `login.live.com` and gets back a Device PUID (Passport Unique ID): a server-assigned value, not derived from any local hardware serial. This is stored in the registry, read by the Connected Devices Platform (`cdp.dll` / `CDPSvc`), registered into Microsoft's Device Directory Service graph, and reported by Delivery Optimization as `UCDOStatus.GlobalDeviceId` whenever the machine participates in peer-to-peer update sharing.

    Read your own GDID without admin rights:
    ```powershell
    (Get-ItemProperty 'HKCU:\SOFTWARE\Microsoft\IdentityCRL\ExtendedProperties').LID
    ```
    This is what the federal complaint used to place a Scattered Spider suspect at specific times and locations across multiple VPN sessions and four countries. Microsoft records matched a specific GDID to the moment an ngrok account was created, regardless of the VPN in use.

Key properties for the threat model:

- VPN/IP-agnostic. The GDID doesn't change with IP address, VPN provider, or exit node. It correlates sessions on the same OS install, not network paths.
- Not disabled by telemetry opt-outs. It doesn't travel through the classic `DiagTrack` pipeline. Disabling standard diagnostic data settings has no effect on it.
- Server-side persistence. Deleting the local registry value is cosmetic. The same identifier re-syncs from Microsoft's servers on the next authenticated request (opening the Microsoft Store, for example), because the canonical copy lives server-side, not on disk.
- Local accounts don't prevent it. A local, non-MSA install still registers an anonymous device path through the Connected Devices Platform. It just isn't tied to an MSA identity unless one is added later.
- A reinstall gets a new GDID, not a clean slate. A fresh install produces a new identifier, but account, OneDrive, and activation records give Microsoft a documented basis for linking the new GDID back to the old one through the same account.

Mitigations:

- Assume any Windows install signed into a Microsoft Account is linkable across all its sessions regardless of VPN discipline. This is a hard requirement for compartmentalization, not a tuning option.
- For genuinely sensitive activity, don't use Windows at all. Use a Linux-based environment (Whonix, Tails, Qubes-Whonix) where this telemetry chain doesn't exist.
- Never reuse a single Windows install, MSA, or even a "cleaned" reinstall on the same physical machine across separate personas.

Reducing exposure, if Windows must be used:

- Use a local account. CDP still creates an anonymous device path, but the GDID won't be tied to an MSA.
- Block `dds.microsoft.com` and `activity.windows.com` via firewall rules or the hosts file, to cut the reporting channel at the network layer.
- Delete the registry keys under `IdentityCRL` to clear the locally stored PUID. This only clears the local cache. It's recreated identical to before on the next MSA sign-in or even a background service touching a Microsoft app, since the canonical value lives server-side.
- Disable the Delivery Optimization service (`DoSvc`). This service reports the GDID via `UCDOStatus.GlobalDeviceId` and is hardened against normal administrative control: `Stop-Service` and `Set-Service` return access-denied even when run elevated. The only reported workaround is disabling it directly in the registry by setting its `Start` value to `4` under its service key, since the Service Manager's block doesn't extend to direct registry writes. Disabling `DoSvc` alongside `CDPSvc`/`CDPUserSvc` breaks Delivery Optimization peer caching, Phone Link / "Continue on PC," and nearby sharing. These are expected tradeoffs, not bugs.

!!! warning "What this does not do"
    None of the above retracts a GDID already reported to Microsoft, and none of it makes the device anonymous. It only stops the local install from continuing to re-register and re-report going forward. The historical link between the device and any prior identified activity already exists on Microsoft's servers and can't be removed by a local user.

!!! note "Further reading / tooling"
    Independent write-ups and a defensive PowerShell toolkit implementing the steps above (read-only audit, preview mode, revert option) are publicly available and worth reviewing directly rather than treating this section as a complete implementation guide. The service-disabling steps carry real breakage tradeoffs and should be tested on a VM snapshot first.

