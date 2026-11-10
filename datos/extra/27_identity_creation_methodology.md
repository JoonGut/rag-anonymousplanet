# Quick note: Correlation vs Attribution { #correlation-vs-attribution }

**Correlation** is a relationship between two or more variables or **[attributes](https://www.digitalshadows.com/blog-and-research/cyber-attacks-the-challenge-of-attribution-and-response/)**. How are attributions determined? During digital forensic and incident response (DFIR), analysts typically look for indicators of compromise (IoCs) following events that call them to act. These indicators usually consist of IP addresses, names, databases; all of which can prescribe a certain behavioral "tag" to an individual or group. This is called attribution. A principal in statistics is that "correlation does not infer causality". What this means is that, while you may leave certain traces on certain areas of a device or network, that only shows presence of action, i.e., not explicitly your presence. It doesn't show who you are, it only resolves that something occurred and _someone_ has done _something_.

Attribution is required to prove fault or guilt, and is the prime reason why people using the Tor network to access the dark web have been compromised: they left traces that were shown to be connected to their real identities. Your IP can be - but is usually not - a large enough indicator to attribute guilt. This is shown in the infamous NotPetya cyber attacks against the U.S., which were later also released upon Ukraine. Though the White House never _said_ it was Russia's doing, they attributed the attack to Russia's [(GRU)](https://www.reuters.com/article/us-britain-russia-gru-factbox/what-is-russias-gru-military-intelligence-agency-idUSKCN1MF1VK) which is a direct office housing the Russian deniable warfare[^311] cyber divisions, uncommonly referred to as "spy makers" in the intelligence community (IC).

_What is the point_, you may ask? Well, bluntly speaking, this a perfect example because NotPetya, which is now undoubtedly the work of Russian cyber operations against foreign countries and governments, has still never been formally attributed to Russia, only to a known group within Russia (colloquially dubbed [Cozy Bear](https://wikiless.tiekoetter.com/wiki/Cozy_Bear)) which can not be confirmed nor denied given that it is highly compartmentalized within the structure of Russia's military. And it's also in part because of the efforts used to disguise itself as a common Ransomware, and because it routinely used the servers of hacked foreign assets not linked to Russia or to its internal networks.

It's all to show you the lengths that state actors will go to. You may not be aware of it, but foreign governments use concealment techniques such as the ones discussed in the sections of this guide. They routinely use Tor, VPNs to conceal traffic; they use hacked devices and access to stolen equipment to perform cyber espionage every day and it makes attribution incredibly difficult, if not improbable, from a forensic examiner's point of view. The problem of correlation is trivial, and you can solve it by simply using IP hiding tools such as a VPN and the Tor network, but still be connected to your IRL name and IP through data leaks or other factors. You can not easily be attributed to your activities if you carefully follow and adopt the given techniques and skills discussed below.

# Creating your anonymous online identities { #creating-identities }

## Methodology to Prevent Anonymity { #deanon-methodology }

If you often use VPNs or Tor, you will quickly encounter many captchas everywhere. Quite often when using Tor or a VPN, even if you succeed in solving all the puzzles (sometimes dozens in a row), you will still be denied after solving it.

See <https://gitlab.torproject.org/legacy/trac/-/wikis/org/doc/ListOfServicesBlockingTor> <sup>[[Archive.org]](https://web.archive.org/web/https://gitlab.torproject.org/legacy/trac/-/wikis/org/doc/ListOfServicesBlockingTor)</sup>

While most people think those puzzles are only about solving a little puzzle, it is important to understand that it is much more complex, and that modern Captchas use advanced machine learning (a "Large Language Model" or "LLM", often mistakenly referred to as AI) and risk analysis algorithms to check if you are "human"; this is often flawed. They may check your browser's cookies and browsing history using intelligent fingerprinting tactics. They may track your cursor movements (e.g., speed, accuracy) and use algorithms to decide if it is "human/organic". They may track your behavior before/during/after the tests to ensure you are "human". It is also highly likely that those platforms could already reliably identify you based on the unique way you interact with those puzzles. This could work despite obfuscation of your IP address/browser and clearing all cookies.

Watch for example this DEF CON 25 presentation: [DEF CON 25 - Svea Eckert, Andreas Dewes - Dark Data](https://www.youtube.com/watch?v=1nvYGi7-Lxo) <sup>[[Invidious]](https://yewtu.be/watch?v=1nvYGi7-Lxo)</sup>

You will often experience several in a row (sometimes endlessly) and sometimes exceedingly difficult ones involving reading undecipherable characters or identifying various objects on endless picture sets. You will also have more if you use an ad-blocking system (uBlock Origin for example) or if your account was flagged for any reason for using VPNs or Tor previously.

You will also have (in my experience) more Captchas (Google's reCAPTCHA) if you do not use a Chromium-based browser. This can be mitigated by using a Chromium-based browser such as Brave. There is also a browser extension called Buster that could help you with those <https://github.com/dessant/buster> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/dessant/buster)</sup>.

As for Cloudflare (hCaptcha), you could also use their accessibility solution here (<https://www.hcaptcha.com/accessibility> <sup>[[Archive.org]](https://web.archive.org/web/https://www.hcaptcha.com/accessibility)</sup>) which would allow you to sign-up (with your anonymous identity created later) and set a cookie within your browser that would allow you to bypass their captchas. Another solution to mitigate hCaptcha would be to use their own solution called "Privacy Pass" <https://privacypass.github.io/> <sup>[[Archive.org]](https://web.archive.org/web/https://privacypass.github.io/)</sup> in the form of a browser extension you could install in your VM Browser. This is less recommended as we will explain further in the guide, due to side-channel attacks.

You should therefore deal with those carefully and force yourself to alter the way you are solving them (speed/movement/accuracy) to prevent captcha fingerprinting.

Fortunately, as far as we are aware, these are not yet officially/publicly used to de-anonymize people for third parties.

To not have those issues, you should consider using a VPN over Tor. And the best option to avoid those is likely to use a self-hosted VPN/Proxy over Tor on a cash/Monero paid VPS server.

![image34](../media/image34.png)![image35](../media/image35.png)

<sub>(Illustrations by Randall Munroe, xkcd.com, licensed under CC BY-NC 2.5)</sub>

Captcha[^371] stands for "Completely Automated Public Turing test to tell Computers and Humans Apart" are Turing tests[^372] puzzles you need to complete before accessing a form/website. You will mostly encounter those provided by Google (reCAPTCHA service[^373]) and Cloudflare (hCaptcha[^374]). hCaptcha is used on 15% of the internet by their own metrics[^375].

They are designed to separate bots from humans but are also clearly used to deter anonymous and private users from accessing services.

If you often use VPNs or Tor, you will quickly encounter many captchas everywhere[^376]. Quite often when using Tor, even if you succeed in solving all the puzzles (sometimes dozens in a row), you will still be denied after solving the puzzles.

See <https://gitlab.torproject.org/legacy/trac/-/wikis/org/doc/ListOfServicesBlockingTor> <sup>[[Archive.org]](https://web.archive.org/web/https://gitlab.torproject.org/legacy/trac/-/wikis/org/doc/ListOfServicesBlockingTor)</sup>

While most people think those puzzles are only about solving a little puzzle, it is important to understand that it is much more complex, and that modern Captchas uses advanced machine learning and risk analysis algorithms to check if you are human[^377]:

- They check your browser, cookies, and browsing history using Browser fingerprinting[^378].

- They track your cursor movements (speed, accuracy) and use algorithms to decide if it is "human/organic".

- They track your behavior before/during/after the tests to ensure you are "human"[^379].

It is also highly likely that those platforms could already reliably identify you based on the unique way you interact with those puzzles. This could work despite obfuscation of your IP address / Browser and clearing all cookies.

Watch for example this DEF CON 25 presentation: [DEF CON 25 - Svea Eckert, Andreas Dewes - Dark Data](https://www.youtube.com/watch?v=1nvYGi7-Lxo) <sup>[[Invidious]](https://yewtu.be/watch?v=1nvYGi7-Lxo)</sup>

You will often experience several in a row (sometimes endlessly) and sometimes exceedingly difficult ones involving reading undecipherable characters or identifying various objects on endless pictures sets. You will also have more captchas if you use an ad-blocking system (uBlock for example) or if your account was flagged for any reason for using VPNs or Tor previously.

You will also have (in my experience) more Captchas (Google's reCAPTCHA) if you do not use a Chromium-based browser. But this can be mitigated by using a Chromium-based browsers such as Brave. There is also a Browser extension called Buster that could help you those <https://github.com/dessant/buster> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/dessant/buster)</sup>.

As for Cloudflare (hCaptcha), you could also use their Accessibility solution here (<https://www.hcaptcha.com/accessibility> <sup>[[Archive.org]](https://web.archive.org/web/https://www.hcaptcha.com/accessibility)</sup>) which would allow you to sign-up (with your anonymous identity created later) and set a cookie within your Browser that would allow you to bypass their captchas. Another solution to mitigate hCaptcha would be to use their own solution called "Privacy Pass"[^380] <https://privacypass.github.io/> <sup>[[Archive.org]](https://web.archive.org/web/https://privacypass.github.io/)</sup> in the form of a Browser extension you could install in your VM Browser.

You should therefore deal with those carefully and force yourself to alter the way you are solving them (speed/movement/accuracy/...) to prevent "Captcha Fingerprinting".

Fortunately, as far as we are aware, these are not yet officially/publicly used to de-anonymize people for third parties.

To not have those issues, you should consider using a VPN over Tor. And the best option to avoid those is likely to use a self-hosted VPN/Proxy over Tor on a cash/Monero paid VPS server.

### Phone verification { #phone-verification }

Phone verification is advertised by most platforms to verify you are human. But do not be fooled, the main reason for phone verification is not only to check if you are human but also to be able to de-anonymize you if needed.

Most platforms (including the privacy-oriented ones such as Signal/Telegram/Proton will require a phone number to register, and most countries now make it mandatory to submit a proof of ID to register[^381].

Fortunately, this guide explained earlier how to get a number for these cases: [Getting an anonymous Phone number](#anonymous-phone).

### E-Mail verification { #email-verification }

E-Mail verification is what used to be enough but is not anymore in most cases. What is important to know is that open e-mail providers (disposable e-mail providers for instance) are flagged as much as open proxies (like Tor).

Most platforms will not allow you to register using an "anonymous" or disposable e-mail. As they will not allow you to register using an IP address from the Tor network.

The key thing to this is that it is becoming increasingly difficult to sign-up for a free e-mail account anywhere without providing (you guessed it) ... a cell phone number. That same cell phone number can be used conveniently to track you down in most places.

It is possible that those services (Proton for instance) might require you to provide an e-mail address for registration. In that case, we would recommend you create an e-mail address from these providers:

- MailFence: <https://mailfence.com/>

- Disroot: <https://disroot.org>

- Autistici: <https://autistici.org>

- Envs.net: <https://envs.net/>

Keep in mind that those do not provide a zero-access design (a zero-access design is where only you can access your e-mail - not even the service's admins can read your messages). This means they can access your e-mail at rest in their database.

> **A note about Riseup:** RiseUp's warrant canary has been renewed late, with their Twitter posting a cryptic message seeming to tell you not to trust them. Due to the suspicious nature of their Tweet, this guide can no longer recommend them.

_Also see: <https://forums.whonix.org/t/riseup-net-likely-compromised/3195>_

<sub>For the <https://riseup.net> [[Tor Mirror]](http://vww6ybal4bd7szmgncyruucpgfkqahzddi37ktceo3ah7ngmcopnpyyd.onion/) (It has come to my attention that the site now, unfortunately, requires an invitation from a current registered user)</sub>

#### Aliasing services { #email-aliasing }

If you want to avoid communicating your anonymous e-mail addresses to various parties. We would strongly suggest considering using e-mail aliasing services such as:

- <https://simplelogin.io/> (preferred first choice due to more options available to the free tier)

- <https://anonaddy.com/>

These services will allow creating random aliases for your anonymous e-mail (on Proton for example) and could increase your general privacy if you do not want to disclose that e-mail for any purpose. They are both recommended by Privacyguides.org and Privacytools.io. I'm recommending them as well.

### User details checking { #user-details-check }

Obviously, Reddit does not do this (yet), but Facebook most likely does and will look for "suspicious" things in your details (which could include face recognition).

Some examples:

- IP address from a country different than your profile country.

- Age in the profile not matching the picture age.

- Ethnicity in the profile not matching the picture ethnicity.

- Language not matching the country language.

- Unknown in anyone else contacts (Meaning nobody else knows you).

- Locking down privacy settings after signing up.

- Name that does not match the correct ethnicity/language/country?

### Proof of ID verification { #id-verification }

The deal-breaker in most cases. As far as we know, only Facebook and LinkedIn (outside of financial services) have requested such verifications which involve sending pictures of some form of identification (passport, national ID card, driver's license ...). The only way to do this would involve creating fake official documents (forgery) using some decent Photoshop skills and this might be illegal in most places.

Therefore, this is a line we are not going to help you cross within this guide. Some services are offering such services online, but we think they are _bad actors_ and are overstepping their boundaries.

In many countries, only law enforcement, some specific processes (such as GDPR requests), and some well-regulated financial services may request proof of identification. So, the legality of asking for such documents is debatable and we beieve such platforms should not be allowed to require those.

In few countries (like Germany), this practice is illegal and online platforms such as Facebook or LinkedIn are legally bound to allow you to use a pseudonym and remain anonymous.

### IP Filters { #ip-filters }

As stated previously in this guide, many platforms will apply IP-based filtering. Tor exit nodes are publicly listed, and VPN exit servers are "well known". There are many commercial and free services providing the ability to block those IPs with ease (hi Cloudflare).

Many platforms' operators and administrators do not want traffic from these IPs as they often drive a lot of unlawful/malicious/unprofitable traffic to their platforms. These platforms usually argue using one of the following points:

- "Think of the children!";
- "Terrorism!";
- "Russian troll propaganda!";
- "Well, it's noise in the data we sell to advertisers!" (e.g., AdSense or Facebook Ads).

"Yet we still pay traffic for them so let us just deny them all instead."

Fortunately, those systems are not perfect, and you will (still) be able to get around those restrictions by switching identities (in the case of Tor) and trying to access the website each time until you find an Exit Node that is not yet blacklisted.

Some platforms will allow you to log in with a Tor IP but not to sign up (See <https://gitlab.torproject.org/legacy/trac/-/wikis/org/doc/ListOfServicesBlockingTor> <sup>[[Archive.org]](https://web.archive.org/web/https://gitlab.torproject.org/legacy/trac/-/wikis/org/doc/ListOfServicesBlockingTor)</sup>). Those platforms will keep a convenient, permanent log of the IP which you used during sign-up - And some will keep such logs indefinitely, e.g., all the IPs which you have used to log in (hi Facebook).

The tolerance is much higher with VPNs as they are not considered "open proxies", but that will not stop many platforms from making them hard to use by forcing increasingly difficult CAPTCHAs on most VPN users.

For this reason, this guide does recommend the use of VPN over Tor (and not Tor over VPN) in certain use cases. **Remember that the best option to avoid those is to use a self-hosted VPN/Proxy over Tor on a cash/Monero paid VPS**.

### Browser and Device Fingerprinting { #fingerprinting }

Your Browser and Device Fingerprints[^382] are a set of properties/capabilities of your System/Browser. These are used on most websites for invisible user tracking but also to adapt the website user experience depending on their browser. For instance, websites will be able to provide a "mobile experience" if you are using a mobile browser or propose a specific language/geographic version depending on your fingerprint. Most of those techniques work with recent Browsers like Chromium-based[^251] browsers (such as Chrome/Edge) or Firefox[^252] unless taking specific measures. Browser and Device[^382] Fingerprinting are usually integrated into the Captcha services but also in other various services.

Many platforms (like Google[^383]) will check your browser for various capabilities and settings and block browsers they do not like. This is one of the reasons we recommend using Chromium-based browsers such as Brave Browser over Tor Browser within this VM.

It should also be noted that while some browsers and extensions will offer some fingerprint resistance, this resistance in itself can also be used to fingerprint you as explained here <https://palant.info/2020/12/10/how-anti-fingerprinting-extensions-tend-to-make-fingerprinting-easier/> <sup>[[Archive.org]](https://web.archive.org/web/https://palant.info/2020/12/10/how-anti-fingerprinting-extensions-tend-to-make-fingerprinting-easier/)</sup>

This guide will mitigate these issues by randomizing or hiding many of those fingerprinting identifiers by:

- Using Virtualization (See [Virtualization](#virtualization));

- Using specific recommendations (See [Additional browser precautions with JavaScript enabled](#browser-precautions-js));

- Using hardening [Hardening your Browsers](#hardening-browsers);

- and by using fingerprint-resistant browsers (like Brave or Tor Browser).

Here are some of the things they check within recent browsers:

- User-Agent: This is your Browser name and Version.

- HTTP_ACCEPT Headers: This is the type of content your Browser can handle.

- Time Zone and Time Zone Offset: Your time zone.

- Screen Size and Color Depth: The resolution of your screen.

- System Fonts: The typing fonts installed on your system.

- Cookies support: If your browser supports cookies or not.

- Hash of Canvas fingerprint and Hash of WebGL fingerprint: These are generated unique IDs based on your graphic rendering capabilities.

- WebGL Vendor & Renderer: Name of your Video card

- Do-Not-Track enabled or not: Well, yes, they can use your DNT information to track you

- Language: The language of your Browser

- Platform: The Operating System you are using

- Touch Support: If your system supports touch (such as a phone/tablet or touchscreen-enabled laptop)

- Ad Blocking use: If your browser block ads

- AudioContext fingerprint: Like the Canvas and WebGL fingerprints these will fingerprint your audio capabilities.

- CPU: What kind of CPU you are using and how many of them

- Memory: How much memory you have in your System

- Browser Permissions: Is your browser allowing some things like geolocation or microphone/webcam access.

Most of the time, those fingerprints will, unfortunately, be unique or nearly unique to your browser/system. This means that even If you log out from a website and then log back in using a different username, your fingerprint might remain the same if you did not take precautionary measures. An adversary could then use such fingerprints to track you across multiple services even if you have no account on any of them and are using adblocking. These fingerprints could in turn be used to de-anonymize you if you keep the same fingerprint between services.

Here are services you can use to check your browser fingerprints:

- <https://abrahamjuliot.github.io/creepjs/> (Probably the best overall)

- <https://coveryourtracks.eff.org/>

- <https://amiunique.org>

- <https://browserleaks.com/>

- <https://www.deviceinfo.me/>

- (Chromium based browsers only) <https://z0ccc.github.io/extension-fingerprints/#>

Chances are you will find your browser fingerprint unique no matter what you do.

### Human interaction { #human-interaction }

Some platforms will add this as a bonus step and require you to have an actual human interaction with a customer care representative. Usually by e-mail but sometimes by chat/phone. They will want to verify that you exist by asking you to reply to an e-mail/chat/phone call.

It is annoying but quite easy to deal with in our case. We are not making bots. This guide is for humans making human accounts.

### User Moderation { #user-moderation }

Many platforms will delegate and rely on their users to moderate the others and their content. These are the "report" features that you will find on most platforms.

Getting reported thousands of times does not matter when you are Donald Trump or Kim Kardashian but if you as a sole "friendless" anonymous user gets reported even once, you might get suspended/flagged/banned instantly.

### Behavioral Analysis { #behavioral-analysis }

See [Your Digital Footprint](#digital-footprint).

### Financial transactions { #financial-transactions }

Simple and efficient, some platforms will require you to perform a financial transaction to verify your account sometimes under the pretext of verifying your age. This could be a credit card verification or an exceedingly small amount bank wire. Some will accept a donation in a main cryptocurrency like Bitcoin or Ethereum.

While this might seem innocent, this is obviously an ID verification and de-anonymization method. This is just indirectly relying on third-party financial KYC[^240] regulations.

E.g., this is now the case on YouTube for some European Users[^384], but it is also used by services like Amazon that requires a valid payment method for creating an account.

![image36](../media/image36.png)

### Sign-in with some platform { #sso-signin }

"Why do this user-verification ourselves when we can just ask others to deal with it?"

You will notice this, and you probably already encountered this. Some apps/platforms will ask/require you to sign in with a well-known and well-used reputable platform instead of their own system (Sign-in with Google/Facebook/Apple/Twitter).

This option is often presented as the "default one", hiding away the "Sign-in with e-mail and password" with clever Dark Patterns[^385] and unfortunately sometimes needed.

This method will delegate the verification process on those platforms instead of assuming that you will not be able to create an anonymous Google/Facebook/Apple/Twitter account with ease.

Fortunately, it is still possible to this day to create those.

### Facial Recognition and Biometrics { #facial-recognition }

This is a common method used on some Crypto trading platforms and some dating Apps.

Some platforms/apps will require you to take a live picture of yourself either doing something (a wink, holding an arm up ...) or showing a custom piece of information (a handwritten text, a passport, or ID) within the picture. Sometimes the platform/app will require several pictures to increase their certainty.

![image37](../media/image37.png)

This guide will not cover this one (yet) as it is mainly used on financial platforms (that will be able to identify you with other means anyway) and some dating apps like Tinder[^386]. Unfortunately, this method is now also sometimes being used on Facebook[^387] and Instagram as part of their verification methods (tho we did not face it yet so far).

![image38](../media/image38.png)

In some cases, these verifications must be done from your Smartphone and with an "in-app" camera to prevent you from sending a previously saved (edited) image.

Recently even platforms such as PornHub decided to implement similar measures in the future[^388].

This verification is extremely hard to defeat but possible. A method to possibly defeat those would be to use "deep fake" technology software such as the open-source FaceSwap <https://github.com/deepfakes/faceswap> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/deepfakes/faceswap)</sup> to generate the required verification pictures using a randomly computer-generated face that would be swapped over the picture of a complicit model (or a stock photo).

Unfortunately, some apps require direct access to a smartphone camera to process the verification. In that case, you will need to find a way to do such "face swaps" on the fly using a filter and another way to feed this into the camera used by the app. A possible approach would be similar to this impressive project <https://github.com/iperov/DeepFaceLive> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/iperov/DeepFaceLive)</sup>.

### Manual reviews { #manual-reviews }

These can be triggered by any of the above and just means someone (usually specialized employees) will review your profile manually and decide whether it is real or not based on their subjective opinion.

Some countries have even developed hotlines where you can report any subversive content[^389].

Pros: Usually that verdict is "final", and you will probably avoid further issues if you are good.

Cons: Usually that verdict is "final", and you will probably be banned without any appeal possibility if you are not good. Sometimes those reviews end up on the platform just ghosting you and cancel you without any reason whatsoever. Any appeal will be left unanswered, ignored, or will generate some random dark pattern bug when trying to appeal that specific identity (this happens on Instagram for instance where if your account gets "suspended" obviously by some manual review, trying to complete the appeal form will just throw an error and tell you to try again later (We have been trying this same appeal for that identity for the past 6 months at least).

