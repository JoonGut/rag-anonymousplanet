# Choosing a Browser for Your Guest VM { #guest-vm-browser-choice }

**Temporary Important Warning: Please see [Microarchitectural Side-channel Deanonymization Attacks:] for all browsers except Tor Browser.**

There are 6 possibilities of browser to use on your guest/disposable VM:

- Brave (Chromium-based)

- Edge (Chromium-based, Windows Only)

- Firefox

- Safari (macOS VM only)

- Tor Browser

Here is a comparison table of one fingerprinting test of various browsers with their native settings (**but Javascript enabled for usability, except for Tor Safest mode**).

**Disclaimer: these tests while nice are not conclusive of the real fingerprinting resistance. But they can help compare browsers between each other.**

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Browser</strong></th>
<th><p><a href="https://coveryourtracks.eff.org/"><strong>https://coveryourtracks.eff.org/</strong></a></p>
<p><strong>Fingerprinting Test with real Ad</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Safari (Normal)*</strong></td>
<td><strong>Fail (Unique)</strong></td>
</tr>
<tr class="even">
<td><strong>Safari (Private Window) *</strong></td>
<td><strong>Fail (Unique)</strong></td>
</tr>
<tr class="odd">
<td><strong>Edge (Normal)**</strong></td>
<td><strong>Fail (Unique)</strong></td>
</tr>
<tr class="even">
<td><strong>Edge (Private Window) **</strong></td>
<td><strong>Fail (Unique)</strong></td>
</tr>
<tr class="odd">
<td><strong>Firefox (Normal)</strong></td>
<td><strong>Fail (Unique)</strong></td>
</tr>
<tr class="even">
<td><strong>Firefox (Private Window)</strong></td>
<td><strong>Fail (Unique)</strong></td>
</tr>
<tr class="odd">
<td><strong>Chrome (Normal)</strong></td>
<td><strong>Fail (Unique)</strong></td>
</tr>
<tr class="even">
<td><strong>Chrome (Private Window)</strong></td>
<td><strong>Fail (Unique)</strong></td>
</tr>
<tr class="odd">
<td><strong>Brave (Normal)</strong></td>
<td><strong>Passed (Randomized)</strong></td>
</tr>
<tr class="even">
<td><strong>Brave (Private Window)</strong></td>
<td><strong>Passed (Randomized)</strong></td>
</tr>
<tr class="odd">
<td><strong>Brave (Tor Window)</strong></td>
<td><strong>Passed (Randomized)</strong></td>
</tr>
<tr class="even">
<td><strong>Tor Browser (Normal mode)</strong></td>
<td><strong>Partial</strong></td>
</tr>
<tr class="odd">
<td><strong>Tor Browser (Safer mode)</strong></td>
<td><strong>Partial</strong></td>
</tr>
<tr class="even">
<td><strong>Tor Browser (Safest mode)</strong></td>
<td><strong>Unknown (Result did not load)</strong></td>
</tr>
</tbody>
</table>

- \*: macOS only. \*\*: Windows only.

Another useful resource to be considered for comparing browsers is: <https://privacytests.org/> <sup>[[Archive.org]](https://web.archive.org/web/https://privacytests.org/)</sup>

## Brave { guest-vm-brave }

**This is my recommended/preferred choice for a Browser within your guest VMs. This is not my recommended choice for a Browser within your Host OS where we strictly recommend Tor Browser as they recommend it themselves**[^503]**.**

Why Brave despite the controversies[^504]?

- You will encounter fewer issues later with account creations (captchas ...). This is based on our experiences trying to create plenty of online identities using various browsers. You will have to trust us on that.

- You will enjoy native ad-blocking where none is available in others by default without adding extensions[^505].

- Performance is arguably better than Firefox[^506].

- Brave is arguably better at fingerprinting resistance than others[^507].

- Security of Chromium-based Browser is arguably better and more secure than Firefox[^508]'[^509]. Within the context of this guide, security should be privileged to prevent any vulnerability or exploit from gaining access to the VM.

- Comparison of both by Mozilla: <https://www.mozilla.org/en-US/firefox/browsers/compare/brave/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.mozilla.org/en-US/firefox/browsers/compare/brave/)</sup>

- Comparison of both by Techlore: <https://www.youtube.com/watch?v=qkJGF3syQy4> <sup>[[Invidious]](https://yewtu.be/watch?v=qkJGF3syQy4)</sup>

- The whole traffic will be routed over a VPN over Tor anyway. So even if you mistakenly opt-in for some telemetry, it is not so important. Remember that in this anonymity threat model, we are mostly after anonymity and security. The privacy of our online identities does not matter that much unless the privacy issue is also a security issue that could help deanonymize you.

- Brave was found to be sending no identifiable telemetry compared to other browsers[^510].

## Ungoogled-Chromium { guest-vm-ungoogled }

**This browser is considered a security liability due to their systemic lagging on security patches**[^511]**.**

**It is strongly advised not to use Ungoogled-Chromium.**

## Edge { guest-vm-edge }

This is for Windows users only. Edge is a solid choice too.

- You will encounter fewer issues later with account creations (captchas ...). This is based on our experiences trying to create plenty of online identities using various browsers. You will have to trust us on that.

- Better Security than Firefox as it is Chromium-based[^512]'[^513].

- Better Performance than Firefox.

- The whole traffic will be router through Tor anyway.

- Can benefit from additional security using Microsoft Defender Application Guard (MDAG)[^514]. Note that this feature cannot be enabled in a Virtualbox VM unfortunately.

- Native tracker blocking (Similar to Brave Shields).

Cons:

- You will have to disable some telemetry within the Browser

## Safari { guest-vm-safari }

The macOS default browser.

Pros:

- It is a Browser with decent security and sandboxing capabilities.

Cons:

- It is macOS only (obviously)

- It requires signing-in into the App Store to install extensions (impossible within the scope of this guide since it is a VM)

- Even if you could, it lacks the best Extensions available for Firefox and Chrome.

Overall, we would not recommend using Safari on a macOS VM but instead, go for another Browser such as Brave or Firefox.

## Firefox { guest-vm-firefox }

And of course, lastly, you could go with Firefox,

Pros:

- Well, it is out of the "Chromium" world and not taking part in expanding Chromium market share

- In addition to being out of the Chromium world, it is also completely out of the Google world (despite the Mozilla Foundation being almost entirely funded by Google[^515]).

- An impressive amount of customization through extensions for every possible need.

- Firefox can be severely hardened to almost match the security of Chromium-based browsers.

Cons:

- Poorer performance compared to Chromium.

Security (especially sandboxing) of Firefox is arguably weaker than Chromium-based browsers[^516].

- You will experience more captchas (this is based on my tests).

## Tor Browser { guest-vm-tor-browser }

If you are extra paranoid and want to use Tor Browser and have "Tor over VPN over Tor", you could go with Tor Browser within the VM as well. This is completely pointless/useless.

We would not recommend this option. It is just silly.

