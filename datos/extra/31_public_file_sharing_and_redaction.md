### How to share files publicly { #share-files-publicly }

**Warning: before sharing anything publicly, make sure your files are curated of any information that could compromise your identity. See [Checklist of things to verify before sharing information](#pre-sharing-checklist).**

Consider the following platforms:

- Cryptpad.fr (<https://cryptpad.fr/>): Free tier limited to 1GB total and recommended by PrivacyGuides.org at <https://privacyguides.org/cloud/> <sup>[[Archive.org]](https://web.archive.org/web/https://privacyguides.org/cloud/)</sup>

- Proton Drive (<https://proton.me/drive/>): Paid. Requires you to have "Proton Unlimited" or "Mail Plus". Proton Drive is E2EE and recommended by PrivacyGuides.org
    - Like Proton and Proton VPN, it's not easy to sign up anonymously. When you try to register through Tor, they request verification either by phone number, or by providing a donation

- Filen (<https://filen.io/>): free tier limited to 10GB total

Consider the use of IPFS[^421]:

- Pinata (<https://www.pinata.cloud/>): Free tier limited to 1GB total

### Redacting Documents Safely { #redacting-documents }

You might want to self-publish some information safely and anonymously in the form of writing, pictures, videos, ...

For all these purposes here are a few recommendations:

- Ideally, you should not use proprietary software such as Adobe Photoshop, Microsoft Office...

- Preferably, you should use open-source software instead such as LibreOffice, Gimp...

While the commercial alternatives are feature-rich, they are also proprietary closed-source and often have various issues such as:

- Sending telemetry information back to the company.

- Adding unnecessary metadata and sometimes watermarks to your documents.

- These apps are not free, and any leak of any metadata could be traced back to you since you had to buy these somewhere.

It is possible to use commercial software for making sensitive documents, but you should be extra careful with all the options in the various Apps (commercial or free) to prevent any data leak from revealing information about you.

Here is a comparative table of recommended/included software compiled from various sources (PrivacyGuides.org, Whonix, Tails, Prism-Break.org, and me). Keep in mind my recommendation considers the context of this guide with only sporadic online presence on a need basis.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 20%" />
<col style="width: 14%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Type</strong></th>
<th><strong>Whonix</strong></th>
<th><strong>Prism-Break.org</strong></th>
<th><strong>PrivacyGuides.org</strong></th>
<th><strong>Tails</strong></th>
<th><strong>This guide</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Offline Document Editing</td>
<td>LibreOffice</td>
<td>N/A</td>
<td>LibreOffice*</td>
<td>LibreOffice</td>
<td><p>LibreOffice,</p>
<p>Notepad++</p></td>
</tr>
<tr class="even">
<td>Online Document Editing (collaboration)</td>
<td>N/A</td>
<td>Cryptpad.fr</td>
<td><p>Cryptpad.fr,</p>
<p>Etherpad.org,</p>
<p>Privatebin.net</p></td>
<td>N/A</td>
<td><p>Cryptpad.fr,</p>
<p>Etherpad.org,</p>
<p>Privatebin.net</p></td>
</tr>
<tr class="odd">
<td>Pictures Editing</td>
<td>Flameshot (L)</td>
<td>N/A</td>
<td>N/A</td>
<td>GIMP</td>
<td>GIMP</td>
</tr>
<tr class="even">
<td>Audio Editing</td>
<td>Audacity</td>
<td>N/A</td>
<td>N/A</td>
<td>Audacity</td>
<td>Audacity</td>
</tr>
<tr class="odd">
<td>Video Editing</td>
<td>Flowblade (L)</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td><p>Flowblade (L)</p>
<p>Olive (?)</p>
<p>OpenShot (?)</p>
<p>ShotCut (?)</p></td>
</tr>
<tr class="even">
<td>Screen Recorder</td>
<td>Vokoscreen</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>Vokoscreen</td>
</tr>
<tr class="odd">
<td>Media Player</td>
<td>VLC</td>
<td>N/A</td>
<td>N/A</td>
<td>VLC</td>
<td>VLC</td>
</tr>
<tr class="even">
<td>PDF Viewer</td>
<td>Ristretto (L)</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>Browser</td>
</tr>
<tr class="odd">
<td>PDF Redaction</td>
<td>PDF-Redact Tools (L)</td>
<td>N/A</td>
<td>N/A</td>
<td>PDF-Redact Tools (L)</td>
<td><p>LibreOffice,</p>
<p>PDF-Redact Tools (L)</p></td>
</tr>
</tbody>
</table>

**Legend:** * Not recommended but mentioned. N/A = Not Included or absence of recommendation for that software type. (L)= Linux Only but can maybe be used on Windows/macOS through other means (HomeBrew, Virtualization, Cygwin). (?)= Not tested but open-source and could be considered.

**In all cases, we strongly recommend only using such applications from within a VM or Tails to prevent as much leaking as possible. If you do not, you will have to sanitize those documents carefully before publishing (See [Metadata auditing](#metadata-auditing)).**

### Communicating sensitive information { #sensitive-communication }

You might be interested in communicating information to some organization such as the press anonymously.

If you must do so, you should take some steps because you cannot trust any organization to protect your anonymity[^422]. See [Checklist of things to verify before sharing information](#pre-sharing-checklist).

For this, we strongly recommend the use of SecureDrop[^423] (<https://securedrop.org/> <sup>[[Archive.org]](https://web.archive.org/web/https://securedrop.org/)</sup>) which is an open-source project from the Freedom of the Press Foundation.

- Do take a moment to their read their "source guide" here: <https://docs.securedrop.org/en/stable/source.html> <sup>[[Archive.org]](https://web.archive.org/web/https://docs.securedrop.org/en/stable/source.html)</sup>

- Ideally, you should use SecureDrop over Tor and you will find a curated list of those here <https://github.com/alecmuffett/real-world-onion-sites#securedrop> <sup>[[Archive.org]](https://web.archive.org/web/https://github.com/alecmuffett/real-world-onion-sites#securedrop)</sup>

If not SecureDrop is not available, you could consider any other means of communication, but you should privilege those that are encrypted end to end. **Do not ever do this from your real identity but only from a secure environment using an anonymous identity.**

Without SecureDrop you could consider:

- Using e-mail with GPG encryption provided your recipient has published a GPG key somewhere. You can look this up here:

    - On their verified Social Media accounts (Twitter) if they provided it.

    - On <https://keybase.io> (Tor address <http://keybase5wmilwokqirssclfnsqrjdsi7jdir5wy7y7iu3tanwmtp6oid.onion>)

    - On OpenPGP directories such as: **(be careful as those are public directories and anyone can upload any key for any e-mail address, you will have to cross-check the signature with other platforms to be sure it is theirs).**

        + <https://pgp.mit.edu/>

        + <https://keyserver.ubuntu.com/>

        + <https://keys.openpgp.org>

- Using any other platform (even Twitter DMs) but again using GPG to encrypt the message for the recipient.

What you should avoid:

- Do not send physical materials using the post due to the risk of leaving DNA/Fingerprints or other traceable information (see [Cash-Paid VPN (preferred)](#anonymous-cash-vpn)).

- Do not use methods linked to a phone number (even a burner one) such as Signal/WhatsApp/Telegram.

- Do not use any kind of voice/video communication.

- Do not leak any clues about your real identity when exchanging messages.

- Do not meet people in real life unless you have absolutely no other option (this is a last resort option).

If you intend to break your anonymity to protect your safety:

- Assess the risks very carefully first.

- Inform yourself carefully on the legality/safety of your intent and the consequences for you and others. Think about it carefully.

- Possibly reach out to a **trusted** lawyer before doing so.

**Maintenance tasks**

- You should sign-up carefully into your accounts from time to time to keep them alive.

- Check your e-mail regularly for security checks and any other account notification.

- Check regularly the eventual appearance of compromise of any of your identities using <https://haveibeenpwned.com/> <sup>[[Archive.org]](https://web.archive.org/web/https://haveibeenpwned.com/)</sup> (obviously from a safe environment).

