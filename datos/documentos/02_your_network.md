## Your Network { #network }

### Your IP address { #ip-addresses }

**Disclaimer: this whole paragraph is about your public-facing Internet IP and not your local network IP.**

Your IP address[^26] is the most known and obvious way you can be tracked. That IP is the IP you are using at the source. This is where you connect to the internet. That IP is usually provided by your ISP (xDSL, Mobile, Cable, Fiber, Cafe, Bar, Friend, Neighbor). Most countries have data retention regulations[^27] that mandate keeping logs of who is using what IP at a certain time/date for up to several years or indefinitely. Your ISP can tell a third party that you were using a specific IP at a specific date and time, years after the fact. If that IP (the original one) leaks at any point for any reason, it can be used to track down you directly. In many countries, you will not be able to have internet access without providing some form of identification to the provider (address, ID, real name, e-mail ...).

Needless to say, that most platforms (such as social networks) will also keep (sometimes indefinitely) the IP addresses you used to sign-up and sign into their services.

Here are some online resources you can use to find some information about your current **public IP** right now:

- Find your IP:

    - <https://resolve.rs/>

    - <https://www.dnsleaktest.com/> (Bonus, check your IP for DNS leaks)

- Find your IP location or the location of any IP:

    - <https://resolve.rs/ip/geolocation.html>

- Find if an IP is "suspicious" (in blacklists) or has downloaded "things" on some public resources:

    - <https://mxtoolbox.com/blacklists.aspx>

    - <https://www.virustotal.com/gui/home/search>

    - <https://iknowwhatyoudownload.com> (Take this with a grain of salt, it might not show anything interesting and has limited data sources. This is more for fun than anything serious.)

- Registration information of an IP (most likely your ISP or the ISP of your connection who most likely know who is using that IP at any time):

    - <https://whois.domaintools.com/>

- Check for open-services or open devices on an IP (especially if there are leaky Smart Devices on it):

    - <https://www.shodan.io/host/185.220.101.134> (replace the IP by your IP or any other, or change in the search box, this example IP is a Tor Exit node)

- Various tools to check your IP such as block-lists checkers and more:

    - <https://browserleaks.com/ip>

    - <https://www.whatismyip.com>

- Would you like to know if you are connected through Tor?

    - <https://check.torproject.org>

For those reasons, you will need to obfuscate and hide that origin IP (the one tied to your identification) or hide it through a combination of various means:

- Using a public Wi-Fi service (free).

- Using the Tor Anonymity Network[^28] (free).

- Using VPN[^29] services anonymously (anonymously paid with cash or Monero).

Do note that, unfortunately, these solutions are not perfect, and you will experience performance issues[^30].

All those will be explained later in this guide.

### Your DNS and IP requests { #dns-requests }

DNS[^31] is the internet's address book: every time your browser opens a connection to `www.google.com`, it first asks a DNS server to translate that name into an IP address. Your browser, and most other apps on your device, do this constantly in the background.

For a visual introduction to how DNS works, see: <https://www.youtube.com/watch?v=vrxwXXytEuI> <sup>[[Invidious]](https://yewtu.be/watch?v=vrxwXXytEuI)</sup>

#### The default DNS problem { #dns-default-problem }

By default, your DNS queries go to your ISP's resolver. This creates several compounding problems:

- **Logging.** ISPs are often subject to data retention laws and may log every domain you resolve, building a complete record of your browsing history. That log can be subpoenaed, sold, or breached.
- **Censorship.** DNS blocking is the most common censorship mechanism worldwide[^32][^33] - ISPs simply return a false address for blocked domains.
- **Tampering.** Even if you configure a private DNS resolver, your ISP can intercept and rewrite DNS responses in transit, because standard DNS traffic is unencrypted.
- **Hardcoded resolvers.** Many devices bypass system DNS settings entirely. Roughly 70% of Smart TVs and 46% of game consoles[^34] use hardcoded DNS servers that cannot be changed through OS settings - you have to block them at the network level[^35] or accept the exposure.

