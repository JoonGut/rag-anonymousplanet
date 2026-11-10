## Your Hardware Identifiers { #hardware-identifiers }

### Windows USB bus telemetry (device enumeration history) { #usb-bus-telemetry }

Windows keeps a permanent enumeration history of every USB device ever connected, independent of whether the device is currently attached.

!!! danger "Deanonymization vector"
    Each USB mass storage device exposes a Vendor ID, Product ID, and, for most drives, a unique serial number at the descriptor level during enumeration. Windows records this under:

    - `HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR`
    - `HKLM\SYSTEM\CurrentControlSet\Enum\USB`
    - `SetupAPI.dev.log`

    This creates a durable, cross-reinstall link between a specific physical USB drive, phone, hardware key, or dongle, and every OS install it has ever touched, because the identifying data lives in the device's own firmware/descriptor, not in the OS.

How it's exploited:

- Physical device correlation. The same USB drive used across a "clean" VM and a personal machine carries its VID/PID/serial into both installs' registries, creating a link forensic analysis, or malware with sufficient privilege, can recover even if the OS itself was reinstalled or the VM rebuilt.
- First-connected timestamps. Registry key metadata records first- and last-connected times per device, which can corroborate or contradict claimed usage timelines.
- Persists across OS reinstall of the host, not the device. Reinstalling Windows resets the host's own identifiers, including the GDID, but does nothing to the USB device's own serial. Replugging it into a new install just writes a fresh, correlatable entry referencing the same hardware ID.

Mitigations:

- Never share USB storage media, security keys, or peripherals between anonymous and identified environments.
- Where sharing is unavoidable, prefer devices that don't expose a unique serial in their descriptor, and treat any device that has ever touched an identified machine as burned for anonymous use.
- Use write-blockers or a live OS (Tails) for cases where a USB device's provenance itself is sensitive, since USB enumeration history is written by the host OS regardless of read/write intent.

### Your IMEI and IMSI { #imei-imsi }

The IMEI and the IMSI are unique numbers created by cell phone manufacturers and cell phone operators.

The IMEI is tied directly to the phone you are using. This number is known and tracked by the cell phone operators and known by the manufacturers. Every time your phone connects to the mobile network, it will register the IMEI on the network along with the IMSI (if a SIM card is inserted but that is not even needed). It is also used by many applications (Banking apps abusing the phone permission on Android for instance[^86]) and smartphone Operating Systems (Android/IOS) for identification of the device[^87]. It is possible but difficult (and not illegal in many jurisdictions[^88]) to change the IMEI on a phone but it is probably easier and cheaper to just find and buy some old (working) Burner phone for a few Euros (this guide is for Germany remember) at a flea market or some random small shop.

The IMSI is tied directly to the mobile subscription or pre-paid plan you are using and is tied to your phone number by your mobile provider. The IMSI is hardcoded directly on the SIM card and cannot be changed. Remember that every time your phone connects to the mobile network, it will also register the IMSI on the network along with the IMEI. Like the IMEI, the IMSI is also being used by some applications and smartphone Operating systems for identification and is being tracked. Some countries in the EU for instance maintain a database of IMEI/IMSI associations for easy querying by Law Enforcement.

Today, giving away your (real) phone number is the same or better than giving away your Social Security number/Passport ID/National ID.

The IMEI and IMSI can be traced back to you in at least six ways:

- The mobile operator subscriber logs will usually store the IMEI along with the IMSI and their subscriber information database. If you use a prepaid anonymous SIM (anonymous IMSI but with a known IMEI), they could see this cell belongs to you if you used that cell phone before with a different SIM card (different anonymous IMSI but same known IMEI).

- The mobile operator antenna logs will conveniently keep a log of which IMEI. IMSI also keep some connection data. They know and log for instance that a phone with this IMEI/IMSI combination connected to a set of mobile antennas and how powerful the signal to each of those antennas were, allowing easy triangulation/geolocation of the signal. They also know which other phones (your real one for instance) connected at the same time to the same antennas with the same signal. This makes it possible to know precisely that this "burner phone" was always connected at the same place/time than this other "known phone" which shows up every time the burner phone is being used. This information can/is used by various third parties to geolocate/track you quite precisely[^89]'[^90].

- The manufacturer of the Phone can trace back the sale of the phone using the IMEI if that phone was bought in a non-anonymous way. Indeed, they will have logs of each phone sale (including serial number and IMEI), to which shop/person to whom it was sold. And if you are using a phone that you bought online (or from someone that knows you). It can be traced to you using that information. Even if they do not find you on CCTV[^91] and you bought the phone using cash, they can still find what other phone (your real one in your pocket) was there (in that shop) at that time/date by using the antenna logs.

- The IMSI alone can be used to find you as well because most countries now require customers to provide an ID when buying a SIM card (subscription or pre-paid). The IMSI is then tied to the identity of the buyer of the card. In the countries where the SIM can still be bought with cash (like the UK), they still know where (which shop) it was bought and when. This information can then be used to retrieve information from the shop itself (such as CCTV footage as for the IMEI case). Or again the antenna logs can also be used to figure out which other phone was there at the moment of the sale.

