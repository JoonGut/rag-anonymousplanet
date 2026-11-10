### Virtualbox on your Host OS { #virtualbox-host }

Remember [Virtualization](#virtualization).

This step and the following steps should be done from within the Host OS. This can either be your Host OS with simple encryption (Windows/Linux/macOS) or your Hidden OS with plausible deniability (Windows only).

In this route, you will make extensive use of the free Oracle Virtualbox[^348] software. This is a virtualization software in which you can create Virtual Machines that emulate a computer running a specific OS (if you want to use something else like Xen, Qemu, KVM, or VMWARE, feel free to do so but this part of the guide covers Virtualbox only for convenience).

So, you should be aware that Virtualbox is not the virtualization software with the best track record in terms of security. Some of the reported issues[^349] have not been completely fixed to date[^350]. If you are using Linux, and you possess a bit more technical skill, you should consider using KVM instead by following the guide available at Whonix here <https://www.whonix.org/wiki/KVM> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/KVM)</sup> and here <z> <sup>[[Archive.org]](https://web.archive.org/web/z)</sup>

Some steps should be taken in all cases:

**All your sensitive activities will be done from within a guest Virtual Machine running Windows 10/11 Pro (not Home this time), Linux, or macOS.**

This has a few advantages that will help you remain anonymous:

- It should prevent the guest VM OS (Windows/Linux/macOS), apps, and any telemetry within the VMs from accessing your hardware directly. Even if your VM is compromised by malware, the malware should not be able to access the Host OS and compromise your actual machine.

- It will allow us to force all the network traffic from your VM to run through another Gateway VM that will direct all the traffic over the Tor Network. This is a network "kill switch". Your VM will lose its network connectivity completely and go offline if the target network VM loses its connection to the Tor Network.

- The VM itself, which only has internet connectivity through a Tor Network Gateway, will connect to your cash-paid VPN service through Tor.

- DNS Leaks will be impossible because the VM is on an isolated network that must go through Tor no matter what.

### Pick your connectivity method { #whonix-connectivity }

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

#### Tor only { #whonix-tor-only }

This is the preferred and most recommended solution.

![image24](../media/image24.png)

With this solution, all your network goes through Tor, and it should be sufficient to guarantee your anonymity in most cases.

There is one main drawback tho: **Some services block/ban Tor Exit nodes outright and will not allow account creations from those.**

To mitigate this, you might have to consider the next option: VPN over Tor but consider some risks associated with it explained in the next section.

#### VPN/Proxy over Tor { #whonix-vpn-over-tor }

This solution can bring some benefits in some specific cases vs using Tor only where accessing the destination service would be impossible from a Tor Exit node. This is because many services will just outright ban, hinder, or block Tor Exit Nodes (see <https://gitlab.torproject.org/legacy/trac/-/wikis/org/doc/ListOfServicesBlockingTor> <sup>[[Archive.org]](https://web.archive.org/web/https://gitlab.torproject.org/legacy/trac/-/wikis/org/doc/ListOfServicesBlockingTor)</sup>).

This solution can be achieved in two ways:

- Paid VPN over Tor (easiest)

- Paid Self-Hosted VPS configured as VPN/Proxy (most efficient in avoiding online obstacles such as captchas but requiring more skills with Linux)

As you can see in this illustration, if your cash (preferred)/Monero paid VPN/Proxy is compromised by an adversary (despite their privacy statement and no-logging policies), they will only find an anonymous cash/Monero paid VPN/Proxy account connecting to their services from a Tor Exit node.

![image25](../media/image25.png)

If an adversary somehow manages to compromise the Tor network too, they will only reveal the IP of a random public Wi-Fi that is not tied to your identity.

If an adversary somehow compromises your VM OS (with malware or an exploit for instance), they will be trapped within the internal Network of Whonix and should be unable to reveal the IP of the public Wi-Fi.

**This solution however has one main drawback to consider: Interference with Tor Stream Isolation**[^351].

Stream isolation is a mitigation technique used to prevent some correlation attacks by having different Tor Circuits for each application. Here is an illustration to show what stream isolation is:

![image26](../media/image26.png)

(Illustration from Marcelo Martins, <https://stakey.club/en/decred-via-tor-network/> <sup>[[Archive.org]](https://web.archive.org/web/https://stakey.club/en/decred-via-tor-network/)</sup>)

VPN/Proxy over Tor falls on the right-side[^352] meaning using a VPN/Proxy over Tor forces Tor to use one circuit for all activities instead of multiple circuits for each. This means that using a VPN/Proxy over Tor can reduce the effectiveness of Tor in some cases and should therefore be used only for some specific cases:

- When your destination service does not allow Tor Exit nodes.

- When you do not mind using a shared Tor circuit for various services. For instance, when using various authenticated services.

**You should however consider not using this method when your aim is just to browse random various unauthenticated websites as you will not benefit from Stream Isolation and this could make correlation attacks easier over time for an adversary between each of your sessions (see [Your Anonymized Tor/VPN traffic](#traffic-anonymization)). If your goal however is to use the same identity at each session on the same authenticated services, the value of Stream isolation is lessened as you can be correlated through other means.**

You should also know that Stream Isolation is not necessarily configured by default on Whonix Workstation. It is only pre-configured for some applications (including Tor Browser).

Also, note that Stream Isolation does not necessarily change all the nodes in your Tor circuit. It can sometimes only change one or two. In many cases, Stream Isolation (for instance within the Tor Browser) will only change the relay (middle) node and the exit node while keeping the same guard (entry) node.

More information at:

- <https://www.whonix.org/wiki/Stream_Isolation> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Stream_Isolation)</sup>

- <https://tails.boum.org/contribute/design/stream_isolation/> <sup>[[Archive.org]](https://web.archive.org/web/https://tails.boum.org/contribute/design/stream_isolation/)</sup>

- <https://www.whonix.org/wiki/Tunnels/Introduction#Comparison_Table> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Tunnels/Introduction#Comparison_Table)</sup>

#### Tor over VPN { #whonix-tor-over-vpn }

You might be wondering: Well, what about using Tor over VPN instead of VPN over Tor? Well, we would not necessarily recommend it:

- Disadvantages:

    - Your VPN provider is just another ISP that will then know your origin IP and will be able to de-anonymize you if required. We do not trust them. We prefer a situation where your VPN provider does not know who you are. It does not add much in terms of anonymity.

    - This would result in you connecting to various services using the IP of a Tor Exit Node which is banned/flagged in many places. It does not help in terms of convenience.

- Advantages:

    - **The main advantage is that if you are in a hostile environment where Tor access is impossible/dangerous/suspicious, but VPN is okay.**

    - This method also does not break Tor Stream isolation.

    - This also hides your Tor activities from your main ISP.

Note, if you are having issues accessing the Tor Network due to blocking/censorship, you could try using Tor Bridges. See [Using Tor bridges in hostile environments](#tor-bridges).

It is also possible to consider **VPN over Tor over VPN (User > VPN > Tor > VPN > Internet)** using two cash/Monero paid VPNs instead. This means that you will connect the Host OS to a first VPN from your Public Wi-Fi, then Whonix will connect to Tor, and finally, your VM will connect to a second VPN over Tor over VPN (see <https://www.whonix.org/wiki/Tunnels/Connecting_to_a_VPN_before_Tor> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Tunnels/Connecting_to_a_VPN_before_Tor)</sup>).

This will of course have a significant performance impact and might be quite slow, but Tor is necessary somewhere for achieving reasonable anonymity.

Achieving this technically is easy within this route, you need two separate anonymous VPN accounts and must connect to the first VPN from the Host OS and follow the route.

Conclusion: Only do this if you think using Tor alone is risky/impossible but VPNs are okay. Or just because you can and so why not. This method will not lower your security/privacy/anonymity.

#### VPN only { #whonix-vpn-only }

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

#### No VPN/Tor { #whonix-no-vpn-tor }

If you cannot use VPN nor Tor where you are, you probably are in a very hostile environment where surveillance and control are extremely high.

Just do not, it is not worth it and too risky. You can be de-anonymized almost instantly by any motivated adversary that could get to your physical location in a matter of minutes.

Do not forget to check back on [Adversaries (threats)](#adversarial-considerations) and [Check your network for surveillance/censorship using OONI](#ooni-censorship-check).

If you have absolutely no other option and still want to do something, see [What about when Tor and VPNs aren't possible?](#tor-vpn-not-possible) **(at your own risk) and consider [the Tails route](#tails-route) instead.**

| Connection Type                    | Anonymity | Ease of Access to online resources | Tor Stream isolation | Safer where Tor is suspicious/dangerous | Speed      | Cost                      | Recommended                                      |
|------------------------------------|-----------|------------------------------------|----------------------|-----------------------------------------|------------|---------------------------|--------------------------------------------------|
| Tor Alone                          | **Good**  | **Medium**                         | **Possible**         | **No**                                  | **Medium** | **Free**                  | **Yes**                                          |
| Tor over VPN                       | **Good+** | **Medium**                         | **Possible**         | **Yes**                                 | **Medium** | **Around 50€/y**          | **If needed (Tor inaccessible)**                 |
| Tor over VPN over Tor              | **Best**  | **Medium**                         | **Possible**         | **Yes**                                 | **Poor**   | **Around 50€/y**          | **Yes**                                          |
| VPN over Tor                       | **Good-** | **Good**                           | **No**               | **No**                                  | **Medium** | **Around 50€/y**          | **If needed (convenience)**                      |
| Self-Hosted VPS VPN/Proxy over Tor | **Good-** | **Very Good**                      | **No**               | **Yes**                                 | **Medium** | **Around 50€/y**          | **If needed (convenience)**                      |
| VPN/Proxy over Tor over VPN        | **Good-** | **Good**                           | **No**               | **Yes**                                 | **Poor**   | **Around 100€/y**         | **If needed (convenience and Tor inaccessible)** |
| VPN/Proxy Alone                    | **Bad**   | **Good**                           | **N/A**              | **Yes**                                 | **Good**   | **Around 50€/y**          | **No.**                                          |
| No Tor and VPN                     | **Bad**   | **Unknown**                        | **N/A**              | **No**                                  | **Good**   | **Around 100€ (Antenna)** | **No.**                                          |

Unfortunately, using Tor alone will raise the suspicion of many destinations' platforms. You will face many hurdles (captchas, errors, difficulties signing up) if you only use Tor. In addition, using Tor where you are could put you in trouble just for that. But Tor is still the best solution for anonymity and must be somewhere for anonymity.

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

### Getting an anonymous VPN/Proxy { #whonix-anon-vpn }

**Skip this step if you want to use Tor only.**

See [Getting an anonymous VPN/Proxy](#anonymous-vpn-proxy)

### Whonix { #whonix }

**Skip this step if you cannot use Tor.**

This route will use Virtualization and Whonix[^353] as part of the anonymization process. Whonix is a Linux distribution composed of two Virtual Machines:

- The Whonix Workstation (this is a VM where you can conduct sensitive activities)

- The Whonix Gateway (this VM will establish a connection to the Tor network and route all the network traffic from the Workstation through the Tor network).

This guide will therefore propose two flavors of this route:

- The Whonix only route where all traffic is routed through the Tor Network (Tor Only or Tor over VPN).

![image27](../media/image27.png)

- A Whonix hybrid route where all traffic is routed through a cash (preferred)/Monero paid VPN over the Tor Network (VPN over Tor or VPN over Tor over VPN).

![image28](../media/image28.png)

You will be able to decide which flavor to use based on my recommendations. We recommend the second one as explained before.

Whonix is well maintained and has extensive and incredibly detailed documentation.

#### A note on Virtualbox Snapshots { #virtualbox-snapshots }

Later, you will create and run several Virtual Machines within Virtualbox for your sensitive activities. Virtualbox provides a feature called "Snapshots"[^354] that allow for saving the state of a VM at any point in time. If for any reason later you want to go back to that state, you can restore that snapshot at any moment.

**I strongly recommend that you do make use of this feature by creating a snapshot after the initial installation/update of each VM. This snapshot should be done before its use for any sensitive/anonymous activity.**

This will allow you to turn your VMs into a kind of disposable "Live Operating Systems" (like Tails discussed earlier). Meaning that you will be able to erase all the traces of your activities within a VM by restoring a Snapshot to an earlier state. Of course, this will not be "as good" as Tails (where everything is stored in memory) as there might be traces of this activity left on your hard disk. Forensics studies have shown the ability to recover data from a reverted VM[^355]. Fortunately, there will be ways to remove those traces after the deletion or reverting to an earlier snapshot. Such techniques will be discussed in the [Some additional measures against forensics](#anti-forensics) section of this guide.

#### Download Virtualbox and Whonix utilities { #download-virtualbox-whonix }

You should download a few things within the host OS:

- The latest version of the Virtualbox installer according to your Host OS <https://www.virtualbox.org/wiki/Downloads> <sup>[[Archive.org]](https://web.archive.org/web/https://www.virtualbox.org/wiki/Downloads)</sup>

- (Skip this if you cannot use Tor natively or through a VPN) The latest stable **Whonix 18.x** OVA from:
    - [GitHub Releases](https://github.com/Whonix/whonix-gw-ga/releases/latest) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Download/VirtualBox)</sup>
    - Or the official download mirror: <https://download.whonix.org/> (XFCE Desktop recommended for beginners)
- (Optional) The [Whonix Text Client](https://www.whonix.org/wiki/Install#Text_Client_Version) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Install)</sup> is available for advanced users who prefer a minimal setup.

**Note on Whonix 18.x**: As of guide v1.2.5, Whonix has been upgraded from version 17 to 18 (Whonix 18.1.4.x). See [[Upgrading to Whonix 18]](#qubes-whonix18) for the upgrade path if you currently use Whonix 17.x.

This will conclude the preparations and you should now be ready to start setting up the final environment that will protect your anonymity online.

#### Virtualbox Hardening (Whonix 17.x & 18.x) { #virtualbox-hardening }

For ideal security, follow the [Whonix Hardening Guide](https://www.whonix.org/wiki/Virtualization_Platform_Security#VirtualBox_Hardening) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Virtualization_Platform_Security)</sup> with these additional notes:

**Recommended Settings (apply to all VMs):**
- Disable Audio
- Do not enable Shared Folders
- Disable 2D acceleration: `VBoxManage modifyvm "vm-name" --accelerate2dvideo off`
- Disable 3D acceleration
- Disable Serial Port
- Remove Floppy and CD/DVD drives (or set to non-functional)
- Disable Remote Display server
- Enable PAE/NX for security features
- Disable ACPI

**Network Time Desync:**
Desync VM clocks to prevent synchronization attacks (see [[Whonix Documentation - Network Time Synchronization]](https://www.whonix.org/wiki/Network_Time_Synchronization) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Network_Time_Synchronization)</sup>):

    ```sh
    # Example offsets (choose different values for each VM)
    VBoxManage modifyvm "Whonix-Gateway-XFCE" --biossystemtimeoffset -35017
    VBoxManage modifyvm "Whonix-Workstation-XFCE" --biossystemtimeoffset +27931
    ```

**Spectre/Meltdown Mitigations:** (optional, may impact performance)
For detailed Spectre/Meltdown hardening, see <https://www.whonix.org/wiki/Spectre_Meltdown> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Spectre_Meltdown)</sup>.

**Additional Security:** (Whonix 18.x+)
- Consider enabling AppArmor on Whonix Workstation: <https://www.whonix.org/wiki/AppArmor> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/AppArmor)</sup>
- Review [DoNot](https://www.whonix.org/wiki/DoNot) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/DoNot)</sup> recommendations

- Disable the USB controller which is enabled by default. Set the Pointing Device to "PS/2 Mouse" or changes will revert.

Finally, also follow this recommendation to desync the clock you are your VM compared to your host OS <https://www.whonix.org/wiki/Network_Time_Synchronization#Spoof_the_Initial_Virtual_Hardware_Clock_Offset> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Network_Time_Synchronization)</sup>

This offset should be within a 60000-millisecond range and should be different for each VM and here are some examples (which can be later applied to any VM):

- ```VBoxManage modifyvm "Whonix-Gateway-XFCE" --biossystemtimeoffset -35017```

- ```VBoxManage modifyvm "Whonix-Gateway-XFCE" --biossystemtimeoffset +27931```

- ```VBoxManage modifyvm "Whonix-Workstation-XFCE" --biossystemtimeoffset -35017```

- ```VBoxManage modifyvm "Whonix-Workstation-XFCE" --biossystemtimeoffset +27931```

Also, consider applying these mitigations from VirtualBox to mitigate Spectre[^356]/Meltdown[^357] vulnerabilities by running this command from the VirtualBox Program Directory. All of these are described here: <https://www.whonix.org/wiki/Spectre_Meltdown> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Spectre_Meltdown)</sup> (be aware these can impact severely the performance of your VMs but should be done for best security).

Finally, consider the security advice from Virtualbox themselves here <https://www.virtualbox.org/manual/ch13.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.virtualbox.org/manual/ch13.html)</sup>

### Tor over VPN { #whonix-setup-tor-over-vpn }

**Skip this step if you do not intend to use Tor over VPN and only intend to use Tor or cannot.**

If you intend to use Tor over VPN for any reason. You first must configure a VPN service on your host OS.

Remember that in this case, we recommend having two VPN accounts. Both paid with cash/Monero (see [Getting an anonymous VPN/Proxy](#anonymous-vpn-proxy)). One will be used in the Host OS for the first VPN connection. The other could be used in the VM to achieve VPN over Tor over VPN (User > VPN > Tor > VPN).

If you intend to only use Tor over VPN, you only need one VPN account.

See [Installing a VPN on your VM or Host OS](#vpn-installation) for instructions.

### Whonix Virtual Machines { #whonix-vms }

**Skip this step if you cannot use Tor.**

- Start Virtualbox on your Host OS.

- Import Whonix OVA into Virtualbox: See [VirtualBox/XFCE](https://www.whonix.org/wiki/VirtualBox/XFCE) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/VirtualBox/XFCE)</sup>
    - You can also use the Text Client version for advanced users

- Start the Whonix VMs

Remember at this stage that if you are having issues connecting to Tor due to censorship or blocking, you should consider connecting using Bridges as explained in [Bridges](https://www.whonix.org/wiki/Bridges) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Bridges)</sup>.

- Update the Whonix VMs by following the instructions on [Operating System Software and Updates](https://www.whonix.org/wiki/Operating_System_Software_and_Updates#Updates) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Operating_System_Software_and_Updates)</sup>

**Note:** For Qubes OS users, see the [[Upgrading to Whonix 18]](#qubes-whonix18) section for migration notes.

- Shutdown the Whonix VMs

- Take a snapshot of the updated Whonix VMs within Virtualbox (select a VM and click the Take Snapshot button). More on that later.

- Go to the next step

**Important Note: You should also read these very good recommendations over there <https://www.whonix.org/wiki/DoNot>** <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/DoNot)</sup> **as most of those principles will also apply to this guide. You should also read their general documentation here <https://www.whonix.org/wiki/Documentation>** <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Documentation)</sup> **which will also provide tons of advice like this guide.**

### Whonix 18.x Improvements and Best Practices { #whonix-18-improvements }

**Key Changes in Whonix 18.x:**
- Automated Release Upgrade process for seamless version transitions from Whonix 17.x
- Improved AppArmor integration for enhanced application sandboxing on Debian-based systems
- Enhanced network configuration with better Tor connectivity options
- Updated security hardening guides with current best practices
- Better Qubes OS integration and compatibility

**Best Practices for Whonix 18.x Users:**

1. **Always take a snapshot** before applying any system updates or configuration changes
2. **Verify system integrity** after upgrades using `sudo checkvm` commands
3. **Review the DoNot page** regularly to stay informed about security best practices
4. **Keep your Whonix VMs updated** using the automated upgrade process when available
5. **Consider KVM instead of VirtualBox**

**For Qubes OS Users:**
Qubes R4.2+ with Whonix 18 is supported. Always verify system integrity after upgrade using `systemcheck`. For detailed migration instructions, see the [[Upgrading to Whonix 18]](#qubes-whonix18) section.

