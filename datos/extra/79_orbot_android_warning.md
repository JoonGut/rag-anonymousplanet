# Orbot on Android Warning { #orbot-android-warning }

While this is often misunderstood, Orbot on Android does not make your Tor-enabled apps go through Tor if you add them to the list. Orbot is acting as a device-wide VPN (also known as a "transparent proxy"). The list of apps using Orbot is a whitelist. This list will not make some apps magically use Tor and unchecked ones use the clear-net. This only ensures the device-wide VPN is using Tor to route traffic. This means that Orbot can only control what app can access the VPN it creates. Other apps will lose connectivity.

What is important to know is that, if you launch an app (or Android does it automatically) while Orbot is not running, the app will just use the normal network, without involving Orbot (with the exception of some apps supporting a proxy Orbot).

Additionally, you should not be surprised by Tor Browser not working when using Orbot in VPN mode, as the Tor design does not allow "Tor over Tor" (you cannot re-enter the Tor network from a Tor exit node).

This is explained rather well by Alexander Færøy, who is a core developer at the Tor Project, in their [TorifyHOWTO: Tor over Tor](https://gitlab.torproject.org/legacy/trac/-/wikis/doc/TorifyHOWTO#tor-over-tor).

"When using a transparent proxy, it is possible to start a Tor session from the client as well as from the transparent proxy (read the warning!), creating a "Tor over Tor" scenario. Doing so produces undefined and potentially unsafe behavior. In theory, however, you can get six hops instead of three, but it is not guaranteed that you'll get three different hops - you could end up with the same hops, maybe in reverse or mixed order. It is not clear if this is safe. It has never been discussed. You can choose an entry/exit point, but you get the best security that Tor can provide when you leave the route selection to Tor; overriding the entry / exit nodes can mess up your anonymity in ways we don't understand. Therefore Tor over Tor usage is highly discouraged."

And from [a post](https://tor.stackexchange.com/questions/427/is-running-tor-over-tor-dangerous) on the Tor Stack Exchange:

"The danger (beyond the performance hit) which keeps me from running Tor over Tor has to do with timing and congestion measurements. Adversaries watching your traffic at the exit(s) of your circuits have a better chance of linking your Whonix activity with your [Tor Browser Bundle] activity when those shared circuits slow down or drop packets at the same time. This can happen without Tor over Tor when your instances use a common upstream link. The linkage will be made tighter and more explicit if you run the Whonix Tor traffic through your TBB SOCKS5 Tor circuits. This tighter linkage raises the danger of successful correlation."

