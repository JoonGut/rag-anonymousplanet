# Getting an Anonymous VPN or Proxy { #anonymous-vpn-proxy }

If you follow our advice, you will also need a VPN subscription but this time you will need an anonymous one that cannot be tied to you by the financial system. Meaning you will need to buy a VPN subscription with cash or a reasonably private cryptocurrency (for example Monero). You will later be able to use this VPN to connect to various services anonymously but **never directly from your IP**. This VPN can never be used in any other non-anonymous context without jeopardzing your anonymity.

There are, two viable options:

## Cash/Monero-Paid VPN { #anonymous-cash-vpn }

There are three VPN companies recommended by PrivacyGuides.org (<https://www.privacyguides.org/vpn/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.privacyguides.org/vpn/)</sup>) that accept cash payments: Mullvad, iVPN, and Proton VPN.

Here are their logging policies:

- Mullvad: <https://mullvad.net/en/help/no-logging-data-policy/> <sup>[[Archive.org]](https://web.archive.org/web/https://mullvad.net/en/help/no-logging-data-policy/)</sup>
- iVPN: <https://www.ivpn.net/privacy/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.ivpn.net/privacy/)</sup>
- ProtonVPN: <https://protonvpn.com/support/no-logs-vpn/> <sup>[[Archive.org]](https://web.archive.org/web/https://protonvpn.com/support/no-logs-vpn/)</sup>

In addition, we will also mention a newcomer to watch: Safing SPN <https://safing.io/> <sup>[[Archive.org]](https://web.archive.org/web/https://safing.io/)</sup>) which (while still in the alpha stage at the time of this writing) which also accepts cash and has a very distinct new concept for a VPN which provides benefits similar to Tor Stream isolation with their "SPN"). Note that Safing SPN is not available on macOS at the moment. This possibility is "provisional" and at your own risk, but we think was worth mentioning.

Personally, for now, we would recommend Mullvad due to personal experience.

**We would not recommend Proton VPN as much because they do require an e-mail for registration unlike Mullvad, iVPN, and Safing. Proton also has a tendency to require phone number verification for users who register over Tor.**

How does this work?

- Access the VPN website with a Safe Browser (see [Safe Browser.](#safe-browser-host-os)

- Go to iVPN, Mullvad, or Safing website and create a new Account ID (on the login page).

- This page will give you an account ID, a token ID (for payment reference), and the details of where to send the money by post.

- Send the required cash amount for the subscription you want in a sealed postal envelope to their offices, including a paper with the Token ID without a return address, or pay with Monero if available. If they do not accept Monero but do accept BTC, consider [Paying anonymously online with BTC](#anonymous-crypto-payments).

- Wait for them to receive the payment and enable your account (this can take a while).

- Open Tor Browser.

- Check your account status and proceed when your account is active.

For extra-security consider:

- Wearing gloves while manipulating anything to avoid leaving fingerprints[^470] and touch DNA[^471].
- A less-obvious alternative could be to put super glue on your fingertips, to avoid making it obvious you're wearing gloves. However, this can prevent effective use of touchscreens, as well as failing to as effectively prevent you from touch DNA. Also, if spotted, it can be quite suspicious to be caught with super glue on your fingers.

- Do not use any material/currency that was manipulated by someone that can be related to you in any way.

- Do not use the currency you just got from an ATM that could record dispensed bills serial numbers.

- Be careful if you print anything that it is not watermarked by your printer (See [Printer Watermarking](#printer-watermarking)).

- Do not lick the envelope or the stamps[^472] if you use them to avoid leaving DNA traces.

- Make sure there are no obvious DNA traces in or on the materials (like hairs).

- Consider doing the whole operation outdoor to reduce the risks of residual DNA traces from your environment or you contaminating the materials.
- The more people frequent a space, the lower the risk, as your DNA will be obscured by the DNA of other people as they pass through

- Security cameras can be a risk. Try to cover your face. Also, gait recognition may be a concern. See [Gait Recognition and Other Long-Range Biometrics]

**Do not in any circumstance use this new VPN account unless instructed or connect to that new VPN account using your known connections. This VPN will only be used later in a secure way as we do not trust VPN providers' "no-logging policies". This VPN provider should ideally never know your real origin IP (your home/work one for instance).**

## Self-hosted VPN/Proxy on a Monero/Cash-paid VPS (for users more familiar with Linux) { #anonymous-self-hosted }

The other alternative is setting up your own VPN/Proxy using a VPS (Virtual Private Server) on a hosting platform that accepts Monero (recommended).

**This will offer some advantages as the chances of your IP being block-listed somewhere are lower than known VPN providers.**

This does also offer some disadvantages as Monero is not perfect as explained earlier in this guide and some global adversaries could maybe still track you. You will need to get Monero from an Exchange using the normal financial system and then pick a hosting (list here <https://www.getmonero.org/community/merchants/#exchanges> <sup>[[Archive.org]](https://web.archive.org/web/https://www.getmonero.org/community/merchants/)</sup>) or from a local reseller using cash from <https://localmonero.co>.

**Do not in any circumstance use this new VPS/VPN/Proxy using your known connections. Only access it through Tor using Whonix Workstation for instance (this is explained later). This VPN will only be used later within a Virtual Machin over the Tor Network in a secure way as we do not trust VPN providers' "no-logging policies". This VPN provider should never know your real origin IP.**

Please see [Recommended VPS hosting providers](#vps-hosting-providers)

### VPN VPS { #anonymous-vpn-vps }

There are plenty of tutorials on how to do this like this one <https://proprivacy.com/vpn/guides/create-your-own-vpn-server> <sup>[[Archive.org]](https://web.archive.org/web/https://proprivacy.com/vpn/guides/create-your-own-vpn-server)</sup>

### Socks Proxy VPS { #anonymous-socks }

This is also an option obviously if you prefer to skip the VPN part.

It is probably the easiest thing to set up since you will just use the SSH connection you have to your VPS and no further configuration should be required besides setting the browser of your guest VM to use the proxy in question.

Here are a few tutorials on how to do this very quickly:

- (Windows/Linux/macOS) <https://linuxize.com/post/how-to-setup-ssh-socks-tunnel-for-private-browsing/> <sup>[[Archive.org]](https://web.archive.org/web/https://linuxize.com/post/how-to-setup-ssh-socks-tunnel-for-private-browsing/)</sup>

- (Windows/Linux/macOS) <https://www.digitalocean.com/community/tutorials/how-to-route-web-traffic-securely-without-a-vpn-using-a-socks-tunnel> <sup>[[Archive.org]](https://web.archive.org/web/https://www.digitalocean.com/community/tutorials/how-to-route-web-traffic-securely-without-a-vpn-using-a-socks-tunnel)</sup>

- (Windows) <https://www.forwardproxy.com/2018/12/using-putty-to-setup-a-quick-socks-proxy/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.forwardproxy.com/2018/12/using-putty-to-setup-a-quick-socks-proxy/)</sup>

- (Linux/macOS) <https://ma.ttias.be/socks-proxy-linux-ssh-bypass-content-filters/> <sup>[[Archive.org]](https://web.archive.org/web/https://ma.ttias.be/socks-proxy-linux-ssh-bypass-content-filters/)</sup>

Here is my basic tutorial:

#### Linux/macOS { #anonymous-linux-macos }

Here are the steps:

- Get your anonymous VPS set-up

- From a terminal, SSH to your server by running: ```ssh -i ~/.ssh/id_rsa -D 8080 -f -C -q -N username@ip_of_your_server```

- Configure your browser to use localhost:8080 as a Socks Proxy for Browsing

- Done!

Explanation of arguments:

- -i: The path to the SSH key to be used to connect to the host

- -D: Tells SSH that we want a SOCKS tunnel on the specified port number (you can choose a number between 1025 and 65536)

- -f: Forks the process to the background

- -C: Compresses the data before sending it

- -q: Uses quiet mode

- -N: Tells SSH that no command will be sent once the tunnel is up

#### Windows { #anonymous-windows }

Here are the steps:

- Get your anonymous VPS set-up

- Download and install Putty from <https://www.putty.org/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.putty.org/)</sup>

- Set the following options in Putty and connect to your server

![image51](../media/image51.png)

- Connect to your VPS using those settings

- Configure your Browser to use localhost:8080 as a Socks Proxy

- Done!

