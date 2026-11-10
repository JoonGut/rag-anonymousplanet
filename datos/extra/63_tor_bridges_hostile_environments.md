# Using Tor Bridges in Hostile Environments { #tor-bridges }

In some environments, your ISPs might be trying to prevent you from accessing Tor. Or accessing Tor openly might be a safety risk.

In those cases, it might be necessary to use Tor bridges to connect to the Tor network (see Tor Documentation <https://2019.www.torproject.org/docs/bridges> <sup>[[Archive.org]](https://web.archive.org/web/https://2019.www.torproject.org/docs/bridges)</sup> and Whonix Documentation <https://www.whonix.org/wiki/Bridges> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Bridges)</sup>). Optionally, if you are able, you should (seriously!) consider running a bridge <https://blog.torproject.org/run-tor-bridges-defend-open-internet/> <sup>[[Archive.org]](https://web.archive.org/web/20220708014922/https://blog.torproject.org/run-tor-bridges-defend-open-internet/)</sup> yourself, as this would greatly help reduce the amount of censorship in the world.

Bridges are special Tor entry nodes that are not listed on the Tor public directory. Some of those are running on people running the Snowflake Browser extension[^520] while others are running on various servers around the world. Most of those bridges are running some type of obfuscation method called obfs4[^521].

_Only available for Desktop Tor users: Recently, the Tor Project has made it incredibly simple to access Bridges with **Connection Assist**, and it is now automatically done in hostile or censored regions. Simply open the Tor Browser and the connection will be configured based on your needs on any hostile network. Previously, we had a list of options below this paragraph which were necessary to enable and configure bridges, but now that this is done automatically using [moat](https://support.torproject.org/glossary/moat/)._ <sup>[[Archive.org]](https://web.archive.org/web/20220801151048/https://support.torproject.org/glossary/moat/)</sup>

Here is the definition from the Tor Browser Manual[^523]: "obfs4 makes Tor traffic look random and prevents censors from finding bridges by Internet scanning. obfs4 bridges are less likely to be blocked than its predecessor, obfs3 bridges".

Some of those are called "Meek" bridges and are using a technique called "Domain Fronting" where your Tor client (Tails, Tor Browser, Whonix Gateway) will connect to a common CDN used by other services. To a censor, it would appear you are connecting to a normal website such as Microsoft.com. See <https://gitlab.torproject.org/legacy/trac/-/wikis/doc/meek> for more information.

As per their definition from their manual: "meek transports make it look like you are browsing a major web site instead of using Tor. meek-azure makes it look like you are using a Microsoft web site". Snowflake bridges make it appear like your connections are phone calls to random internet users. This is a type of "domain fronting" [^524]. See ["domain fronting"](https://www.bamsoftware.com/papers/fronting/#sec:introduction) from the link in the previous paragraph for a detailed explanation of these types of secret "bridges".

Lastly, there are also bridges called Snowflake bridges that rely on users running the snowflake extension in their browser to become themselves entry nodes. See <https://snowflake.torproject.org/> <sup>[[Archive.org]](https://web.archive.org/web/https://snowflake.torproject.org/)</sup>.

First, you should proceed with the following checklist to make sure you cannot circumvent Tor Blocking (double-check) and try to use Tor Bridges (<https://bridges.torproject.org/> <sup>[[Archive.org]](https://web.archive.org/web/https://bridges.torproject.org/)</sup>):

- (Recommended if blocked but **safe**) Try to get an obfs4 bridge in the Tor connection options.

- (Recommended if blocked but **safe**) Try to get a snowflake bridge in the Tor connection options.

- **(Recommended if hostile/risky environment)** Try to get a meek bridge in the Tor connection options (might be your only option if you are for instance in China).

![image54](../media/image54.png)

(Illustration from Tor Browser Bridge Configuration)

If none of those build-in methods are working, you could try getting a manual bridge either from:

- <https://bridges.torproject.org/bridges?transport=meek> (for a meek bridge)

- <https://bridges.torproject.org/bridges?transport=obfs4> (for an obfs4 bridge)

This website obviously could be blocked/monitored too so you could instead (if you have the ability) ask someone to do this for you if you have a trusted contact and some e2e encrypted messaging app.

Finally, you could also request a bridge request by e-mail to <bridges@torproject.org> with the subject empty and the body being: "get transport obfs4" or "get transport meek". There is some limitation with this method tho as it is only available from a Gmail e-mail address or Riseup.

- See: [A note about Riseup:] Riseup has potentially been compromised. Use it at your own risk.

Hopefully, these bridges should be enough to get you connected even in a hostile environment.

If not, consider [What about when Tor and VPNs aren't possible?](#tor-vpn-not-possible)

