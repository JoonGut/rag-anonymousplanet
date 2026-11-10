## The Qubes Route { #qubes-route }

**Note that the guide has been updated to Qubes OS 4.1**

As they say on their website, Qubes OS is a reasonably secure, free, open-source, and security-oriented operating system for single-user desktop computing. Qubes OS leverages and extensively uses Xen-based virtualization to allow for the creation and management of isolated compartments called Qubes.

Qubes OS is not a Linux distribution[^362] but a Xen distribution. It is different from Linux distributions because it will make extensive use of Virtualization and Compartmentalization so that any app will run in a different VM (Qube). As a bonus, Qubes OS integrates Whonix by default and allows for increased privacy and anonymity. It is highly recommended that you document yourself over Qubes OS principles before going this route. Here are some recommended resources:

- Qubes OS Introduction, <https://www.qubes-os.org/intro/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.qubes-os.org/intro/)</sup>

- Qubes OS Video Tours, <https://www.qubes-os.org/video-tours/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.qubes-os.org/video-tours/)</sup>

- Qubes OS Getting Started, <https://www.qubes-os.org/doc/getting-started/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.qubes-os.org/doc/getting-started/)</sup>

- YouTube, Life Behind the Tinfoil: A Look at Qubes and Copperhead - Konstantin Ryabitsev, The Linux Foundation <https://www.youtube.com/watch?v=8cU4hQg6GvU> <sup>[[Invidious]](https://yewtu.be/watch?v=8cU4hQg6GvU)</sup>

- YouTube, We used the reasonably-secure Qubes OS for 6 months and survived - Matty McFatty [@themattymcfatty] <https://www.youtube.com/watch?v=sbN5Bz3v-uA> <sup>[[Invidious]](https://yewtu.be/watch?v=sbN5Bz3v-uA)</sup>

- YouTube, Qubes OS: How it works, and a demo of this VM-centric OS <https://www.youtube.com/watch?v=YPAvoFsvSbg> <sup>[[Invidious]](https://yewtu.be/watch?v=YPAvoFsvSbg)</sup>

This OS is recommended by prominent figures such as Edward Snowden, PrivacyGuides.org.

