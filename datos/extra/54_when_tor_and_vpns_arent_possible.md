# When Tor and VPNs Aren't Possible { #tor-vpn-not-possible }

**USE EXTREME CAUTION: THIS IS HIGHLY RISKY.**

There might be worst-case situations where using Tor and VPNs are not possible due to extensive active censorship or blocking. Even when using Tor Bridges (see [Using Tor bridges in hostile environments](#tor-bridges))

Now, there might also be situations where simply using Tor or a VPN alone could be suspicious and could be dangerous for your safety. If this is the case, you could be in a very hostile environment where surveillance and control are high.

But you still want to do something anonymously without disclosing/leaking any information.

In that case, my last resort recommendation is to connect safely **from a distance** to a Public Wi-Fi (See [Find some safe places with decent public Wi-Fi](#safe-wifi)) using your laptop and Tails "unsafe browser". See <https://tails.boum.org/contribute/design/Unsafe_Browser/> <sup>[[Archive.org]](https://web.archive.org/web/https://tails.boum.org/contribute/design/Unsafe_Browser/)</sup>.

**If Tor usage alone is suspicious or risky, you should NOT allow Tails to try establishing a Tor connection at start-up by doing the following:**

- At startup open the Additional Settings.

- Enable Unsafe Browser.

- Change the Connection from Direct to "Configure a Tor Bridge or Local Proxy"

- After Start-up, Connect to a safe Network

- When prompted, just quit the Tor Connection Wizard (to not establish a Tor connection)

- Start and use the Unsafe Browser

**We would strongly recommend the use of a long-range "Yagi" type directional Antenna with a suitable USB Wi-Fi Adapter. At least this will allow you to connect to public Wi-Fis from a "safe distance" but keep in mind that triangulation by a motivated adversary is still possible with the right equipment. So, this option should not be used during an extended period (minutes at best). See [Using long-range Antenna to connect to Public Wi-Fis from a safe distance](#long-range-wifi).**

Using Tails should prevent local data leaks (such as MAC addresses or telemetry) and allow you to use a Browser to get what you want (utilities, VPN account) before leaving that place as fast as possible.

You could also use the other routes (Whonix and Qubes OS without using Tor/VPN) instead of Tails in such hostile environments if you want data persistence but this might be riskier. We would not risk it personally unless there was absolutely no other option. If you go for this option, you will only do sensitive activities from a reversible/disposable VM in all cases. Never from the Host OS.

**If you resort to this, please keep your online time as short as possible (minutes and not hours).**

**Be safe and extremely cautious. This is entirely at your own risk.**

Consider reading this older but still relevant guide <https://archive.flossmanuals.net/bypassing-censorship/index.html> <sup>[[Archive.org]](https://web.archive.org/web/https://archive.flossmanuals.net/bypassing-censorship/index.html)</sup>

