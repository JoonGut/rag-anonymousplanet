## Bad Cryptography { #on-bad-cryptography }

There is a frequent adage among the infosec community: "Don't roll your own crypto!".

And there are reasons[^255]'[^256]'[^257]'[^258] for that:

We would not want people discouraged from studying and innovating in the crypto field because of that adage. So instead, we would recommend people to be cautious with "Roll your own crypto" because it is not necessarily good crypto:

- Good cryptography is not easy and usually takes years of research to develop and fine-tune.

- Good cryptography is transparent and not proprietary/closed source so it can be reviewed by peers.

- Good cryptography is developed carefully, slowly, and rarely alone.

- Good cryptography is usually presented and discussed in conferences and published in various journals.

- Good cryptography is extensively peer-reviewed before it is released for use in the wild.

- Using and implementing existing good cryptography correctly is already a challenge.

Yet, this is not stopping some from doing it anyway and publishing various production Apps/Services using their self-made cryptography or proprietary closed-source methods:

- You should apply caution when using Apps/Services using closed-source or proprietary encryption methods. All the good crypto standards are public and peer-reviewed and there should be no issue disclosing the one you use.

- You should be wary of Apps/Services using a "modified" or proprietary cryptographic method[^259].

- By default, you should not trust any "Roll your own crypto" until it was audited, peer-reviewed, vetted, and accepted by the cryptography community[^260]'[^261].

- There is no such thing as "military-grade crypto"[^262]'[^263]'[^264].

Cryptography is a complex topic and bad cryptography could easily lead to your de-anonymization.

In the context of this guide,we recommend sticking to Apps/Services using well-established, published, and peer-reviewed methods.

So, what to prefer and what to avoid as of 2021? You will have to look up for yourself to get the technical details of each app and see if they are using "bad crypto" or "good crypto". Once you get the technical details, you could check this page for seeing what it is worth: <https://latacora.micro.blog/2018/04/03/cryptographic-right-answers.html> <sup>[[Archive.org]](https://web.archive.org/web/https://latacora.micro.blog/2018/04/03/cryptographic-right-answers.html)</sup>

Here are some examples:

- Hashes:

    - Prefer: SHA-3 or BLAKE2[^265]

    - Still relatively ok to use: SHA-2 (such as the widely used SHA-256 or SHA-512)

    - Avoid: SHA-1, MD5 (unfortunately still widely used), CRC, MD6 (rarely used)

- File/Disk Encryption:

    - Prefer:

        + Hardware Accelerated[^266]: AES (Rijndael) 256 Bits with HMAC-SHA-2 or HMAC-SHA-3 (This is what Veracrypt, Bitlocker, Filevault 2, KeepassXC, and LUKS use by default). Prefer SHA-3.

        + Non-Hardware Accelerated: Same as accelerated above or if available consider:

            * ChaCha20[^267] or XChaCha20 (You can use ChaCha20 with Kryptor <https://www.kryptor.co.uk>, unfortunately, it is not available with Veracrypt).

            * Serpent[^268]

            * TwoFish[^269]

    - Avoid: Pretty much anything else

- Password Storage:

    - Prefer: Argon2, scrypt
    - If these aren't options, use bcrypt, or if not possible at least PBKDF2 (only as a last resort)
    - Be skeptical of Argon2d, as it's vulnerable to some forms of side-channels. Prefer Argon2i or Argon2id

    - Avoid: SHA-3, SHA-2, SHA-1, MD5

- Browser Security (HTTPS):

    - Prefer: TLS 1.3 (ideally TLS 1.3 with ECH/eSNI support) or at least TLS 1.2 (widely used)

    - Avoid: Anything Else (TLS =<1.1, SSL =<3)

- Signing messages/files with GnuPG (GPG):

    - Prefer ECDSA (ed25519)+ECDH (ec25519) or RSA 4096 Bits*

        + **Consider a more modern**[^270] **alternative to PGP/GPG: Minisign <https://jedisct1.github.io/minisign/>** <sup>[[Archive.org]](https://web.archive.org/web/https://jedisct1.github.io/minisign/)</sup>

    - Avoid: RSA 2048 bits

- SSH keys:

    - ED25519 (preferred) or RSA 4096 Bits*

    - Avoid: RSA 2048 bits

- **Warning: RSA and ED25519 are unfortunately not seen as "Quantum Resistant"**[^271] **and while they have not been broken yet, they probably will be broken someday into the future. It is just a matter of when rather than if RSA will ever be broken. So, these are preferred in those contexts due to the lack of a better possibility.**

Here are some real cases of issues bad cryptography:

- Telegram: <https://democratic-europe.eu/2021/07/20/cryptographers-uncover-four-vulnerabilities-in-telegram/> <sup>[[Archive.org]](https://web.archive.org/web/https://democratic-europe.eu/2021/07/20/cryptographers-uncover-four-vulnerabilities-in-telegram/)</sup>

- Telegram: <https://buttondown.email/cryptography-dispatches/archive/cryptography-dispatches-the-most-backdoor-looking/> <sup>[[Archive.org]](https://web.archive.org/web/https://buttondown.email/cryptography-dispatches/archive/cryptography-dispatches-the-most-backdoor-looking/)</sup>

- Cryptocat: <https://web.archive.org/web/20130705051050/https://blog.crypto.cat/2013/07/new-critical-vulnerability-in-cryptocat-details/>

- Some other examples can be found here: <https://www.cryptofails.com/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.cryptofails.com/)</sup>

Later this guide will not recommend "bad cryptography" and that should hopefully be enough to protect you?

