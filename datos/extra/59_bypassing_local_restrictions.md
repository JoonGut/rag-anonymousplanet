# Bypassing Local Restrictions on Supervised Computers { #bypass-local-restrictions }

There might be situations where the only device you have at your disposal is not really yours such as:

- Using a Work computer with restrictions in place on what you can do/run.

- Misuse of Parental control features to monitor your computer usage (despite you being a non-consenting Adult).

- Misuse of various monitoring apps to monitor your computer usage against your will.

The situation might look desperate, but it is not necessarily the case as there are some safe ways to bypass these depending on how well your adversaries did their job securing your computer.

## Portable Apps { #use-portable-apps }

There are plenty of methods you could use to bypass those restrictions locally. One of them would be to use portable apps[^502]. Those apps do not require installation on your system and can be run from a USB key or anywhere else.

**But this is not a method we would recommend.**

This is because those portable apps will not necessarily hide themselves (or be able to hide themselves) from the usage reports and forensic examination. This method is just too risky and will probably arise issues if noticed if you are in such a hostile environment.

Even the most basic controls (supervision or parental) will send out detailed app usage to your adversary.

## Bootable Live Systems { #use-live-os }

This method is the one we would recommend in those cases.

It is relatively easy for your adversary to prevent this by setting up firmware BIOS/UEFI (see [Bios/UEFI/Firmware Settings of your laptop](#bios-uefi-settings)) controls but usually most adversaries will overlook this possibility which requires more technical knowledge than just relying on Software.

This method could even decrease suspicion and increase your plausible deniability as your adversaries think they have things under control and that everything appears normal in their reports.

This method only depends on one security feature (that they probably did not turn on in most cases): Boot Security.

Boot Security is divided into several types:

- Simple BIOS/UEFI password preventing the change of the boot order. This means you cannot start such a live system in place of your supervised OS without providing the BIOS/UEFI password.

- Secure Boot. This is a "standard" feature preventing you from starting unsigned systems from your computer. While this feature could be configured to only allow your supervised system, usually by default it will allow running an entire range of signed systems (signed by Microsoft or the Manufacturer for instance).

Secure Boot is relatively easy to bypass as there are plenty of Live Systems that are now Secure Boot compliant (meaning they are signed) and will be allowed by your laptop.

The BIOS/UEFI password on the other hand is much harder to bypass without risks. In that case, you are left with two options:

- Guess/Know the password so that you can change the boot order of your laptop without raising suspicions

- Reset the password using various methods to remove the password. **we would not recommend doing this because if your adversaries went the extra length of enabling this security feature, they probably will be suspicious if it were disabled, and this might increase suspicion and decrease your plausible deniability considerably.**

Again, this feature is usually overlooked by most unskilled/lazy adversaries and in my experience left disabled.

**This is your best chance into bypassing local controls without traces.**

The reason is that most of the controls are within your main Operating System software and only monitor what happens within the Operating System. Those measures will not be able to monitor what happened at the Hardware/Firmware level before the Operating System loads.

## Precautions { #live-os-precautions }

While you might be able to bypass local restrictions easily using a Live System such as Tails, remember that your network might also be monitored for unusual activities.

Unusual network activities showing up from a computer at the same time your computer is seemingly powered off might raise suspicions.

If you are to resort to this, you should never do so from a monitored/known network but only from a safe different network. Ideally a safe public wi-fi (See [Find some safe places with decent public Wi-Fi](#safe-wifi)).

**Do not use a live system on a Software supervised/monitored device on a known network.**

**Refer to the Tails route to achieve this. See [the Tails route](#tails-route) and [What about when Tor and VPNs aren't possible?](#tor-vpn-not-possible) sections.**