- The smartphone OS makers (Google/Apple for Android/IOs) also keep logs of IMEI/IMSI identifications tied to Google/Apple accounts and which user has been using them. They too can trace back the history of the phone and to which accounts it was tied in the past[^92].

- Government agencies around the world interested in your phone number can and do use[^93] special devices called "IMSI catchers"[^94] like the Stingray[^95] or more recently the Nyxcell[^96]. These devices can impersonate (to spoof) a cell phone Antenna and force a specific IMSI to connect to it to access the cell network. Once they do, they will be able to use various MITM[^97] that will allow them to:

    - Tap your phone (voice calls and SMS).

    - Sniff and examine your data traffic.

    - Impersonate your phone number without controlling your phone.

Here is also a good YouTube video on this topic: [DEFCON Safe Mode - Cooper Quintin - Detecting Fake 4G Base Stations in Real-Time](https://www.youtube.com/watch?v=siCk4pGGcqA) <sup>[[Invidious]](https://yewtu.be/watch?v=siCk4pGGcqA)</sup>

 **For these reasons, it is crucial to get a dedicated anonymous phone number and/or an anonymous burner phone with a cash-bought pre-paid sim card that is not tied to you in any way (past or present) for conducting sensitive activities. It is also possible to get an anonymous pre-paid but preferably dedicated number from free and paid online services accepting anonymous cryptocurrencies like Monero. Get more practical guidance here: [Getting an anonymous Phone number](#anonymous-phone).**

While there are some smartphones manufacturers like Purism with their Librem series[^98] who claim to have your privacy in mind, they still do not allow IMEI randomization which we believe is a key anti-tracking feature that should be provided by such manufacturers. While this measure will not prevent IMSI tracking within the SIM card, it would at least allow you to keep the same "burner phone" and only switch SIM cards instead of having to switch both for privacy.

See [Warning about smartphones and smart devices](#smartphones-warning)

### Your Wi-Fi or Ethernet MAC address { #mac-address }

The MAC address[^99] is a unique identifier tied to your physical Network Interface (Wired Ethernet or Wi-Fi) and could of course be used to track you if it is not randomized. As it was the case with the IMEI, manufacturers of computers and network cards usually keep logs of their sales (usually including things like serial number, IMEI, Mac Addresses, ...) and it is possible again for them to track where and when the computer with the MAC address in question was sold and to whom. Even if you bought it with cash in a supermarket, the supermarket might still have CCTV (or a CCTV just outside that shop) and again the time/date of sale could be used to find out who was there using the Mobile Provider antenna logs at that time (IMEI/IMSI).

Operating Systems makers (Google/Microsoft/Apple) will also keep logs of devices and their MAC addresses in their logs for device identification (Find my device type services for example). Apple can tell that the MacBook with this specific MAC address was tied to a specific Apple Account before. Maybe yours before you decided to use the MacBook for sensitive activities. Maybe to a different user who sold it to you but remembers your e-mail/number from when the sale happened.

Your home router/Wi-Fi access point keeps logs of devices that are registered on the Wi-Fi, and these can be accessed too to find out who has been using your Wi-Fi. Sometimes this can be done remotely (and silently) by the ISP depending on if that router/Wi-Fi access point is being "managed" remotely by the ISP (which is often the case when they provide the router to their customers).

Some commercial devices will keep a record of MAC addresses roaming around for various purposes such as road congestion[^100].

**So, it is important again not to bring your phone along when/where you conduct sensitive activities. If you use your own laptop, then it is crucial to hide that MAC address (and Bluetooth address) anywhere you use it and be extra careful not to leak any information. Thankfully many recent OSes now feature or allow the possibility to randomize MAC addresses (Android, IOS, Linux, and Windows 10/11)** with the notable exception of macOS which does not support this feature even in its latest Big Sur version.

See [Warning about smartphones and smart devices](#smartphones-warning)

### Your Bluetooth MAC address { #bluetooth-mac }

Your Bluetooth MAC is like the earlier MAC address except it is for Bluetooth. Again, it can be used to track you as manufacturers and operating system makers keep logs of such information. It could be tied to a sale place/time/date or accounts and then could be used to track you with such information, the shop billing information, the CCTV, or the mobile antenna logs in correlation.

Operating systems have protections in place to randomize those addresses but are still subject to vulnerabilities[^101].

For this reason, and unless you really need those, you should just disable Bluetooth completely in the BIOS/UEFI settings if possible or in the Operating System otherwise.

On Windows 10, you will need to disable and enable the Bluetooth device in the device manager itself to force randomization of the address for next use and prevent tracking.

In general, this should not be too much of a concern compared to MAC Addresses. BT Addresses are randomized quite often.

See [Warning about smartphones and smart devices](#smartphones-warning)

