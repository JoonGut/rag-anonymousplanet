# Connecting to Public Wi-Fi from a Safe Distance { #long-range-wifi }

It is possible to access/connect to remote distant Public Wi-Fis from a distance using a cheap directional Antenna that looks like this:

![image52](../media/image52.png)

These antennas are widely available on various online shops for a cheap price (Amazon, AliExpress, Banggood ...). The only issue is that they are not discrete, and you might have to find a way to hide it (for instance in a Poster cardboard container in a Backpack). Or in a large enough Bag. Optionally (but riskier) you could even consider using it from your home if you have a nice Window view to various places where some Public Wi-Fi is available.

Such antennas need to be combined with specific USB adapters that have an external Antenna plug and sufficiently high power to use them.

**We would recommend the AWUS036 series in the Alfa brand of adapters (see <https://www.alfa.com.tw/>** <sup>[[Archive.org]](https://web.archive.org/web/https://www.alfa.com.tw/)</sup>**).** But you could also go with some other brands if you want such as the TP-Link TL-WN722 (see <https://www.tp-link.com/us/home-networking/usb-adapter/tl-wn722n/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.tp-link.com/us/home-networking/usb-adapter/tl-wn722n/)</sup>).

See this post for a comparison of various adapters: <https://www.wirelesshack.org/best-kali-linux-compatible-usb-adapter-dongles.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.wirelesshack.org/best-kali-linux-compatible-usb-adapter-dongles.html)</sup> (Usually those antennas are used by Penetration Testers to probe Wi-Fis from a distance and are often discussed within the scope of the Kali Linux distribution).

The process is simple:

- Plugin and install your USB adapter on your Host OS.

- **Do not forget to randomize your MAC Address in case you bought this adapter online to prevent traceability (this is enabled by default in Tails).**

- Connect the Long-Range Antenna to the USB adapter (in place of the supplied one).

- Get to a convenient spot where you have a distant view of a place with Public Wi-Fi available (this can be a rooftop for instance), but you could also imagine hiding the Antenna in some bag and just sit on a bench somewhere.

- Point the Directional Antenna in the direction of the Public Wi-Fi.

- Connect to the Wi-Fi of your choice.

**Do not forget tho that this will only delay a motivated adversary. Your signal can be triangulated easily by a motivated adversary in a matter of minutes once they reach the physical location of the Wi-Fi you're connecting to (for instance using a device such as AirCheck <https://www.youtube.com/watch?v=8FV2QZ1BPnw>** <sup>[[Invidious]](https://yewtu.be/watch?v=8FV2QZ1BPnw)</sup>**, also see their other products here <https://www.netally.com/products/>** <sup>[[Archive.org]](https://web.archive.org/web/https://www.netally.com/products/)</sup>**). These products can easily be deployed on mobile units (in a Car for instance) and pinpoint your location in a matter of minutes.**

Ideally, this should "not be an issue" since this guide provides multiple ways of hiding your origin IP using VPNs and Tor. But if you are in a situation where VPN and Tor are not an option, then this could be your only security.

