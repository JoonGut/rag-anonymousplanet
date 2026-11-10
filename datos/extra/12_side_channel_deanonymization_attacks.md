## Microarchitectural Side-channel Deanonymization Attacks { #side-channel-attacks }

There was an attack published that can deanonymize users if they have a known alias. For example, an attacker trying to track the activities of a journalist can use that journalist's public Twitter handle to link their anonymous identities with their public one. This breaks compartmentalization of identities and can lead to complete deanonymization, even of users who practice proper OPSEC.

The attack, published at <https://leakuidatorplusteam.github.io/> <sup>[[Archive.org]](https://web.archive.org/web/20220720023429/https://leakuidatorplusteam.github.io/)</sup>, can be mitigated using the well-known [NoScript](https://noscript.net/) extension and will be our preferred recommendation.

One loosely documented attack might take the following approach to fingerprinting: Alice is browsing the web using Firefox. The website she has just visited is using an invisible `iframe` that creates long strings, e.g., sentences or hashes, to produce some non-user-viewable string. These strings are setting a certain font type, Arial. Whether the browser renders this is non-essential, it only matters if the font changes. The `iframe` in this case serves no purpose but to identify whether a user has installed a certain font on their machine. If Alice is using a font that this frame has tried to render, then it is reported back to the website and to the person in control of the website.

The font renders a box with a specific height and width around itself, so that means a specific height and width of the text contained within. The `iframe` keeps doing this for each installed font to create a list of installed fonts for Alice. Because of stylistic differences between each font family, the same string and the same font size will add up to a different height and a different width than Arial. It is used as a fallback font to display text that won't display otherwise, in the case of a user not having that font on their machine and thus non-viewable from their browser.

If a font requested by an `iframe` is not available, Arial will be used to show that text to the user. Every time the font measurement (identified by the dimensions of the box produced) changed, it means the font is present on Alice's browser and her machine. By doing this for hundreds of fonts, websites can use this information to track users using their installed fonts across websites. Imagine a website then selling this “anonymized” information as a dataset to advertisement companies to serve you ads based on the websites you visit, because they know every font you have installed on your machine and can now track your identity across the internet. This attack is demonstrated here: [Everything you always wanted to know about web-based device fingerprinting (but were afraid to ask)](https://www.youtube.com/watch?v=5Y1Y96jC5AA) by Dr. Nick Nikiforakis, PhD in Computer Science from KU Leuven. He explains how his team of researchers identified which sites were using such techniques on Alexa's top 10,000 websites. Primarily, they found that of those, 145 were fingerprinting browsers. They were fingerprinted 100% of the time - whether they were using the Do Not Track header, a popular Privacy & Security setting in many browsers, did not matter.

Attacks such as invisible iframes and media elements can be avoided by blocking all scripts globally by using something like uBlock Origin <https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm> or by using NoScript <https://chrome.google.com/webstore/detail/noscript/doojmbjmlfjjnbmnoijecmcbfeoakpjm>. This is highly encouraged, not only to those wishing to be anonymous, but also to general web users.

**Tor Browser**

**Note: This attack is now prevented by default by an update of [NoScript](https://noscript.net/) (11.4.8 and above) on all security levels in Tor Browser.**

**All others**

Installing the [NoScript](https://noscript.net/) extension will prevent the attack **by default only in private Windows** using their new "TabGuard feature". But can be enabled in the NoScript options to work on all Windows. See:

- Release tweet: <https://twitter.com/ma1/status/1557751019945299969> <sup>[[Archive.org]](https://web.archive.org/web/https://twitter.com/ma1/status/1557751019945299969)</sup>
- User explanation: <https://noscript.net/usage/#crosstab-identity-leak-protection> <sup>[[Archive.org]](https://web.archive.org/web/https://noscript.net/usage/#crosstab-identity-leak-protection)</sup>
- Tor Project Forum Post: <https://forum.torproject.net/t/tor-browser-can-leak-your-identity-through-side-channel-attack/4005/2> <sup>[[Archive.org]](https://web.archive.org/web/https://forum.torproject.net/t/tor-browser-can-leak-your-identity-through-side-channel-attack/4005/2)</sup>
- NoScript extension for Firefox (Firefox, and other Firefox-based browsers except Tor Browser): <https://addons.mozilla.org/en-US/firefox/addon/noscript/>
- NoScript extension for Chromium based browsers (Brave, Chrome, Edge, and other Chromium-based browsers): <https://chrome.google.com/webstore/detail/noscript/doojmbjmlfjjnbmnoijecmcbfeoakpjm?hl=en>

### Alternative to NoScript for all other browsers { #noscript-alternative }

The researches who disclosed the issue also made an extension available below. Again, **nothing is required in Tor Browser**. This path is not our preferred path but is still available if you do not want to use NoScript.

- Leakuidator+ extension for Chromium based browsers (Brave, Chrome, Edge, and other Chromium-based browsers): <https://chrome.google.com/webstore/detail/leakuidator%2B/hhfpajcjkikoocmmhcimllpinjnbedll>
- Leakuidator+ extension for Firefox (Firefox, and other Firefox-based browsers except Tor Browser): <https://addons.mozilla.org/en-US/firefox/addon/leakuidatorplus/>

Separating identities via separate browsers or even with VMs is not enough to avoid this attack. However, another solution is to make sure that when you start working with an anonymous identity, you entirely close all activities linked to other identities. The vulnerability only works if you're actively logged into a non-anonymous identity. The issue with this is that it can hinder effective workflow, as multitasking across multiple identities becomes impossible.

