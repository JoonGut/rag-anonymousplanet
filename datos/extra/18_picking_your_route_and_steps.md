# General Preparations { #general-preparations }

Personally, in the context of this guide, it is also interesting to have a look at your security model. And in this context,we only have one to recommend:

Zero-Trust Security[^391] ("Never trust, always verify").

Here are some various resources about what Zero-Trust Security is:

- DEFCON, Zero Trust a Vision for Securing Cloud, <https://www.youtube.com/watch?v=euSsqXO53GY> <sup>[[Invidious]](https://yewtu.be/watch?v=euSsqXO53GY)</sup>

- From the NSA themselves, Embracing a Zero Trust Security Model, <https://media.defense.gov/2021/Feb/25/2002588479/-1/-1/0/CSI_EMBRACING_ZT_SECURITY_MODEL_UOO115131-21.PDF> <sup>[[Archive.org]](https://web.archive.org/web/https://media.defense.gov/2021/Feb/25/2002588479/-1/-1/0/CSI_EMBRACING_ZT_SECURITY_MODEL_UOO115131-21.PDF)</sup>

## Picking your route { #picking-route }

First, here is a small basic UML diagram showing your available options according to your skills/budget/time/resources.

![image18](../media/image18.png)

### Timing limitations { #timing-limitations }

- You have no time at all:

    - **Go for the Tor Browser route.**

