# Hardening Your Browsers { #hardening-browsers }

In this section, we'll discuss hardening your browsers. This has a heavy focus on the difference between Tracking Reduction and Tracking Evasion, and the pros and cons of either. First, let's define what they are [as described by Rohan Kumar](https://seirdy.one/posts/2022/06/25/two-types-of-privacy/):

- Tracking reduction (TR)
    - TR aims to reduce the amount of data collected about an exposed user. It reduces a footprint’s spread primarily by blocking trackers. Sometimes this can increase the size of a footprint.

- Tracking evasion (TE)
    - TE reduces the amount of data exposed by a user. Rather than eliminating data collection itself, TE prevents useful data from being made available in the first place. In other words, it reduces a footprint’s size.

Browsers that provide Tracking Reduction are to be used for a more casual [Threat Model][Threat modeling resources](#threat-modeling-resources) whereas Tracking Evasion is more complex. But both need to be explored. Tracking Reduction focuses on browsing with less tracking. It involves things like content-blocking, firewalls, opt-outs, flipping telemetry buttons, etc. If you're this far into the guide, you likely have a very good understanding of this already. Tracking Evasion, however, involves techniques like using the portable Tor Browser Bundle to anonymize your footprint and online identity, avoiding identifiable extensions, and using randomized keystroke delays. It's more about minimizing your online footprint, to give you a less fingerprintable browsing environment and internet usage.

A brief mention of this is necessary in determining operation needs for both. You need a certain level of understanding in both to achieve good standards and develop better browsing habits. This can and will overall provide you with a more viable solution to public trackers, government organizations looking to trace/track your browsing habits back to you, even just trolls attempting to doxx you.

The following are the recommended safest routes for each browser according to the current versions of their respective software and the ability each one has to become more secure. In the guide we will provide both Tracking Reduction & Evasion and it will not require you to write even a single line of code.

## Brave { #hardening-brave }

- Download and install Brave browser from <https://brave.com/download/> <sup>[[Archive.org]](https://web.archive.org/web/https://brave.com/download/)</sup>

- **Open** Brave Browser

- Go into **Settings** > **Appearances** (`brave://settings/appearance`)

    - **Disable** "Show Top Sites"

    - **Disable** "Show Brave Suggested Sites"

    - **Disable** "Show Brave Rewards icon in address bar"

    - **Enable** "Always show full URLs"

- Go into **Settings** > **Shields** (`brave://settings/shields`)

    - Set Shields to **Advanced**

    - Set "Trackers and Ads blocking" to **Aggressive**

    - Set Upgrade connections to HTTPS to **Enabled**

    - Set Cookie blocking to **Only cross-site**

    - Set Fingerprinting blocking to **Standard** or **Strict**

- Go into **Settings** > **Social media blocking** (`brave://settings/socialBlocking`)

    - **Uncheck** everything unless needed

- Go to **Settings** > **Search engine** (`brave://settings/search`)

    - See [Search Engines](#search-engines)

- Go into **Settings** > **Extensions** (`brave://settings/extensions`)

    - **Disable** everything except "Private Window with Tor"

    - Set both **Resolve** methods to "Ask"

- Go into **Settings** > **Wallet** (`brave://settings/wallet`)

    - **Disable** "Show Brave Wallet icon on toolbar"

    - Set **Default Ethereum wallet** to "None"

    - Set **Default Solana wallet** to "None"

- Go into **Settings** > **Privacy and Security** (`brave://settings/privacy`)

    - Leave **WebRTC** to "Default"

    - **Disable** "Allow privacy-preserving product analytics (P3A)"

    - **Disable** "Automatically send daily usage ping to Brave"

    - Go into "Clear Browsing Data"

        + Select **On Exit**

        + Check all options

        + **Click** "Save"

- Open a new Tab

- **Click** "Customize" in the lower right corner

    - **Disable** everything in Customize Dashboard except maybe the clock

- Go into **Settings** > **Shields** > **Content filters** (`brave://settings/shields/filters`)

    - Select any additional adblocking filter you want

        + Recommended: **CJX's Annoyance List**, **Easylist-Cookie List**, **Fanboy Annoyances List**, **Fanboy Social List**, **Fanboy's Mobile Notifications List**, and **uBlock Annoyances List**

    - Add custom filter lists

        + Add the [Actually Legitimate URL Shortener Tool](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/ClearURLs%20for%20uBo/clear_urls_uboified.txt) which uses the rules found in ClearURLs below

        + Add the [AdGuard URL Tracking Protection](https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_17_TrackParam/filter.txt) which enables generic `$removeparam` rules

    - To keep all applied filters, **click** "Save"

- Do not ever enable Brave Rewards (button should be hidden on all sites)

Addons to consider on Brave if you want additional protections:

- LocalCDN (<https://chrome.google.com/webstore/detail/localcdn/njdfdhgcmkocbgbhcioffdbicglldapd>)

    - Alternatively, DecentralEyes (<https://chrome.google.com/webstore/detail/decentraleyes/ldpochfccmkkmhdbclfhpagapcfdljkj>)

- PrivacyBadger (<https://chrome.google.com/webstore/detail/privacy-badger/pkehgijcmpdhfbdbbnkijodmdjhbjlgp>)

- NoScript (<https://chrome.google.com/webstore/detail/noscript/doojmbjmlfjjnbmnoijecmcbfeoakpjm>)

- Either ClearURLs (<https://chrome.google.com/webstore/detail/clearurls/lckanjgmijmafbedllaakclkaicjfmnk>) **OR** the custom list above

- LibRedirect (<https://libredirect.github.io/>)

That's it and you should be pretty much covered. For full paranoia, you can also just "Block Scripts" to disable Javascript. Note that even disabling Javascript might not protect you fully[^517].

## Ungoogled-Chromium { #hardening-ungoogled-chromium }

**This browser is considered a security liability due to their systemic lagging on security patches**[^518]**.**

**It is strongly advised not to use Ungoogled-Chromium.**

## Edge { #hardening-edge }

Windows only:

- Open Edge

- Go into Settings

- Go to Profiles and make sure everything is unchecked in every section (Personal Info, Passwords, Payment info, Profile preferences)

- Go to Privacy, search, and services:

    - Go to Tracking Prevention:

        + Set to Strict or at least Balanced

        + Set to always use Strict with InPrivate Windows

    - Go to Privacy:

        + Enable send Do Not Track

        + Disable the options for the website to check your payment methods

    - Go to Optional Diagnostic Data:

        + Disable it

    - Go to Personalize your Web Experience:

        + Disable it

    - Go to Security

        + Disable everything

    - Go to Services

        + Disable everything

        + In Address Bar and Search:

            * Disable everything and change the search engine (see [Search Engines](#search-engines))

    - Go to Cookies and Sites Permissions:

        + Within All Permissions:

            * Within Cookies, make sure "Block Third-Party Cookies" is checked

            * Block everything except:

                - Javascript

                - Images

Enable Application Guard for Edge (only on Host OS, not possible within a VirtualBox VM):

**Skip if this is a VM**

- Open Control Panel.

- Click on Programs

- Click on Turn Windows features on or off link

- Check the Windows Defender Application Guard option

- Click OK.

- Click Restart.

- Now you can open Edge and open a new "Application Guard" Window.

That's about it for Edge but you are also free to add extensions from the Chrome Store such as:

- uBlock Origin (<https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm>)

- LocalCDN (<https://chrome.google.com/webstore/detail/localcdn/njdfdhgcmkocbgbhcioffdbicglldapd>)

    - Alternatively, DecentralEyes (<https://chrome.google.com/webstore/detail/decentraleyes/ldpochfccmkkmhdbclfhpagapcfdljkj>)

- PrivacyBadger (<https://chrome.google.com/webstore/detail/privacy-badger/pkehgijcmpdhfbdbbnkijodmdjhbjlgp>)

- HTTPS Everywhere (<https://chrome.google.com/webstore/detail/https-everywhere/gcbommkclmclpchllfjekcdonpmejbdp>)

- NoScript (<https://chrome.google.com/webstore/detail/noscript/doojmbjmlfjjnbmnoijecmcbfeoakpjm>)

- ClearURLs (<https://chrome.google.com/webstore/detail/clearurls/lckanjgmijmafbedllaakclkaicjfmnk>)

- LibRedirect (<https://libredirect.github.io/>)

## Safari { #hardening-safari }

macOS Only:

- Open Safari

- Click the Safari top left Menu

- Click Preferences

    - On the General Tab:

        + Change New Windows to "Empty Page"

        + Change New Tabs to "Empty page"

        + Change the Remove History after to "1 day"

        + Change the Remove Download list items to "When Safari Quits" or "When Successful Download"

        + Uncheck "Open Safe Files After Downloading"

    - On the Security Tab:

        + Disable "Warn when visiting a Fraudulent Website" (this sends the URLs your visit to Google for screening)

    - On the Privacy Tab:

        + Uncheck "Web Advertising"

    - On the Advanced Tab:

        + Check the "Show full website address"

Consider [Additional browser precautions with JavaScript enabled](#browser-precautions-js)

That's about it. Unfortunately, you will not be able to add extensions as those will require you to sign in into the App Store which you cannot do from a macOS VM. Again, we would not recommend sticking to Safari in a macOS VM but instead switching to Brave or Firefox.

## Firefox { #hardening-firefox }

### Normal settings { #hardening-firefox-normal }

- Open Firefox

- On the Firefox Home Page:

    - Click Personalize

    - Uncheck/Disable Everything

- Open Settings:

    - Go into Search

        + Change the search engine (See [Search Engines](#search-engines))

    - Go into Privacy & Security

        + Set to Custom

            * Cookies: Select All Third-Party Cookies

            * Tracking Content: In all Windows

            * Check Cryptominers

            * Check Fingerprinters

        + Set always send "Do Not Track"

    - Go to Logins and Passwords

        + Uncheck "Ask to save logins and passwords for websites"

    - Go to Permissions

        + Location: check block new requests

        + Camera: check block new requests

        + Microphone: check block new requests

        + Notifications: check block new requests

        + Autoplay: select Disable Audio and Video

        + Virtual Reality: check block new requests

        + Check Block Pop-ups

        + Check Warn when websites try to install add-ons

    - Go to Firefox Data Collection and Use

        + Disable everything

    - Go to HTTPS-Only Mode

        + Enable it on all Windows

### Advanced settings { #hardening-firefox-advanced }

Consider [Arkenfox/user.js](https://github.com/arkenfox/user.js/), a heavily maintained and very easy to use browser config which uses a "user.js" to set all the privacy settings and disk avoidance values. Below we recommend that if you are not setting the Arkenfox config, at least setting the **about:config** values below. Arkenfox applies many others but these are the bare minimum for your protection while browsing. Remember: doing nothing and using a browser with its defaults will already be leaking many identifiable and trackable characteristics which are unique to you. See [Browser and Device Fingerprinting](#fingerprinting) for more details on why default settings in browsers are unsafe.

Those settings are explained on the following resources in order of recommendation if you want more details about what each setting does:

1. <https://wiki.archlinux.org/title/Firefox/Privacy> <sup>[[Archive.org]](https://web.archive.org/web/https://wiki.archlinux.org/title/Firefox/Privacy)</sup> **(most recommended)**

2. <https://proprivacy.com/privacy-service/guides/firefox-privacy-security-guide> <sup>[[Archive.org]](https://web.archive.org/web/https://proprivacy.com/privacy-service/guides/firefox-privacy-security-guide)</sup>

Here are most of the steps combined from the sources above (some have been omitted due to the extensions recommended later below):

- Navigate to "about:config" in the URL bar

- Click Accept the Risk and Continue

    - Safe Settings (should not break anything)

        + Disable Firefox Pocket

            * Set "extensions.pocket.enabled" to false

        + Disable All Telemetry

            * Set "browser.newtabpage.activity-stream.feeds.telemetry" to false

            * Set "browser.ping-centre.telemetry" to false

            * Set "browser.tabs.crashReporting.sendReport" to false

            * Set "devtools.onboarding.telemetry.logged" to false

            * Set "toolkit.telemetry.enabled" to false

            * Search for "toolkit.telemetry.server" and clear it

            * Set "toolkit.telemetry.unified" to false

            * Set "beacon.enabled" to false

        + Disable Pre-Fetching

            * Set "network.dns.disablePrefetch" to true

            * Set "network.dns.disablePrefetchFromHTTPS" to true

            * Set "network.predictor.enabled" to false

            * Set "network.predictor.enable-prefetch" to false

            * Set "network.prefetch-next" to false

            * Set "browser.urlbar.speculativeConnect.enabled" to false

        + Disable Javascript in PDFs

            * Set "pdfjs.enableScripting" to false

        + Disable obsolete SSL encryption

            * Set "security.ssl3.rsa_des_ede3_sha" to false

            * Set "security.ssl.require_safe_negotiation" to true

        + Disable Firefox Accounts

            * Set "identity.fxaccounts.enabled" to false

        + Disable Geolocation

            * Set "geo.enabled" to false

        + Disable Web Notifications

            * Set "dom.webnotifications.enabled" to false

        + Disable Copy/Paste Notifications

            * Set "dom.event.clipboardevents.enabled" to false

        + Disable Microphone/Camera status fetching

            * Set "media.navigator.enabled" to false

        + Enable "Do Not Track"

            * Set "privacy.donottrackheader.enabled" to true

        + Disable SafeBrowsing

            * Set "browser.safebrowsing.malware.enabled" to false

            * Set "browser.safebrowsing.phishing.enabled" to false

            * Set "browser.safebrowsing.downloads.remote.enabled" to false

    - Moderate Settings (could break some websites)

        + Disable WebRTC (this will break all websites with video/audio communications)

            * Set "media.peerconnection.enabled" to false

            * Set "media.navigator.enabled" to false

        + Disable WebGL (this will break some media intensive websites)

            * Set "webgl.disabled" to true

        + Disable DRM

            * Set "media.eme.enabled" to false

            * Set "media.gmp-widevinecdm.enabled" to false

        + Set Cookiies Behavior

            * Set "network.cookie.cookieBehavior" to 1

            * Set "network.http.referer.XOriginPolicy" to 2

        + Change referer policy

            * Set "network.http.referer.XOriginTrimmingPolicy" to 2

        + Change Session Storage behavior

            * Set "browser.sessionstore.privacy_level" to 2

        + Disable Connection Tests for Captive Portals

            * Set "network.captive-portal-service.enabled" to false

        + Disable "Trusted Recursive Resolver"

            * Set/Create "network.trr.mode" and set it to 5

    - Advanced (this will break some websites)

        + Set "privacy.resistFingerprinting" to true

        + Set "privacy.trackingprotection.fingerprinting.enabled" to true

        + Set "privacy.trackingprotection.cryptomining.enabled" to true

        + Set "privacy.trackingprotection.enabled" to true

        + Set "browser.send_pings" to false

        + Set "change privacy.firstparty.isolate" to true

        + Set "network.http.referer.XOriginPolicy" to "2" or use **Smart Referer** below

        + Set "change network.cookie.lifetimePolicy" to 2 (this deletes all cookies after each session)

### Addons to install/consider { #hardened-firefox-addons }

- uBlock Origin (<https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/>)

- Smart Referer (<https://addons.mozilla.org/firefox/addon/smart-referer/>)

    - Set "network.http.referer.XOriginPolicy" value of "2" to "0" (so the extension works). **Disable** the whitelist (uncheck the **Use default whitelist** box) and set **Domain name matching** to **Strict**.

- NoScript (<https://addons.mozilla.org/en-US/firefox/addon/noscript/>)

    - Blocks **all** scripts by default, no exceptions. Necessary in regular browser if you want to block all script executions. Not necessary in Tor Browser.

    - Within the options, change **Default** options to check everything except "ping", "unrestricted CSS", and "LAN". This will re-enable JavaScript and other web features, to prevent many websites from breaking

- LibRedirect (<https://libredirect.github.io/>)

    - Redirect less privacy friendly websites like YouTube and Wikipedia to more privacy friendly open-source alternatives

- Skip Redirect (<https://github.com/sblask/webextension-skip-redirect>)

### Bonus resources { #hardened-firefox-guides }

Here are also two recent guides to harden Firefox:

- <https://chrisx.xyz/blog/yet-another-firefox-hardening-guide/> <sup>[[Archive.org]](https://web.archive.org/web/https://chrisx.xyz/blog/yet-another-firefox-hardening-guide/)</sup>

- <https://ebin.city/~werwolf/posts/firefox-hardening-guide/> <sup>[[Archive.org]](https://web.archive.org/web/https://ebin.city/~werwolf/posts/firefox-hardening-guide/)</sup>

