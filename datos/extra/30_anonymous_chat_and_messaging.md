### How to Chat & Share Files Anonymously { #anonymous-chat-files }

There are plenty of messaging apps everywhere. Some have excellent UI and UX and terrible Security/Privacy. Some have excellent Security/Privacy but terrible UI and UX. It is not easy to pick the ones that you should use for sensitive activities. So, this section will help you do that.

Before going further, there are also some key basic concepts you should understand:

#### E2E Encryption { #on-e2e-encryption }

End-to-end Encryption[^409] (aka e2ee) is a rather simple concept. It just means only you and your destination know each-others public encryption keys and no one in between that would be eavesdropping would be able to decrypt the communication.

However, the term is often used differently depending on the provider:

- Some providers will claim e2ee but forget to mention what is covered by their protocols. For instance, is metadata also protected within their e2ee protocol? Or is it just the content of the messages?

- Some providers do provide e2ee but only as an opt-in option (disabled by default).

- Some providers do offer e2ee with 1 to 1 messaging but not with group messaging.

- Some providers will claim the use of e2ee, but their proprietary apps are closed source where no one can verify the claim and the strength of the encryption used.

For these reasons, it is always important to check the claims of various apps. Open-Source apps should always be preferred to verify what kind of encryption they are using and if their claims are true. If not open source, such apps should have an openly available independent (made by a reputable third party) report confirming their claims.

#### Roll your own crypto { #roll-your-own-crypto }