#### Encrypted DNS (DoH / DoT) { #dns-encrypted }

Encrypting your DNS queries using DoH (DNS over HTTPS)[^36] or DoT (DNS over TLS)[^37] prevents your ISP from reading or tampering with them in transit. You can run this:

- **Locally**, with a self-hosted resolver such as Pi-hole[^38].
- **Remotely**, via a privacy-focused provider such as nextdns.io.
- **Automatically**, through your VPN provider's DNS, or through the Tor network.

This is a meaningful improvement over plaintext DNS - but it is not sufficient on its own.

> **Note:** This guide does not endorse or recommend Cloudflare services. Cloudflare is referenced here only for technical context.

#### SNI leakage and ECH { #dns-sni-ech }

Even with encrypted DNS, the TLS handshake itself leaks the destination domain name through Server Name Indication (SNI)[^39]. An observer watching your connection - your ISP, a network monitor, or a rogue access point - can see which domain you are connecting to from the SNI field, even though the DNS query itself was encrypted.

![](../media/image04.png)

Encrypted Client Hello (ECH)[^40] (formerly eSNI[^41]) is the fix: it encrypts the SNI field so the destination domain is hidden from network observers[^42]. However, ECH has significant deployment constraints[^44]:

- Only Firefox-based browsers support ECH. It is not enabled by default and must be turned on manually.
- ECH only works with sites hosted behind Cloudflare's CDN. It is not supported by most major platforms, including Amazon (AWS, Twitch), Microsoft (Azure, OneDrive, Office 365), Google (Gmail, Google Cloud), Apple (iCloud, iMessage), Reddit, YouTube, Facebook, Instagram, Twitter, and GitHub.
- Russia[^45] and China[^46] are reported to block ECH handshakes at the network level, preventing connections to any service that requires ECH to function.

#### OCSP leakage { #dns-ocsp }

A separate leak occurs during TLS certificate validation. Firefox-based browsers use OCSP[^47] to check whether a site's certificate has been revoked. This check sends the certificate's serial number to a third-party OCSP responder - and that serial number can be matched against public certificate databases to identify exactly which site you are visiting[^48].

OCSP stapling[^49] mitigates this by having the server include a pre-signed OCSP response in the TLS handshake, removing the need for the browser to make a separate request. Firefox supports OCSP stapling but does not enforce it, and not all servers implement it. Chromium-based browsers use CRLSets[^50][^51] instead, which is arguably a cleaner approach.

Browser comparison: <https://www.ssl.com/blogs/how-do-browsers-handle-revoked-ssl-tls-certificates/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.ssl.com/blogs/how-do-browsers-handle-revoked-ssl-tls-certificates/)</sup>

![](../media/image05.png)

#### Traffic analysis defeats all of the above { #dns-traffic-analysis }