- You have extremely limited time to learn and need a fast-working solution:

    - **Your best option is to go for [the Tails route](#tails-route) (excluding the persistent plausible deniability section).**

- You have time and more importantly motivation to learn:

    - **Go with any route.**

### Budget & Material limitations { #budget-limitations }

- You have no budget and even accessing a laptop is complicated or you only have your smartphone:

    - **Go for the Tor Browser route.**

- You only have one laptop available and cannot afford anything else. You use this laptop for either work, family, or your personal stuff (or both):

    - **Your best option is to go for [the Tails route](#tails-route).**

- You can afford a spare dedicated unsupervised/unmonitored laptop for your sensitive activities:

    - But it is old, slow, and has bad specs (less than 6GB of RAM, less than 250GB disk space, old/slow CPU):

        + **You should go for [the Tails route](#tails-route).**

    - It is not that old, and it has decent specs (at least 8GB of RAM, 250GB of disk space or more, decent CPU):

        + **You could go for Tails, Whonix routes.**

    - It is new and it has great specs (more than 16GB or ideally 32GB of RAM, >250GB of disk space, recent fast CPU):

        + **You could go for any route, but we would recommend Qubes OS if your threat model allows it. Please see the requirements.[^363]**

    - If it is an ARM-based M1/M2 Mac:

        + **Not possible currently for these reasons:**

            * Virtualization of Intel x86 images on ARM (M1/M2) hosts is still limited to commercial software (e.g., Parallels, Fusion) which are mostly not supported by Whonix, yet. They are very buggy and for advanced people only. Please seek this information yourself.

            * [Virtualbox is now available natively for ARM64 architecture](https://osxdaily.com/2022/10/22/you-can-now-run-virtualbox-on-apple-silicon-m1-m2/) in a package as of October 2022. Download the ["Developer preview for macOS/Arm64 (M1/M2) hosts"](https://www.virtualbox.org/wiki/Downloads).

            * Whonix does not support macOS easily. "You need to build Whonix using the build script to get it running on Apple Silicon." [See the forum thread](https://www.whonix.org/wiki/MacOS#M1).

            * Tails is not supported on ARM64 architecture yet. [See this thread](https://gitlab.tails.boum.org/tails/blueprints/-/wikis/ARM_platforms/) for more information (keep in mind this page hasn't been updated recently).

            * Qubes OS is not supported on ARM64 architecture yet, but there is work being done to make it available on aarch64, which may be delayed for the unforseeable future..

**The general advice in this guide regarding virtualization software is that it's costly. That said, you should probably get a dedicated laptop, capable of running virtualization software, preferably a 64-bit architecture, to be used for more sensitive activities and testing.**

### Skills { #skills }

- Do you have no IT skills at all the content of this guide look like an alien language to you? Consider:

    - **The Tor Browser route (simplest of all)**

    - **[The Tails route](#tails-route) (excluding the persistent plausible deniability section).**

- You have some IT skills and mostly understand this guide so far, consider:

    - **The Tails route (with the optional persistent plausible deniability section).**

    - **The Whonix route.**

- You have moderate to high IT skills, and you are already familiar with some of the content of this guide, consider:

    - **Any route (Qubes OS is preferred if you can afford it).**

- You are an l33T hacker, "there is no spoon", "the cake is a lie", you have been using "doas" for years, and "all your base is belong to us", and you have strong opinions on systemd.

    - **This guide is not meant for you and will not help you with your HardenedBSD on your hardened Libreboot laptop ;-)**

### Adversarial considerations { #adversarial-considerations }

Now that you know what is possible, you should also consider threats and adversaries before picking the right route.

#### Threats { #threats }

- If your main concern is a forensic examination of your devices, you should consider the Tor Browser route or [the Tails route](#tails-route).

- If your main concerns are remote adversaries that might uncover your online identity on various platforms, you should consider the Tails, Whonix, or Qubes OS routes (listed in order of difficulty).

- If you want system-wide plausible deniability[^311]'[^294] despite the risks[^295]'[^314], consider the Tails route, including the persistent plausible deniability section (see [Persistent Plausible Deniability using Whonix & Tails](#whonix-tails-deniability)).**

- If you are in a hostile environment where Tor/VPN usage alone is impossible/dangerous/suspicious, consider the Tails route (without actually using Tor), or more advanced routes like Whonix or Qubes OS.

#### Adversaries { #adversaries }

- Low skills:

    - Low resources:

        + Any motivation: Any Route

    - Medium resources:

        + Low to Medium motivation: Any Route

        + High motivation: TAILS, Whonix, Qubes OS Routes

    - High resources:

        + Low motivation: Any route

        + Medium to High motivation: TAILS, Whonix, Qubes OS Routes

- Intermediate skills:

    - Low resources:

        + Low motivation: Any Route

        + Medium to High motivation: TAILS, Whonix, Qubes OS Routes

    - Medium resources:

        + Low motivation: Any Route

        + Medium to High motivation: TAILS, Whonix, Qubes OS Routes

    - High resources:

        + Low to High motivation: TAILS, Whonix, Qubes OS Routes

- Highly skilled:

    - Low resources:

        + Low motivation: Any Route

        + Medium to High motivation: TAILS, Whonix, Qubes OS Routes

    - Medium resources:

        + Low to High motivation: TAILS, Whonix, Qubes OS Routes

    - High resources:

        + Low to High motivations: TAILS, Whonix, Qubes OS Routes **(but likely out of scope from this guide as this is probably a global adversary)**

In all cases, you should read these two pages from the Whonix documentation that will give you in-depth insight into your choices:

- [Warning](https://www.whonix.org/wiki/Warning) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Warning)</sup>
- [Dev/Threat Model](https://www.whonix.org/wiki/Dev/Threat_Model) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Dev/Threat_Model)</sup>
- [Comparison with Others](https://www.whonix.org/wiki/Comparison_with_Others) <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Comparison_with_Others)</sup>

You might be asking yourself: "How do I know if I'm in a hostile online environment where activities are actively monitored and blocked?"

- First read more about it at the EFF here: <https://ssd.eff.org/en/module/understanding-and-circumventing-network-censorship> <sup>[[Archive.org]](https://web.archive.org/web/https://ssd.eff.org/en/module/understanding-and-circumventing-network-censorship)</sup>

- Check some data yourself here on the Tor Project OONI[^296] (Open Observatory of Network Interference) website: <https://explorer.ooni.org/>

- Have a look at <https://censoredplanet.org/> and see if they have data about your country.

- Specific to China, look at <https://gfwatch.org/> and <https://www.usenix.org/system/files/sec21-hoang.pdf> <sup>[[Archive.org]](https://web.archive.org/web/https://www.usenix.org/system/files/sec21-hoang.pdf)</sup>

- Test for yourself using OONI (this can be risky in a hostile environment).

## Steps for all routes { #steps-all-routes }

### Getting used to using better passwords { #better-passwords }

See [Guidelines for passwords and passphrases](#password-guidelines).

### Getting an anonymous Phone number { #anonymous-phone }

**Skip this step if you have no intention of creating anonymous accounts on most mainstream platforms but just want anonymous browsing or if the platforms you will use allow registration without a phone number.**

#### Physical Burner Phone and prepaid SIM card { #burner-phone }

##### Get a burner phone { #get-burner-phone }

This is rather easy. Leave your smartphone on and at home. Have some cash and go to some random flea market or small shop (ideally one without CCTV inside or outside and while avoiding being photographed/filmed) and just buy the cheapest phone you can find with cash and without providing any personal information. It only needs to be in working order.

_A note regarding your current phone:_ The point of leaving your smartphone on is to create avoid leaking the fact that you're not using the device. If a smartphone is turned off, this creates a metadata trail that can be used to correlate the time your smartphone was turned off with the activation of your burner. If possible, leave your phone doing something (for example, watching YouTube on auto-play) to obscure the metadata trail further. This will not make it impossible to correlate your inactivity, but may make it more difficult if your phone's usage patterns can look convincing while you buy your burner.

We would recommend getting an old "dumbphone" with a removable battery (old Nokia if your mobile networks still allow those to connect as some countries phased out 1G-2G completely). This is to avoid the automatic sending/gathering of any telemetry/diagnostic data on the phone itself. You should never connect that phone to any Wi-Fi.

**Site Note: Be careful of some sellers as shown here <https://therecord.media/malware-found-preinstalled-in-classic-push-button-phones-sold-in-russia>** <sup>[[Archive.org]](https://therecord.media/malware-found-preinstalled-in-classic-push-button-phones-sold-in-russia)</sup>

It will also be crucial not to power on that burner phone ever (not even without the SIM card) in any geographical location that could lead to you (at your home/work for instance) and never at the same location as your other known smartphone (because that one has an IMEI/IMSI that will easily lead to you). This might seem like a big burden, but it is not as these phones are only being used during the setup/sign-up process and for verification from time to time.

See [Warning about smartphones and smart devices](#smartphones-warning)

You should test that the phone is in working order before going to the next step. But we will repeat ourselves and state that it is important to leave your smartphone at home when going (or turn it off before leaving if you must keep it) and that you test the phone at a random location that cannot be tracked back to you (and again, do not do that in front of a CCTV, avoid cameras, be aware of your surroundings). No need for Wi-Fi at this place either.

When you are certain the phone is in working order, disable Bluetooth then power it off (remove the battery if you can) and go back home and resume your normal activities. Go to the next step.

##### Getting an anonymous pre-paid SIM card { #prepaid-sim }

This is the hardest part of the whole guide. It is a SPOF (Single Point of Failure). The places where you can still buy prepaid SIM cards without ID registration are getting increasingly limited due to various KYC type regulations[^297].

So here is a list of places where you can still get them now: <https://prepaid-data-sim-card.fandom.com/wiki/Registration_Policies_Per_Country> <sup>[[Archive.org]](https://web.archive.org/web/https://prepaid-data-sim-card.fandom.com/wiki/Registration_Policies_Per_Country)</sup>

You should be able to find a place that is "not too far" and just go there physically to buy some pre-paid cards and top-up vouchers with cash. Do verify that no law was passed before going that would make registration mandatory (in case the above wiki was not updated). Try to avoid CCTV and cameras and do not forget to buy a Top-Up voucher with the SIM card (if it is not a package) as most pre-paid cards will require a top-up before use.

See [Warning about smartphones and smart devices](#smartphones-warning)

Double-check that the mobile operators selling the pre-paid SIM cards will accept the SIM activation and top-up without any ID registration of any kind before going there. Ideally, they should accept SIM activation and top-up from the country you live in.

We would recommend GiffGaff in the UK as they are "affordable", do not require identification for activation and top-up, and will even allow you to change your number up to two times from their website. One GiffGaff prepaid SIM card will therefore grant you three numbers to use for your needs.

Power off the phone after activation/top-up and before going home. Do not ever power it on again unless you are not at a place that can be used to reveal your identity and ideally leave your real phone on but at home before going to the safe place with only your burner phone.

#### Online Phone Number { #online-phone-number }

**DISCLAIMER: Do not attempt this until you are done setting up a secure environment according to one of the selected routes. This step will require online access and should only be done from an anonymous network. Do not do this from any known/unsecured environment. Skip this until you have finished one of the routes.**

There are many commercial services offering numbers to receive SMS messages online but most of those have no anonymity/privacy and can be of no help as most Social Media platforms place a limit on how many times a phone number can be used for registration.

There are some forums and subreddits (like r/phoneverification/) where users will offer the service of receiving such SMS messages for you for a small fee (using PayPal or some crypto payment). Unfortunately, these are full of scammers and very risky in terms of anonymity. **You should not use those under any circumstance.**

To this date, we do not know any reputable service that would offer this service and accept cash payments (by post for instance) like some VPN providers. But a few services are providing online phone numbers and do accept Monero which could be reasonably anonymous (yet less recommended than that physical way in the earlier chapter) that you could consider:

- **Recommended**: No name, no e-mail, and no KYC:

    - (Iceland based, accepts Monero) <https://crypton.sh> <sup>[[Tor Mirror]](http://cryptonx6nsmspsnpicuihgmbbz3qvro4na35od3eht4vojdo7glm6yd.onion)</sup> <sup>[[Archive.org]](https://web.archive.org/web/https://crypton.sh/)</sup>

    - (Ukraine based, accepts Monero) <https://virtualsim.net/> <sup>[[Archive.org]](https://web.archive.org/web/https://virtualsim.net/)</sup>

    - (180+ countries, accepts crypto) <https://cypheresim.com/esim-with-number> <sup>[[Archive.org]](https://web.archive.org/web/https://cypheresim.com/esim-with-number)</sup>

- Require valid e-mail:

    - (US California based, accepts Monero) <https://mobilesms.io> <sup>[[Archive.org]](https://web.archive.org/web/https://mobilesms.io/)</sup>

    - (Germany based, accepts Monero) <https://www.sms77.io/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.sms77.io/)</sup>

    - (Russia based, accepts Monero) <https://onlinesim.ru/> <sup>[[Archive.org]](https://web.archive.org/web/https://onlinesim.ru/)</sup>

There are some other possibilities listed here <https://cryptwerk.com/companies/sms/xmr/> <sup>[[Archive.org]](https://web.archive.org/web/https://cryptwerk.com/companies/sms/xmr/)</sup>. **Use at your own risk.**

Now, what if you have no money? Well, in that case, you will have to try your luck with free services and hope for the best. Here are some examples, **use at your own risk**:

- <https://oksms.org>

- <https://smspva.com>

- <https://sms24.me>

**Disclaimer: We cannot vouch for any of these providers. We recommend doing it yourself physically. In this case, you will have to rely on the anonymity of Monero and you should not use any service that requires any kind of identification using your real identity. Please do read [Monero Disclaimer](#monero-disclaimer).**

It is more convenient, cheaper, and less risky to just get a pre-paid SIM card from one of the physical places that still sell them for cash without ID.

### Get a USB key { #usb-key }

**Skip this step if you have no intention of creating anonymous accounts on most mainstream platforms, but you will want anonymous browsing; or if the platforms which you will use allow registration without a phone number.**

Get at least one or two decent size generic USB keys (at least 16GB but we would recommend 32GB).

Please do not buy or use gimmicky self-encrypting devices such as these: <https://syscall.eu/blog/2018/03/12/aigo_part1/> <sup>[[Archive.org]](https://web.archive.org/web/https://syscall.eu/blog/2018/03/12/aigo_part1/)</sup>

Some might be very efficient[^298] but many are gimmicky gadgets that offer no real protection[^299].

### Find some safe places with decent public Wi-Fi { #safe-wifi }

You need to find safe places where you will be able to do your sensitive activities using some publicly accessible Wi-Fi (without any account/ID registration, avoid CCTVs).

This can be anywhere that will not be tied to you directly (your home/work) and where you can use the Wi-Fi for a while without being bothered. But also, a place where you can do this without being "noticed" by anyone.

If you think Starbucks is a clever idea, you may reconsider:

- They probably have CCTVs in all their shops and keep those recordings for an unknown amount of time.

- You will need to buy a coffee to get the Wi-Fi access code in most. If you pay for this coffee with an electronic method, they will be able to tie your Wi-Fi access with your identity.

Situational awareness is key, and you should be constantly aware of your surroundings and avoid touristy places like it was plagued by Ebola. You want to avoid appearing on any picture/video of anyone while someone is taking a selfie, making a TikTok video, or posting some travel pictures on their Instagram. If you do, remember chances are high that those pictures will end up online (publicly or privately) with full metadata attached to them (time/date/geolocation) and your face. Remember these can and will be indexed by Facebook/Google/Yandex/Apple and probably all three letters' agencies.

While this will not be available yet to your local police officers, it could be in the near future.

You will ideally need a set of 3-5 separate places such as this to avoid using the same place twice. Several trips will be needed over the weeks for the various steps in this guide.

You could also consider connecting to these places from a safe distance for added security. See [Using long-range Antenna to connect to Public Wi-Fis from a safe distance.](#long-range-wifi)

