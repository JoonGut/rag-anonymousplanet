# Post-Quantum Cryptography { #post-quantum-cryptography }

**Note: This section deals with a threat that is not immediate for most users. If your threat model involves a nation-state adversary or communications whose sensitivity extends years into the future, read carefully. If you are an average user, you can skim this section for now but should revisit it as the technology matures.**

Most of the encryption protecting your communications today - including the key exchanges inside Signal, HTTPS connections, VPNs, and PGP - relies on mathematical problems that are computationally infeasible for any classical computer to solve. A sufficiently powerful quantum computer[^553] running Shor's algorithm[^271] would break these problems efficiently. No such computer exists yet. The largest current machines are still far from the scale needed. But that is not a reason to ignore the problem.

The threat is called **"harvest now, decrypt later"** (HNDL). It works like this: an adversary - a government intelligence agency is the realistic candidate here - records and stores your encrypted traffic today, at scale. They cannot read it now. But if a capable quantum computer is built in the next 10-20 years, they decrypt that archived traffic retroactively. For most people reading this, that is not a pressing concern. For a journalist protecting a source whose identity would still be dangerous to expose in 2035, or an activist living under a government that keeps very long institutional memories, it is worth taking seriously.

The good news is that the cryptographic community has been aware of this problem for over a decade, and the tooling is arriving. In 2024, NIST finalized the first post-quantum cryptographic standards[^555]:

- **ML-KEM** (Module-Lattice-Based Key-Encapsulation Mechanism, formerly known as Kyber[^556]) - replaces the classical key exchange step in protocols such as TLS and Signal's X3DH. It is based on the hardness of the Module Learning With Errors (MLWE) problem, which is believed to resist both classical and quantum attacks.

- **ML-DSA** (Module-Lattice-Based Digital Signature Algorithm, formerly Dilithium) - a post-quantum replacement for RSA and ECDSA signatures used to authenticate identities and sign software.

- **SPHINCS+** (now standardized as SLH-DSA) - a hash-based signature scheme. Slower and larger than ML-DSA, but it relies only on the security of hash functions rather than lattice assumptions, making it a conservative fallback if lattice-based cryptography is ever weakened.

NIST explicitly recommends deploying these in **hybrid mode** during the transition period - meaning alongside classical algorithms rather than replacing them outright. This way, an attacker would need to break both simultaneously.

## Signal's PQXDH { #on-signal-post-quantum }

In September 2023, Signal deployed **PQXDH**[^557] (Post-Quantum Extended Diffie-Hellman), upgrading its X3DH key agreement protocol to combine ML-KEM-1024 with the classical X25519 Diffie-Hellman exchange. The result is hybrid: security holds as long as either component remains unbroken.

For Signal users, **this was automatic and transparent**. No configuration is required. New conversations started after the rollout use PQXDH by default. This directly addresses the HNDL threat for forward secrecy - an adversary who recorded your Signal traffic cannot use a future quantum computer to derive your session keys.

Note that this only covers the key exchange layer. The authentication layer (identity keys) is not yet post-quantum hardened in Signal, though this is an active area of development.

## What you should do now { #pqc-next-action }

For most threat models, the practical steps are straightforward:

- **Use Signal.** PQXDH is already deployed, no action required.

- **Keep your browser updated.** Chrome and Firefox have had hybrid post-quantum key exchange (X25519 + ML-KEM) in TLS enabled by default since 2024[^558]. This protects your HTTPS connections against HNDL at the transport layer.

- **Do not rely on PGP/GPG for long-term confidentiality of highly sensitive material.** PGP key exchanges (RSA, ECDH) are not post-quantum hardened. Messages encrypted to a PGP key today could be decrypted retroactively by a quantum-capable adversary who has stored them. If you must use PGP, treat it as protection against present-day adversaries only.

- **Check your VPN provider.** Most commercial VPNs have not yet deployed post-quantum key exchange. Some (Mullvad, ProtonVPN) have added it. If HNDL is in your threat model, check your provider's documentation or switch to one that supports it.

For those with genuinely high-risk profiles: communications whose exposure would still be dangerous in ten or more years deserve attention now. Switching to Signal and establishing fresh sessions (rather than relying on long-running session state from before the PQXDH rollout) is the most practical near-term step.

## A note on Monero { #on-monero }

Monero's cryptographic primitives - specifically its use of Ed25519 and Curve25519 - are vulnerable to Shor's algorithm on a sufficiently powerful quantum computer. The Monero Research Lab has studied this problem[^535] and no post-quantum upgrade has been deployed. The community regards this as a medium-term concern, not an immediate one, given the current state of quantum hardware. For operational anonymity today, Monero remains appropriate. Do not assume long-term financial privacy against a quantum-capable adversary.