Even with encrypted DNS, ECH, and OCSP stapling all in place, traffic analysis[^52] can still identify the sites you visit by matching IP addresses - since most websites have unique IPs - or by fingerprinting traffic patterns. DNS over Tor shows the strongest DNS privacy in current research, but it can still be defeated by other methods (see [Traffic Anonymization](#traffic-anonymization)).

Two advanced options exist for DNS beyond standard DoH/DoT:

- **Tor Hidden DNS / ODoH** (Oblivious DNS over HTTPS[^53]): separates the query from the requester so no single party knows both who is asking and what they are asking for. Currently only offered by Cloudflare[^54], which introduces its own trust tradeoff. ODoH does not protect against a global passive adversary (GPA) who can observe traffic between the client resolver and the recursive resolver, between the recursive and ODNS resolvers, or between the ODNS resolver and an authoritative server.
- **DoHoT** (DNS over HTTPS over Tor): routes encrypted DNS queries through Tor for stronger anonymity. Requires Linux and more technical configuration. See <https://github.com/alecmuffett/dohot> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/alecmuffett/dohot)</sup>.

![](../media/image06.png)

#### Browser choice { #dns-browser-choice }

For daily non-sensitive use: only Firefox-based browsers support ECH, and ECH only helps for Cloudflare-hosted sites. If you prefer a Chromium-based browser, Brave is the most privacy-preserving option - it supports all Chrome extensions while adding meaningful protections that Chrome lacks.

#### IP addresses remain a residual leak { #dns-ip-residual }

Regardless of DNS encryption, the IP address your device connects to is visible to network observers. Since most websites have unique, publicly known IP addresses[^89], an adversary can match your connection destinations against a database of known site IPs and infer which sites you are visiting - without ever touching your DNS traffic. OCSP stapling, ECH, and encrypted DNS do not prevent this.

This is why the guide ultimately recommends Tor, combined with a virtualized multi-layered architecture (see [Virtualization](#virtualization)), as the only realistic mitigation: VPN over Tor hides both DNS queries and IP destinations. Alternative configurations (Tor over VPN, VPN only, no Tor/VPN) are covered later but are less recommended for high-sensitivity use.

### Your RFID enabled devices { #rfid-devices }

RFID stands for Radio-frequency identification[^55], it is the technology used for instance for contactless payments and various identification systems. Of course, your smartphone is among those devices and has RFID contactless payment capabilities through NFC[^56]. As with everything else, such capabilities can be used for tracking by various actors.

But unfortunately, this is not limited to your smartphone, and you also probably carry some amount of RFID enabled device with you all the time such as:

- Your contactless-enabled credit/debit cards
- Your store loyalty cards
- Your transportation payment cards
- Your work-related access cards
- Your car keys
- Your national ID or driver license
- Your passport
- The price/anti-theft tags on object/clothing

While all these cannot be used to de-anonymize you from a remote online adversary, they can be used to narrow down a search if your approximate location at a certain time is known. For instance, you cannot rule out that some stores will effectively scan (and log) all RFID chips passing through the door. They might be looking for their loyalty cards but are also logging others along the way. Such RFID tags could be traced to your identity and allow for de-anonymization.

More information over at Wikipedia: <https://en.wikipedia.org/wiki/Radio-frequency_identification#Security_concerns> <sup>[[Wikiless]](https://wikiless.tiekoetter.com/wiki/Radio-frequency_identification)</sup> <sup>[[Archive.org]](https://web.archive.org/web/https://web.archive.org/web/20220530073225/https://en.wikipedia.org/wiki/Radio-frequency_identification)</sup> and <https://en.wikipedia.org/wiki/Radio-frequency_identification#Privacy> <sup>[[Wikiless]](https://wikiless.tiekoetter.com/wiki/Radio-frequency_identification)</sup> <sup>[[Archive.org]](https://web.archive.org/web/https://web.archive.org/web/20220530073225/https://en.wikipedia.org/wiki/Radio-frequency_identification)</sup>

The only way to mitigate this problem is to have no RFID tags on you or to shield them again using a type of Faraday cage. You could also use specialized wallets/pouches that specifically block RFID communications. Many of those are now made by well-known brands such as Samsonite[^57]. You should just not carry such RFID devices while conducting sensitive activities.

See [Warning about smartphones and smart devices](#smartphones-warning)

### The Wi-Fi and Bluetooth devices around you { #wifi-bluetooth-tracking }

Geolocation is not only done by using mobile antennas triangulation. It is also done using the Wi-Fi and Bluetooth devices around you. Operating systems makers like Google (Android[^58]) and Apple (IOS[^59]) maintain a convenient database of most Wi-Fi access points, Bluetooth devices, and their location. When your Android smartphone or iPhone is on (and not in Plane mode), it will scan actively (unless you specifically disable this feature in the settings) Wi-Fi access points, and Bluetooth devices around you and will be able to geolocate you with more precision than when using a GPS.

This active and continuous probing can then be sent back to Google/Apple/Microsoft as part of their Telemetry. The issue is that this probing is unique and can be used to uniquely identify a user and track such user. Shops, for example, can use this technique to fingerprint customers including when they return, where they go in the shop and how long they stay at a particular place. There are several papers[^60]'[^61] and articles[^62] describing this issue in depth.

This allows them to provide accurate locations even when GPS is off, but it also allows them to keep a convenient record of all Wi-Fi Bluetooth devices all over the world. Which can then be accessed by them or third parties for tracking.

Note: If you have an Android smartphone, Google probably knows where it is no matter what you do. You cannot really trust the settings. The whole operating system is built by a company that wants your data. Remember that if it is free then you are the product.

But that is not what all those Wi-Fi access points can do. Recently developed techs could even allow someone to track your movements accurately just based on radio interferences. What this means is that it is possible to track your movement inside a room/building based on the radio signals passing through. This might seem like a tinfoil hat conspiracy theory claim but here are the references[^63] with demonstrations showing this tech in action: <http://rfpose.csail.mit.edu/> <sup>[[Archive.org]](https://web.archive.org/web/http://rfpose.csail.mit.edu/)</sup> and the video here: <https://www.youtube.com/watch?v=HgDdaMy8KNE> <sup>[[Invidious]](https://yewtu.be/watch?v=HgDdaMy8KNE)</sup>

Other researchers have found a way to count the people in a defined space using only Wi-Fi, see <https://www.news.ucsb.edu/2021/020392/dont-fidget-wifi-will-count-you> <sup>[[Archive.org]](https://web.archive.org/web/https://www.news.ucsb.edu/2021/020392/dont-fidget-wifi-will-count-you)</sup>

You could therefore imagine many use cases for such technologies like recording who enters specific buildings/offices (hotels, hospitals, or embassies for instance) and then discover who meets who and thereby tracking them from outside. Even if they have no smartphone on them.

![](../media/image07.png)

Again, such an issue could only be mitigated by being in a room/building that would act as a Faraday cage.

Here is another video of the same kind of tech in action: <https://www.youtube.com/watch?v=FDZ39h-kCS8> <sup>[[Invidious]](https://yewtu.be/watch?v=FDZ39h-kCS8)</sup>

See: [Warning about smartphones and smart devices](#smartphones-warning).

There is not much you can do about these. Besides being non-identifiable in the first place.

### Rogue Wi-Fi Access Points { #rogue-wifi }

These have been used at least since 2008 using an attack called "Jasager"[^64] and can be done by anyone using self-built tools or using commercially available devices such as Wi-Fi Pineapple[^65].

Here are some videos explaining more about the topic:

- HOPE 2020, <https://archive.org/details/hopeconf2020/20200725_1800_Advanced_Wi-Fi_Hacking_With_%245_Microcontrollers.mp4>

- YouTube, Hak5, Wi-Fi Pineapple Mark VII <https://www.youtube.com/watch?v=7v3JR4Wlw4Q> <sup>[[Invidious]](https://yewtu.be/watch?v=7v3JR4Wlw4Q)</sup>

These devices can fit in a small bag and can take over the Wi-Fi environment of any place within their range. For instance, a Bar/Restaurant/Café/Hotel Lobby. These devices can force Wi-Fi clients to disconnect from their current Wi-Fi (using de-authentication, disassociation attacks[^66]) while spoofing the normal Wi-Fi networks at the same location. They will continue to perform this attack until your computer, or you decide to try to connect to the rogue AP.

These devices can then mimic a captive portal[^67] with the exact same layout as the Wi-Fi you are trying to access (for instance an Airport Wi-Fi registration portal). Or they could just give you unrestricted access internet that they will themselves get from the same place.

Once you are connected through the Rogue AP, this AP will be able to execute various man-in-the-middle attacks to perform analysis on your traffic. These could be malicious redirections or simple traffic sniffing. These can then easily identify any client that would for instance try to connect to a VPN server or the Tor Network.

This can be useful when you know someone you want to de-anonymize is in a crowded place, but you do not know who. This would allow such an adversary to possibly fingerprint any website you visit despite the use of HTTPS, DoT, DoH, ODoH, VPN, or Tor using traffic analysis as pointed above in the DNS section.

These techniques can also be employed to design sophisticated phishing websites aimed at capturing your credentials or persuading you to install a malicious certificate. Such a certificate could enable attackers to intercept and decrypt your encrypted traffic.

How to mitigate those? If you do connect to a public wi-fi access point, use Tor, or use a VPN and then Tor or even VPN over Tor to obfuscate your traffic from the rogue AP while still using it.

In addition, you should see the BlackHat USA conference talk, [Surveilling the Masses with Wi-Fi Positioning Systems](https://www.youtube.com/watch?v=hlbjUvkoyBA) <sup>[[Invidious]](https://yewtu.be/watch?v=hlbjUvkoyBA)</sup>. The talk details a critical vulnerability in the Wi-Fi positioning API by Apple, which can be used to geofence the population using unique identifiers. See: [Warning about smartphones and smart devices](#smartphones-warning). Your neighbors' iPhones are a unique threat, too.

### Traffic Anonymization { #traffic-anonymization }

Tor and VPNs are not silver bullets. Many advanced techniques have been developed and studied to de-anonymize encrypted Tor traffic over the years[^68]. Most of those techniques are Correlation attacks that will correlate your network traffic in one way or another to logs or datasets. Here are some examples:

- **Correlation Fingerprinting Attack:** As illustrated (simplified) below, this attack will fingerprint your encrypted Tor traffic (like the websites you visited) based on the analysis of your encrypted traffic without decrypting it. Some of those methods can do so with a 96% success rate **in a closed-world setting**. **The efficacy of those methods in a real open-world setting** **has not been demonstrated yet and would probably require tremendous resources computing power making it very unlikely that such techniques would be used by a local adversary in the near future.** Such techniques could however hypothetically be used by an advanced and probably global adversary with access to your source network to determine some of your activity. Examples of those attacks are described in several research papers[^69]'[^70]'[^71] as well as their limitations[^72]. The Tor Project itself published an article about these attacks with some mitigations: <https://blog.torproject.org/new-low-cost-traffic-analysis-attacks-mitigations> <sup>[[Archive.org]](https://web.archive.org/web/https://blog.torproject.org/new-low-cost-traffic-analysis-attacks-mitigations)</sup>.

![](../media/image08.png)

- **Correlation Timing Attacks:** As illustrated (simplified) below, an adversary that has access to network connection logs (IP or DNS for instance, remember that most VPN servers and most Tor nodes are known and publicly listed) at the source and the destination could correlate the timings to de-anonymize you without requiring any access to the Tor or VPN network in between. A real use case of this technique was done by the FBI in 2013 to de-anonymize[^73] a bomb threat hoax at Harvard University.

![](../media/image09.png)

- **Correlation Counting Attacks:** As illustrated (simplified) below, an adversary that has no access to detailed connection logs (cannot see that you used Tor or Netflix) but has access to data counting logs could see that you have downloaded 600MB on a specific time/date that matches the 600MB upload at the destination. This correlation can then be used to de-anonymize you over time.

![](../media/image10.png)

There are ways to mitigate these such as:

- Do not use Tor/VPNs to access services that are on the same network (ISP) as the destination service. For example, do not connect to Tor from your University Network to access a University Service anonymously. Instead, use a different source point (such as a public Wi-Fi) that cannot be correlated easily by an adversary.

- Do not use Tor/VPN from an obviously heavily monitored network (such as a corporate/governmental network) but instead try to find an unmonitored network such as a public Wi-Fi or a residential Wi-Fi.

- Consider the use of multiple layers (such as what will be recommended in this guide later: VPN over Tor) so that an adversary might be able to see that someone connected to the service through Tor but will not be able to see that it was you because you were connected to a VPN and not the Tor Network.

Be aware again that this might not be enough against a motivated global adversary[^74] with wide access to global mass surveillance. Such an adversary might have access to logs no matter where you are and could use those to de-anonymize you. Usually, these attacks are part of what is called a Sybil Attack[^75]. **These adversaries are out of the scope of this guide.**

Be also aware that all the other methods described in this guide such as Behavioral analysis can also be used to deanonymize Tor users indirectly (also see [Your Digital Footprint](#digital-footprint).

I also strongly recommend reading this very good, complete, and thorough (and more detailed) guide on most known Attack Vectors on Tor: <https://github.com/Attacks-on-Tor/Attacks-on-Tor> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/Attacks-on-Tor/Attacks-on-Tor)</sup> as well as this recent research publication <https://www.researchgate.net/publication/323627387_Shedding_Light_on_the_Dark_Corners_of_the_Internet_A_Survey_of_Tor_Research> <sup>[[Archive.org]](https://web.archive.org/web/https://www.researchgate.net/publication/323627387_Shedding_Light_on_the_Dark_Corners_of_the_Internet_A_Survey_of_Tor_Research)</sup>

As well as this great series of blog posts: <https://www.hackerfactor.com/blog/index.php?/archives/906-Tor-0day-The-Management-Vulnerability.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.hackerfactor.com/blog/index.php?/archives/906-Tor-0day-The-Management-Vulnerability.html)</sup>

Recently, one of these attacks was attempted on the Tor Network with more information here: <https://arstechnica.com/information-technology/2014/07/active-attack-on-tor-network-tried-to-decloak-users-for-five-months/> <sup>[[Archive.org]](https://web.archive.org/web/https://arstechnica.com/information-technology/2014/07/active-attack-on-tor-network-tried-to-decloak-users-for-five-months/)</sup>

Lastly, do remember that using Tor can already be considered suspicious activity[^76], and its use could be considered malicious by some[^77].

This guide will later propose some mitigations to such attacks by changing your origin from the start (using public wi-fi's for instance). Remember that such attacks are usually carried by highly skilled, highly resourceful, and motivated adversaries and are out of scope from this guide. It is also recommended that you learn about practical correlation attacks, as performed by intelligence agencies: <https://officercia.mirror.xyz/WeAilwJ9V4GIVUkYa7WwBwV2II9dYwpdPTp3fNsPFjo> <sup>[[Archive.org]](https://web.archive.org/web/20220516000616/https://officercia.mirror.xyz/WeAilwJ9V4GIVUkYa7WwBwV2II9dYwpdPTp3fNsPFjo)</sup>

**Disclaimer: it should also be noted that Tor is not designed to protect against a global adversary.**[^550]

### Traffic analysis and the limits of Tor { #traffic-analysis-tor }

**Note: This section expands on the [Traffic Anonymization](#traffic-anonymization) above. What follows is a more detailed treatment of the specific attack classes that matter in practice.**

Tor[^28] provides strong anonymity against most adversaries most of the time. It is not, however, unconditional. Understanding what that means in practice, and who realistically is such an adversary, is more useful than either dismissing the concern or being paralyzed by it.

#### Timing correlation attacks { #timing-correlation }

The foundational attack against anonymity networks is traffic correlation: if an adversary can observe the traffic entering the Tor network from your computer and the traffic exiting toward a destination, they can correlate the two streams by timing, volume, and packet patterns - without ever breaking Tor's encryption.

Murdoch and Danezis demonstrated in 2005[^551] that a relatively low-resource adversary controlling even a small number of Tor nodes could use timing analysis to identify which node a hidden service was using, dramatically narrowing the anonymity set. This was an early result and the Tor network has evolved significantly since, but the underlying principle - that correlation across observation points does not require decrypting anything - has only been confirmed by subsequent research.

**RAPTOR**[^552] (2015) showed that Autonomous System (AS) level adversaries - large ISPs and internet exchanges, not just intelligence agencies - could perform traffic analysis by observing BGP routing and inferring path overlap between a Tor user and their destination. The key insight is that the same AS may carry both the user's traffic to the guard node and the exit node's traffic to the destination, making correlation possible without any Tor node compromise.

**DeepCorr** (2018) used deep learning to correlate Tor flows with significantly higher accuracy than prior methods, achieving correlation rates above 96% in controlled conditions. The authors are careful to note that their evaluation was performed in a closed-world lab setting - a fixed set of websites, controlled conditions - and that real-world performance against a large open network with diverse traffic would be substantially harder. This distinction matters: closed-world accuracy figures are frequently misquoted as if they apply to real-world deployments. They do not, at least not yet.

#### Who is a global passive adversary in practice? { #global-passive-adversary }

A true global passive adversary - one who can observe arbitrary internet traffic worldwide simultaneously - does not exist in the form often imagined. What does exist is a collection of national intelligence agencies with broad but not unlimited visibility into internet traffic (GCHQ's TEMPORA, NSA's PRISM and upstream collection programmes), large ISPs and internet exchanges that carry a disproportionate share of global traffic, and cloud providers whose infrastructure spans most of the world's AS paths.

For the vast majority of Tor users, none of these entities are targeting them specifically. For a journalist communicating with a source inside a country whose intelligence services have close partnerships with major Western agencies, or an activist whose traffic transits only a small number of AS paths, the picture is more concerning. The honest answer is: **if a Five Eyes agency is specifically targeting you, Tor alone is probably not sufficient. For everyone else, Tor provides strong protection.**

#### Website fingerprinting { #website-fingerprinting }

Website fingerprinting attacks attempt to identify which website a Tor user is visiting by analysing the pattern of encrypted traffic - packet sizes, timing, direction sequences - without decrypting it. Accuracy in closed-world evaluations (where the attacker knows the user is visiting one of N monitored sites) has reached high levels in research settings. In open-world conditions, where the user may be visiting any of millions of sites, false positive rates make these attacks far less practical. WTF-PAD and related padding defences, partially deployed in Tor Browser, further degrade fingerprinting accuracy. This is an active research area and the situation will evolve.

#### Guard node persistence and what it means { #guard-node-persistence }

Tor uses **guard nodes** - a small, stable set of entry nodes that your client reuses over weeks - specifically to limit timing correlation exposure. If you used a random entry node for every circuit, an adversary who controls even a modest fraction of Tor nodes would eventually observe you entering the network directly. By persisting a small guard set, Tor limits the probability that any given adversary controls your entry point. The tradeoff is that if your guard node is malicious or observed, it remains so for the duration of the guard period. On balance, the Tor Project's research shows guard persistence improves anonymity for most people most of the time.

#### When Tor is and is not sufficient { #tor-sufficiency }

Tor is sufficient against: local network observers (your ISP, your university, a café Wi-Fi), most law enforcement agencies without intelligence partnerships, commercial data brokers, and advertisers.

Tor is not sufficient against: a targeted operation by a well-resourced national intelligence agency with upstream internet visibility, an adversary who controls both your guard node and the destination's exit node simultaneously, or an adversary who can correlate your Tor usage timing with known real-world events (you were the only person in a particular location at a particular time).

The most practical mitigation beyond Tor itself is changing your entry point: connecting to Tor from public Wi-Fi rather than your home connection removes the most reliable correlation anchor - your ISP-assigned IP - from the equation entirely. This guide recommends this approach for high-sensitivity activities throughout.

### Some Devices can be tracked even when offline { #offline-tracking }

You have seen this in action/spy/Sci-Fi movies and shows, the protagonists always remove the battery of their phones to make sure it cannot be used. Most people would think that's overkill. Well, unfortunately, no, this is now becoming true at least for some devices:

- iPhones and iPads (IOS 13 and above)[^78]'[^79]

- Samsung Phones (Android 10 and above)[^80]

- MacBooks (macOS 10.15 and above)[^81]

Such devices will continue to broadcast identity information to nearby devices even when offline using Bluetooth Low-Energy[^82]. They do not have access to the devices directly (which are not connected to the internet) but instead use BLE to find them through other nearby devices[^83]. They are using peer-to-peer short-range Bluetooth communication to broadcast their status through nearby online devices.

They could now find such devices and keep the location in some database that could then be used by third parties or themselves for various purposes (including analytics, advertising, or evidence/intelligence gathering).

See [Warning about smartphones and smart devices](#smartphones-warning)

TLDR: Do not take such devices with you when conducting sensitive activities.