See the [Bad Cryptography](#on-bad-cryptography) section at the start of this guide.

**Always be cautious of apps rolling their own crypto until it has been reviewed by many in the crypto community (or even better published and peer-reviewed academically)**. Again, this is harder to verify with closed-source proprietary apps.

It is not that rolling your own crypto is bad in essence, it is that good cryptography needs real peer-reviewing, auditing, testing... And since you are probably not a cryptanalyst (and we are not either), chances are high we are not competent to assess the cryptography of some apps.

#### Forward Secrecy { #forward-secrecy }

Forward Secrecy[^410] (FS aka PFS for Perfect Forward Secrecy) is a property of the key agreement protocol of some of those messaging apps and is a companion feature of e2ee. This happens before you establish communication with the destination. The "Forward" refers to the future in time and means that every time you establish a new e2ee communication, a new set of keys will be generated for that specific session. The goal of forward secrecy is to maintain the secrecy of past communications (sessions) even if the current one is compromised. If an adversary manages to get hold of your current e2ee keys, that adversary will then be limited to the content of the single session and will not be able to easily decrypt past ones.

This has some user experience drawbacks like for instance, a new device could not be able to conveniently access the remotely stored chat history without additional steps.

**So, in short, Forward Secrecy protects past sessions against future compromises of keys or passwords.**

More on this topic on this YouTube video: <https://www.youtube.com/watch?v=zSQtyW_ywZc> <sup>[[Invidious]](https://yewtu.be/watch?v=zSQtyW_ywZc)</sup>

Some providers and apps claiming to offer e2ee do not offer FS/PFS sometimes for usability reasons (group messaging for instance is more complex with PFS). It is therefore important to prefer open-source apps providing forward secrecy to those that do not.

#### Zero-Access Encryption at rest { #zero-access-encryption }

Zero-Access Encryption[^411] at rest is used when you store data at some provider (let us say your chat history or chat backups) but this history or backup is encrypted on your side and cannot be read or decrypted by the provider hosting it.

Zero-Access encryption is an added feature/companion to e2ee but is applied mainly to data at rest and not communications.

Examples of this issue would be iMessage and WhatsApp, see the [Your Cloud Backup & Sync Services](#cloud-backups) at the start of this guide.

So again, it is best to prefer Apps/Providers that do offer Zero-Access Encryption at rest and cannot read/access any of your data/metadata even at rest and not only limited to communications.

Such a feature would have prevented important hacks such as the Cambridge Analytica scandal[^412] if it were implemented.

#### Metadata Protection { #metadata-protection }

Remember the [Your Metadata](#metadata) section (including geo-location). End-to-end Encryption is one thing, but it does not necessarily protect your metadata.

For Instance, WhatsApp might not know what you are saying but they might know who you are talking to, how long and when you have been talking to someone, who else is in groups with you, and if you transferred data with them (such as large files).

End-to-end Encryption does not in itself protect an eavesdropper from harvesting your metadata.

This data can also be protected/obfuscated by some protocols to make metadata harvesting substantially harder for eavesdroppers. This is the case for instance with the Signal Protocol which does offer some added protection with features like:

- The Sealed Sender option[^413].

- The Private Contact Discovery[^414].

- The Private Group System[^415].

Other Apps like Briar or OnionShare will protect metadata by using the Tor Network as a shield and storing everything locally on-device. Nothing is stored remotely, and all communications are either direct using proximity wi-fi/Bluetooth or remotely through the Tor network.

Most apps however and especially closed-source proprietary commercial apps will collect and retain your metadata for various purposes. And such metadata alone is enough to figure out a lot of things about your communications.

Again, it is important to prefer open-source apps with privacy in mind and various methods in place to protect not only the content of communications but all the associated metadata.

#### Open-Source { #open-source }

Finally, Open-Source apps should always be preferred because they allow third parties to check actual capabilities and weaknesses vs claims of marketing departments. Open-Source does not mean the app should be free or non-commercial. It just means transparency.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>App<sup>0</sup></th>
<th>e2ee<sup>1</sup></th>
<th>Roll Your Own Crypto</th>
<th><p>Perfect</p>
<p>Forward Secrecy</p></th>
<th>Zero-Access Encryption at-rest<sup>5</sup></th>
<th>Metadata Protection (obfuscation, encryption…)</th>
<th>Open-Source</th>
<th>Default Privacy Settings</th>
<th>Native Anonymous Sign-up (no e-mail or phone)</th>
<th>Possible through Tor</th>
<th>Privacy and Security Track Record ***</th>
<th>De-centralized</th>
<th>Additional notes</th>
</tr>
</thead>
<tbody>
<tr class="even">
<td><p>Berty</p>
<p>(avoid)</p></td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes <a href="#fn13" class="footnote-ref" id="fnref13" role="doc-noteref"><sup>13</sup></a></td>
<td>Good</td>
<td>Yes</td>
<td>Yes</td>
<td>Good</td>
<td>Yes (peer to peer)</td>
<td>Not sufficiently reviewed by this project, cannot recommend</td>
</tr>
<tr class="odd">
<td>Briar (preferred)</td>
<td>Yes</td>
<td>No <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></td>
<td>Yes</td>
<td>Yes</td>
<td>Yes (strong)</td>
<td>Yes</td>
<td>Good</td>
<td>Yes</td>
<td>Natively<sup>3</sup></td>
<td>Good</td>
<td>Yes (peer to peer)</td>
<td></td>
</tr>
<tr class="even">
<td><p>Cwtch</p>
<p>(preferred)</p></td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes (strong)</td>
<td>Yes</td>
<td>Good</td>
<td>Yes</td>
<td>Natively</td>
<td>Good</td>
<td>Yes (peer to peer)</td>
<td></td>
</tr>
<tr class="odd">
<td><p>Discord</p>
<p>(avoid)</p></td>
<td>No</td>
<td>Closed-source<sup>7</sup></td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Bad</td>
<td>E-Mail Required</td>
<td>Virtualization</td>
<td>Bad</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td>Element / Matrix.org (preferred)</td>
<td>Yes (opt-in)</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Poor<a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a></td>
<td>Yes</td>
<td>Good</td>
<td>Yes</td>
<td>Via Proxy<sup>3</sup> or Virtualization</td>
<td>Good</td>
<td>Partial (federated servers)</td>
<td></td>
</tr>
<tr class="odd">
<td>Facebook Messenger (avoid)</td>
<td>Partial (Only 1to1 / opt-in)</td>
<td>Closed-source<sup>7</sup></td>
<td>Yes</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Bad</td>
<td>E-Mail and Phone required</td>
<td>Virtualization</td>
<td>Bad</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td>OnionShare (preferred)</td>
<td>Yes</td>
<td>No</td>
<td>TBD<sup>8</sup></td>
<td>TBD<sup>8</sup></td>
<td>Yes (strong)</td>
<td>Yes</td>
<td>Good</td>
<td>Yes</td>
<td>Natively</td>
<td>Good</td>
<td>Yes (peer to peer)</td>
<td></td>
</tr>
<tr class="odd">
<td>Apple Messages (aka iMessage)</td>
<td>Yes</td>
<td>Closed-source<sup>7</sup></td>
<td>No</td>
<td>Partial</td>
<td>No</td>
<td>No</td>
<td>Good</td>
<td>Apple device Required</td>
<td>Maybe Virtualization using real Apple device ID</td>
<td>Bad</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td>IRC</td>
<td>Yes (OTR plugins)</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Bad</td>
<td>Yes</td>
<td>Via Proxy<sup>3</sup> or Virtualization</td>
<td>Good</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><p>Jami</p>
<p>(preferred)</p></td>
<td>Yes</td>
<td>No<a href="#fn3" class="footnote-ref" id="fnref3" role="doc-noteref"><sup>3</sup></a></td>
<td>Yes</td>
<td>Yes</td>
<td>Partial</td>
<td>Yes</td>
<td>Good</td>
<td>Yes</td>
<td>Via Proxy<sup>3</sup> or Virtualization<sup>9</sup></td>
<td>Good</td>
<td>Partial</td>
<td>Tor breaks some features</td>
</tr>
<tr class="even">
<td>KakaoTalk (avoid)</td>
<td>Yes</td>
<td>Closed-source<sup>7</sup></td>
<td>No<a href="#fn4" class="footnote-ref" id="fnref4" role="doc-noteref"><sup>4</sup></a></td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Bad</td>
<td>No (but possible)</td>
<td>Virtualization</td>
<td>Bad</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td>Keybase</td>
<td>Yes</td>
<td>No</td>
<td>Partial (exploding message)</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Good</td>
<td>E-Mail Required</td>
<td></td>
<td></td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td>Kik (avoid)</td>
<td>No</td>
<td>Closed-source<sup>7</sup></td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Bad</td>
<td>No (but possible)</td>
<td>Virtualization</td>
<td>Bad</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td>Line (avoid)</td>
<td>Partial (opt-in)</td>
<td>Closed-source<sup>7</sup></td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Bad</td>
<td>No (but possible)</td>
<td>Virtualization</td>
<td>Bad</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td>Pidgin with OTR (avoid)</td>
<td>Yes (OTR<a href="#fn5" class="footnote-ref" id="fnref5" role="doc-noteref"><sup>5</sup></a>)</td>
<td>No</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Bad</td>
<td>Yes</td>
<td>Via Proxy<sup>3</sup> or Virtualization</td>
<td>Bad<a href="#fn6" class="footnote-ref" id="fnref6" role="doc-noteref"><sup>6</sup></a></td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td>Tox (avoid)</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Good</td>
<td>Yes</td>
<td>Via Proxy<sup>3</sup> or Virtualization</td>
<td>Medium<a href="#fn7" class="footnote-ref" id="fnref7" role="doc-noteref"><sup>7</sup></a></td>
<td>Yes</td>
<td>Known cryptographic weaknesses<a href="#fn14" class="footnote-ref" id="fnref14" role="doc-noteref"><sup>14</sup></a></td>
</tr>
<tr class="even">
<td><p>Session</p>
<p>(Preferred only on iOS)</p></td>
<td>Yes</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Good</td>
<td>Yes</td>
<td>Via Proxy<sup>3</sup> or Virtualization<sup>10</sup></td>
<td>Good</td>
<td>Yes</td>
<td>Lacks PFS, deniability</td>
</tr>
<tr class="odd">
<td>Signal</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes (moderate)</td>
<td>Yes</td>
<td>Good</td>
<td>Phone Required</td>
<td>Virtualization</td>
<td>Good</td>
<td>No</td>
<td>Requires burner or anonymous VOIP number for anonymous usage</td>
</tr>
<tr class="even">
<td>Skype (avoid)</td>
<td>Partial (Only 1to1 / opt-in)</td>
<td>Closed-source<sup>7</sup></td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Bad</td>
<td>No (but possible)</td>
<td>Virtualization</td>
<td>Bad</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td>SnapChat (avoid)</td>
<td>No</td>
<td>Closed-source<sup>7</sup></td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Bad</td>
<td>No (but possible)</td>
<td>Virtualization</td>
<td>Bad</td>
<td>No</td>
<td>Deleted/expired messages are easily recoverable<a href="#fn15" class="footnote-ref" id="fnref15" role="doc-noteref"><sup>15</sup></a>,<a href="#fn16" class="footnote-ref" id="fnref16" role="doc-noteref"><sup>16</sup></a></td>
</tr>
<tr class="even">
<td>Teams (avoid)</td>
<td>Yes</td>
<td>Closed-source<sup>7</sup></td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Bad</td>
<td>No (but possible)</td>
<td>Virtualization</td>
<td>Bad</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td>Telegram</td>
<td>Partial (Only 1to1 / opt-in)</td>
<td>Yes (MTProto<a href="#fn8" class="footnote-ref" id="fnref8" role="doc-noteref"><sup>8</sup></a>)</td>
<td>Partial (secret chats only)</td>
<td>Yes</td>
<td>No</td>
<td>Partial<sup>5</sup></td>
<td>Medium (e2ee off by default)</td>
<td>Phone Required</td>
<td>Via Proxy<sup>3</sup> or Virtualization</td>
<td>Medium<a href="#fn9" class="footnote-ref" id="fnref9" role="doc-noteref"><sup>9</sup></a></td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td>Viber (avoid)</td>
<td>Partial (Only 1to1)</td>
<td>Closed-source<sup>7</sup></td>
<td>Yes</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Bad</td>
<td>No (but possible)</td>
<td>Virtualization</td>
<td>Bad</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td>WeChat (avoid)</td>
<td>No</td>
<td>Closed-source<sup>7</sup></td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Bad</td>
<td>No</td>
<td>Virtualization</td>
<td>Bad</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td>WhatsApp (avoid)</td>
<td>Yes</td>
<td>Closed-source<sup>7</sup></td>
<td>Yes</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Bad</td>
<td>Phone Required</td>
<td>Virtualization</td>
<td>Bad</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td>Wickr Me</td>
<td>Partial (Only 1to1)</td>
<td>No</td>
<td>Yes</td>
<td>No</td>
<td>Yes (moderate)</td>
<td>No</td>
<td>Good</td>
<td>Yes</td>
<td>Virtualization</td>
<td>Good</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td>Gajim (XMPP) (preferred)</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Good</td>
<td>Yes</td>
<td>Via Proxy<sup>3</sup> or Virtualization</td>
<td>Good</td>
<td>Partial</td>
<td></td>
</tr>
<tr class="odd">
<td>Zoom (avoid<a href="#fn10" class="footnote-ref" id="fnref10" role="doc-noteref"><sup>10</sup></a>)</td>
<td>Disputed<a href="#fn11" class="footnote-ref" id="fnref11" role="doc-noteref"><sup>11</sup></a></td>
<td>No</td>
<td>TBD<sup>8</sup></td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Bad</td>
<td>E-Mail Required</td>
<td>Virtualization</td>
<td>Bad<a href="#fn12" class="footnote-ref" id="fnref12" role="doc-noteref"><sup>12</sup></a></td>
<td>No</td>
<td>Malware risk<a href="#fn17" class="footnote-ref" id="fnref17" role="doc-noteref"><sup>17</sup></a></td>
</tr>
<tr class="Even">
<td>Molly</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes (moderate)</td>
<td>Yes</td>
<td>Good</td>
<td>Phone Required</td>
<td>Virtualization</td>
<td>Good</td>
<td>No</td>
<td>Requires phone number. Security hardened fork of Signal client. Security may be delayed for up to a week</td>
</tr>
</tbody>
</table>
<section class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1" role="doc-endnote"><p>Briar Documentation, Bramble Transport Protocol version 4 <a href="https://code.briarproject.org/briar/briar-spec/blob/master/protocols/BTP.md">https://code.briarproject.org/briar/briar-spec/blob/master/protocols/BTP.md</a> <a href="https://web.archive.org/web/https://code.briarproject.org/briar/briar-spec/blob/master/protocols/BTP.md"><sup>[Archive.org]</sup></a><a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2" role="doc-endnote"><p>Serpentsec, Matrix <a href="https://web.archive.org/web/https://serpentsec.1337.cx/matrix">https://web.archive.org/web/https://serpentsec.1337.cx/matrix</a><a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn3" role="doc-endnote"><p>Wikipedia, GnuTLS, <a href="https://en.wikipedia.org/wiki/GnuTLS">https://en.wikipedia.org/wiki/GnuTLS</a> <a href="https://wikiless.tiekoetter.com/wiki/GnuTLS"><sup>[Wikiless]</sup></a> <a href="https://web.archive.org/web/https://en.wikipedia.org/wiki/GnuTLS"><sup>[Archive.org]</sup></a><a href="#fnref3" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn4" role="doc-endnote"><p>KTH ROYAL INSTITUTE OF TECHNOLOGYSCHOOL OF ELECTRICAL ENGINEERING, A Security and Privacy Audit of KakaoTalk’s End-to-End Encryption <a href="http://www.diva-portal.org/smash/get/diva2:1046438/FULLTEXT01.pdf">www.diva-portal.org/smash/get/diva2:1046438/FULLTEXT01.pdf</a> <a href="https://web.archive.org/web/http://www.diva-portal.org/smash/get/diva2:1046438/FULLTEXT01.pdf"><sup>[Archive.org]</sup></a><a href="#fnref4" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn5" role="doc-endnote"><p>Wikipedia, OTR <a href="https://en.wikipedia.org/wiki/Off-the-Record_Messaging">https://en.wikipedia.org/wiki/Off-the-Record_Messaging</a> <a href="https://wikiless.tiekoetter.com/wiki/Off-the-Record_Messaging"><sup>[Wikiless]</sup></a> <a href="https://web.archive.org/web/https://en.wikipedia.org/wiki/Off-the-Record_Messaging"><sup>[Archive.org]</sup></a><a href="#fnref5" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn6" role="doc-endnote"><p>Pidgin Security Advisories, <a href="https://www.pidgin.im/about/security/advisories/">https://www.pidgin.im/about/security/advisories/</a> <a href="https://web.archive.org/web/https://www.pidgin.im/about/security/advisories/"><sup>[Archive.org]</sup></a><a href="#fnref6" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn7" role="doc-endnote"><p>Whonix Forum, Tox Integration <a href="https://forums.whonix.org/t/tox-qtox-whonix-integration/1219">https://forums.whonix.org/t/tox-qtox-whonix-integration/1219</a> <a href="https://web.archive.org/web/https://forums.whonix.org/t/tox-qtox-whonix-integration/1219"><sup>[Archive.org]</sup></a><a href="#fnref7" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn8" role="doc-endnote"><p>Telegram Documentation, MTProto Mobile Protocol <a href="https://core.telegram.org/mtproto">https://core.telegram.org/mtproto</a> <a href="https://web.archive.org/web/https://core.telegram.org/mtproto"><sup>[Archive.org]</sup></a><a href="#fnref8" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn9" role="doc-endnote"><p>Wikipedia, Telegram Security Breaches, <a href="https://en.wikipedia.org/wiki/Telegram_(software)#Security_breaches">https://en.wikipedia.org/wiki/Telegram_(software)#Security_breaches</a> <a href="https://wikiless.tiekoetter.com/wiki/Telegram_(software)"><sup>[Wikiless]</sup></a> <a href="https://web.archive.org/web/https://en.wikipedia.org/wiki/Telegram_(software)#Security_breaches"><sup>[Archive.org]</sup></a><a href="#fnref9" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn10" role="doc-endnote"><p>TechCrunch, Maybe we shouldn’t use Zoom after all, <a href="https://techcrunch.com/2020/03/31/zoom-at-your-own-risk/">https://techcrunch.com/2020/03/31/zoom-at-your-own-risk/</a> <a href="https://web.archive.org/web/https://techcrunch.com/2020/03/31/zoom-at-your-own-risk/"><sup>[Archive.org]</sup></a><a href="#fnref10" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn11" role="doc-endnote"><p>The Incercept, Zoom Meetings Aren’t End-to-End Encrypted, Despite Misleading Marketing <a href="https://theintercept.com/2020/03/31/zoom-meeting-encryption/">https://theintercept.com/2020/03/31/zoom-meeting-encryption/</a> <a href="http://27m3p2uv7igmj6kvd4ql3cct5h3sdwrsajovkkndeufumzyfhlfev4qd.onion/2020/03/31/zoom-meeting-encryption/"><sup>[Tor Mirror]</sup></a> <a href="https://web.archive.org/web/https://theintercept.com/2020/03/31/zoom-meeting-encryption/"><sup>[Archive.org]</sup></a><a href="#fnref11" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn12" role="doc-endnote"><p>Serpentsec, Secure Messaging: Choosing a chat app <a href="https://web.archive.org/web/https://serpentsec.1337.cx/secure-messaging-choosing-a-chat-app">https://web.archive.org/web/https://serpentsec.1337.cx/secure-messaging-choosing-a-chat-app</a><a href="#fnref12" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn13" role="doc-endnote"><p>Berty, Development, <a href="https://berty.tech">https://berty.tech</a><a href="#fn13" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn14" role="doc-endnote"><p>Tox Handshake Vulnerable to KCI, <a href="https://github.com/TokTok/c-toxcore/issues/426">https://github.com/TokTok/c-toxcore/issues/426</a><a href="#fn13" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn15" role="doc-endnote"><p>The Guardian, Deleted Snapchat photos recovered 'within days' by forensics company, <a href="https://www.theguardian.com/technology/2013/may/09/snapchat-photos-not-deleted">https://www.theguardian.com/technology/2013/may/09/snapchat-photos-not-deleted</a><a href="#fn13" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn16" role="doc-endnote"><p>The Guardian, Snapchat's expired snaps are not deleted, just hidden, <a href="https://web.archive.org/web/20131115224243/https://www.theguardian.com/media-network/partner-zone-infosecurity/snapchat-photos-not-deleted-hidden">https://web.archive.org/web/20131115224243/https://www.theguardian.com/media-network/partner-zone-infosecurity/snapchat-photos-not-deleted-hidden</a><a href="#fn13" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn17" role="doc-endnote"><p>The Guardian, ‘Zoom is malware’: why experts worry about the video conferencing platform, <a href="https://www.theguardian.com/technology/2020/apr/02/zoom-technology-security-coronavirus-video-conferencing">https://www.theguardian.com/technology/2020/apr/02/zoom-technology-security-coronavirus-video-conferencing</a><a href="#fn13" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</section>

**Legend:**

1. The mention "preferred" or "avoid" refers to the use of those apps for sensitive communications. This is just my opinion, and you can make your own using the resources above and others. Remember "Trust but verify".

2. e2ee refers to "end-to-end encryption"

3. Additional steps might be needed for securing Tor Connectivity

4. Their ability and willingness to fight for privacy and not cooperate with various adversaries

5. Only the client apps are open-source, not the server-side apps

6. This means the data is fully encrypted at rest (and not only during transit) and unreadable by any third party without a key you only know (including backups)

7. Unverifiable because it is proprietary closed source.

8. To Be Determined, unknown at the time of this writing

9. Jami will require you to enable DHTProxy in their options to work and it will be limited to text only.

10. Session also uses their own Onion Routing solution called LokiNet

**Some apps like Threema and Wire were excluded from this comparison due to not being free and not accepting anonymous cash methods such as Cash/Monero.**

#### Conclusion { #comms-conclusion }

**Remember: [Checklist of things to verify before sharing information](#pre-sharing-checklist).**

We will recommend these options in that order (as also recommend by Privacyguides.org[^416]'[^417] except for Session and Cwtch):

- macOS:

    - Native Tor Onion Routing Support (**preferred**):

        + OnionShare version >2.3 (<https://onionshare.org/> <sup>[[Tor Mirror]](http://lldan5gahapx5k7iafb3s4ikijc4ni7gx5iywdflkba5y2ezyg6sjgyd.onion/)</sup> <sup>[[Archive.org]](https://web.archive.org/web/https://onionshare.org/)</sup>)**

        + Cwtch (<https://cwtch.im> <sup>[[Archive.org]](https://web.archive.org/web/https://cwtch.im/)</sup> **warning, this is at the alpha/beta stage**)**

    - Non-Native Tor Support (needs additional steps for ideal anonymity to proxy it through Tor through Virtualization or Proxying):

        + Element/Matrix.org (<https://element.io/> <sup>[[Archive.org]](https://web.archive.org/web/https://element.io/)</sup>)

        + Jami (<https://jami.net/> <sup>[[Archive.org]](https://web.archive.org/web/https://jami.net/)</sup>)*

        + Gajim/XMPP (<https://gajim.org/> <sup>[[Archive.org]](https://web.archive.org/web/https://gajim.org/)</sup>)

- Windows:

    - Native Tor Onion Routing Support (**preferred**):

        + OnionShare version >2.3 (<https://onionshare.org/> <sup>[[Tor Mirror]](http://lldan5gahapx5k7iafb3s4ikijc4ni7gx5iywdflkba5y2ezyg6sjgyd.onion/)</sup> <sup>[[Archive.org]](https://web.archive.org/web/https://onionshare.org/)</sup>)**

        + Cwtch (<https://cwtch.im> <sup>[[Archive.org]](https://web.archive.org/web/https://cwtch.im/)</sup> **warning, this is at the alpha/beta stage**)**

    - Non-Native Tor Support (needs additional steps for ideal anonymity to proxy it through Tor through Virtualization or Proxying):

        + Element/Matrix.org (<https://element.io/> <sup>[[Archive.org]](https://web.archive.org/web/https://element.io/)</sup>)

        + Jami (<https://jami.net/> <sup>[[Archive.org]](https://web.archive.org/web/https://jami.net/)</sup>)*

        + Gajim/XMPP (<https://gajim.org/> <sup>[[Archive.org]](https://web.archive.org/web/https://gajim.org/)</sup>)

- Linux:

    - Native Tor Onion Routing Support (**preferred**):

        + Briar (<https://briarproject.org/> <sup>[[Archive.org]](https://web.archive.org/web/https://briarproject.org/)</sup>)*

        + OnionShare version >2.3 (<https://onionshare.org/> <sup>[[Tor Mirror]](http://lldan5gahapx5k7iafb3s4ikijc4ni7gx5iywdflkba5y2ezyg6sjgyd.onion/)</sup> <sup>[[Archive.org]](https://web.archive.org/web/https://onionshare.org/)</sup>)**

        + Cwtch (<https://cwtch.im> <sup>[[Archive.org]](https://web.archive.org/web/https://cwtch.im/)</sup> **warning, this is at the alpha/beta stage**)**

    - Non-Native Tor Support (needs additional steps for ideal anonymity to proxy it through Tor through Virtualization or Proxying):

        + Element/Matrix.org (<https://element.io/> <sup>[[Archive.org]](https://web.archive.org/web/https://element.io/)</sup>)

        + Jami (<https://jami.net/> <sup>[[Archive.org]](https://web.archive.org/web/https://jami.net/)</sup>)*

        + Gajim/XMPP (<https://gajim.org/> <sup>[[Archive.org]](https://web.archive.org/web/https://gajim.org/)</sup>)

- Note that for Jami to work over Tor, you will have to enable the local DHTProxy option within Jami Settings. This will only work for text messages and not for calls/videos)

** Note that these options (Briar, Cwtch, and OnionShare) do not support multi-devices yet. Your information is strictly stored on the device/OS where you are setting it up. Do not use those on a non-persistent OS unless you want ephemeral use.

Any safe options for mobile devices? **Yes, but these are not endorsed/recommended except Briar on Android. Remember also that this guide discourages the use of smartphones for sensitive activities in general.**

- Android:

    - Briar (<https://briarproject.org/> <sup>[[Archive.org]](https://web.archive.org/web/https://briarproject.org/)</sup>)

    - Cwtch (<https://cwtch.im> <sup>[[Archive.org]](https://web.archive.org/web/https://cwtch.im/)</sup> **warning, this is at the alpha/beta stage**)

- iOS:

    - Due to the lack of any better option and while it is **normally not recommended**: Session Messenger: <https://getsession.org/> <sup>[[Archive.org]](https://web.archive.org/web/https://getsession.org/)</sup>. Why is it not recommended these days within the privacy community? **See: [Caution about Session messenger](#session-messenger-caution) to find out why we are cautious about Session Messenger**.

**Note that all the non-native Tor options must be used over Tor for safety (from Tails or a guest OS running behind the Whonix Gateway such as the Whonix Workstation or an Android-x86 VM).**

WhileWedo not recommend most of the messaging platforms for the various reasons outlined above (phone number and e-mail requirements), this does not mean it is not possible to use them anonymously if you know what you are doing. You can use even Facebook Messenger anonymously by taking the necessary precautions outlined in this guide (virtualization behind a Tor Gateway on a non-persistent OS).

The ones that are preferred are recommended due to their stance on privacy, their default settings, their crypto choices but also because they allow convenient anonymous sign-up without going through the many hassles of having a phone number/e-mail verification method and are open source. Those should be privileged in most cases.

You can also consult the following external resources for more comparisons (**we do not necessarily endorse their opinions**):

- SecuChart, <https://bkil.gitlab.io/secuchart/> <sup>[[Archive.org]](https://web.archive.org/web/https://bkil.gitlab.io/secuchart/)</sup> <sup>[[Repository]](https://github.com/bkil/secuchart)</sup> (Maintained open-source project)
- Wikipedia, <https://en.wikipedia.org/wiki/Comparison_of_cross-platform_instant_messaging_clients> <sup>[[Wikiless]](https://wikiless.tiekoetter.com/wiki/Comparison_of_cross-platform_instant_messaging_clients)</sup> <sup>[[Archive.org]](https://web.archive.org/web/https://en.wikipedia.org/wiki/Comparison_of_cross-platform_instant_messaging_clients)</sup>
    - Wikipedia, <https://en.wikipedia.org/wiki/Comparison_of_instant_messaging_protocols> <sup>[[Wikiless]](https://wikiless.tiekoetter.com/wiki/Comparison_of_instant_messaging_protocols)</sup> <sup>[[Archive.org]](https://web.archive.org/web/https://en.wikipedia.org/wiki/Comparison_of_instant_messaging_protocols)</sup>
- Whonix Documentation, Instant Messenger Chat <https://www.whonix.org/wiki/Chat> <sup>[[Archive.org]](https://web.archive.org/web/https://www.whonix.org/wiki/Chat)</sup> (Outdated, Unmaintained but contains insightful information)

- **Outdated, or unmaintained, or abandoned resources scheduled for removal from our guide in next release:**

    - <del>Secure Messaging Apps <https://www.securemessagingapps.com/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.securemessagingapps.com/)</sup></del>
    - <del>Proton Blog, <https://proton.me/blog/whatsapp-alternatives/> <sup>[[Archive.org]](https://web.archive.org/web/2022053117143/https://proton.me/blog/whatsapp-alternatives)</sup></del>
    - <del>SecureChart.org, <https://securechatguide.org/featuresmatrix.html> <sup>[[Archive.org]](https://web.archive.org/web/https://securechatguide.org/featuresmatrix.html)</sup></del>
    - <del>Messenger-Matrix.de at <https://www.messenger-matrix.de/messenger-matrix-en.html> <sup>[[Archive.org]](https://web.archive.org/web/https://www.messenger-matrix.de/messenger-matrix-en.html)</sup></del>

**We do not endorse or recommend some mainstream platforms for anonymity including the much-praised Signal which to this date still requires a phone number to register and contact others. In the context of this guide, we strongly recommend against using Signal if possible. The same recommendation applies to popular forks of Signal such as Molly (<https://molly.im><sup>[[Archive.org]](https://web.archive.org/web/https://molly.im)</sup>)**

