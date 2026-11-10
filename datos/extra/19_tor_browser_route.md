## The Tor Browser route { #tor-browser-route }

This part of the guide will help you in setting up the simplest and easiest way to browse the web anonymously. It is not necessarily the best method and there are more advanced methods below with (much) better security and (much) better mitigations against various adversaries. Yet, this is a straightforward way of accessing resources anonymously and quickly with no budget, no time, no skills, and limited usage.

So, what is Tor Browser? Tor Browser (<https://www.torproject.org/> <sup>[[Archive.org]](https://web.archive.org/web/https://www.torproject.org/)</sup>) is a web browser like Safari/Firefox/Chrome/Edge/Brave designed with privacy and anonymity in mind.

This browser is different from other browsers as it will connect to the internet through the Tor Network using Onion Routing. We first recommend that you watch this very nice introduction video by the Tor Project themselves: <https://www.youtube.com/watch?v=JWII85UlzKw> <sup>[[Invidious]](https://yewtu.be/watch?v=JWII85UlzKw)</sup>. After that, you should probably head over to their page to read their quick overview here: <https://2019.www.torproject.org/about/overview.html.en> <sup>[[Archive.org]](https://web.archive.org/web/https://2019.www.torproject.org/about/overview.html.en)</sup>. Without going into too many technical details, Tor Browser is an easy and simple "fire and forget" solution to browse the web anonymously from pretty much any device. It is probably sufficient for most people and can be used from any computer or smartphone.

Here are several ways to set it up for all main OSes.

**Warning:** You should avoid installing extensions in Tor Browser, as they can be used to fingerprint and identify you.

### Windows, Linux, and macOS { #tor-windows-linux-macos }

Please see [Installing and using desktop Tor Browser](#desktop-tor-browser).

### Android { #tor-android }

**Note on Tor Browser for Android: The development of Tor Browser for Android is behind desktop Tor Browser Bundle (TBB). Some features are not available yet. E.g., the desktop version of Tor now enables automatic bridges using Moat:**

"**Connection Assist** works by looking up and downloading an up-to-date list of country-specific options to try using your location (with your consent). It manages to do so without needing to connect to the Tor Network first by utilizing [moat](https://support.torproject.org/glossary/moat/) – the same domain-fronting tool that Tor Browser uses to request a bridge from torproject.org."

- Head over to:

    - Play Store: <https://play.google.com/store/apps/details?id=org.torproject.torbrowser>

    - F-Droid Store: It's not yet there but you can add it manually following the instructions at <https://support.torproject.org/tormobile/tormobile-7/> <sup>[[Archive.org]](https://web.archive.org/web/https://support.torproject.org/tormobile/tormobile-7/)</sup>

- Install

- Launch Tor Browser

- After launching, click the upper right **Settings** icon

- Select **Settings** > **Privacy and security** > **Tor network**

- Select **Config Bridge**.

- Read [Using Tor bridges in hostile environments](#tor-bridges).

- **If needed (after reading the appendix above)**, activate the option and select the type of bridge you want:

    - Obfs4

    - Meek-Azure

    - Snowflake

- **If your internet isn't censored**, consider running one of the bridge types to help the network!

    - Easy: Obsf4 - You can run your own Obsf4 easily with these instructions. <https://community.torproject.org/relay/setup/bridge/>

    - Medium: Snowflake - More about Snowflakes here. <https://snowflake.torproject.org/>

    - Hard: Meek - This is the documentation. It's not as simple. <https://gitlab.torproject.org/legacy/trac/-/wikis/doc/meek/#how-to-run-a-meek-server-bridge>

Personally, if you need to use a Bridge (this is not necessary for a non-hostile environment), you should pick a Meek-Azure. Those will probably work even if you are in China and want to bypass the Great Firewall. It is probably the best option to obfuscate your Tor activities if needed and Microsoft servers are usually not blocked.

_Only available for Desktop Tor users: Recently, the Tor Project has made it incredibly simple to access Bridges with **Connection Assist**, and it is now automatically done in hostile or censored regions. Simply open the Tor Browser and the connection will be configured based on your needs on any hostile network. Previously, we had a list of options below this paragraph which were necessary to enable and configure bridges, but now that this is done automatically using [moat](https://support.torproject.org/glossary/moat/)._ <sup>[[Archive.org]](https://web.archive.org/web/20220801151048/https://support.torproject.org/glossary/moat/)</sup>

- You are almost done

As with the desktop version, you need to know there are safety levels in Tor Browser. On Android, you can access these by following these steps:

- Click the menu (bottom right)

- Click **Settings**.

- Head over to the **Privacy and security** section.

- Click **Security Settings**.

You will find details about each level here: <https://tb-manual.torproject.org/security-settings/> <sup>[[Archive.org]](https://web.archive.org/web/https://tb-manual.torproject.org/security-settings/)</sup> but here is a summary:

- Standard (the default):

    - All features are enabled (including JavaScript)

- Safer:

    - JavaScript is disabled on non-HTTPS websites

    - Some fonts and symbols are disabled

    - Any media playback is "click to play" (disabled by default)

- Safest:

    - Javascript is disabled everywhere

    - Some fonts and symbols are disabled

    - Any media playback is "click to play" (disabled by default)

We would recommend the "Safer" level for most cases. The Safest level should be enabled if you think you are accessing suspicious or dangerous websites and/or if you are extra paranoid.

If you are extra paranoid, use the "Safest" level by default and consider downgrading to Safer is the website is unusable because of Javascript blocking.

However, the Safer level should be used with some extra precautions while using some websites: see [Additional browser precautions with JavaScript enabled](#browser-precautions-js).

Now, you are really done, and you can now surf the web anonymously from your Android device.

**Please see** [Warning for using Orbot on Android](#orbot-android-warning).

### iOS { #tor-ios }

**Disclaimer: Onion Browser, following a 2018 release on iOS, has had IP leaks via WebRTC. It is still the only officially endorsed browser for the Tor network for iOS. Users should exercise caution when using the browser and check for any DNS leaks.**

While the official Tor Browser is not yet available for iOS, there is an alternative called Onion Browser endorsed by the Tor Project[^300].

- Head over to <https://apps.apple.com/us/app/onion-browser/id519296448>

- Install

- Disable Wi-Fi and Mobile Data

- Launch Onion Browser

- After Launching, click the upper right Settings icon (Disabling Wi-Fi and Mobile Data previously were to prevent Onion Browser from connecting automatically and to allow access to these options).

- Select "Bridge Configuration" and read [Using Tor bridges in hostile environments](#tor-bridges)

- **If needed (after reading the appendix above)**, activate the option and select the type of bridge you want:

    - Obfs4

    - Snowflake

    - (Meek-Azure is unfortunately not available on Onion Browser for iOS (See [commit 21bc18428](https://github.com/OnionBrowser/OnionBrowser/commit/21bc18428368224507b27ee58464ad352f4ec810) for more information.)

- **If your internet isn't censored**, consider running one of the bridge types to help the network!

    - Easy: Obsf4 - You can run your own Obsf4 easily with these instructions. <https://community.torproject.org/relay/setup/bridge/>

    - Medium: Snowflake - More about Snowflakes here. <https://snowflake.torproject.org/>

    - Hard: Meek - This is the documentation. It's not as simple. <https://gitlab.torproject.org/legacy/trac/-/wikis/doc/meek/#how-to-run-a-meek-server-bridge>

Personally, if you need to use a Bridge (this is not necessary for a non-hostile environment), you should pick a Snowflake one (since Meek-Azure bridges are not available). Those will probably work even if you are in China and want to bypass the Great Firewall. It is probably the best option you have on iOS.

- You are almost done

As with the desktop version, you need to know there are safety levels in Onion Browser. On iOS, you can access these by following these steps:

- Click the shield icon (upper left)

- You will have three levels to pick from

| Security Level | JavaScript | WS/XHR/Geo | A/V | Apps | WebRTC | HTTP↔HTTPS | Ads/Pop-ups |
  |-------|------------|-------------|------|------|---------|------------|-------------|
  | **Gold** | Disabled | Disabled | No | Blocked | Blocked | Blocked | Blocked |
  | Silver | Partially allowed | Disabled | No | Blocked | Blocked | Blocked | Blocked |
  | Bronze | Allowed | Enabled | Allowed | Blocked | Not blocked | Not blocked | Blocked |

We would recommend the "Silver" level for most cases. The Gold level should only be enabled if you think you are accessing suspicious or dangerous websites or if you are extra paranoid. The Gold mode will also most likely break many websites that rely actively on JavaScript.

As JavaScript is enabled in the Silver mode, please see [Additional browser precautions with JavaScript enabled](#browser-precautions-js).

Now, you are really done, and you can now surf the web anonymously from your iOS device.

### Important Warning { #important-warning }

**This route is the easiest but is not designed to resist highly skilled adversaries. It is however usable on any device regardless of the configuration. This route is also vulnerable to correlation attacks (See [Your Anonymized Tor/VPN traffic](#traffic-anonymization)) and is blind to anything that might be on your device (this could be any malware, exploit, virus, remote administration software, parental controls...). Yet, if your threat model is quite low, it is probably sufficient for most people.**

If you have time and want to learn, we recommend going for other routes instead as they offer far better security and mitigate far more risks while lowering your attack surface considerably.

