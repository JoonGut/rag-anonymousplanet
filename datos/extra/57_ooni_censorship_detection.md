# Network Surveillance and Censorship Detection with OONI { #ooni-censorship-check }

So, what is OONI? OONI stands for Open Observatory of Network Interference and is a sub-project of the Tor Project[^296].

First OONI will allow you to check online for surveillance/censorship in your country just by looking at their Explorer that features test results from other people. This can be done here: <https://explorer.ooni.org/>

But these tests are limited and could not apply to your personal situation. If that is the case, you could consider running the OONI Probe yourself and running the tests yourself.

The problem is that your network providers will be able to see those tests and your attempts at connecting to various services if the network is monitored. The other issue is that there are solutions to prevent OONI from working properly[^473].

While this might not be important in a normal environment, this could put you at risk in a hostile environment. **So, running these tests can be risky.**

**If you are in such a hostile environment where you suspect network activity is actively monitored and the simple fact of trying to access some resources can put you at risk, you should take some precautions before even attempting this:**

- **Do not run the tests from your home/work network.**

- **Do not run these tests from a known device or a smartphone but only for a secured OS on an ideally dedicated laptop.**

    - **You will not be able to do this from Tails as Tails will try to connect to Tor by default**

    - **You should only do this with the Qubes OS route or the Whonix Route of this guide after completing one of the routes.**

- **Only consider running these tests quickly from a Public Wi-Fi from a safe distance (see [What about when Tor and VPNs aren't possible?](#tor-vpn-not-possible)).**

The probe can be found here: <https://ooni.org/install/> <sup>[[Archive.org]](https://web.archive.org/web/https://ooni.org/install/)</sup> for various platforms (iOS, Android, Windows, macOS, and Linux).