Qubes is the best option in this guide for people who are more comfortable with Linux and tech in general. But it has some downsides such as the lack of OS-wide plausible deniability, its hardware requirements, and its hardware compatibility. While you can run this on 4GB of RAM as per their requirements <sup>[[Archive.org]](https://yewtu.be/watch?v=sbN5Bz3v-uA)</sup>, the recommended RAM is 16GB. We would recommend against using Qubes OS if you have less than 8GB of RAM. If you want a comfortable experience, you should have 16GB, if you want a particularly enjoyable experience, you should have 24GB or 32GB.

The reason for this RAM requirement is that each app will run in a different VM and each of those VM will require and allocate a certain amount of memory that will not be available for other apps. If you are running native Windows apps within Qubes OS Qubes, the ram overhead will be significant.

You should also check their hardware compatibility here <https://www.qubes-os.org/hcl/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.qubes-os.org/hcl/)</sup> before proceeding. Your mileage might vary, and you might experience several issues about hardware compatibility that you will have to troubleshoot and solve yourself.

I think that if you can afford it and are comfortable with the idea of using Linux, you should go with this route as it is probably the best one in terms of security and privacy. The only disadvantage of this route is that it does not provide a way to enable OS-wide [plausible deniability](https://en.wikipedia.org/wiki/Plausible_deniability) <https://en.wikipedia.org/wiki/Plausible_deniability> <sup>[[Wikiless]](https://wikiless.tiekoetter.com/wiki/Plausible_deniability)</sup>, unlike the Whonix route.

### Pick your connectivity method { #qubes-connectivity }

There are seven possibilities within this route:

- **Recommended and preferred:**

    - **Use Tor alone (User > Tor > Internet)**

    - **Use VPN over Tor (User > Tor > VPN > Internet) in specific cases**

    - **Use a VPS with a self-hosted VPN/Proxy over Tor (User > Tor > Self-Hosted VPN/Proxy > Internet) in specific cases**

- Possible if required by context:

    - Use VPN over Tor over VPN (User > VPN > Tor > VPN > Internet)

    - Use Tor over VPN (User > VPN > Tor > Internet)

- Not recommended and risky:

    - Use VPN alone (User > VPN > Internet)

    - Use VPN over VPN (User > VPN > VPN > Internet)

- **Not recommended and highly risky (but possible)**

    - No VPN and no Tor (User > Internet)

![image23](../media/image23.png)

#### Tor only { #qubes-tor-only }

This is the preferred and most recommended solution.

![image32](../media/image32.png)

With this solution, all your network goes through Tor, and it should be sufficient to guarantee your anonymity in most cases.

There is one main drawback tho: **Some services block/ban Tor Exit nodes outright and will not allow account creations from those.**

To mitigate this, you might have to consider the next option: VPN over Tor but consider some risks associated with it explained in the next section.

#### VPN/Proxy over Tor { #qubes-vpn-over-tor }

This solution can bring some benefits in some specific cases vs using Tor only where accessing the destination service would be impossible from a Tor Exit node. This is because many services will just outright ban, hinder, or block Tor Exit Nodes (see <https://gitlab.torproject.org/legacy/trac/-/wikis/org/doc/ListOfServicesBlockingTor> <sup>[[Archive.org]](https://web.archive.org/web/https://gitlab.torproject.org/legacy/trac/-/wikis/org/doc/ListOfServicesBlockingTor)</sup>).

This solution can be achieved in two ways:

- Paid VPN over Tor (easiest)

- Paid Self-Hosted VPS configured as VPN/Proxy (most efficient in avoiding online obstacles such as captchas but requiring more skills with Linux)

As you can see in this illustration, if your cash (preferred)/Monero paid VPN/Proxy is compromised by an adversary (despite their privacy statement and no-logging policies), they will only find an anonymous cash/Monero paid VPN account connecting to their services from a Tor Exit node.

![image33](../media/image33.png)

If an adversary somehow manages to compromise the Tor network too, they will only reveal the IP of a random public Wi-Fi that is not tied to your identity.

If an adversary somehow compromises your VM OS (with malware or an exploit for instance), they will be trapped within the internal Network of Whonix and should be unable to reveal the IP of the public Wi-Fi.

**This solution however has one main drawback to consider: Interference with Tor Stream Isolation**[^364].

Stream isolation is a mitigation technique used to prevent some correlation attacks by having different Tor Circuits for each application. Here is an illustration to show what stream isolation is:

![image26](../media/image26.png)

(Illustration from Marcelo Martins, <https://stakey.club/en/decred-via-tor-network/> <sup>[[Archive.org]](https://web.archive.org/web/https://stakey.club/en/decred-via-tor-network/)</sup>)

VPN/Proxy over Tor falls on the right-side[^365] meaning using a VPN/Proxy over Tor forces Tor to use one circuit for all activities instead of multiple circuits for each. This means that using a VPN/Proxy over Tor can reduce the effectiveness of Tor in some cases and should therefore be used only for some specific cases:

- When your destination service does not allow Tor Exit nodes.

- When you do not mind using a shared Tor circuit for various services. For instance for using various authenticated services.

**You should however consider not using this method when your aim is just to browse random various unauthenticated websites as you will not benefit from Stream Isolation and this could make correlation attacks easier for an adversary between each of your sessions (see [Your Anonymized Tor/VPN traffic](#traffic-anonymization)).**

More information at:

- <https://www.whonix.org/wiki/Stream_Isolation> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Stream_Isolation)</sup>

- <https://tails.boum.org/contribute/design/stream_isolation/> <sup>[[Archive.org]](https://web.archive.org/web/https://tails.boum.org/contribute/design/stream_isolation/)</sup>

- <https://www.whonix.org/wiki/Tunnels/Introduction#Comparison_Table> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Tunnels/Introduction#Comparison_Table)</sup>

#### Tor over VPN { #qubes-tor-over-vpn }

You might be wondering: Well, what about using Tor over VPN instead of VPN over Tor?

- Disadvantages

    - Your VPN provider is just another ISP that will then know your origin IP and will be able to de-anonymize you if needed. We do not trust them. Prefer a situation where your VPN provider does not know who you are. It does not add much in terms of anonymity.

    - This would result in you connecting to various services using the IP of a Tor Exit Node which is banned/flagged in many places. It does not help in terms of convenience.

- Advantages:

    - **The main advantage is that if you are in a hostile environment where Tor access is impossible/dangerous/suspicious, but VPN is okay.**

    - This method also does not break Tor Stream isolation.

Note, if you're having issues accessing the Tor Network due to blocking/censorship, you could try using Tor Bridges (see Tor Documentation <https://2019.www.torproject.org/docs/bridges> <sup>[[Archive.org]](https://web.archive.org/web/https://2019.www.torproject.org/docs/bridges)</sup> and Whonix Documentation <https://www.whonix.org/wiki/Bridges> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Bridges)</sup>).

It is also possible to consider **VPN over Tor over VPN (User > VPN > Tor > VPN > Internet)** using two cash/Monero paid VPNs instead. This means that you will connect the Host OS to a first VPN from your Public Wi-Fi, then Whonix will connect to Tor, and finally, your VM will connect to a second VPN over Tor over VPN (see <https://www.whonix.org/wiki/Tunnels/Connecting_to_a_VPN_before_Tor> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Tunnels/Connecting_to_a_VPN_before_Tor)</sup>).

This will of course have a significant performance impact and might be quite slow, but Tor is necessary somewhere for achieving reasonable anonymity.

Achieving this technically is easy within this route, you need two separate anonymous VPN accounts and must connect to the first VPN from the Host OS and follow the route.

Conclusion: Only do this if you think using Tor alone is risky/impossible but VPNs are okay. Or just because you can and so why not. This method will not lower your security/privacy/anonymity.

#### VPN only { #qubes-vpn-only }

This route will not be explained nor recommended.

**If you can use VPNs then you should be able to add a Tor layer over it. And if you can use Tor, then you can add an anonymous VPN over Tor to get the preferred solution.**

Just using a VPN or even a VPN over VPN makes no sense as those can be traced back to you over time. One of the VPN providers will know your real origin IP (even if it is in a safe public space) and even if you add one over it, the second one will still know you were using that other first VPN service. This will only slightly delay your de-anonymization. Yes, it is an added layer ... but it is a persistent centralized added layer, and you can be de-anonymized over time. This is just chaining 3 ISPs that are all subject to lawful requests.

For more info, please see the following references:

- <https://www.whonix.org/wiki/Comparison_Of_Tor_with_CGI_Proxies,_Proxy_Chains,_and_VPN_Services#Tor_and_VPN_Services_Comparison> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Comparison_Of_Tor_with_CGI_Proxies,_Proxy_Chains,_and_VPN_Services)</sup>

- <https://www.whonix.org/wiki/Why_does_Whonix_use_Tor> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Why_does_Whonix_use_Tor)</sup>

- <https://www.researchgate.net/publication/324251041_Anonymity_communication_VPN_and_Tor_a_comparative_study> <sup>[[Archive.org]](https://web.archive.org/web/https://www.researchgate.net/publication/324251041_Anonymity_communication_VPN_and_Tor_a_comparative_study)</sup>

- <https://gist.github.com/joepie91/5a9909939e6ce7d09e29#file-vpn-md> <sup>[[Archive.org]](https://web.archive.org/web/https://gist.github.com/joepie91/5a9909939e6ce7d09e29)</sup>

- <https://schub.wtf/blog/2019/04/08/very-precarious-narrative.html> <sup>[[Archive.org]](https://web.archive.org/web/https://schub.wtf/blog/2019/04/08/very-precarious-narrative.html)</sup>

**In the context of this guide, Tor is required somewhere to achieve reasonable and safe anonymity and you should use it if you can.**

#### No VPN/Tor { #qubes-no-vpn-tor }

If you cannot use VPN nor Tor where you are, you probably are in a very hostile environment where surveillance and control are extremely high.

Just do not, it is not worth it and too risky. You can be de-anonymized almost instantly by any motivated adversary that could get to your physical location in a matter of minutes.

Do not forget to check back on [Adversaries (threats)](#adversarial-considerations) and [Check your network for surveillance/censorship using OONI](#ooni-censorship-check).

If you have absolutely no other option and still want to do something, see [What about when Tor and VPNs aren't possible?](#tor-vpn-not-possible) **(at your own risk)**

| Connection Type                    | Anonymity | Ease of Access to online resources | Tor Stream isolation | Safer where Tor is suspicious/dangerous | Speed      | Cost                      | Recommended                                      |
|------------------------------------|-----------|------------------------------------|----------------------|-----------------------------------------|------------|---------------------------|--------------------------------------------------|
| Tor Alone                          | **Good**  | **Medium**                         | **Possible**         | **No**                                  | **Medium** | **Free**                  | **Yes**                                          |
| Tor over VPN                       | **Good+** | **Medium**                         | **Possible**         | **Yes**                                 | **Medium** | **Around 50€/y**          | **If needed (Tor inaccessible)**                 |
| Tor over VPN over Tor              | **Best**  | **Medium**                         | **Possible**         | **Yes**                                 | **Poor**   | **Around 50€/y**          | **Yes**                                          |
| VPN over Tor                       | **Good-** | **Good**                           | **No**               | **No**                                  | **Medium** | **Around 50€/y**          | **If needed (convenience)**                      |
| Self-Hosted VPS VPN/Proxy over Tor | **Good-** | **Very Good**                      | **No**               | **No**                                  | **Medium** | **Around 50€/y**          | **If needed (convenience)**                      |
| VPN/Proxy over Tor over VPN        | **Good-** | **Good**                           | **No**               | **Yes**                                 | **Poor**   | **Around 100€/y**         | **If needed (convenience and Tor inaccessible)** |
| VPN/Proxy Alone                    | **Bad**   | **Good**                           | **N/A**              | **Yes**                                 | **Good**   | **Around 50€/y**          | **No**                                           |
| No Tor and VPN                     | **Bad**   | **Unknown**                        | **N/A**              | **No**                                  | **Good**   | **Around 100€ (Antenna)** | **No. At your own risk.**                        |

Unfortunately, using Tor alone will raise the suspicion of many destinations' platforms. You will face many hurdles (captchas, errors, difficulties signing up) if you only use Tor. In addition, using Tor where you are could put you in trouble just for that. But Tor remains the best solution for anonymity and must be somewhere for anonymity.

- If you intend to create persistent shared and authenticated identities on various services where access from Tor is hard, we recommend the **VPN over Tor** and **VPS VPN/Proxy over Tor** options (or VPN over Tor over VPN if needed). It might be a bit less secure against correlation attacks due to breaking Tor Stream isolation but provides much better convenience in accessing online resources than just using Tor. It is an "acceptable" trade-off IMHP if you are careful enough with your identity.

    - **Note: It is becoming more common that mainstream services and CDNS are also blocking or hindering VPN users with captchas and other various obstacles**. **In that case, a self-hosted VPS with a VPN/Proxy over Tor is the best solution for this as having your own dedicated VPS guarantees you are the sole user of your IP and encounter little to no obstacles.** Consider a [Self-hosted VPN/Proxy on a Monero/Cash-paid VPS (for users more familiar with Linux)](#anonymous-self-hosted) if you want the least amount of issues (this will be explained in the next section in more details).

- If your intent however is just to browse random services anonymously without creating specific shared identities, using tor friendly services; or if you do not want to accept that trade-off in the earlier option. **Then we recommend using the Tor Only route to keep the full benefits of Stream Isolation (or Tor over VPN if you need to).**

- If cost is an issue, we recommend the Tor Only option if possible.

- If both Tor and VPN access are impossible or dangerous then you have no choice but to rely on Public wi-fi safely. See [What about when Tor and VPNs aren't possible?](#tor-vpn-not-possible)

For more information, you can also see the discussions here that could help decide yourself:

- Tor Project: <https://gitlab.torproject.org/legacy/trac/-/wikis/doc/TorPlusVPN> <sup>[[Archive.org]](https://web.archive.org/web/https://gitlab.torproject.org/legacy/trac/-/wikis/doc/TorPlusVPN)</sup>

- Tails Documentation:

    - <https://gitlab.tails.boum.org/tails/blueprints/-/wikis/vpn_support/> <sup>[[Archive.org]](https://web.archive.org/web/https://gitlab.tails.boum.org/tails/blueprints/-/wikis/vpn_support/)</sup>

    - <https://tails.boum.org/support/faq/index.en.html#index20h2> <sup>[[Archive.org]](https://web.archive.org/web/https://tails.boum.org/support/faq/index.en.html)</sup>

- Whonix Documentation (in this order):

    - <https://www.whonix.org/wiki/Tunnels/Introduction> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Tunnels/Introduction)</sup>

    - <https://www.whonix.org/wiki/Tunnels/Connecting_to_Tor_before_a_VPN> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Tunnels/Connecting_to_Tor_before_a_VPN)</sup>

    - <https://www.whonix.org/wiki/Tunnels/Connecting_to_a_VPN_before_Tor> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Tunnels/Connecting_to_a_VPN_before_Tor)</sup>

- Some papers on the matter:

    - <https://www.researchgate.net/publication/324251041_Anonymity_communication_VPN_and_Tor_a_comparative_study> <sup>[[Archive.org]](https://web.archive.org/web/https://www.researchgate.net/publication/324251041_Anonymity_communication_VPN_and_Tor_a_comparative_study)</sup>

### Getting an anonymous VPN/Proxy { #qubes-anon-vpn }

**Skip this step if you want to use Tor only or VPN is not an option.**

See [Getting an anonymous VPN/Proxy](#anonymous-vpn-proxy)

### Note about Plausible Deniability { #qubes-deniability }

Qubes OS uses LUKS for full disk encryption and it is technically possible to achieve a form of deniability by using detached LUKS headers. This is not yet integrated into this guide but you will find an evolving tutorial on how to achieve this here: <https://forum.qubes-os.org/t/qubes-os-installation-detached-encrypted-boot-and-header/6205> and some more background information within the Linux Host OS section (see [Note about plausible deniability on Linux]).

### Installation { #qubes-install }

You will follow the instructions from their own guide <https://www.qubes-os.org/doc/installation-guide/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.qubes-os.org/doc/installation-guide/)</sup>:

(Secure Boot is not supported as per their FAQ: <https://www.qubes-os.org/faq/#is-secure-boot-supported> <sup>[[Archive.org]](https://web.archive.org/web/https://www.qubes-os.org/faq/)</sup> so it should be disabled in the BIOS/UEFI settings.)

- Download the latest Qubes OS 4.1.x installation ISO according to their hardware compatibility list.

- Get and verify the Qubes OS Master Signing key: <https://keys.qubes-os.org/keys/qubes-master-signing-key.asc>

- Prepare a USB key with the Qubes OS ISO file

- Install Qubes OS according to the installation guide:

    - **If you want to use Tor or VPN over Tor: Check the** "**Enabling system and template updates over the Tor anonymity network using Whonix" during the last step. This will force all Qubes OS updates to go through Tor. While this will significantly reduce your update speed, it will increase your anonymity from the start.** (If you are having issues connecting to Tor due to censorship or blocking, consider using Tor Bridges as recommended earlier. Just follow the tutorial provided here: <https://www.whonix.org/wiki/Bridges> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Bridges)</sup>)

    - If you want to use Tor over VPN or cannot use any of those, leave it unchecked.

    - Be absolutely sure that you are verifying the signature of the ISO, which you can find on this page: <https://www.qubes-os.org/security/verifying-signatures/> <sup>[[Archive.org]](https://web.archive.org/web/20220511015546/https://www.qubes-os.org/security/verifying-signatures/)</sup>. Check by obtaining the fingerprint from multiple independent sources in several different ways as recommended. This is to ensure the image has not been tampered with. Do not skip this vital step even though you know you are getting the ISO from a trusted source, because it's possible for the Qubes website to be compromised.

- If you are prevented from using Tor, there is no point in installing the Whonix VM templates. You can disable Whonix installation during the post-installation, initial setup wizard.

To be sure your Qubes ISO hasn't been tampered with, you should get the Qubes master key fingerprint from multiple different sources. This guide can be used as one source.

The Qubes master signing key fingerprint should match `427F 11FD 0FAA 4B08 0123  F01C DDFA 1A3E 3687 9494`.

_Remember to read the guide to verifying signatures on the Qubes website: <https://www.qubes-os.org/security/verifying-signatures/> <sup>[[Archive.org]](https://web.archive.org/web/20220511015546/https://www.qubes-os.org/security/verifying-signatures/)</sup>._

### Lid Closure Behavior { #qubes-lid-closure }

Unfortunately, Qubes OS does not support hibernation[^366] which is an issue regarding cold-boot attacks. To mitigate those, I highly recommend that you configure Qubes OS to shut down on any power action (power button, lid closure). You can do set this from the XFCE Power Manager. Do not use the sleep features.

### Anti Evil Maid (AEM) { #qubes-aem }

**Warning**, this step only works with Intel CPUs, a legacy BIOS, TPM 1.2. If you do not meet those requirements, skip this step.

Anti Evil Maid is an implementation of a TPM-based static trusted boot with a primary goal to prevent Evil Maid attacks. Installing and using AEM requires attaching a USB drive directly to dom0. So the user must make a choice between protecting dom0 from a potentially malicious USB drive, and protecting the system from Evil Maid attacks. Note that AEM is only compatible with Intel CPUs and Legacy boot options.

The preference for mitigating any evil maid attack is to maintain physical control of your device at all times. If that is not possible, then this might be relevant to your threat model.

Before deciding to use this system, please read [Important notes about evil-maid and tampering](#evil-maid-tampering-notes)

See the following links for more details and installation instructions:

- <https://www.qubes-os.org/doc/anti-evil-maid/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.qubes-os.org/doc/anti-evil-maid/)</sup>

- <https://blog.invisiblethings.org/2011/09/07/anti-evil-maid.html> <sup>[[Archive.org]](https://web.archive.org/web/https://blog.invisiblethings.org/2011/09/07/anti-evil-maid.html)</sup>

- <https://github.com/QubesOS/qubes-antievilmaid> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/QubesOS/qubes-antievilmaid)</sup>

### Connect to a Public Wi-Fi { #qubes-wifi }

Remember this should be done from a safe place (see [Find some safe places with decent public Wi-Fi](#safe-wifi) and [Using long-range Antenna to connect to Public Wi-Fis from a safe distance](#long-range-wifi):

- In the upper right corner, Left-click the network icon and note the Wi-Fi SSID you want to connect to

- Now right-click the network icon and select Edit Connections

- Add one using the + sign

- Select Wi-Fi

- Enter the SSID of the desired network you noted before (if needed)

- Select Cloned Mac Address

- Select Random to randomize your Mac Address

    - **Warning: This setting should work in most cases but can be unreliable on some network adapters. Please refer to this documentation if you want to be sure: <https://github.com/Qubes-Community/Contents/blob/master/docs/privacy/anonymizing-your-mac-address.md>** <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/Qubes-Community/Contents/blob/master/docs/privacy/anonymizing-your-mac-address.md)</sup>

- Save

- Now again Left-click the connection account and connect to the desired Wi-Fi

- If this is an Open Wi-Fi requiring registration: You will have to start a browser to register

    - After you are connected, Start a Disposable Fedora Firefox Browser

    - Go into the upper left Menu

    - Select Disposable, Fedora, Firefox

    - Open Firefox and register (anonymously) into the Wi-Fi

### Upgrading Qubes OS from 4.0.x to 4.1.x (you should do it) { #qubes-upgrade }

Personally, we wouldn't do it in-place and do a fresh install.

But if you really want to, it's technically possible by following this guide: <https://www.qubes-os.org/doc/upgrade/4.1/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.qubes-os.org/doc/upgrade/4.1/)</sup>

### Updating Qubes OS { #qubes-updates }

After you are connected to a Wi-Fi you need to update Qubes OS and Whonix. You must keep Qubes OS always updated before conducting any sensitive activities. Especially your Browser VMs. Normally, Qubes OS will warn you about updates in the upper right corner with a gear icon. As this might take a while in this case due to using Tor, you can force the process by doing the following:

- Click the upper left Applications icon

- Select Qubes Tools

- Select Qubes Update

- Check the "Enable updates for Qubes without known available updates"

- Select all the Qubes

- Click Next and wait for updates to complete

- If you checked the Tor option during install, be patient as this might take a while over Tor

### Upgrade to Whonix 18 { #qubes-whonix18 }

**Overview of Whonix 18.x Improvements:**

- Automated Release Upgrade process (no manual intervention required)
- Improved AppArmor integration for better application sandboxing
- Enhanced network configuration and Tor connectivity
- Updated documentation across all sections
- Better Qubes OS compatibility (now officially supported on R4.3+)

**To upgrade Whonix 17 to Whonix 18:**

1. **Backup all data** - Clone the VMs before upgrading using Virtualbox snapshots or your preferred method.

1. **Upgrade your Qubes host first:**
    - Ensure you're running at least Qubes R4.2 (for Whonix 17 compatibility)
    - Update to Qubes R4.3+ if possible (recommended for Whonix 18 support)

1. **Run standard updates per OS instructions on your templates:**

    ```sh
    sudo unattended-upgrade --auto-run
    ```

1. **Execute the automated upgrade:**

    ```sh
    sudo release-upgrade
    ```

    - This will handle the upgrade automatically without requiring user input.

1. **Reboot VMs and run** `systemcheck` **to verify system integrity after the upgrade:**

    ```sh
    sudo checkvm --all
    sudo tor --verify
    ```

1. **For Qubes, update APT repo sources post-upgrade (optional later).**

**Important Notes:**

- **Qubes R4.2+ with Whonix 18 is now officially supported**. See <https://www.whonix.org/wiki/Release_Upgrade_17_to_18> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Release_Upgrade_17_to_18)</sup> for detailed instructions.
- Always verify system integrity after upgrade using `systemcheck` and Tor verification tools.
- If you're not using Qubes OS, follow the general [Whonix Upgrade Guide](https://www.whonix.org/wiki/Release_Upgrade_17_to_18) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Release_Upgrade_17_to_18)</sup>.

### Hardening Qubes OS { #qubes-hardening }

**Disclaimer: This section is under construction and will be worked on heavily in the next releases. This section is for more advanced users.**

#### Application Sandboxing { #qubes-sandboxing }

While Qubes OS is already sandboxing everything by design, it is also useful to consider sandboxing apps themselves using AppArmor or SELinux.

##### AppArmor { #qubes-apparmor }

"AppArmor is a Mandatory Access Control framework. When enabled, AppArmor confines programs according to a set of rules that specify what files a given program can access. This initiative-taking approach helps protect the system against both known and unknown vulnerabilities" (Debian.org).

Basically, AppArmor[^367] is an application sandboxing system. By default, it is not enabled but supported by Qubes OS.

- About the Fedora VMs:

    - Fedora does not use AppArmor but rather SELinux so see the next section for that.

- About the Debian VMs:

    - Head out and read <https://wiki.debian.org/AppArmor> <sup>[[Archive.org]](https://web.archive.org/web/https://wiki.debian.org/AppArmor)</sup>

- About any other Linux VM:

    - Head out and read:

        + <https://wiki.archlinux.org/title/AppArmor> <sup>[[Archive.org]](https://web.archive.org/web/https://wiki.archlinux.org/title/AppArmor)</sup>

        + <https://wiki.debian.org/AppArmor> <sup>[[Archive.org]](https://web.archive.org/web/https://wiki.debian.org/AppArmor)</sup>

- About the Whonix VMs, you should consider enabling and using AppArmor, especially on the Whonix VMs of Qubes OS:

    - First, you should head out and read <https://www.whonix.org/wiki/AppArmor> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/AppArmor)</sup>

    - Secondly, you should head out again and read <https://www.whonix.org/wiki/Qubes/AppArmor> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Qubes/AppArmor)</sup>

##### SELinux { #qubes-selinux }

SELinux[^368] is similar to AppArmor. The differences between SELinux and AppArmor are technical details into which we will not get.

Here is a good explanation of what it is: <https://www.youtube.com/watch?v=_WOKRaM-HI4> <sup>[[Invidious]](https://yewtu.be/watch?v=_WOKRaM-HI4)</sup>

In this guide and the context of Qubes OS, it is important to mention it as it is the recommended method by Fedora which is one of the default systems on Qubes OS.

So, head out and read <https://docs.fedoraproject.org/en-US/quick-docs/getting-started-with-selinux/> <sup>[[Archive.org]](https://web.archive.org/web/https://docs.fedoraproject.org/en-US/quick-docs/getting-started-with-selinux/)</sup>

You could make use of SELinux on your Fedora Templates. But this is up to you. Again, this is for advanced users.

### Setup the VPN ProxyVM { #qubes-vpn-proxyvm }

**Skip this step if you do not want to use a VPN and just use Tor only or if VPN is not an option either.**

This tutorial should also work with any OpenVPN provider (Mullvad, IVPN, Safing.io, or Proton VPN for instance).

This is based on the tutorial provided by Qubes OS themselves (<https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/vpn.md> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/vpn.md)</sup>). If you are familiar with this process, you can follow their tutorial.

Alternatively, Mullvad also have a help article that guides you through setting up a Proxy VM <https://mullvad.net/en/help/qubes-os-4-and-mullvad-vpn/> <sup>[[Archive.org]](https://web.archive.org/web/https://mullvad.net/en/help/qubes-os-4-and-mullvad-vpn/)</sup>.

#### Create the ProxyVM { #qubes-create-proxyvm }

- Click the Applications icon (upper left corner)

- Click Create Qubes VM

- Name and label as you wish: I suggest "VPNGatewayVM"

- Select Type: Standalone Qube copied from a template

- Select Template: Debian-11 (the default)

- Select Networking:

    - Select sys-whonix if you want to do VPN over Tor / Tor only (recommended)

    - Select sys-firewall if you want to do Tor over VPN / No Tor or VPN / Just VPN

- Advanced: Check provides network

- Check "Start Qube automatically on boot"

- Create the VM

    - If you are going for VPN over Tor, you need to go into the settings of the ProxyVM you made and select "sys-vpn" for networking.
        + An easier way to setup your ProxyVM is to simply run a VPN client on the ProxyVM.
        + Usually when you connect to your VPN provider's website, it'll tell you whether your traffic is being properly routed through the VPN.

    - If you are going for Tor over VPN, the opposite should be done, the ProxyVM should have its networking set as "sys-tor" and the "sys-tor" VM should have "sys-vpn" for its networking.
        + Test the VM connectivity to the internet by launching a Browser within the ProxyVM. Visit <https://check.torproject.org> <sup>[[Archive.org]](https://web.archive.org/web/https://check.torproject.org/)</sup> (It should say you are connected to Tor)

#### Download the VPN configuration from your cash/Monero paid VPN provider { #qubes-vpn-config-download }

##### If you can use Tor { #qubes-vpn-tor }

**Using Tor Browser (be careful not to use any Clearnet Browser for this),** download the necessary OpenVPN configuration files for Linux from your VPN provider.

This can be done by using the Qubes OS integrated Tor Browser by accessing the Applications icon (upper left corner) and selecting the Disposable Tor Browser application.

##### If you cannot use Tor { #qubes-vpn-no-tor }

Launch a browser from a DisposableVM and download the necessary OpenVPN configuration files for Linux from your VPN provider. See [What about when Tor and VPNs aren't possible?](#tor-vpn-not-possible)

When you are done downloading the configuration files within the Disposable Browser (usually a zip file), copy them to your ProxyVM VPN Gateway machine (using right-click on the file and send to another AppVM).

#### Configure the ProxyVM { #qubes-configure-proxyvm }

**Skip this step if you are not going to use a VPN**

- Click the upper left corner

- Select the VPN VM you just created

- Open the Files of the VPN VM

- Go into "Qubesincoming" > dispXXXX (This was your Disposable Browser VM)

- Double Click your downloaded zip file containing your OpenVPN configuration files to unzip it

- Now select the VPN VM again and start a terminal

- Install OpenVPN with the following command ```sudo apt-get install openvpn```

- Copy all the OpenVPN configuration files provided by your VPN provider in /etc/openvpn/

- For all the OpenVPN configuration files (for each location):

    - Edit each file using ```sudo nano configfile``` (do not forget sudo to edit the file within /etc)

    - Change the protocol from "udp" to "tcp" (Tor does not support UDP)

    - Change the port to a supported (by your VPN provider) TCP port (like 80 or 443)

    - Save and exit each file

- Edit the OpenVPN config file (/etc/default/openvpn) by typing ```sudo nano /etc/default/openvpn```

    - Change ```#AUTOSTART="all"``` to ```AUTOSTART="all"``` (in other words, remove the "#")

    - Save and Exit

- Edit the Qubes firewall rules file (/rw/config/qubes-firewall-user-script) by typing "sudo nano /rw/config/qubes-firewall-user-script"

    - Add the following lines (without the quotes and remarks in parentheses)

        + ```virtualif=10.137.0.17```

> (This is the IP of the ProxyVM, this is not dynamic, and you might need to change it at reboot)

- ```vpndns1=10.8.0.1```

> (This is the first DNS server of your VPN provider; it should not change)

- ```vpndns2=10.14.0.1```

> (This is the second DNS server of your VPN provider; it should not change)

- ```iptables -F OUTPUT```

- ```iptables -I FORWARD -o eth0 -j DROP```

- ```iptables -I FORWARD -i eth0 -j DROP```

- ```ip6tables -I FORWARD -o eth0 -j DROP```

- ```ip6tables -I FORWARD -i eth0 -j DROP```

> (These will block outbound traffic when the VPN is down, it is a kill switch, more information here <https://linuxconfig.org/how-to-create-a-vpn-killswitch-using-iptables-on-linux> <sup>[[Archive.org]](https://web.archive.org/web/https://linuxconfig.org/how-to-create-a-vpn-killswitch-using-iptables-on-linux)</sup> )

- ```iptables -A OUTPUT -d 10.8.0.1 -j ACCEPT```

- ```iptables -A OUTPUT -d 10.14.0.1 -j ACCEPT```

> (These will allow DNS requests to your VPN provider DNS to resolve the name of the VPN servers in the OpenVPN configuration files)

- ```iptables -F PR-QBS -t nat```

- ```iptables -A PR-QBS -t nat -d $virtualif -p udp --dport 53 -j DNAT --to $vpndns1```

- ```iptables -A PR-QBS -t nat -d $virtualif -p tcp --dport 53 -j DNAT --to $vpndns1```

- ```iptables -A PR-QBS -t nat -d $virtualif -p udp --dport 53 -j DNAT --to $vpndns2```

- ```iptables -A PR-QBS -t nat -d $virtualif -p tcp --dport 53 -j DNAT --to $vpndns2```

> (These will redirect all DNS requests from the ProxyVM to the VPN provider DNS servers)

- Restart the ProxyVM by typing "sudo reboot"

- Test the ProxyVM VPN connectivity by starting a Browser within it and going to your VPN provider test page. It should now say you are connected to a VPN:

    - Mullvad: <https://mullvad.net/en/check/> <sup>[[Archive.org]](https://web.archive.org/web/https://mullvad.net/en/check/)</sup>

    - IVPN: <https://www.ivpn.net/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.ivpn.net/)</sup> (check the top banner)

    - Proton VPN: Follow their instructions here <https://protonvpn.com/support/vpn-ip-change/> <sup>[[Archive.org]](https://web.archive.org/web/https://protonvpn.com/support/vpn-ip-change/)</sup>

#### VPN over Tor { #qubes-vpn-over-tor-setup }

##### Set up a disposable Browser Qube for VPN over Tor use { #qubes-browser-qube }

- Within the Applications Menu (upper left corner), Select the Disposable Fedora VM

- Go into Qube Settings

- Click Clone Qube and name it like "sys-VPNoverTor" for example

- Again, within the Application Menu, Select the Clone you just created

- Go into Qube Settings

- Change the Networking to your ProxyVPN created earlier

- Click OK

- Start a Browser within the Whonix Workstation

- Check that you have VPN connectivity, and it should work

You should now have a Disposable Browser VM that works with your cash/Monero paid VPN over Tor.

#### Tor Over VPN { #qubes-tor-over-vpn-setup }

Reconfigure your Whonix Gateway VM to use your ProxyVM as NetVM instead of sys-firewall:

- Within the Applications Menu (upper left corner), Select the sys-whonix VM.

- Go into Qube Settings

- Change the Networking NetVM to your ProxyVPN created earlier instead of sys-firewall

- Click OK

- Create a Whonix Workstation Disposable VM (follow this tutorial <https://www.whonix.org/wiki/Qubes/DisposableVM> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Qubes/DisposableVM)</sup>)

- Launch a browser from the VM and Check that you have VPN connectivity, and it should work.

Alternatively, you can also create any other type of disposable VM (but less secure than the Whonix one):

- Within the Applications Menu (upper left corner), Select the Disposable Fedora VM

- Go into Qube Settings

- Click Clone Qube and name it like "sys-TorOverVPN" for example

- Again, within the Application Menu, Select the Clone you just created

- Go into Qube Settings

- Change the Networking to your sys-whonix created earlier

- Click OK

- Start a Browser within the VM

- Check that you have VPN connectivity, and it should work

You should now have a Disposable Browser VM that works with Tor over a cash/Monero paid VPN.

#### Any other combination? { #qubes-other-combo }

**E.g., VPN over Tor over VPN**

By now you should understand how easy it is to route traffic from one VM to the other with Qubes.

You can create several ProxyVMs for VPN accesses and keep the Whonix one for Tor. You just need to change the NetVM settings of the various VMs to change the layout.

You could have:

- One VPN ProxyVM for the base Qubes OS connection

- Use the sys-whonix VM (Whonix Gateway) getting its network from the first ProxyVM

- A second VPN ProxyVM getting network from sys-whonix

- Disposable VMs getting their NetVM from the second ProxyVM

This would result in User > VPN > Tor > VPN > Internet (VPN over Tor over VPN). Experiment for yourself. Qubes OS is great for these things.

### Setup a safe Browser within Qubes OS { #qubes-safe-browser }

See: [What browser to use in your Guest VM/Disposable VM](#guest-vm-browser-choice)

#### Fedora Disposable VM { #qubes-fedora-vm }

Within the Applications Menu (upper left), Select the Fedora-36 template:

- Go into Qube Settings

- Clone the VM and name it "fedora-36-brave" (this VM template will have Brave)

- Again, go into the Applications Menu and select the clone you just created

- Go into Qube Settings

- Change its network to the ProxyVPN and Apply

- Launch a terminal from the VM

If you want to use Brave: apply the instructions from [their documentation](https://brave.com/linux/) <sup>[[Archive.org]](https://web.archive.org/web/https://brave.com/linux/)</sup> and run the following commands:

```sudo dnf install dnf-plugins-core```

```sudo dnf config-manager --add-repo https://brave-browser-rpm-release.s3.brave.com/x86_64/```

```sudo rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc```

```sudo dnf install brave-browser```

You should also consider hardening your browser, see [Hardening your Browsers](#hardening-browsers)

#### Whonix Disposable VM { #qubes-whonix-vm }

Edit the Whonix Disposable VM template and follow instructions here <https://www.whonix.org/wiki/Install_Software> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Install_Software)</sup>

#### Additional browser precautions { #qubes-browser-precautions }

- See: [Hardening your Browsers](#hardening-browsers)

- See: [Additional browser precautions with JavaScript enabled](#browser-precautions-js)

### Setup an Android VM { #qubes-android-vm }

Because sometimes you want to run mobile Apps anonymously too. You can also set up an Android VM for this purpose. As in other cases, ideally, this VM will also be sitting behind the Whonix Gateway for Tor network connectivity. But this can also be set up as VPN over Tor over VPN.

Since the Android-x86 does not work "well" with Qubes OS (my own experience). We will instead recommend using AnBox (<https://anbox.io/> <sup>[[Archive.org]](https://web.archive.org/web/https://anbox.io/)</sup>) which works "well enough" with Qubes OS. More information can also be found at <https://www.whonix.org/wiki/Anbox> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Anbox)</sup>

#### If you can use Tor { #qubes-android-tor }

Later in the Qubes settings during creation:

- Select Networking

- Change to sys-whonix to put it behind the Whonix Gateway (over Tor).

#### If you cannot use Tor { #qubes-android-no-tor }

Just use the tutorials as is. See [What about when Tor and VPNs aren't possible?](#tor-vpn-not-possible).

**Installation**

Basically, follow the tutorial here:

- Click the Applications icon (upper left corner)

- Click Create Qubes VM

- Name and label as you wish: we suggest "Android"

- Select Type: Standalone Qube copied from a template

- Select Template: Debian-11

- Select Networking:

    - Select sys-whonix if you want to do VPN over Tor / Tor only (recommended)

    - Select sys-firewall if you want to do Tor over VPN / No Tor or VPN / Just VPN

- Start the Qube and open a Terminal

Now you will have to follow the instructions from here: <https://github.com/anbox/anbox-modules> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/anbox/anbox-modules)</sup>:

- Start by closing the AnBox Modules repository by running:

    - ```git clone https://github.com/anbox/anbox-modules.git```

    - Go into the cloned directory

    - Run ```./INSTALL.sh``` (or follow the manual instructions on the tutorial)

- Reboot the machine

- Open a new terminal

- Install Snap by running:

    - ```sudo apt install snapd```

Now you will follow their other tutorial from here: <https://github.com/anbox/anbox/blob/master/docs/install.md> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/anbox/anbox/blob/master/docs/install.md)</sup>:

- Install AnBox by running:

    - ```snap install --devmode --beta anbox```

- To update AnBox later, run:

    - ```snap refresh --beta --devmode anbox```

- Reboot the machine

- Open a terminal again and start the emulator by running:

    - ```anbox.appmgr```

This should pop up an Android interface. Sometimes it will crash, and you might have to run it twice to make it work.

If you want to install apps on this emulator:

- Install ADB by running:

    - ```sudo apt install android-tools-adb```

- First start Anbox (run ```anbox.appmgr```)

- Grab the APK of any app you want to install

- Now install any APK by running:

    - ```adb install my-app.apk```

That's it, you should now have an Android Qube over Tor (or anything else) capable of running pretty much any App you can sideload with ADB. This is, for now, the easiest way to get Android emulation on Qubes OS.

### KeePassXC { #qubes-keepassxc }

You will need somewhere to store your data (logins/passwords, identities, and TOTP[^369] information).

For this purpose, KeePassXC is recommended because of its integrated TOTP feature. This is the ability to create entries for 2FA[^370] authentication with the authenticator feature.

In the context of Qubes OS you should store your sensitive information within the vault Qube:

- First, click the Applications icon (upper left) and select the vault Qube.

- Click Qubes Settings

- Select the Applications tab

- From the list of available applications, add KeePassXC to the list of selected applications.

You are done and can now skip the rest to go to the "[Creating your anonymous online identities](#creating-identities)" part.

### Tutorial for installing Windows based VMs on Qubes OS { #qubes-windows-vm-tutorial }

See their tutorial here: <https://github.com/Qubes-Community/Contents/blob/master/docs/os/windows/windows-tools41.md> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/Qubes-Community/Contents/blob/master/docs/os/windows/windows-tools41.md)</sup>

